"""
Control Flow -- Ranges and Itertools
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage02_exercise04.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage02/exercise04/ and import it as a submodule (e.g.
`from exercises.stage02.exercise04 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


def stepped_range(start: int, stop: int, step: int) -> list[int]:
    """list(range(start, stop, step))."""
    raise NotImplementedError


def numbered_multiples(n: int, factor: int) -> list[str]:
    """Multiples of factor up to n, each labeled "i: value" via enumerate()."""
    raise NotImplementedError


def cycle_colors(colors: list[str], count: int) -> list[str]:
    """First `count` items of colors repeated forever (itertools.cycle + islice)."""
    raise NotImplementedError


def chain_lists(list1: list, list2: list) -> list:
    """list1 followed by list2, via itertools.chain (not list1 + list2)."""
    raise NotImplementedError


def all_pairs(list1: list, list2: list) -> list[tuple]:
    """Every (a, b) combination, via itertools.product."""
    raise NotImplementedError
