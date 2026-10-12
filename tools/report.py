"""
Generates a per-student progress report as an Excel workbook.

Each student works on their own branch named "<group>/<user_id>" (e.g.
"group1/orgutier" -- see README.md, "Progress reports"). This script
fetches every branch matching that shape, checks each one out into a
throwaway git worktree, runs THIS checkout's own test suite (never the
student's copy of it -- see "Why the canonical test suite" below) against
their exercises/, challenges/, and exams/ trees, and writes the pass/fail
results into report.xlsx: one row per student, one column per exercise
(grouped by stage) on one sheet, one column per challenge (grouped by
stage) on another, one column per exam on a third, and a Summary sheet
with solved/total counts for all three.

Usage (from the repo root):
    python tools/report.py
    python tools/report.py --pattern "cohort2025-*/*" --output cohort2025.xlsx
    python tools/report.py --skip-fetch --workers 8
    python tools/report.py --local                     # use local branches, no fetch

Run `python tools/report.py --help` for every option.

Why the canonical test suite
-----------------------------
tests/ is staff-authored and explicitly not meant to be edited by
trainees (see README.md, "Structure"). A student's branch might still
have an outdated or (accidentally or not) modified copy of it. Trusting
it would mean every student is graded by a different rubric. So for each
branch this script only reads exercises/ and challenges/ (their actual
solutions) and overlays THIS checkout's own tests/ and conftest.py on
top before running pytest -- every student is graded against the exact
same, current test suite, regardless of what's sitting in their branch's
tests/ directory.

A student branch that predates a given exercise/challenge (e.g. it
branched off before Stage 14 existed) simply doesn't have that
exercises/stageNN/exerciseXX/ folder -- the corresponding test file fails
to import and is recorded as not solved. That's a known, accepted
limitation: this reports what currently passes, not intent or timing.
"""
import argparse
import concurrent.futures
import fnmatch
import re
import shutil
import subprocess
import sys
import tempfile
import threading
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from core import REPO_ROOT, EXERCISES, CHALLENGES, EXAMS  # noqa: E402

try:
    import openpyxl
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.utils import get_column_letter
    from openpyxl.formatting.rule import ColorScaleRule
except ImportError:
    print(
        "openpyxl is required to write the .xlsx report -- "
        "pip install -r requirements.txt",
        file=sys.stderr,
    )
    raise

DEFAULT_EXCLUDE = ["HEAD", "main", "master", "claude/*", "dependabot/*", "renovate/*", "gh-pages"]

_WORKTREE_LOCK = threading.Lock()
_PRINT_LOCK = threading.Lock()


# --------------------------------------------------------------------------- branch discovery

def discover_branches(remote: str, pattern: str, exclude: list, local: bool) -> list:
    """Every "group/user" branch under refs/heads (local) or
    refs/remotes/<remote> (default), matching `pattern` and not matching
    any glob in `exclude`. Returns [(group, user, ref), ...] sorted."""
    ref_root = "refs/heads/" if local else f"refs/remotes/{remote}/"
    result = subprocess.run(
        ["git", "for-each-ref", ref_root, "--format=%(refname:lstrip=2)" if local else "--format=%(refname:lstrip=3)"],
        cwd=REPO_ROOT, capture_output=True, text=True, check=True,
    )
    branches = []
    for name in result.stdout.splitlines():
        name = name.strip()
        if not name or name == "HEAD":
            continue
        if any(fnmatch.fnmatch(name, pat) for pat in exclude):
            continue
        if not fnmatch.fnmatch(name, pattern):
            continue
        group, sep, user = name.partition("/")
        if not sep or "/" in user:
            # No slash at all, or more than one -- doesn't match the
            # "group/user_id" shape this script expects. Skip it rather
            # than guess.
            continue
        ref = name if local else f"{remote}/{name}"
        branches.append((group, user, ref))
    return sorted(branches)


def fetch_remote(remote: str) -> None:
    print(f"Fetching {remote}...")
    subprocess.run(["git", "fetch", remote, "--prune"], cwd=REPO_ROOT, check=True)


# --------------------------------------------------------------------------- per-student test run

