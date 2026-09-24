"""
Data Structures -- Hashable Records: Frozen Dataclasses and Manual __hash__
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage04_advanced02.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage04/advanced02/ and import it as a submodule (e.g.
`from exercises.stage04.advanced02 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import dataclasses
import math


@dataclasses.dataclass
class Point:
    x: int
    y: int

    def distance_from_origin(self) -> float:
        """(x**2 + y**2) ** 0.5. Point is NOT hashable (mutable + eq=True -> __hash__ is None)."""
        raise NotImplementedError


@dataclasses.dataclass(frozen=True)
class FrozenPoint:
    x: int
    y: int

    def distance_from_origin(self) -> float:
        """(x**2 + y**2) ** 0.5. frozen=True gives FrozenPoint a working, auto-generated __hash__."""
        raise NotImplementedError


class SimpleFraction:
    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ZeroDivisionError("denominator cannot be 0")
        if denominator < 0:
            numerator, denominator = -numerator, -denominator
        g = math.gcd(numerator, denominator)
        self.numerator = numerator // g
        self.denominator = denominator // g

    def __eq__(self, other) -> bool:
        """True if other is a SimpleFraction with the same reduced numerator/denominator."""
        raise NotImplementedError

    def __hash__(self) -> int:
        """hash((self.numerator, self.denominator)) -- must be written BY HAND; nothing generates it for a plain class."""
        raise NotImplementedError


def dedupe_preserving_order(items: list) -> list:
    """Remove duplicates, preserving first-seen order: list(dict.fromkeys(items))."""
    raise NotImplementedError
