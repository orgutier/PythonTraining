"""
Data Structures -- Dict and Set Operations
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_week04_exercise02.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/week04/exercise02/ and import it as a submodule (e.g.
`from exercises.week04.exercise02 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


def word_lengths(words: list[str]) -> dict:
    """{w: len(w) for w in words}."""
    raise NotImplementedError


def index_lookup(items: list[str]) -> dict:
    """{item: i for i, item in enumerate(items)}."""
    raise NotImplementedError


def numbered_pairs(items: list[str]) -> list[tuple]:
    """list(enumerate(items))."""
    raise NotImplementedError


def pair_and_dict(keys: list[str], values: list) -> dict:
    """dict(zip(keys, values))."""
    raise NotImplementedError


def common_elements(a: set, b: set) -> set:
    """a & b -- intersection."""
    raise NotImplementedError


def unique_to_first(a: set, b: set) -> set:
    """a - b -- difference."""
    raise NotImplementedError


def all_elements(a: set, b: set) -> set:
    """a | b -- union."""
    raise NotImplementedError
