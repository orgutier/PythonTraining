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

It also builds a day-by-day telemetry history of exercises solved per
branch -- see "Daily telemetry" below -- written as three more sheets:
Daily Progress (a cumulative solved-count table, one column per branch,
plus a line chart), Daily Delta (the same grid but day-over-day new
exercises solved, plus a class-wide daily total), and Leaderboard (one
row per branch -- total solved, first/last commit, days active,
average/day, best single day -- sorted so the most-progressed branch is
the top row and the least-progressed is the bottom, plus a bar chart of
the same ranking).

Usage (from the repo root):
    python tools/report.py
    python tools/report.py --pattern "cohort2025-*/*" --output cohort2025.xlsx
    python tools/report.py --skip-fetch --workers 8
    python tools/report.py --local                     # use local branches, no fetch
    python tools/report.py --history-days 14            # only the last 2 weeks of history
    python tools/report.py --no-history                 # skip the daily telemetry pass entirely
    python tools/report.py --reference origin/main      # diff baseline (this is already the default)
    python tools/report.py --no-diff-skip               # test every file for every branch (slower, for debugging)
    python tools/report.py --no-baseline-cache           # always re-test the reference branch, ignore any cache
    python tools/report.py --no-branch-cache             # always re-test every student branch, ignore any cache
    python tools/report.py --assume-reference-fails      # skip testing the reference branch, assume it fails everything

Run `python tools/report.py --help` for every option.

Skipping untouched files
-----------------------------
Before grading any student branch, the reference branch (`--reference`,
default "origin/main", or "main" with --local) is graded once itself --
one worktree-and-pytest run, same as any other branch. Then, for each
student branch, a single cheap `git diff --name-only` (no worktree)
against that reference finds which exercise/challenge/exam solution.py
files actually differ from it.

A solution.py the student hasn't touched is byte-identical to the
reference's own copy, and since both are graded against the exact same
overlaid tests/ (see "Why the canonical test suite" below), an unchanged
file is *guaranteed* to produce whatever result the reference branch
itself got for that id -- so it's never re-tested; that id's result is
just copied from the one-time reference run. Only files a student has
actually edited get their own pytest run. Early in a rolling course, most
of a branch's tree (every stage they haven't reached yet) is still an
untouched copy of the reference's skeleton, so this tends to cut the
current-state pass down to roughly "one pytest run per file the student
has actually written" rather than one per tracked exercise/challenge/exam
id, for every branch. `--no-diff-skip` disables this and tests every file
for every branch, as this script always worked before this optimization.

The reference run itself can't skip anything -- there's nothing to diff
it against -- so every ref's result (the reference branch's, and every
student branch's) is cached on disk in .cache/report_test_cache/
(gitignored) under that ref's *resolved commit*. A later run against a
commit that's already cached -- a student branch nobody has touched
since last time, just as much as the reference branch itself -- skips
re-testing it entirely: not even the diff against the reference branch,
let alone pytest. The cache key also folds in this checkout's own
tests/+conftest.py content (see tests_fingerprint), so fixing a test
invalidates every cached result that fix could affect, rather than a
stale pass/fail surviving a rubric change; a new commit on a branch, or
a changed set of tracked ids, invalidates it the same way. `--no-
baseline-cache` ignores the cache for the reference branch specifically;
`--no-branch-cache` ignores it for every student branch; either forces a
fresh test regardless of what's on disk. `--assume-reference-fails`
skips testing the reference branch at all, trusting that it's always an
unsolved skeleton (true by how this course is run -- everyone branches
from it) -- fastest even on an uncached first run, but silently wrong
the moment that assumption isn't (e.g. --reference points somewhere
that already has working code). Prefer the cache; reach for that flag
only when you're confident and want to skip even that.

Daily telemetry
-----------------------------
Re-grading a branch's entire history, one worktree-and-pytest run per
distinct commit-day, used to be how this pass worked -- correct, but
expensive enough to multiply the script's total running time by roughly
the number of distinct commit-days across all branches.

It doesn't need to run pytest at all. The current-state pass above
already knows, as of each branch's tip, exactly which exercises pass. For
each of those *passing* exercises, `git log --follow --name-only` (one
call per branch, no worktree) finds the last commit date its own
solution.py was modified on that branch. Since that file hasn't changed
since that date, and it's known to pass as of the tip (same content,
same overlaid tests/), it necessarily already passed as of that date too
-- so that date IS the day the exercise became solved, with no need to
re-test anything to find out. Challenges/exams are still left out of this
pass (exercises are what "day to day progress" means here).

`--history-days N` (default 30) bounds how far back the resulting sheets
show; `--history-days 0` means the branch's entire history (now cheap
either way, since it no longer re-tests anything). `--no-history` skips
this pass entirely and produces just the current-state sheets, same as
before this feature existed.

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
import hashlib
import json
import re
import shutil
import statistics
import subprocess
import sys
import tempfile
import threading
import time
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from core import REPO_ROOT, EXERCISES, CHALLENGES, EXAMS  # noqa: E402

try:
    import openpyxl
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.utils import get_column_letter
    from openpyxl.formatting.rule import ColorScaleRule
    from openpyxl.chart import BarChart, LineChart, Reference
except ImportError:
    print(
        "openpyxl is required to write the .xlsx report -- "
        "pip install -r requirements.txt",
        file=sys.stderr,
    )
    raise

# stdout is fully block-buffered (not line-buffered) whenever it isn't a
# terminal -- piped to a file/tee, or captured by a CI/log viewer. Without
# this, a long silent stretch (the reference-branch baseline below; any
# slow pytest run) just sits in the buffer and only appears once it's
# flushed, which can make a script that's actually working look hung.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(line_buffering=True)

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