def run_student_tests(ref: str, exercise_ids: list, challenge_ids: list, exam_ids: list) -> dict:
    """Check out `ref` into a throwaway worktree, overlay this checkout's
    tests/ + conftest.py, run every exercise's, challenge's, and exam's own
    test file, and return {"exercises": {id: bool}, "challenges": {id: bool},
    "exams": {id: bool}, "error": str | None}."""
    worktree_dir = Path(tempfile.mkdtemp(prefix="pt-report-"))
    outcome = {"exercises": {}, "challenges": {}, "exams": {}, "error": None}
    added = False
    try:
        with _WORKTREE_LOCK:
            result = subprocess.run(
                ["git", "worktree", "add", "--detach", "--force", str(worktree_dir), ref],
                cwd=REPO_ROOT, capture_output=True, text=True,
            )
        if result.returncode != 0:
            outcome["error"] = f"git worktree add failed: {result.stderr.strip()}"
            return outcome
        added = True

        shutil.rmtree(worktree_dir / "tests", ignore_errors=True)
        shutil.copytree(REPO_ROOT / "tests", worktree_dir / "tests")
        shutil.copy2(REPO_ROOT / "conftest.py", worktree_dir / "conftest.py")

        for ex_id in exercise_ids:
            outcome["exercises"][ex_id] = _run_one_test_file(worktree_dir, f"tests/test_{ex_id}.py")
        for ch_id in challenge_ids:
            outcome["challenges"][ch_id] = _run_one_test_file(worktree_dir, f"tests/test_{ch_id}.py")
        for exam_id in exam_ids:
            outcome["exams"][exam_id] = _run_one_test_file(worktree_dir, f"tests/test_{exam_id}.py")
    except Exception as e:  # noqa: BLE001 -- one bad branch must not kill the whole report run
        outcome["error"] = f"{type(e).__name__}: {e}"
    finally:
        if added:
            with _WORKTREE_LOCK:
                subprocess.run(
                    ["git", "worktree", "remove", "--force", str(worktree_dir)],
                    cwd=REPO_ROOT, capture_output=True,
                )
        shutil.rmtree(worktree_dir, ignore_errors=True)
    return outcome


def _run_one_test_file(worktree_dir: Path, relative_path: str) -> bool:
    if not (worktree_dir / relative_path).exists():
        return False
    result = subprocess.run(
        [sys.executable, "-m", "pytest", relative_path, "-q"],
        cwd=worktree_dir, capture_output=True, text=True,
    )
    return result.returncode == 0


# --------------------------------------------------------------------------- stage grouping

def exercise_stage(exercise_id: str) -> str:
    return exercise_id.split("_", 1)[0]


def challenge_stage(challenge_id: str) -> str:
    """The stage a challenge belongs to, read from its own README.md's
    "Do this after: Stage NN" line -- not hardcoded, so this stays correct
    even if the challenges-per-stage convention ever changes."""
    readme = REPO_ROOT / "challenges" / challenge_id / "README.md"
    if readme.exists():
        m = re.search(r"Stage (\d+)", readme.read_text())
        if m:
            return f"stage{int(m.group(1)):02d}"
    return "unknown"


def exam_label(exam_id: str) -> str:
    """A short column header for an exam, e.g. "Exam 1 (Stages 1-4)", read
    from its own README.md's "Covers: Stages NN-NN" line when present."""
    readme = REPO_ROOT / "exams" / exam_id / "README.md"
    n = int(exam_id.replace("exam", ""))
    if readme.exists():
        m = re.search(r"Covers: Stages (\d+-\d+)", readme.read_text())
        if m:
            return f"Exam {n} (Stages {m.group(1)})"
    return f"Exam {n}"


# --------------------------------------------------------------------------- report building

HEADER_FILL = PatternFill("solid", fgColor="1F2933")
STAGE_FILL = PatternFill("solid", fgColor="334155")
PASS_FILL = PatternFill("solid", fgColor="C6EFCE")
FAIL_FILL = PatternFill("solid", fgColor="FFC7CE")
ERROR_FILL = PatternFill("solid", fgColor="FFEB9C")
HEADER_FONT = Font(color="FFFFFF", bold=True)
THIN_BORDER = Border(*(Side(style="thin", color="D0D0D0"),) * 4)


