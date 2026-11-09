"""
Generates an attendance report as an Excel workbook from a folder of
Microsoft Teams meeting-attendance CSV exports -- one CSV per session
(e.g. one per class day). Standalone script, no dependency on
tools/report.py, though it reuses the same visual conventions (color
fills, grid-sheet shape) for a consistent look across both reports.

Usage (from the repo root):
    python tools/attendance_report.py /path/to/attendance/csvs
    python tools/attendance_report.py /path/to/csvs --output attendance.xlsx
    python tools/attendance_report.py /path/to/csvs --pattern "*.csv"

Run `python tools/attendance_report.py --help` for every option.

What it expects
-----------------------------
One CSV file per session in the given folder (matching --pattern, default
"*.csv"). Each file is Teams' own "Download attendance list" export --
format varies by Teams client/version, so the parser is deliberately
tolerant rather than assuming one fixed shape:

- Encoding: tries utf-8-sig, utf-16, then utf-8 in order (Teams desktop
  exports are commonly UTF-16 with a BOM; web exports are commonly
  UTF-8).
- Delimiter: auto-detected per file (comma or tab -- Teams has used
  both across versions).
- A "1. Summary" header block (meeting title/start time/participant
  count) is read if present, for the session's title and as a date
  fallback, but isn't required.
- The actual participant table's header row is found by scanning for a
  row containing a recognized "name" column alongside a recognized
  "join"/"leave"/"duration" column -- not assumed to be at a fixed line
  number, since the summary block's length varies. Recognized header
  aliases (case-insensitive): Name/Full Name/Participant Name;
  Join Time/First Join; Leave Time/Last Leave;
  Duration/In-Meeting Duration; Email/Participant ID (UPN)/UPN.
- Only "Name" and some duration/join signal are required for a row to
  count -- email is used to de-duplicate the same person across
  sessions when present, falling back to name otherwise.

Each file is treated as one session, dated by (in order): a date found
in the filename (YYYY-MM-DD, YYYY_MM_DD, or MM-DD-YYYY), else the
"Meeting start time" summary field if the file has one, else the file's
own last-modified date (printed as a warning, since it's the least
reliable of the three).

If your actual exports use column names or a layout this doesn't
recognize, the alias sets (NAME_ALIASES etc., just below the imports)
are the place to extend them.
"""
import argparse
import csv
import io
import re
import sys
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path

try:
    import openpyxl
    from openpyxl.styles import Alignment, Font, PatternFill
    from openpyxl.formatting.rule import ColorScaleRule
    from openpyxl.chart import BarChart, Reference
except ImportError:
    print(
        "openpyxl is required to write the .xlsx report -- "
        "pip install -r requirements.txt",
        file=sys.stderr,
    )
    raise

# --------------------------------------------------------------------------- column recognition

NAME_ALIASES = {"name", "full name", "participant name"}
JOIN_ALIASES = {"join time", "first join"}
LEAVE_ALIASES = {"leave time", "last leave"}
DURATION_ALIASES = {"duration", "in-meeting duration", "total duration"}
EMAIL_ALIASES = {"email", "participant id (upn)", "upn", "participant email"}

FILENAME_DATE_PATTERNS = [
    re.compile(r"(\d{4})-(\d{2})-(\d{2})"),
    re.compile(r"(\d{4})_(\d{2})_(\d{2})"),
    re.compile(r"(\d{2})-(\d{2})-(\d{4})"),  # MM-DD-YYYY
]

DURATION_RE = re.compile(r"(?:(\d+)h)?\s*(?:(\d+)m)?\s*(?:(\d+)s)?", re.IGNORECASE)


def _norm(cell: str) -> str:
    return (cell or "").strip().lower().lstrip("﻿")


# --------------------------------------------------------------------------- file reading

def _read_text(path: Path) -> str:
    """Try the encodings Teams actually exports in, in likelihood order."""
    for encoding in ("utf-8-sig", "utf-16", "utf-8"):
        try:
            return path.read_text(encoding=encoding)
        except (UnicodeError, UnicodeDecodeError):
            continue
    # Last resort: decode permissively rather than crash on one bad file.
    return path.read_bytes().decode("utf-8", errors="replace")


def _sniff_rows(text: str) -> list:
    sample = text[:4096]
    try:
        dialect = csv.Sniffer().sniff(sample, delimiters=",\t;")
    except csv.Error:
        dialect = csv.excel
        dialect.delimiter = "\t" if sample.count("\t") > sample.count(",") else ","
    return list(csv.reader(io.StringIO(text), dialect))


# --------------------------------------------------------------------------- duration/date parsing

