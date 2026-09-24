import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

import pytest

# --------------------------------------------------------------------------
# On any failure/error, print which exercise/challenge/exam this test
# belongs to, that specific test's docstring (if it has one -- a one-line
# note on exactly which README.md requirement it's checking), and where to
# go read the full problem statement. The goal: a trainee staring at a wall
# of pytest failures shouldn't have to reverse-engineer the test file to
# figure out what's actually still missing.
# --------------------------------------------------------------------------


def _readme_path_for(nodeid: str):
    """Guess the README.md a test's problem statement lives in, purely from
    its test file's name -- test_stageNN_<name>.py -> exercises/stageNN/<name>/,
    test_challengeNN.py -> challenges/challengeNN/, test_examNN.py ->
    exams/examNN/. Works for every test with no per-test setup required."""
    stem = Path(nodeid.split("::")[0]).stem  # "tests/test_stage01_basic01.py" -> "test_stage01_basic01"
    if not stem.startswith("test_"):
        return None
    name = stem.removeprefix("test_")
    if name.startswith("stage"):
        stage, sep, exercise = name.partition("_")
        if sep:
            return Path("exercises") / stage / exercise / "README.md"
        return None
    if name.startswith("challenge"):
        return Path("challenges") / name / "README.md"
    if name.startswith("exam"):
        return Path("exams") / name / "README.md"
    return None


def _requirement_note(nodeid: str, docstring: str) -> str:
    lines = []
    doc = (docstring or "").strip()
    if doc:
        lines.append(f"Checks: {doc}")
    readme = _readme_path_for(nodeid)
    if readme is not None:
        exists = " (exists)" if readme.exists() else ""
        lines.append(f"Full requirement: {readme}{exists}")
    return "\n".join(lines)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """A test FUNCTION failed (an assertion, or an exception raised while it
    ran) -- attach its own docstring + README path to the failure output."""
    outcome = yield
    report = outcome.get_result()
    if report.when != "call" or not report.failed:
        return
    note = _requirement_note(item.nodeid, getattr(item.function, "__doc__", None))
    if note:
        report.sections.append(("requirement", note))


@pytest.hookimpl(hookwrapper=True)
def pytest_collectreport(report):
    """A test MODULE failed to even import -- this is how a script-style
    exercise's module-level `raise NotImplementedError` shows up (see
    generator/stage01.py), since nothing has run yet for pytest to attach a
    per-test docstring to. Point at the README instead."""
    outcome = yield
    if not report.failed:
        return
    readme = _readme_path_for(report.nodeid)
    if readme is not None:
        exists = " (exists)" if readme.exists() else ""
        report.sections.append(("requirement", f"Full requirement: {readme}{exists}"))
