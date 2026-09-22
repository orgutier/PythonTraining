"""
Data Structures -- Comprehensions
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage04_exercise03.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage04/exercise03/ and import it as a submodule (e.g.
`from exercises.stage04.exercise03 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


def squares(n: int) -> list[int]:
    """[x ** 2 for x in range(n)]."""
    raise NotImplementedError


def evens_squared_dict(n: int) -> dict:
    """{x: x ** 2 for x in range(n) if x % 2 == 0}."""
    raise NotImplementedError


def flatten(matrix: list[list[int]]) -> list[int]:
    """Nested comprehension: [x for row in matrix for x in row]."""
    raise NotImplementedError
