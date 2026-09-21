"""
Control Flow -- The else Clause on Loops
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_week02_exercise07.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/week02/exercise07/ and import it as a submodule (e.g.
`from exercises.week02.exercise07 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


def contains_value(items: list, target) -> bool:
    """for...else: True if target is found in items."""
    raise NotImplementedError


def all_positive(numbers: list[int]) -> bool:
    """for...else: True if every number in numbers is > 0."""
    raise NotImplementedError


def find_first_negative_index(numbers: list[int]) -> int:
    """while...else: index of the first negative number, or -1."""
    raise NotImplementedError


def retry_until_success(attempts: list[bool]) -> bool:
    """while...else: True if any attempt is True, else False."""
    raise NotImplementedError


def first_positive_index(numbers: list[int]) -> int:
    """while...else: index of the first positive number, or -1."""
    raise NotImplementedError
