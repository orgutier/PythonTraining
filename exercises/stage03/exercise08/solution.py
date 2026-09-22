"""
Functions -- Generators
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage03_exercise08.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage03/exercise08/ and import it as a submodule (e.g.
`from exercises.stage03.exercise08 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


def count_up_to(n: int):
    """Generator: yield 1, 2, ..., n."""
    raise NotImplementedError


def evens_only(numbers: list[int]):
    """Generator: yield only the even numbers from numbers, in order."""
    raise NotImplementedError


def infinite_counter():
    """Generator: yield 0, 1, 2, 3, ... forever. Consume with take(), never list()."""
    raise NotImplementedError


def take(iterable, n: int) -> list:
    """First n items of iterable, via itertools.islice(iterable, n)."""
    raise NotImplementedError
