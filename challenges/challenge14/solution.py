"""
Challenge 14 - Shape Library with Protocols and Composition
Interview-style challenge. Correctness is pytest-tested (see
tests/test_challenge14.py / `python tools/cli.py test challenge14`); see
README.md in this folder for the full problem statement and the constraints
your solution must follow (a runtime_checkable typing.Protocol, composition (not inheritance) for a composite shape, and isinstance()-based structural filtering).

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module, matching the convention used by
exercises/weekNN/solution.py.
"""


from typing import Protocol, runtime_checkable


@runtime_checkable
class Drawable(Protocol):
    def area(self) -> float: ...
    def perimeter(self) -> float: ...


class Circle:
    def __init__(self, radius: float) -> None:
        raise NotImplementedError

    def area(self) -> float:
        raise NotImplementedError

    def perimeter(self) -> float:
        raise NotImplementedError


class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        raise NotImplementedError

    def area(self) -> float:
        raise NotImplementedError

    def perimeter(self) -> float:
        raise NotImplementedError


class CompositeShape:
    def __init__(self, shapes: list) -> None:
        raise NotImplementedError

    def area(self) -> float:
        """Sum of every held shape's area()."""
        raise NotImplementedError

    def perimeter(self) -> float:
        """Sum of every held shape's perimeter()."""
        raise NotImplementedError


def total_area(shapes: list) -> float:
    """Sum area() across every Drawable in shapes (isinstance-checked); skip the rest."""
    raise NotImplementedError


def largest_by_area(shapes: list):
    """The shape with the largest area() -- works uniformly, no isinstance/type() branching."""
    raise NotImplementedError