def _solution_path(id_: str, kind: str) -> str:
    """Repo-relative path (git-diff/git-log style, forward slashes) to the
    one solution.py a given exercise/challenge/exam id's test file
    imports -- see "Why the canonical test suite": every test file in
    tests/ imports exactly one solution.py, so that file's own history is
    all that matters for diffing or dating that id. `kind` is one of
    "exercises"/"challenges"/"exams" (matching run_student_tests' outcome
    dict keys)."""
    if kind == "exercises":
        stage, _, name = id_.partition("_")
        return f"exercises/{stage}/{name}/solution.py"
    if kind == "challenges":
        return f"challenges/{id_}/solution.py"
    return f"exams/{id_}/solution.py"


def discover_changed_paths(ref_a: str, ref_b: str):
    """Repo-relative paths whose content differs between two refs -- a
    plain tree-to-tree `git diff`, no worktree needed. Returns None if the
    diff itself fails (e.g. a bad ref), signaling the caller to fall back
    to testing everything rather than silently trust a broken diff."""
    result = subprocess.run(
        ["git", "diff", "--name-only", ref_a, ref_b],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )
    if result.returncode != 0:
        return None
    return set(result.stdout.splitlines())


def _resolve_sha(ref: str) -> str:
    """The commit `ref` currently points at, or None if `ref` doesn't
    resolve (a bad branch name, etc.)."""
    result = subprocess.run(["git", "rev-parse", ref], cwd=REPO_ROOT, capture_output=True, text=True)
    return result.stdout.strip() if result.returncode == 0 else None


def _commit_cache_path(sha: str) -> Path:
    """One cache file per commit (not one shared file) -- cheap, and
    lets many branches' results be saved concurrently (ThreadPoolExecutor
    workers each touch their own branch's own sha's file, so there's no
    shared-file write race to guard against)."""
    return REPO_ROOT / ".cache" / "report_test_cache" / f"{sha}.json"


def tests_fingerprint() -> str:
    """A content hash of THIS checkout's own tests/ + conftest.py -- the
    canonical overlay every worktree gets (see "Why the canonical test
    suite"). Part of every cache key below, so editing a test (fixing a
    bug in one, say) invalidates every cached result that rubric change
    could affect, rather than a stale pass/fail surviving it."""
    digest = hashlib.sha256()
    paths = sorted((REPO_ROOT / "tests").rglob("*.py")) + [REPO_ROOT / "conftest.py"]
    for p in paths:
        digest.update(p.read_bytes())
    return digest.hexdigest()


def load_cached_outcome(ref: str, exercise_ids: list, challenge_ids: list, exam_ids: list,
                        tests_fp: str):
    """A cached test outcome for `ref`'s exact current commit (see
    save_cached_outcome), reused only if the exact set of tracked ids
    AND this checkout's tests/+conftest.py (`tests_fp`, see
    tests_fingerprint) both still match what was cached -- any change to
    either invalidates it, so a stale result is never served. A ref --
    the reference branch or any student branch -- whose commit hasn't
    changed since it was last graded doesn't need re-testing at all: not
    even the diff against the reference branch, let alone pytest.
    Returns None on any miss: no cache yet, ids/tests changed, a bad
    ref, or a corrupt/unreadable cache file."""
    sha = _resolve_sha(ref)
    if not sha:
        return None
    path = _commit_cache_path(sha)
    if not path.exists():
        return None
    try:
        cached = json.loads(path.read_text())
    except (json.JSONDecodeError, OSError):
        return None
    if (cached.get("exercise_ids") != exercise_ids
            or cached.get("challenge_ids") != challenge_ids
            or cached.get("exam_ids") != exam_ids
            or cached.get("tests_fingerprint") != tests_fp):
        return None
    outcome = cached.get("outcome")
    if not isinstance(outcome, dict):
        return None
    return {
        "exercises": outcome.get("exercises", {}),
        "challenges": outcome.get("challenges", {}),
        "exams": outcome.get("exams", {}),
        "error": None,
    }


def save_cached_outcome(ref: str, exercise_ids: list, challenge_ids: list, exam_ids: list,
                         outcome: dict, tests_fp: str) -> None:
    """Persists a freshly-computed, error-free test outcome to disk (see
    load_cached_outcome) keyed by `ref`'s current commit and this
    checkout's tests_fp, so a later run against that same commit with
    that same rubric -- this same branch untouched since last time, or
    any other ref that happens to share it -- can skip re-testing it
    entirely. Silently does nothing if the ref won't resolve or the
    outcome carries an error (never cache a failed run)."""
    if outcome.get("error"):
        return
    sha = _resolve_sha(ref)
    if not sha:
        return
    path = _commit_cache_path(sha)
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "ref": ref,
        "sha": sha,
        "exercise_ids": exercise_ids,
        "challenge_ids": challenge_ids,
        "exam_ids": exam_ids,
        "tests_fingerprint": tests_fp,
        "outcome": {
            "exercises": outcome["exercises"],
            "challenges": outcome["challenges"],
            "exams": outcome["exams"],
        },
    }
    tmp_path = path.with_suffix(f".{threading.get_ident()}.tmp")
    tmp_path.write_text(json.dumps(payload))
    tmp_path.replace(path)


