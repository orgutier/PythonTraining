"""
Control Flow -- Loop Controls
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the aggregated test suite in
tests/test_week02.py imports directly from here. Need a helper function or
class of your own? Add another .py file next to this one inside
exercises/week02/exercise02/ and import it as a submodule (e.g.
`from exercises.week02.exercise02 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


def sum_until_negative(numbers: list[int]) -> int:
    """Sum numbers, stopping (break) at the first negative one."""
    raise NotImplementedError


def skip_multiples(numbers: list[int], factor: int) -> list[int]:
    """Return numbers with any multiple of factor skipped (continue)."""
    raise NotImplementedError


def countdown(n: int) -> list[int]:
    """[n, n-1, ..., 1] built with a while loop."""
    raise NotImplementedError


def safe_int_list(values: list) -> list[int]:
    """int(v) for each value, silently skipping ones that fail (except: pass)."""
    raise NotImplementedError
