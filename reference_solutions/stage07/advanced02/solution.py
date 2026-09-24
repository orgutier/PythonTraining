from typing import Protocol, runtime_checkable


@runtime_checkable
class SupportsArea(Protocol):
    def area(self) -> float: ...


class Coin:
    def __init__(self, radius):
        self.radius = radius

    def area(self) -> float:
        return 3.14159 * self.radius ** 2


def total_area(shapes: list) -> float:
    return sum(s.area() for s in shapes)


def supports_area(obj) -> bool:
    return isinstance(obj, SupportsArea)