def _parse_duration_minutes(text: str) -> float:
    """"1h 2m 30s" / "45m" / "30s" -> minutes (float). 0.0 if unparseable."""
    if not text:
        return 0.0
    m = DURATION_RE.search(text)
    if not m or not any(m.groups()):
        return 0.0
    h, mi, s = (int(g) if g else 0 for g in m.groups())
    return h * 60 + mi + s / 60


def _date_from_filename(path: Path) -> date:
    stem = path.stem
    for pattern in FILENAME_DATE_PATTERNS:
        m = pattern.search(stem)
        if not m:
            continue
        a, b, c = m.groups()
        try:
            if len(a) == 4:
                return date(int(a), int(b), int(c))
            return date(int(c), int(a), int(b))  # MM-DD-YYYY
        except ValueError:
            continue
    return None


def _date_from_summary(rows: list) -> date:
    for row in rows:
        if not row:
            continue
        if _norm(row[0]) in ("meeting start time", "meeting start date"):
            rest = ",".join(row[1:])
            for fmt in ("%m/%d/%y, %I:%M:%S %p", "%m/%d/%Y, %I:%M:%S %p",
                        "%Y-%m-%d %H:%M:%S", "%m/%d/%y %I:%M:%S %p"):
                try:
                    return datetime.strptime(rest.strip(), fmt).date()
                except ValueError:
                    continue
    return None


def _meeting_title(rows: list) -> str:
    for row in rows:
        if row and _norm(row[0]) == "meeting title":
            return ",".join(row[1:]).strip() or None
    return None


# --------------------------------------------------------------------------- per-file parsing

def parse_attendance_csv(path: Path) -> dict:
    """One session's worth of attendance: {"date": date|None, "title": str|None,
    "participants": [{"name", "email", "duration_minutes"}, ...], "warning": str|None}."""
    text = _read_text(path)
    rows = _sniff_rows(text)

    header_idx = None
    col_for = {}
    for i, row in enumerate(rows):
        normed = [_norm(c) for c in row]
        name_col = next((j for j, c in enumerate(normed) if c in NAME_ALIASES), None)
        signal_col = next(
            (j for j, c in enumerate(normed) if c in JOIN_ALIASES | LEAVE_ALIASES | DURATION_ALIASES),
            None,
        )
        if name_col is not None and signal_col is not None:
            header_idx = i
            col_for = {
                "name": name_col,
                "join": next((j for j, c in enumerate(normed) if c in JOIN_ALIASES), None),
                "leave": next((j for j, c in enumerate(normed) if c in LEAVE_ALIASES), None),
                "duration": next((j for j, c in enumerate(normed) if c in DURATION_ALIASES), None),
                "email": next((j for j, c in enumerate(normed) if c in EMAIL_ALIASES), None),
            }
            break

    outcome = {"date": None, "title": _meeting_title(rows[:header_idx] if header_idx else rows),
               "participants": [], "warning": None}

    if header_idx is None:
        outcome["warning"] = f"{path.name}: couldn't find a participant table (no recognized header row) -- skipped."
        return outcome

    seen_in_file = set()
    for row in rows[header_idx + 1:]:
        if not row or all(not c.strip() for c in row):
            break  # blank line -- end of the participant table (another section may follow)
        if len(row) <= col_for["name"]:
            continue
        name = row[col_for["name"]].strip()
        if not name:
            continue
        email = row[col_for["email"]].strip() if col_for["email"] is not None and len(row) > col_for["email"] else ""
        duration = (
            _parse_duration_minutes(row[col_for["duration"]])
            if col_for["duration"] is not None and len(row) > col_for["duration"] else 0.0
        )
        key = (email or name).lower()
        if key in seen_in_file:
            # Same person listed twice in one export (e.g. rejoined) --
            # keep them present once, summing their time in the room.
            for p in outcome["participants"]:
                if (p["email"] or p["name"]).lower() == key:
                    p["duration_minutes"] += duration
                    break
            continue
        seen_in_file.add(key)
        outcome["participants"].append({"name": name, "email": email, "duration_minutes": duration})

    outcome["date"] = _date_from_filename(path) or _date_from_summary(rows[:header_idx])
    if outcome["date"] is None:
        outcome["date"] = date.fromtimestamp(path.stat().st_mtime)
        outcome["warning"] = (
            f"{path.name}: no date in the filename or a \"Meeting start time\" summary row -- "
            f"used the file's last-modified date ({outcome['date'].isoformat()}) instead. "
            "Rename the file to include a YYYY-MM-DD if that's wrong."
        )

    return outcome


# --------------------------------------------------------------------------- aggregation

def discover_csv_files(folder: Path, pattern: str) -> list:
    return sorted(folder.glob(pattern))


