"""
Data Structures -- List and Tuple Basics
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_week04_exercise01.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/week04/exercise01/ and import it as a submodule (e.g.
`from exercises.week04.exercise01 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


def build_shopping_list(items: list[str]) -> list[str]:
    """Build a new list by .append()-ing each item in a loop."""
    raise NotImplementedError


def unique_sorted(numbers: list[int]) -> list[int]:
    """sorted(set(numbers))."""
    raise NotImplementedError


def sort_in_place(items: list) -> None:
    """items.sort() -- mutate in place, return None."""
    raise NotImplementedError


def as_tuple_pairs(names: list[str], ages: list[int]) -> list[tuple]:
    """list(zip(names, ages))."""
    raise NotImplementedError


def zip_and_sum(list1: list[int], list2: list[int]) -> list[int]:
    """[a + b for a, b in zip(list1, list2)]."""
    raise NotImplementedError


def label_each(items: list[str]) -> list[str]:
    """[f"{i}:{v}" for i, v in enumerate(items)]."""
    raise NotImplementedError


def count_items(items: list) -> int:
    """len(items)."""
    raise NotImplementedError