def _autosize(ws, min_width=4, max_width=28):
    widths = {}
    for row in ws.iter_rows():
        for cell in row:
            if cell.value is None:
                continue
            col = cell.column_letter
            widths[col] = max(widths.get(col, min_width), min(len(str(cell.value)) + 2, max_width))
    for col, width in widths.items():
        ws.column_dimensions[col].width = width


def _write_grid_sheet(wb, title: str, rows: list, ids: list, stage_of, results_key: str):
    ws = wb.create_sheet(title)
    id_cols = {id_: 3 + i for i, id_ in enumerate(ids)}

    ws.cell(row=1, column=1, value="Group").font = HEADER_FONT
    ws.cell(row=1, column=2, value="User").font = HEADER_FONT
    ws.cell(row=2, column=1, value="").fill = HEADER_FILL
    ws.cell(row=2, column=2, value="").fill = HEADER_FILL
    for col in (1, 2):
        ws.cell(row=1, column=col).fill = HEADER_FILL
        ws.merge_cells(start_row=1, start_column=col, end_row=2, end_column=col)

    # Stage-grouped merged header row, then one sub-header per id.
    stages_in_order = []
    for id_ in ids:
        w = stage_of(id_)
        if not stages_in_order or stages_in_order[-1] != w:
            stages_in_order.append(w)
    stage_start_col = {}
    col = 3
    for id_ in ids:
        w = stage_of(id_)
        stage_start_col.setdefault(w, col)
        col += 1
    col = 3
    prev_stage = None
    for id_ in ids:
        w = stage_of(id_)
        if w != prev_stage:
            span_ids = [i for i in ids if stage_of(i) == w]
            start = stage_start_col[w]
            end = start + len(span_ids) - 1
            cell = ws.cell(row=1, column=start, value=w.replace("stage", "Stage "))
            cell.font = HEADER_FONT
            cell.fill = STAGE_FILL
            cell.alignment = Alignment(horizontal="center")
            if end > start:
                ws.merge_cells(start_row=1, start_column=start, end_row=1, end_column=end)
            prev_stage = w
        is_exercise = id_.startswith("stage")
        short_label = id_.split("_", 1)[1] if is_exercise else id_.replace("challenge", "")
        label = ("Ex " + short_label) if is_exercise else ("Ch " + short_label)
        c = ws.cell(row=2, column=col, value=label)
        c.font = HEADER_FONT
        c.fill = HEADER_FILL
        c.alignment = Alignment(horizontal="center")
        col += 1

    r = 3
    for row_data in rows:
        ws.cell(row=r, column=1, value=row_data["group"])
        ws.cell(row=r, column=2, value=row_data["user"])
        if row_data["error"]:
            for id_, cc in id_cols.items():
                cell = ws.cell(row=r, column=cc, value="ERROR")
                cell.fill = ERROR_FILL
                cell.alignment = Alignment(horizontal="center")
                cell.border = THIN_BORDER
        else:
            for id_, cc in id_cols.items():
                passed = row_data[results_key].get(id_, False)
                cell = ws.cell(row=r, column=cc, value="PASS" if passed else "")
                cell.fill = PASS_FILL if passed else FAIL_FILL
                cell.alignment = Alignment(horizontal="center")
                cell.border = THIN_BORDER
        r += 1

    # Class-wide solve-rate footer row.
    footer_row = r
    ws.cell(row=footer_row, column=2, value="Solved by").font = Font(italic=True)
    for id_, cc in id_cols.items():
        n_solved = sum(
            1 for row_data in rows
            if not row_data["error"] and row_data[results_key].get(id_, False)
        )
        ws.cell(row=footer_row, column=cc, value=n_solved).alignment = Alignment(horizontal="center")

    ws.freeze_panes = "C3"
    _autosize(ws)
    return ws


