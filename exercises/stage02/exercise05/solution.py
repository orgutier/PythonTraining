"""
Control Flow -- Short-Circuit Guards and Truthiness
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage02_exercise05.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage02/exercise05/ and import it as a submodule (e.g.
`from exercises.stage02.exercise05 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


def is_valid_username(name) -> bool:
    """Non-empty str, len <= 20 -- one chained `and` expression."""
    raise NotImplementedError


def has_valid_first_item(items: list) -> bool:
    """items is non-empty AND items[0] is truthy -- `and` guards items[0]."""
    raise NotImplementedError


def is_within_bounds(numbers: list[int], index: int) -> bool:
    """0 <= index < len(numbers) AND numbers[index] >= 0."""
    raise NotImplementedError


def describe_truthiness(value) -> str:
    """"truthy" or "falsy" based on bare truthiness of value."""
    raise NotImplementedError


def filter_truthy(values: list) -> list:
    """Only the truthy values, order preserved."""
    raise NotImplementedError


def count_falsy(values: list) -> int:
    """How many values are falsy."""
    raise NotImplementedError
