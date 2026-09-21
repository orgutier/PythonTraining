"""
Shared test-running logic for the CLI and GUI test runners.
Both tools/cli.py and tools/gui.py import from here so there's a single
source of truth for how tests get invoked.
"""
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
WEEKS = [f"week{n:02d}" for n in range(1, 15)]
CHALLENGES = [f"challenge{n:02d}" for n in range(1, 27)]


def _discover_exercises() -> list:
    """Every "weekNN_exerciseXX" id with a tests/test_weekNN_exerciseXX.py
    file on disk, sorted. Computed from the filesystem (not hardcoded) so
    it can't drift out of sync with what generate.py actually produced."""
    tests_dir = REPO_ROOT / "tests"
    ids = [
        path.stem.removeprefix("test_")
        for path in tests_dir.glob("test_week[0-9][0-9]_exercise[0-9][0-9].py")
    ]
    return sorted(ids)


EXERCISES = _discover_exercises()

WEEK_TOPICS = {
    "week01": "Python Fundamentals",
    "week02": "Control Flow",
    "week03": "Functions",
    "week04": "Data Structures",
    "week05": "Files, Exceptions, Regex",
    "week06": "OOP I - Classes, Encapsulation, Properties",
    "week07": "OOP II - Inheritance, Polymorphism, Abstraction",
    "week08": "The Python Data Model",
    "week09": "OS, JSON, Datetime, XML",
    "week10": "Pandas",
    "week11": "OpenCV",
    "week12": "Requests + Threading",
    "week13": "Local API Endpoints (FastAPI)",
    "week14": "Capstone",
}


def _test_targets(id: str) -> list:
    """Resolve a test id to the test file(s) that cover it.

    "week01_exercise03" (or "challenge01") maps to its own single test
    file. A plain week id like "week01" has no test file of its own --
    it maps to every exercise test file for that week
    (test_week01_exercise*.py), so testing "week01" always covers
    everything currently in it, however many exercises that turns out to
    be.
    """
    exact = REPO_ROOT / "tests" / f"test_{id}.py"
    if exact.exists():
        return [exact]
    return sorted((REPO_ROOT / "tests").glob(f"test_{id}_exercise*.py"))


def run_week_tests(id: str) -> subprocess.CompletedProcess:
    """Run pytest for one week, one exercise, or one challenge (by id).
    Returns the completed process."""
    targets = _test_targets(id)
    if not targets:
        raise FileNotFoundError(f"No test file(s) found for {id}")
    return subprocess.run(
        [sys.executable, "-m", "pytest", *(str(t) for t in targets), "-v"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )


def run_all_tests() -> subprocess.CompletedProcess:
    """Run the full test suite across every week."""
    return subprocess.run(
        [sys.executable, "-m", "pytest", "tests/", "-v"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
