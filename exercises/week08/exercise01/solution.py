"""
The Python Data Model -- Vector: The Flagship Dunder Class
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the aggregated test suite in
tests/test_week08.py imports directly from here. Need a helper function or
class of your own? Add another .py file next to this one inside
exercises/week08/exercise01/ and import it as a submodule (e.g.
`from exercises.week08.exercise01 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        """f"Vector({self.x}, {self.y})"."""
        raise NotImplementedError

    def __str__(self) -> str:
        """f"({self.x}, {self.y})"."""
        raise NotImplementedError

    def __eq__(self, other) -> bool:
        """True if other is a Vector with the same x/y."""
        raise NotImplementedError

    def __add__(self, other):
        """New Vector(x+x, y+y) if other is a Vector, else NotImplemented."""
        raise NotImplementedError

    def __radd__(self, other):
        """self if other == 0 (for sum()), else NotImplemented."""
        raise NotImplementedError

    def __hash__(self) -> int:
        """hash((self.x, self.y))."""
        raise NotImplementedError

    def __bool__(self) -> bool:
        """False only for the zero vector."""
        raise NotImplementedError

    def __getitem__(self, index):
        """(self.x, self.y)[index]."""
        raise NotImplementedError