def aggregate_sessions(files: list) -> tuple:
    """Parses every file, merges same-day files together (summing
    duration, union of participants), and returns
    (date_strs, titles_by_date, {person_key: {"name","email","minutes_by_date"}}, warnings)."""
    by_date = defaultdict(list)  # date -> [participant dicts]
    titles = {}
    warnings = []

    for path in files:
        session = parse_attendance_csv(path)
        if session["warning"]:
            warnings.append(session["warning"])
        if not session["participants"]:
            continue
        d = session["date"]
        by_date[d].extend(session["participants"])
        if session["title"] and d not in titles:
            titles[d] = session["title"]

    date_strs = sorted(d.isoformat() for d in by_date)

    people = {}
    for d in by_date:
        for p in by_date[d]:
            key = (p["email"] or p["name"]).lower()
            rec = people.setdefault(key, {"name": p["name"], "email": p["email"], "minutes_by_date": {}})
            rec["minutes_by_date"][d.isoformat()] = rec["minutes_by_date"].get(d.isoformat(), 0.0) + p["duration_minutes"]
            if p["email"] and not rec["email"]:
                rec["email"] = p["email"]

    return date_strs, {d.isoformat(): titles.get(d) for d in by_date}, people, warnings


# --------------------------------------------------------------------------- report building

HEADER_FILL = PatternFill("solid", fgColor="1F2933")
STAGE_FILL = PatternFill("solid", fgColor="334155")
PRESENT_FILL = PatternFill("solid", fgColor="C6EFCE")
ABSENT_FILL = PatternFill("solid", fgColor="FFC7CE")
HEADER_FONT = Font(color="FFFFFF", bold=True)


def _autosize(ws, min_width=4, max_width=28):
    widths = {}
    for row in ws.iter_rows():
        for cell in row:
            if cell.value is None:
                continue
            widths[cell.column_letter] = max(widths.get(cell.column_letter, min_width), min(len(str(cell.value)) + 2, max_width))
    for col, width in widths.items():
        ws.column_dimensions[col].width = width


def _write_attendance_sheet(wb, date_strs: list, people: dict, present_only: bool):
    """The "exercises-like" grid: one row per person, one column per
    session date. present_only=True -> PASS/FAIL-style Present/blank grid
    (this is "attendance per date"); False -> the same shape with minutes
    attended in each cell instead (a richer duration view)."""
    title = "Attendance" if present_only else "Duration (minutes)"
    ws = wb.create_sheet(title)

    ws.cell(row=1, column=1, value="Name").font = HEADER_FONT
    ws.cell(row=1, column=1).fill = HEADER_FILL
    ws.cell(row=1, column=2, value="Email").font = HEADER_FONT
    ws.cell(row=1, column=2).fill = HEADER_FILL

    date_cols = {}
    for i, d in enumerate(date_strs):
        col = 3 + i
        date_cols[d] = col
        c = ws.cell(row=1, column=col, value=d)
        c.font = HEADER_FONT
        c.fill = HEADER_FILL
        c.alignment = Alignment(horizontal="center")

    sorted_people = sorted(people.values(), key=lambda p: p["name"].lower())
    r = 2
    for person in sorted_people:
        ws.cell(row=r, column=1, value=person["name"])
        ws.cell(row=r, column=2, value=person["email"])
        for d, col in date_cols.items():
            minutes = person["minutes_by_date"].get(d)
            present = minutes is not None
            if present_only:
                cell = ws.cell(row=r, column=col, value="Present" if present else "")
            else:
                cell = ws.cell(row=r, column=col, value=round(minutes, 1) if present else "")
            cell.fill = PRESENT_FILL if present else ABSENT_FILL
            cell.alignment = Alignment(horizontal="center")
        r += 1

    footer_row = r
    ws.cell(row=footer_row, column=2, value="Attended by").font = Font(italic=True)
    for d, col in date_cols.items():
        n_present = sum(1 for p in sorted_people if d in p["minutes_by_date"])
        ws.cell(row=footer_row, column=col, value=n_present).alignment = Alignment(horizontal="center")

    ws.freeze_panes = "C2"
    _autosize(ws)
    return ws


