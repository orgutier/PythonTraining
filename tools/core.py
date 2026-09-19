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
CHALLENGES = [f"challenge{n:02d}" for n in range(1, 6)]

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


def run_week_tests(week: str) -> subprocess.CompletedProcess:
    """Run pytest for a single week's exercise. Returns the completed process."""
    test_file = REPO_ROOT / "tests" / f"test_{week}.py"
    if not test_file.exists():
        raise FileNotFoundError(f"No test file found for {week}: {test_file}")
    return subprocess.run(
        [sys.executable, "-m", "pytest", str(test_file), "-v"],
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
