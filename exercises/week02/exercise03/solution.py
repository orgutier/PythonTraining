"""
Control Flow -- Pairing and Indexing
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_week02_exercise03.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/week02/exercise03/ and import it as a submodule (e.g.
`from exercises.week02.exercise03 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


def pair_names_scores(names: list[str], scores: list[int]) -> list[tuple]:
    """list(zip(names, scores))."""
    raise NotImplementedError


def merge_records(keys: list[str], values: list) -> dict:
    """dict(zip(keys, values))."""
    raise NotImplementedError


def count_equal_pairs(list1: list, list2: list) -> int:
    """Count positions i where list1[i] == list2[i], walking both with zip()."""
    raise NotImplementedError


def indexed_items(items: list[str]) -> list[str]:
    """[f"{i}: {item}" for i, item in enumerate(items)]."""
    raise NotImplementedError


def labeled_from(items: list[str], start: int) -> dict:
    """{i: item for i, item in enumerate(items, start)}."""
    raise NotImplementedError