def run_student_tests(ref: str, exercise_ids: list, challenge_ids: list, exam_ids: list,
                       reference_outcome: dict = None, changed_paths: set = None,
                       on_step=None) -> dict:
    """Check out `ref` into a throwaway worktree, overlay this checkout's
    tests/ + conftest.py, run every exercise's, challenge's, and exam's own
    test file, and return {"exercises": {id: bool}, "challenges": {id: bool},
    "exams": {id: bool}, "error": str | None}.

    reference_outcome/changed_paths (see discover_changed_paths, and
    "Skipping untouched files" in the module docstring) let a caller skip
    pytest entirely for any id whose solution.py is identical between
    `ref` and the reference branch that produced reference_outcome: that
    id's result is just copied from reference_outcome instead. Pass
    neither (both None, the default) to test every id, as before.

    on_step, if given, is called with a one-line str at every major step
    (worktree created, overlay done, each test file's own result) --
    this function is otherwise silent while it runs (a worktree add or a
    slow pytest file gives no output of its own), so a caller grading
    just one ref on its own -- the reference-branch baseline in main(),
    not the many-branches-at-once loop, which already logs one line per
    *branch* -- should pass one to actually see it working rather than
    staring at a blank terminal until it's done."""
    def _step(msg: str) -> None:
        if on_step:
            on_step(msg)

    outcome = {"exercises": {}, "challenges": {}, "exams": {}, "error": None}
    can_reuse = changed_paths is not None and reference_outcome is not None

    def _to_test(ids: list, kind: str) -> list:
        if not can_reuse:
            return list(ids)
        pending = []
        for id_ in ids:
            if _solution_path(id_, kind) in changed_paths:
                pending.append(id_)
            else:
                outcome[kind][id_] = reference_outcome[kind][id_]
        return pending

    exercises_to_test = _to_test(exercise_ids, "exercises")
    challenges_to_test = _to_test(challenge_ids, "challenges")
    exams_to_test = _to_test(exam_ids, "exams")
    total_to_test = len(exercises_to_test) + len(challenges_to_test) + len(exams_to_test)

    if can_reuse:
        _step(f"{total_to_test} file(s) differ from the reference branch "
              f"(out of {len(exercise_ids) + len(challenge_ids) + len(exam_ids)} tracked) -- "
              "the rest are reused from the reference run.")

    if not (exercises_to_test or challenges_to_test or exams_to_test):
        _step("Nothing to test -- no worktree needed.")
        return outcome  # every file identical to the reference branch -- nothing to actually test

    worktree_dir = Path(tempfile.mkdtemp(prefix="pt-report-"))
    added = False
    try:
        _step(f"Creating worktree for {ref}...")
        t0 = time.time()
        with _WORKTREE_LOCK:
            result = subprocess.run(
                ["git", "worktree", "add", "--detach", "--force", str(worktree_dir), ref],
                cwd=REPO_ROOT, capture_output=True, text=True,
            )
        if result.returncode != 0:
            outcome["error"] = f"git worktree add failed: {result.stderr.strip()}"
            _step(f"git worktree add failed: {result.stderr.strip()}")
            return outcome
        added = True
        _step(f"Worktree ready ({time.time() - t0:.1f}s).")

        _step("Overlaying this checkout's tests/ and conftest.py...")
        shutil.rmtree(worktree_dir / "tests", ignore_errors=True)
        shutil.copytree(REPO_ROOT / "tests", worktree_dir / "tests")
        shutil.copy2(REPO_ROOT / "conftest.py", worktree_dir / "conftest.py")

        done = 0
        for kind, ids, outcome_key in (
            ("exercise", exercises_to_test, "exercises"),
            ("challenge", challenges_to_test, "challenges"),
            ("exam", exams_to_test, "exams"),
        ):
            if not ids:
                continue
            _step(f"Running pytest for {len(ids)} {kind}(s)...")
            for id_ in ids:
                t0 = time.time()
                passed = _run_one_test_file(worktree_dir, f"tests/test_{id_}.py")
                outcome[outcome_key][id_] = passed
                done += 1
                _step(f"  [{done}/{total_to_test}] {id_}: {'PASS' if passed else 'FAIL'} ({time.time() - t0:.1f}s)")
    except Exception as e:  # noqa: BLE001 -- one bad branch must not kill the whole report run
        outcome["error"] = f"{type(e).__name__}: {e}"
        _step(f"ERROR: {outcome['error']}")
    finally:
        if added:
            _step("Removing worktree...")
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


# --------------------------------------------------------------------------- daily telemetry

def discover_file_last_modified(ref: str, paths: list) -> dict:
    """{path: date_str} the last commit date each of `paths` was modified
    on `ref` -- one `git log --name-only` call covering every path at
    once (no worktree). `git log` is newest-commit-first, so the FIRST
    time a path is seen in --name-only output is already its last
    modification date; paths never touched in `ref`'s history are simply
    absent from the result."""
    if not paths:
        return {}
    result = subprocess.run(
        ["git", "log", "--format=__commit__%cd", "--date=format:%Y-%m-%d", "--name-only", ref, "--", *paths],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )
    if result.returncode != 0:
        return {}

    found = {}
    wanted = set(paths)
    current_date = None
    for line in result.stdout.splitlines():
        if line.startswith("__commit__"):
            current_date = line[len("__commit__"):]
        elif line in wanted and line not in found:
            found[line] = current_date
    return found


def _first_commit_date(ref: str) -> str:
    result = subprocess.run(
        ["git", "log", "--format=%cd", "--date=format:%Y-%m-%d", "--reverse", ref],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )
    lines = result.stdout.splitlines()
    return lines[0] if lines else date.today().isoformat()


def run_daily_history(branches: list, exercise_ids: list, passing_by_branch: dict,
                       history_days: int, workers: int) -> dict:
    """{(group, user): {date_str: cumulative_exercises_solved}} built with
    no pytest runs at all -- see "Daily telemetry" in the module
    docstring. `passing_by_branch` is {(group, user): {exercise_id: bool}}
    from the current-state pass that already ran (run_student_tests);
    for each branch's *passing* exercises, one `git log` call (no
    worktree) finds when each one's solution.py was last modified, and
    that date is necessarily the day it became solved."""
    history = {}
    if not branches:
        return history

    def _work(item):
        group, user, ref = item
        passing = passing_by_branch.get((group, user), {})
        wanted_paths = {ex_id: _solution_path(ex_id, "exercises") for ex_id in exercise_ids if passing.get(ex_id)}
        if not wanted_paths:
            return group, user, {}

        last_modified = discover_file_last_modified(ref, list(set(wanted_paths.values())))
        fallback = None
        counts = defaultdict(int)
        for path in wanted_paths.values():
            day_str = last_modified.get(path)
            if day_str is None:
                if fallback is None:
                    fallback = _first_commit_date(ref)
                day_str = fallback
            counts[day_str] += 1

        cumulative = {}
        running_total = 0
        for day_str in sorted(counts):
            running_total += counts[day_str]
            cumulative[day_str] = running_total

        if history_days > 0:
            cutoff = date.today() - timedelta(days=history_days - 1)
            cumulative = {d: c for d, c in cumulative.items() if date.fromisoformat(d) >= cutoff}
        return group, user, cumulative

    done = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [executor.submit(_work, item) for item in branches]
        for future in concurrent.futures.as_completed(futures):
            group, user, cumulative = future.result()
            done += 1
            with _PRINT_LOCK:
                solved = max(cumulative.values()) if cumulative else 0
                print(f"[history {done}/{len(branches)}] {group}/{user}: "
                      f"{solved}/{len(exercise_ids)} exercises, {len(cumulative)} progress day(s)")
            if cumulative:
                history[(group, user)] = cumulative

    return history


