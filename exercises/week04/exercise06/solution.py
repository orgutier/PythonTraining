"""
Data Structures -- Records and Hashability
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the aggregated test suite in
tests/test_week04.py imports directly from here. Need a helper function or
class of your own? Add another .py file next to this one inside
exercises/week04/exercise06/ and import it as a submodule (e.g.
`from exercises.week04.exercise06 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import collections
import math

Coordinate = collections.namedtuple("Coordinate", ["x", "y"])


def make_coordinate(x: int, y: int):
    """Return Coordinate(x, y)."""
    raise NotImplementedError


class SimpleFraction:
    def __init__(self, numerator: int, denominator: int):
        """Reduce to lowest terms via math.gcd; raise ZeroDivisionError if denominator == 0."""
        raise NotImplementedError

    def __eq__(self, other) -> bool:
        """True if other is a SimpleFraction with the same reduced numerator/denominator."""
        raise NotImplementedError

    def __hash__(self) -> int:
        """hash((self.numerator, self.denominator)) -- required alongside __eq__."""
        raise NotImplementedError


def dedupe_preserving_order(items: list) -> list:
    """Remove duplicates, preserving first-seen order: list(dict.fromkeys(items))."""
    raise NotImplementedError
