"""
OOP II -- Protocol Structural Typing
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage07_advanced02.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage07/advanced02/ and import it as a submodule (e.g.
`from exercises.stage07.advanced02 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


from typing import Protocol, runtime_checkable


@runtime_checkable
class SupportsArea(Protocol):
    def area(self) -> float: ...


class Coin:
    def __init__(self, radius):
        raise NotImplementedError

    def area(self) -> float:
        """3.14159 * radius ** 2 -- Coin never inherits from SupportsArea."""
        raise NotImplementedError


def total_area(shapes: list) -> float:
    """sum(s.area() for s in shapes)."""
    raise NotImplementedError


def supports_area(obj) -> bool:
    """isinstance(obj, SupportsArea) -- structural, not inheritance-based."""
    raise NotImplementedError
