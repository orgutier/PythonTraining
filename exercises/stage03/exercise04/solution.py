"""
Functions -- Scope: global and nonlocal
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage03_exercise04.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage03/exercise04/ and import it as a submodule (e.g.
`from exercises.stage03.exercise04 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


_counter = 0


def increment_counter() -> int:
    """global _counter; increment it by 1 and return the new value."""
    raise NotImplementedError


def reset_counter() -> None:
    """global _counter; set it back to 0."""
    raise NotImplementedError


def set_counter(value: int) -> None:
    """global _counter; set it directly to value."""
    raise NotImplementedError


def get_counter() -> int:
    """Return _counter (no `global` needed -- this only reads it)."""
    raise NotImplementedError


def make_counter():
    """Return a zero-arg closure yielding 1, 2, 3, ... on successive calls (nonlocal)."""
    raise NotImplementedError


def make_accumulator(start: int = 0):
    """Return a one-arg closure add(x) that accumulates a running total (nonlocal)."""
    raise NotImplementedError


def make_toggle(initial: bool = False):
    """Return a zero-arg closure that flips/returns a running bool each call (nonlocal)."""
    raise NotImplementedError
