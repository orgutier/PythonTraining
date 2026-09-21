"""
Python Fundamentals -- Profile Basics
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the aggregated test suite in
tests/test_week01.py imports directly from here. Need a helper function or
class of your own? Add another .py file next to this one inside
exercises/week01/exercise01/ and import it as a submodule (e.g.
`from exercises.week01.exercise01 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


def build_profile(name: str, age: int, height_m: float, is_student: bool) -> dict:
    """Return {"name": name, "age": age, "height_m": height_m, "is_student": is_student}."""
    raise NotImplementedError


def value_kind(x) -> str:
    """Return the name of x's type, e.g. value_kind(5) == "int"."""
    raise NotImplementedError


def display_profile(profile: dict) -> None:
    """Print "NAME is AGE years old, HEIGHT_Mm tall, student=IS_STUDENT"."""
    raise NotImplementedError
