"""
Files, Exceptions, Regex -- Regex Named Groups
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage05_exercise05.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage05/exercise05/ and import it as a submodule (e.g.
`from exercises.stage05.exercise05 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import re


def parse_log_line(line: str) -> dict:
    """{"level": ..., "message": ...} via re.match + named groups; ValueError if no match."""
    raise NotImplementedError


def parse_date(text: str) -> dict:
    """{"year": ..., "month": ..., "day": ...} via re.search + named groups; ValueError if none found."""
    raise NotImplementedError


def parse_key_value(text: str) -> dict:
    """{"key": ..., "value": ...} via re.match + named groups; ValueError if no match."""
    raise NotImplementedError