def build_daily_series(branches: list, history: dict) -> tuple:
    """Forward-fills each branch's {date: cumulative_solved} history across
    a shared, continuous calendar range (the earliest commit-day seen for
    any branch, through today) so every branch has one value per date --
    missing days (no commit that day) just repeat the last known count,
    making a proper step function instead of a sparse/jagged one. Returns
    (date_strs, {(group, user): [count_per_date]})."""
    all_days = sorted({d for per_branch in history.values() for d in per_branch})
    if not all_days:
        return [], {}

    start = date.fromisoformat(all_days[0])
    end = date.today()
    date_strs = []
    d = start
    while d <= end:
        date_strs.append(d.isoformat())
        d += timedelta(days=1)

    series = {}
    for group, user, ref in branches:
        per_branch = history.get((group, user), {})
        values = []
        last = 0
        for day_str in date_strs:
            if day_str in per_branch:
                last = per_branch[day_str]
            values.append(last)
        series[(group, user)] = values

    return date_strs, series


def compute_branch_stats(branches: list, history: dict, exercise_ids: list) -> list:
    """One stats dict per branch: total solved "as of today" comes from
    the most recent day in its own history (not the current-state pass,
    which also counts challenges/exams), first/last commit day, how many
    distinct days it actually has a commit on, average new exercises per
    active day, and its single best day."""
    stats = []
    for group, user, ref in branches:
        per_branch = history.get((group, user), {})
        if not per_branch:
            stats.append({
                "group": group, "user": user, "branch": ref,
                "total_solved": 0, "first_commit": None, "last_commit": None,
                "days_active": 0, "avg_per_day": 0.0, "best_day": None, "best_day_count": 0,
            })
            continue

        days_sorted = sorted(per_branch)
        first_commit = days_sorted[0]
        last_commit = days_sorted[-1]
        total_solved = per_branch[last_commit]

        prev = 0
        best_day, best_day_count = None, 0
        for day_str in days_sorted:
            delta = max(0, per_branch[day_str] - prev)
            if delta >= best_day_count:
                best_day, best_day_count = day_str, delta
            prev = per_branch[day_str]

        days_active = len(days_sorted)
        stats.append({
            "group": group, "user": user, "branch": ref,
            "total_solved": total_solved, "first_commit": first_commit, "last_commit": last_commit,
            "days_active": days_active,
            "avg_per_day": (total_solved / days_active) if days_active else 0.0,
            "best_day": best_day, "best_day_count": best_day_count,
        })

    stats.sort(key=lambda s: s["total_solved"], reverse=True)
    return stats


# --------------------------------------------------------------------------- management/class-wide aggregates
#
# Everything below rolls the per-branch data above up to the whole class
# (or whole cohort/group) -- no student is ever named. This is what the
# Training Impact / Daily Class Progress / Group Progress sheets are
# built from: the audience is management ("is the training working, are
# people engaged"), not a per-trainee scoreboard (that's what Summary/
# Exercises/Leaderboard are for).

def compute_class_daily_rows(date_strs: list, series: dict, branches: list, n_exercises: int) -> list:
    """One row per date, class-wide: new exercises solved that day
    (summed across every student), the running cumulative total, how
    many students solved something new that day ("active"), what
    fraction of the roster that is, and the class's cumulative
    completion rate (solved / possible, across everyone)."""
    n_students = len(branches)
    rows = []
    prev_total = 0
    prev_value = {key: 0 for key in series}
    for i, d in enumerate(date_strs):
        day_total = 0
        active = 0
        for key, values in series.items():
            v = values[i]
            day_total += v
            if v > prev_value[key]:
                active += 1
            prev_value[key] = v
        rows.append({
            "date": d,
            "new_solved": day_total - prev_total,
            "cumulative_solved": day_total,
            "active_students": active,
            "active_pct": (active / n_students) if n_students else 0.0,
            "completion_pct": (day_total / (n_students * n_exercises)) if n_students and n_exercises else 0.0,
        })
        prev_total = day_total
    return rows


def compute_group_daily_series(date_strs: list, series: dict, branches: list) -> dict:
    """{group: [cumulative_solved_per_date]} -- the same per-date shape
    as build_daily_series' per-branch `series`, but summed within each
    branch-name group (the "group" in "group/user_id") instead of per
    student, so cohorts can be compared without naming anyone in them."""
    groups = sorted({group for group, user, ref in branches})
    totals = {g: [0] * len(date_strs) for g in groups}
    for group, user, ref in branches:
        for i, v in enumerate(series[(group, user)]):
            totals[group][i] += v
    return totals


