from typing import Protocol, runtime_checkable


class LoggingMixin:
    def log(self, message: str) -> str:
        return f"[{self.__class__.__name__}] {message}"


class SerializableMixin:
    def to_dict(self) -> dict:
        return dict(self.__dict__)


class Widget(LoggingMixin, SerializableMixin):
    def __init__(self, name):
        self.name = name


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