def _write_summary_sheet(wb, date_strs: list, people: dict):
    ws = wb.create_sheet("Summary", 0)
    headers = ["Name", "Email", "Sessions Attended", "Total Sessions", "Attendance %",
               "Total Minutes", "Avg Minutes/Session", "First Session", "Last Session"]
    for c, h in enumerate(headers, start=1):
        cell = ws.cell(row=1, column=c, value=h)
        cell.font = HEADER_FONT
        cell.fill = HEADER_FILL
        cell.alignment = Alignment(horizontal="center")

    n_sessions = len(date_strs)
    sorted_people = sorted(people.values(), key=lambda p: p["name"].lower())
    r = 2
    for person in sorted_people:
        attended_dates = sorted(person["minutes_by_date"])
        n_attended = len(attended_dates)
        total_minutes = sum(person["minutes_by_date"].values())
        values = [
            person["name"], person["email"],
            n_attended, n_sessions,
            (n_attended / n_sessions) if n_sessions else 0,
            round(total_minutes, 1),
            round(total_minutes / n_attended, 1) if n_attended else 0,
            attended_dates[0] if attended_dates else "",
            attended_dates[-1] if attended_dates else "",
        ]
        for c, v in enumerate(values, start=1):
            cell = ws.cell(row=r, column=c, value=v)
            cell.alignment = Alignment(horizontal="center")
            if c == 5:
                cell.number_format = "0%"
        r += 1

    last_row = r - 1
    if last_row >= 2:
        rule = ColorScaleRule(
            start_type="min", start_color="FFC7CE",
            mid_type="percentile", mid_value=50, mid_color="FFEB9C",
            end_type="max", end_color="C6EFCE",
        )
        ws.conditional_formatting.add(f"E2:E{last_row}", rule)

    # Class-wide, per-session total attendance footer.
    footer_row = last_row + 2
    ws.cell(row=footer_row, column=1, value="Total attendance per session:").font = Font(italic=True, bold=True)
    for i, d in enumerate(date_strs):
        n_present = sum(1 for p in sorted_people if d in p["minutes_by_date"])
        c = ws.cell(row=footer_row + 1 + i, column=1, value=d)
        ws.cell(row=footer_row + 1 + i, column=2, value=n_present)

    ws.freeze_panes = "A2"
    _autosize(ws)

    if sorted_people:
        chart = BarChart()
        chart.type = "bar"
        chart.title = "Attendance % by person"
        chart.style = 10
        chart.width = 22
        chart.height = max(8, len(sorted_people) * 0.6)
        data = Reference(ws, min_col=5, max_col=5, min_row=1, max_row=last_row)
        cats = Reference(ws, min_col=1, max_col=1, min_row=2, max_row=last_row)
        chart.add_data(data, titles_from_data=True)
        chart.set_categories(cats)
        chart.legend = None
        ws.add_chart(chart, f"A{footer_row + len(date_strs) + 3}")

    return ws


def build_workbook(date_strs: list, people: dict) -> "openpyxl.Workbook":
    wb = openpyxl.Workbook()
    wb.remove(wb.active)
    _write_summary_sheet(wb, date_strs, people)
    _write_attendance_sheet(wb, date_strs, people, present_only=True)
    _write_attendance_sheet(wb, date_strs, people, present_only=False)
    return wb


# --------------------------------------------------------------------------- main

def main():
    parser = argparse.ArgumentParser(
        description="Generate an Excel attendance report from a folder of Teams attendance CSVs.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "examples:\n"
            "  python tools/attendance_report.py /path/to/csvs\n"
            "  python tools/attendance_report.py /path/to/csvs --output attendance.xlsx\n"
            "  python tools/attendance_report.py /path/to/csvs --pattern \"Attendance-*.csv\"\n"
        ),
    )
    parser.add_argument("path", help="Folder containing one Teams attendance .csv export per session")
    parser.add_argument("--pattern", default="*.csv", help='Glob pattern for attendance files within that folder (default: "*.csv")')
    parser.add_argument("--output", default="attendance.xlsx", help="Output .xlsx path (default: attendance.xlsx)")
    args = parser.parse_args()

    folder = Path(args.path)
    if not folder.is_dir():
        print(f"{folder} is not a directory.", file=sys.stderr)
        sys.exit(1)

    files = discover_csv_files(folder, args.pattern)
    if not files:
        print(f"No files matching {args.pattern!r} in {folder}.", file=sys.stderr)
        sys.exit(1)

    print(f"Found {len(files)} attendance file(s) in {folder}.")
    date_strs, titles, people, warnings = aggregate_sessions(files)

    for w in warnings:
        print(f"WARNING: {w}", file=sys.stderr)

    if not date_strs:
        print("No sessions with a recognized participant table were found -- nothing to report.", file=sys.stderr)
        sys.exit(1)

    print(f"{len(date_strs)} session(s), {len(people)} unique attendee(s).")
    for d in date_strs:
        n_present = sum(1 for p in people.values() if d in p["minutes_by_date"])
        title = f" -- {titles[d]}" if titles.get(d) else ""
        print(f"  {d}{title}: {n_present} present")

    wb = build_workbook(date_strs, people)
    wb.save(args.output)
    print(f"\nWrote {args.output} ({len(date_strs)} sessions, {len(people)} attendees).")


if __name__ == "__main__":
    main()
