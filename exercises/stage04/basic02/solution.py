"""
Data Structures -- Inventory Category Summary
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage04_basic02.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage04/basic02/ and import it as a submodule (e.g.
`from exercises.stage04.basic02 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


def category_by_product(names: list[str], categories: list[str]) -> dict:
    """{name: cat for name, cat in zip(names, categories)} -- a dict comprehension."""
    raise NotImplementedError


def unique_categories(categories: list[str]) -> set:
    """set(categories)."""
    raise NotImplementedError


def products_in_category(names: list[str], categories: list[str], target: str) -> list[str]:
    """[name for name, cat in zip(names, categories) if cat == target] -- a filtered list comprehension."""
    raise NotImplementedError


def category_counts(categories: list[str]) -> dict:
    """{cat: categories.count(cat) for cat in set(categories)}."""
    raise NotImplementedError


def product_count(names: list[str]) -> int:
    """len(names)."""
    raise NotImplementedError
