"""
Files, Exceptions, Regex -- File Basics
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage05_exercise01.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage05/exercise01/ and import it as a submodule (e.g.
`from exercises.stage05.exercise01 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


def write_lines(path: str, lines: list[str]) -> None:
    """Open path for writing and write each line, each followed by "\n"."""
    raise NotImplementedError


def read_lines(path: str) -> list[str]:
    """Open path for reading; return f.read().splitlines()."""
    raise NotImplementedError


def append_line(path: str, line: str) -> None:
    """Open path in append mode ("a") and write line + "\n"."""
    raise NotImplementedError


def count_lines(path: str) -> int:
    """Open path for reading and return how many lines it has."""
    raise NotImplementedError