def _write_flat_grid_sheet(wb, title: str, rows: list, ids: list, label_of, results_key: str):
    """Same PASS/FAIL grid as _write_grid_sheet, but a single header row
    with no stage-grouping -- for exams, which each span several stages
    rather than belonging to just one."""
    ws = wb.create_sheet(title)
    id_cols = {id_: 3 + i for i, id_ in enumerate(ids)}

    ws.cell(row=1, column=1, value="Group").font = HEADER_FONT
    ws.cell(row=1, column=2, value="User").font = HEADER_FONT
    for col in (1, 2):
        ws.cell(row=1, column=col).fill = HEADER_FILL

    for id_, cc in id_cols.items():
        c = ws.cell(row=1, column=cc, value=label_of(id_))
        c.font = HEADER_FONT
        c.fill = HEADER_FILL
        c.alignment = Alignment(horizontal="center")

    r = 2
    for row_data in rows:
        ws.cell(row=r, column=1, value=row_data["group"])
        ws.cell(row=r, column=2, value=row_data["user"])
        if row_data["error"]:
            for id_, cc in id_cols.items():
                cell = ws.cell(row=r, column=cc, value="ERROR")
                cell.fill = ERROR_FILL
                cell.alignment = Alignment(horizontal="center")
                cell.border = THIN_BORDER
        else:
            for id_, cc in id_cols.items():
                passed = row_data[results_key].get(id_, False)
                cell = ws.cell(row=r, column=cc, value="PASS" if passed else "")
                cell.fill = PASS_FILL if passed else FAIL_FILL
                cell.alignment = Alignment(horizontal="center")
                cell.border = THIN_BORDER
        r += 1

    footer_row = r
    ws.cell(row=footer_row, column=2, value="Solved by").font = Font(italic=True)
    for id_, cc in id_cols.items():
        n_solved = sum(
            1 for row_data in rows
            if not row_data["error"] and row_data[results_key].get(id_, False)
        )
        ws.cell(row=footer_row, column=cc, value=n_solved).alignment = Alignment(horizontal="center")

    ws.freeze_panes = "C2"
    _autosize(ws)
    return ws


def _write_summary_sheet(wb, rows: list, n_exercises: int, n_challenges: int, n_exams: int):
    ws = wb.create_sheet("Summary", 0)
    headers = ["Group", "User", "Branch", "Exercises Solved", "Exercises Total", "Exercises %",
               "Challenges Solved", "Challenges Total", "Challenges %",
               "Exams Solved", "Exams Total", "Exams %", "Status"]
    for c, h in enumerate(headers, start=1):
        cell = ws.cell(row=1, column=c, value=h)
        cell.font = HEADER_FONT
        cell.fill = HEADER_FILL
        cell.alignment = Alignment(horizontal="center")

    r = 2
    for row_data in rows:
        ex_solved = sum(1 for v in row_data["exercises"].values() if v)
        ch_solved = sum(1 for v in row_data["challenges"].values() if v)
        exam_solved = sum(1 for v in row_data["exams"].values() if v)
        status = row_data["error"] or "ok"
        values = [
            row_data["group"], row_data["user"], row_data["branch"],
            ex_solved, n_exercises,
            (ex_solved / n_exercises) if n_exercises else 0,
            ch_solved, n_challenges,
            (ch_solved / n_challenges) if n_challenges else 0,
            exam_solved, n_exams,
            (exam_solved / n_exams) if n_exams else 0,
            status,
        ]
        for c, v in enumerate(values, start=1):
            cell = ws.cell(row=r, column=c, value=v)
            if c in (6, 9, 12):
                cell.number_format = "0%"
        r += 1

    last_row = r - 1
    if last_row >= 2:
        for col_letter in ("F", "I", "L"):
            rule = ColorScaleRule(
                start_type="min", start_color="FFC7CE",
                mid_type="percentile", mid_value=50, mid_color="FFEB9C",
                end_type="max", end_color="C6EFCE",
            )
            ws.conditional_formatting.add(f"{col_letter}2:{col_letter}{last_row}", rule)

    ws.freeze_panes = "A2"
    _autosize(ws)
    return ws