def compute_management_stats(rows: list, stats: list, n_exercises: int, recent_days: int = 7) -> dict:
    """Class-wide, name-free figures for the Training Impact sheet:
    completion-rate distribution and totals (from `rows`, the
    current-state pass, always available), plus engagement/pace figures
    that need the daily-telemetry `stats` (compute_branch_stats'
    output) -- left as None if --no-history skipped that pass."""
    ok_rows = [r for r in rows if not r["error"]]
    n_students = len(ok_rows)
    pct_per_student = [
        (sum(1 for v in r["exercises"].values() if v) / n_exercises) if n_exercises else 0.0
        for r in ok_rows
    ]

    buckets = [
        ("0% (not started)", lambda p: p == 0),
        ("1-24%", lambda p: 0 < p < 0.25),
        ("25-49%", lambda p: 0.25 <= p < 0.5),
        ("50-74%", lambda p: 0.5 <= p < 0.75),
        ("75-99%", lambda p: 0.75 <= p < 1),
        ("100% (complete)", lambda p: p >= 1),
    ]
    distribution = [(label, sum(1 for p in pct_per_student if test(p))) for label, test in buckets]

    out = {
        "n_students": n_students,
        "n_errors": len(rows) - n_students,
        "total_solved": round(sum(pct_per_student) * n_exercises) if n_exercises else 0,
        "avg_completion_pct": (sum(pct_per_student) / n_students) if n_students else 0.0,
        "median_completion_pct": statistics.median(pct_per_student) if pct_per_student else 0.0,
        "distribution": distribution,
        "recently_active": None, "recently_active_pct": None,
        "first_activity": None, "last_activity": None,
        "class_days_elapsed": None, "avg_new_per_day": None,
    }

    if stats:
        cutoff = (date.today() - timedelta(days=recent_days - 1)).isoformat()
        recently_active = sum(1 for s in stats if s["last_commit"] and s["last_commit"] >= cutoff)
        out["recently_active"] = recently_active
        out["recently_active_pct"] = recently_active / len(stats)

        first_days = [s["first_commit"] for s in stats if s["first_commit"]]
        last_days = [s["last_commit"] for s in stats if s["last_commit"]]
        if first_days and last_days:
            first_activity, last_activity = min(first_days), max(last_days)
            elapsed = (date.fromisoformat(last_activity) - date.fromisoformat(first_activity)).days + 1
            out["first_activity"] = first_activity
            out["last_activity"] = last_activity
            out["class_days_elapsed"] = elapsed
            out["avg_new_per_day"] = (out["total_solved"] / elapsed) if elapsed else 0.0

    return out


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


def _write_training_impact_sheet(wb, mgmt: dict, n_exercises: int):
    """The management-facing overview: class-wide totals, a completion-
    rate distribution across students, and engagement figures -- no
    student's name appears anywhere on this sheet."""
    ws = wb.create_sheet("Training Impact")
    ws.cell(row=1, column=1, value="Training Impact Overview").font = Font(bold=True, size=14)

    r = 3

    def _stat(label, value, number_format=None):
        nonlocal r
        ws.cell(row=r, column=1, value=label).font = Font(bold=True)
        cell = ws.cell(row=r, column=2, value=value)
        if number_format:
            cell.number_format = number_format
        r += 1

    _stat("Students graded", mgmt["n_students"])
    if mgmt["n_errors"]:
        _stat("Students with a grading error", mgmt["n_errors"])
    _stat("Exercises tracked", n_exercises)
    _stat("Total exercises solved (class-wide)", mgmt["total_solved"])
    _stat("Average completion per student", mgmt["avg_completion_pct"], "0%")
    _stat("Median completion per student", mgmt["median_completion_pct"], "0%")
    if mgmt["class_days_elapsed"] is not None:
        _stat("First exercise solved (class)", mgmt["first_activity"])
        _stat("Most recent exercise solved (class)", mgmt["last_activity"])
        _stat("Training days elapsed so far", mgmt["class_days_elapsed"])
        _stat("Average new exercises solved per day (class)", round(mgmt["avg_new_per_day"], 2))
    if mgmt["recently_active"] is not None:
        _stat("Students active in the last 7 days", mgmt["recently_active"])
        _stat("% of class active in the last 7 days", mgmt["recently_active_pct"], "0%")

    r += 1
    ws.cell(row=r, column=1, value="Completion distribution (students, not exercises)").font = Font(bold=True)
    r += 1
    header_row = r
    ws.cell(row=r, column=1, value="Bucket").font = HEADER_FONT
    ws.cell(row=r, column=1).fill = HEADER_FILL
    ws.cell(row=r, column=2, value="Students").font = HEADER_FONT
    ws.cell(row=r, column=2).fill = HEADER_FILL
    r += 1
    first_data_row = r
    for label, count in mgmt["distribution"]:
        ws.cell(row=r, column=1, value=label)
        ws.cell(row=r, column=2, value=count)
        r += 1
    last_data_row = r - 1

    _autosize(ws)

    if mgmt["n_students"]:
        chart = BarChart()
        chart.title = "Students by completion level"
        chart.y_axis.title = "Students"
        chart.style = 10
        chart.width = 20
        chart.height = 10
        data = Reference(ws, min_col=2, max_col=2, min_row=header_row, max_row=last_data_row)
        cats = Reference(ws, min_col=1, max_col=1, min_row=first_data_row, max_row=last_data_row)
        chart.add_data(data, titles_from_data=True)
        chart.set_categories(cats)
        chart.legend = None
        ws.add_chart(chart, f"D{header_row}")

    return ws


