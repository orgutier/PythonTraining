"""
OS, JSON, Datetime, XML -- Datetime Basics
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage09_exercise05.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage09/exercise05/ and import it as a submodule (e.g.
`from exercises.stage09.exercise05 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import datetime


def current_timestamp_iso() -> str:
    """datetime.datetime.now().isoformat()."""
    raise NotImplementedError


def format_date(dt) -> str:
    """dt.strftime("%Y-%m-%d")."""
    raise NotImplementedError


def parse_iso(text: str):
    """datetime.datetime.fromisoformat(text)."""
    raise NotImplementedError


def days_between(d1, d2) -> int:
    """(d2 - d1).days."""
    raise NotImplementedError
