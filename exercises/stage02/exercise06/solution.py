"""
Control Flow -- Ternary Expressions
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage02_exercise06.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage02/exercise06/ and import it as a submodule (e.g.
`from exercises.stage02.exercise06 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


def grade_label(score: int) -> str:
    """"pass" if score >= 60 else "fail" -- as a ternary expression."""
    raise NotImplementedError


def abs_value(n: int) -> int:
    """n if n >= 0 else -n -- as a ternary expression."""
    raise NotImplementedError


def clamp_to_range(n: int, lo: int, hi: int) -> int:
    """n clamped into [lo, hi] -- as a chained ternary expression."""
    raise NotImplementedError
