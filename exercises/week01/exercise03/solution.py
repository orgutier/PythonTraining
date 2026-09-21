"""
Python Fundamentals -- Type Inspector
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the aggregated test suite in
tests/test_week01.py imports directly from here. Need a helper function or
class of your own? Add another .py file next to this one inside
exercises/week01/exercise03/ and import it as a submodule (e.g.
`from exercises.week01.exercise03 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


def describe_value(value) -> str:
    """"None (the absence of a value)" for None, else f"{value!r} is a {type(value).__name__}"."""
    raise NotImplementedError


def print_type_report(value) -> None:
    """print(describe_value(value))."""
    raise NotImplementedError


def classify_values(values: list) -> dict:
    """Bucket values into {"ints": [...], "floats": [...], "strs": [...], "bools": [...], "nones": [...]}."""
    raise NotImplementedError
