"""
Python Fundamentals -- Mutability and Identity
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the aggregated test suite in
tests/test_week01.py imports directly from here. Need a helper function or
class of your own? Add another .py file next to this one inside
exercises/week01/exercise06/ and import it as a submodule (e.g.
`from exercises.week01.exercise06 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


def append_and_return(lst: list, item) -> list:
    """Mutate lst in place (append item) and return that same object."""
    raise NotImplementedError


def concat_strings(a: str, b: str) -> str:
    """Return a + b -- always a new string object (str is immutable)."""
    raise NotImplementedError


def same_object(a, b) -> bool:
    """True if a and b are the identical object (use `is`, not `==`)."""
    raise NotImplementedError


def equal_but_not_identical() -> tuple:
    """Return two separately-built, `==`-equal lists that are NOT the same object."""
    raise NotImplementedError


def default_if_none(value, default):
    """Return default if value is None, else value unchanged."""
    raise NotImplementedError