def _write_daily_class_sheet(wb, class_rows: list):
    """Class-wide day-to-day table -- new/cumulative exercises solved,
    how many students were active, and the class's cumulative
    completion rate, with no student named or broken out -- plus a
    training-impact line chart and a participation/engagement one."""
    ws = wb.create_sheet("Daily Class Progress")
    headers = ["Date", "New Solved (Class)", "Cumulative Solved (Class)",
               "Students Active", "% Active", "Cumulative Completion %"]
    for c, h in enumerate(headers, start=1):
        cell = ws.cell(row=1, column=c, value=h)
        cell.font = HEADER_FONT
        cell.fill = HEADER_FILL
        cell.alignment = Alignment(horizontal="center")

    for r, row in enumerate(class_rows, start=2):
        ws.cell(row=r, column=1, value=row["date"])
        ws.cell(row=r, column=2, value=row["new_solved"])
        ws.cell(row=r, column=3, value=row["cumulative_solved"])
        ws.cell(row=r, column=4, value=row["active_students"])
        ws.cell(row=r, column=5, value=row["active_pct"]).number_format = "0%"
        ws.cell(row=r, column=6, value=row["completion_pct"]).number_format = "0%"

    last_row = 1 + len(class_rows)
    ws.freeze_panes = "A2"
    _autosize(ws)

    if class_rows:
        impact = LineChart()
        impact.title = "Cumulative exercises solved -- whole class (training impact)"
        impact.y_axis.title = "Exercises solved"
        impact.x_axis.title = "Date"
        impact.style = 10
        impact.width = 24
        impact.height = 12
        data = Reference(ws, min_col=3, max_col=3, min_row=1, max_row=last_row)
        cats = Reference(ws, min_col=1, min_row=2, max_row=last_row)
        impact.add_data(data, titles_from_data=True)
        impact.set_categories(cats)
        impact.legend = None
        ws.add_chart(impact, "H1")

        engagement = LineChart()
        engagement.title = "Students active per day (engagement)"
        engagement.y_axis.title = "Active students"
        engagement.x_axis.title = "Date"
        engagement.style = 12
        engagement.width = 24
        engagement.height = 12
        data2 = Reference(ws, min_col=4, max_col=4, min_row=1, max_row=last_row)
        engagement.add_data(data2, titles_from_data=True)
        engagement.set_categories(cats)
        engagement.legend = None
        ws.add_chart(engagement, "H26")

    return ws


def _write_group_progress_sheet(wb, date_strs: list, group_series: dict):
    """Cumulative exercises solved per day, one column per GROUP/cohort
    -- never per student -- mirroring attendance_report.py's Group
    Comparison sheet. Only called when there's more than one group to
    compare (see build_workbook)."""
    ws = wb.create_sheet("Group Progress")
    ws.cell(row=1, column=1, value="Date").font = HEADER_FONT
    ws.cell(row=1, column=1).fill = HEADER_FILL

    groups = sorted(group_series)
    group_cols = {}
    for i, g in enumerate(groups):
        col = 2 + i
        group_cols[g] = col
        c = ws.cell(row=1, column=col, value=g)
        c.font = HEADER_FONT
        c.fill = HEADER_FILL
        c.alignment = Alignment(horizontal="center")

    for r, d in enumerate(date_strs, start=2):
        ws.cell(row=r, column=1, value=d)
        for g, col in group_cols.items():
            ws.cell(row=r, column=col, value=group_series[g][r - 2]).alignment = Alignment(horizontal="center")

    last_row = 1 + len(date_strs)
    ws.freeze_panes = "B2"
    _autosize(ws)

    if date_strs and groups:
        chart = LineChart()
        chart.title = "Cumulative exercises solved, by group"
        chart.y_axis.title = "Exercises solved"
        chart.x_axis.title = "Date"
        chart.style = 2
        chart.width = 24
        chart.height = max(10, len(groups) * 1.2)
        data = Reference(ws, min_col=2, max_col=1 + len(groups), min_row=1, max_row=last_row)
        cats = Reference(ws, min_col=1, min_row=2, max_row=last_row)
        chart.add_data(data, titles_from_data=True)
        chart.set_categories(cats)
        ws.add_chart(chart, f"A{last_row + 3}")

    return ws


def _write_summary_sheet(wb, rows: list, n_exercises: int, n_challenges: int, n_exams: int):
    ws = wb.create_sheet("Summary")
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


def _branch_col_header(group: str, user: str) -> str:
    return f"{group}/{user}"


def _write_daily_progress_sheet(wb, date_strs: list, series: dict, branches: list):
    """Cumulative exercises-solved-per-day table, one column per branch,
    plus a line chart of the same data -- the "day to day graph" and its
    backing table."""
    ws = wb.create_sheet("Daily Progress")
    ws.cell(row=1, column=1, value="Date").font = HEADER_FONT
    ws.cell(row=1, column=1).fill = HEADER_FILL

    branch_cols = {}
    for i, (group, user, ref) in enumerate(branches):
        col = 2 + i
        branch_cols[(group, user)] = col
        c = ws.cell(row=1, column=col, value=_branch_col_header(group, user))
        c.font = HEADER_FONT
        c.fill = HEADER_FILL
        c.alignment = Alignment(horizontal="center")

    for r, day_str in enumerate(date_strs, start=2):
        ws.cell(row=r, column=1, value=day_str)
        for key, col in branch_cols.items():
            ws.cell(row=r, column=col, value=series[key][r - 2]).alignment = Alignment(horizontal="center")

    last_row = 1 + len(date_strs)
    ws.freeze_panes = "B2"
    _autosize(ws)

    if date_strs and branches:
        chart = LineChart()
        chart.title = "Cumulative exercises solved, by branch"
        chart.y_axis.title = "Exercises solved"
        chart.x_axis.title = "Date"
        chart.style = 10
        chart.width = 26
        chart.height = 14
        data = Reference(ws, min_col=2, max_col=1 + len(branches), min_row=1, max_row=last_row)
        cats = Reference(ws, min_col=1, min_row=2, max_row=last_row)
        chart.add_data(data, titles_from_data=True)
        chart.set_categories(cats)
        ws.add_chart(chart, f"A{last_row + 3}")

    return ws


