"""
The Python Data Model -- Point: repr, str, eq
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage08_basic01.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage08/basic01/ and import it as a submodule (e.g.
`from exercises.stage08.basic01 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        """f"Point({self.x}, {self.y})"."""
        raise NotImplementedError

    def __str__(self) -> str:
        """f"({self.x}, {self.y})"."""
        raise NotImplementedError

    def __eq__(self, other) -> bool:
        """True if other is a Point with the same x/y."""
        raise NotImplementedError