def build_workbook(rows: list, exercise_ids: list, challenge_ids: list, exam_ids: list):
    wb = openpyxl.Workbook()
    wb.remove(wb.active)
    _write_summary_sheet(wb, rows, len(exercise_ids), len(challenge_ids), len(exam_ids))
    _write_grid_sheet(wb, "Exercises", rows, exercise_ids, exercise_stage, "exercises")
    _write_grid_sheet(wb, "Challenges", rows, challenge_ids, challenge_stage, "challenges")
    _write_flat_grid_sheet(wb, "Exams", rows, exam_ids, exam_label, "exams")
    return wb


# --------------------------------------------------------------------------- main

def main():
    parser = argparse.ArgumentParser(
        description="Generate an Excel progress report from every student's group/user_id branch.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "examples:\n"
            "  python tools/report.py\n"
            "  python tools/report.py --pattern \"cohort2025-*/*\" --output cohort2025.xlsx\n"
            "  python tools/report.py --skip-fetch --workers 8\n"
            "  python tools/report.py --local\n"
        ),
    )
    parser.add_argument("--remote", default="origin", help="Remote to fetch/read branches from (default: origin)")
    parser.add_argument("--pattern", default="*/*", help='fnmatch pattern for "group/user_id" branch names (default: */*)')
    parser.add_argument("--exclude", default=",".join(DEFAULT_EXCLUDE),
                         help=f"Comma-separated glob patterns to always exclude (default: {','.join(DEFAULT_EXCLUDE)})")
    parser.add_argument("--output", default="report.xlsx", help="Output .xlsx path (default: report.xlsx)")
    parser.add_argument("--workers", type=int, default=4, help="Branches to test in parallel (default: 4)")
    parser.add_argument("--skip-fetch", action="store_true", help="Don't run 'git fetch' first; use what's already local")
    parser.add_argument("--local", action="store_true", help="Read local branches (refs/heads) instead of a remote's")
    args = parser.parse_args()

    exclude = [p.strip() for p in args.exclude.split(",") if p.strip()]

    if not args.skip_fetch and not args.local:
        fetch_remote(args.remote)

    branches = discover_branches(args.remote, args.pattern, exclude, args.local)
    if not branches:
        print(
            f"No branches matched pattern {args.pattern!r} "
            f"(after excluding {exclude}). Nothing to report.",
            file=sys.stderr,
        )
        sys.exit(1)

    print(f"Found {len(branches)} student branch(es): " + ", ".join(f"{g}/{u}" for g, u, _ in branches))

    exercise_ids = list(EXERCISES)
    challenge_ids = list(CHALLENGES)
    exam_ids = list(EXAMS)
    total = len(exercise_ids) + len(challenge_ids) + len(exam_ids)

    rows = []
    done = 0

    def _work(item):
        group, user, ref = item
        outcome = run_student_tests(ref, exercise_ids, challenge_ids, exam_ids)
        return group, user, ref, outcome

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = [executor.submit(_work, item) for item in branches]
        for future in concurrent.futures.as_completed(futures):
            group, user, ref, outcome = future.result()
            done += 1
            with _PRINT_LOCK:
                if outcome["error"]:
                    print(f"[{done}/{len(branches)}] {group}/{user}: ERROR -- {outcome['error']}")
                else:
                    ex_solved = sum(1 for v in outcome["exercises"].values() if v)
                    ch_solved = sum(1 for v in outcome["challenges"].values() if v)
                    exam_solved = sum(1 for v in outcome["exams"].values() if v)
                    print(
                        f"[{done}/{len(branches)}] {group}/{user}: "
                        f"{ex_solved}/{len(exercise_ids)} exercises, "
                        f"{ch_solved}/{len(challenge_ids)} challenges, "
                        f"{exam_solved}/{len(exam_ids)} exams"
                    )
            rows.append({
                "group": group, "user": user, "branch": ref,
                "exercises": outcome["exercises"], "challenges": outcome["challenges"],
                "exams": outcome["exams"], "error": outcome["error"],
            })

    rows.sort(key=lambda r: (r["group"], r["user"]))

    wb = build_workbook(rows, exercise_ids, challenge_ids, exam_ids)
    wb.save(args.output)
    print(f"\nWrote {args.output} ({total} tracked exercises/challenges/exams, {len(rows)} students).")


if __name__ == "__main__":
    main()