def _write_daily_delta_sheet(wb, date_strs: list, series: dict, branches: list):
    """Day-over-day NEW exercises solved (the cumulative table's first
    difference) -- "incremental number ... of exercises" per day, per
    branch, plus a class-wide daily total column."""
    ws = wb.create_sheet("Daily Delta")
    ws.cell(row=1, column=1, value="Date").font = HEADER_FONT
    ws.cell(row=1, column=1).fill = HEADER_FILL

    branch_cols = {}
    for i, (group, user, ref) in enumerate(branches):
        col = 2 + i
        branch_cols[(group, user)] = col
        c = ws.cell(row=1, column=col, value=_branch_col_header(group, user))
        c.font = HEADER_FONT
        c.fill = HEADER_FILL
        c.alignment = Alignment(horizontal="center")

    total_col = 2 + len(branches)
    tc = ws.cell(row=1, column=total_col, value="Class Total")
    tc.font = HEADER_FONT
    tc.fill = STAGE_FILL
    tc.alignment = Alignment(horizontal="center")

    prev = {key: 0 for key in branch_cols}
    for r, day_str in enumerate(date_strs, start=2):
        ws.cell(row=r, column=1, value=day_str)
        day_total = 0
        for key, col in branch_cols.items():
            cumulative = series[key][r - 2]
            delta = max(0, cumulative - prev[key])
            prev[key] = cumulative
            day_total += delta
            cell = ws.cell(row=r, column=col, value=delta)
            cell.alignment = Alignment(horizontal="center")
            if delta > 0:
                cell.fill = PASS_FILL
        tcell = ws.cell(row=r, column=total_col, value=day_total)
        tcell.alignment = Alignment(horizontal="center")
        tcell.font = Font(bold=True)

    ws.freeze_panes = "B2"
    _autosize(ws)
    return ws


def _write_leaderboard_sheet(wb, stats: list, n_exercises: int):
    """One row per branch, ranked by total exercises solved (most
    progress first), with the top and bottom rows highlighted, plus a bar
    chart of the same ranking -- the "most updated / least updated
    branch" graph."""
    ws = wb.create_sheet("Leaderboard")
    headers = ["Rank", "Group", "User", "Exercises Solved", "Exercises Total", "%",
               "First Commit", "Last Commit", "Days Active", "Avg New/Day", "Best Day", "Best Day Count"]
    for c, h in enumerate(headers, start=1):
        cell = ws.cell(row=1, column=c, value=h)
        cell.font = HEADER_FONT
        cell.fill = HEADER_FILL
        cell.alignment = Alignment(horizontal="center")

    MOST_FILL = PatternFill("solid", fgColor="C6EFCE")
    LEAST_FILL = PatternFill("solid", fgColor="FFC7CE")

    r = 2
    for rank, s in enumerate(stats, start=1):
        values = [
            rank, s["group"], s["user"],
            s["total_solved"], n_exercises,
            (s["total_solved"] / n_exercises) if n_exercises else 0,
            s["first_commit"] or "", s["last_commit"] or "",
            s["days_active"], round(s["avg_per_day"], 2),
            s["best_day"] or "", s["best_day_count"],
        ]
        for c, v in enumerate(values, start=1):
            cell = ws.cell(row=r, column=c, value=v)
            cell.alignment = Alignment(horizontal="center")
            if c == 6:
                cell.number_format = "0%"
            if rank == 1:
                cell.fill = MOST_FILL
            elif rank == len(stats) and len(stats) > 1:
                cell.fill = LEAST_FILL
        r += 1

    if stats:
        ws.cell(row=r + 1, column=1, value="Most progress → top row (green); least progress → bottom row (red).").font = Font(italic=True)

    ws.freeze_panes = "A2"
    _autosize(ws)

    if stats:
        last_row = 1 + len(stats)
        chart = BarChart()
        chart.type = "bar"  # horizontal -- easier to read branch names
        chart.title = "Exercises solved, ranked (most progress → least)"
        chart.y_axis.title = "Branch"
        chart.x_axis.title = "Exercises solved"
        chart.style = 10
        chart.width = 24
        chart.height = max(8, len(stats) * 0.8)
        data = Reference(ws, min_col=4, max_col=4, min_row=1, max_row=last_row)
        cats = Reference(ws, min_col=2, max_col=3, min_row=2, max_row=last_row)
        chart.add_data(data, titles_from_data=True)
        chart.set_categories(cats)
        chart.legend = None
        ws.add_chart(chart, f"A{last_row + 3}")

    return ws


