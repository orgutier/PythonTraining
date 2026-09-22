"""
Files, Exceptions, Regex -- Exceptions and Hierarchies
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage05_exercise02.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage05/exercise02/ and import it as a submodule (e.g.
`from exercises.stage05.exercise02 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


class ValidationError(Exception):
    pass


class NegativeValueError(ValidationError):
    pass


def validate_positive(n: int) -> int:
    """Return n if n >= 0, else raise NegativeValueError."""
    raise NotImplementedError


def safe_parse_int(s: str):
    """int(s), or None if that raises ValueError."""
    raise NotImplementedError


_attempts = 0


def divide_with_cleanup(a: float, b: float) -> float:
    """a / b; re-raise ZeroDivisionError unchanged; always count the attempt in finally."""
    raise NotImplementedError


def get_attempts() -> int:
    raise NotImplementedError


def reset_attempts() -> None:
    raise NotImplementedError
