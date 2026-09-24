"""
OOP I -- Slotted Geometry
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage06_mid01.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage06/mid01/ and import it as a submodule (e.g.
`from exercises.stage06.mid01 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


class PointSlots:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        raise NotImplementedError


class Vector3DSlots:
    __slots__ = ("x", "y", "z")

    def __init__(self, x, y, z):
        raise NotImplementedError

    def magnitude(self) -> float:
        """(x**2 + y**2 + z**2) ** 0.5."""
        raise NotImplementedError