def build_workbook(rows: list, exercise_ids: list, challenge_ids: list, exam_ids: list,
                    daily: tuple = None, stats: list = None,
                    class_daily: list = None, group_daily: tuple = None):
    wb = openpyxl.Workbook()
    wb.remove(wb.active)

    # Management-facing, class-wide sheets first -- see "management/
    # class-wide aggregates" above the stats functions that feed these.
    mgmt = compute_management_stats(rows, stats, len(exercise_ids))
    _write_training_impact_sheet(wb, mgmt, len(exercise_ids))
    if class_daily:
        _write_daily_class_sheet(wb, class_daily)
    if group_daily is not None:
        date_strs, group_series = group_daily
        if len(group_series) > 1:
            _write_group_progress_sheet(wb, date_strs, group_series)

    _write_summary_sheet(wb, rows, len(exercise_ids), len(challenge_ids), len(exam_ids))
    _write_grid_sheet(wb, "Exercises", rows, exercise_ids, exercise_stage, "exercises")
    _write_grid_sheet(wb, "Challenges", rows, challenge_ids, challenge_stage, "challenges")
    _write_flat_grid_sheet(wb, "Exams", rows, exam_ids, exam_label, "exams")

    if daily is not None:
        date_strs, series, branches = daily
        if date_strs:
            _write_daily_progress_sheet(wb, date_strs, series, branches)
            _write_daily_delta_sheet(wb, date_strs, series, branches)
    if stats is not None and stats:
        _write_leaderboard_sheet(wb, stats, len(exercise_ids))

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
            "  python tools/report.py --history-days 14\n"
            "  python tools/report.py --no-history     # current-state sheets only, no daily telemetry\n"
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
    parser.add_argument("--history-days", type=int, default=30,
                         help="How many calendar days of daily telemetry to compute, counting back from today "
                              "(default: 30). 0 means the branch's entire history.")
    parser.add_argument("--no-history", action="store_true",
                         help="Skip the daily telemetry pass (Daily Progress / Daily Delta / Leaderboard sheets) "
                              "entirely -- just the current-state Summary/Exercises/Challenges/Exams sheets.")
    parser.add_argument("--reference", default=None,
                         help="Branch/ref each student branch is diffed against to skip re-testing files they "
                              "haven't touched (see \"Skipping untouched files\" in this script's docstring). "
                              "Default: 'origin/main', or 'main' with --local.")
    parser.add_argument("--no-diff-skip", action="store_true",
                         help="Disable the reference-branch diff optimization and test every file for every "
                              "branch (slower; useful if you suspect the diff-skip is hiding a problem).")
    parser.add_argument("--no-baseline-cache", action="store_true",
                         help="Always re-test the reference branch, even if a cached result from its current "
                              "commit is on disk (see .cache/report_test_cache/). Use this if you suspect the "
                              "cache is stale for some reason other than a new commit on the reference branch.")
    parser.add_argument("--no-branch-cache", action="store_true",
                         help="Always re-test every student branch, even if a cached result from its exact "
                              "current commit is on disk (see .cache/report_test_cache/) -- i.e. even one that "
                              "hasn't changed at all since the last time this script graded it. Use this if "
                              "you suspect a branch's cached result is stale for some reason other than the "
                              "branch's own commit changing (e.g. tests/ itself changed).")
    parser.add_argument("--assume-reference-fails", action="store_true",
                         help="Skip testing the reference branch entirely and assume every tracked "
                              "exercise/challenge/exam fails on it, trusting that it's always an unsolved "
                              "skeleton (true by how this course is run: everyone branches from it). Fastest "
                              "option, but silently wrong the moment that's not true -- e.g. a reference "
                              "branch that isn't really an unsolved skeleton, or one accidental merge of a "
                              "working solution into it. Prefer the on-disk cache (the default) unless you "
                              "specifically want to skip even the first, cache-populating run.")
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

    tests_fp = tests_fingerprint()

    reference_ref = args.reference or (f"{args.remote}/main" if not args.local else "main")
    reference_outcome = None
    if args.assume_reference_fails:
        print(
            f"Assuming reference branch {reference_ref} fails every tracked id (--assume-reference-fails) -- "
            "skipping its pytest run entirely."
        )
        reference_outcome = {
            "exercises": {i: False for i in exercise_ids},
            "challenges": {i: False for i in challenge_ids},
            "exams": {i: False for i in exam_ids},
            "error": None,
        }
    elif not args.no_diff_skip:
        reference_outcome = None if args.no_baseline_cache else load_cached_outcome(
            reference_ref, exercise_ids, challenge_ids, exam_ids, tests_fp)
        if reference_outcome is not None:
            print(f"Reusing cached baseline results for reference branch {reference_ref} "
                  "(same commit, same tracked ids as last time).")
        else:
            print(f"Computing baseline results from reference branch {reference_ref} "
                  f"({total} files to test, no diff to skip against on this one)...")
            t0 = time.time()
            reference_outcome = run_student_tests(
                reference_ref, exercise_ids, challenge_ids, exam_ids,
                on_step=lambda msg: print(f"  [baseline] {msg}"),
            )
            print(f"Baseline done in {time.time() - t0:.1f}s.")
            if reference_outcome["error"]:
                print(
                    f"WARNING: couldn't test reference branch {reference_ref} ({reference_outcome['error']}) -- "
                    "skipping the diff optimization, testing every file for every branch.",
                    file=sys.stderr,
                )
                reference_outcome = None
            else:
                save_cached_outcome(reference_ref, exercise_ids, challenge_ids, exam_ids, reference_outcome, tests_fp)

    rows = []
    done = 0

    def _work(item):
        group, user, ref = item
        with _PRINT_LOCK:
            print(f"[{group}/{user}] starting ({ref})...")

        if not args.no_branch_cache:
            cached = load_cached_outcome(ref, exercise_ids, challenge_ids, exam_ids, tests_fp)
            if cached is not None:
                with _PRINT_LOCK:
                    print(f"[{group}/{user}] unchanged since last time (same commit, same tests/) -- "
                          "reusing its cached result, no testing needed.")
                return group, user, ref, cached

        changed_paths = discover_changed_paths(reference_ref, ref) if reference_outcome is not None else None
        outcome = run_student_tests(ref, exercise_ids, challenge_ids, exam_ids,
                                     reference_outcome=reference_outcome, changed_paths=changed_paths)
        if not outcome["error"]:
            save_cached_outcome(ref, exercise_ids, challenge_ids, exam_ids, outcome, tests_fp)
        return group, user, ref, outcome

    print(f"\nTesting {len(branches)} branch(es) ({args.workers} at a time)...")
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

    daily = None
    stats = None
    class_daily = None
    group_daily = None
    if not args.no_history:
        print(f"\nComputing daily telemetry ({'full history' if args.history_days <= 0 else f'last {args.history_days} days'})...")
        passing_by_branch = {(r["group"], r["user"]): r["exercises"] for r in rows if not r["error"]}
        history = run_daily_history(branches, exercise_ids, passing_by_branch, args.history_days, args.workers)
        date_strs, series = build_daily_series(branches, history)
        daily = (date_strs, series, branches)
        stats = compute_branch_stats(branches, history, exercise_ids)
        if date_strs:
            class_daily = compute_class_daily_rows(date_strs, series, branches, len(exercise_ids))
            group_daily = (date_strs, compute_group_daily_series(date_strs, series, branches))
        if stats:
            leader = stats[0]
            trailer = stats[-1]
            print(
                f"Most progress: {leader['group']}/{leader['user']} "
                f"({leader['total_solved']}/{len(exercise_ids)} exercises). "
                f"Least progress: {trailer['group']}/{trailer['user']} "
                f"({trailer['total_solved']}/{len(exercise_ids)} exercises)."
            )

    wb = build_workbook(rows, exercise_ids, challenge_ids, exam_ids,
                         daily=daily, stats=stats, class_daily=class_daily, group_daily=group_daily)
    wb.save(args.output)
    print(f"\nWrote {args.output} ({total} tracked exercises/challenges/exams, {len(rows)} students).")


if __name__ == "__main__":
    main()
