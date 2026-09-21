from typing import Protocol, runtime_checkable


@runtime_checkable
class Drawable(Protocol):
    def area(self) -> float: ...
    def perimeter(self) -> float: ...


class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return 3.14159 * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * 3.14159 * self.radius


class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


class CompositeShape:
    def __init__(self, shapes: list) -> None:
        self.shapes = shapes

    def area(self) -> float:
        return sum(shape.area() for shape in self.shapes)

    def perimeter(self) -> float:
        return sum(shape.perimeter() for shape in self.shapes)


def total_area(shapes: list) -> float:
    """
    Sum area() across every Drawable-conforming item in shapes.

    Edge cases handled:
      - Empty shapes -> 0.0.
      - A list with only non-Drawable items -> 0.0, not an error.
    """
    return sum(shape.area() for shape in shapes if isinstance(shape, Drawable))


def largest_by_area(shapes: list):
    return max(shapes, key=lambda shape: shape.area())
