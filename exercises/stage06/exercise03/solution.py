"""
OOP I -- Rectangle Properties
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage06_exercise03.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage06/exercise03/ and import it as a submodule (e.g.
`from exercises.stage06.exercise03 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


class Rectangle:
    def __init__(self, width: float, height: float):
        raise NotImplementedError

    @property
    def width(self) -> float:
        raise NotImplementedError

    @width.setter
    def width(self, value) -> None:
        """Raise ValueError if value <= 0, else store it."""
        raise NotImplementedError

    @property
    def height(self) -> float:
        raise NotImplementedError

    @height.setter
    def height(self, value) -> None:
        """Raise ValueError if value <= 0, else store it."""
        raise NotImplementedError

    @property
    def area(self) -> float:
        """width * height (read-only, no setter)."""
        raise NotImplementedError

    @property
    def perimeter(self) -> float:
        """2 * (width + height) (read-only)."""
        raise NotImplementedError

    @property
    def is_square(self) -> bool:
        """width == height (read-only)."""
        raise NotImplementedError
