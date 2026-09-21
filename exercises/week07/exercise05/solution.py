"""
OOP II -- Mixins and Protocols
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the aggregated test suite in
tests/test_week07.py imports directly from here. Need a helper function or
class of your own? Add another .py file next to this one inside
exercises/week07/exercise05/ and import it as a submodule (e.g.
`from exercises.week07.exercise05 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


from typing import Protocol, runtime_checkable


class LoggingMixin:
    def log(self, message: str) -> str:
        """f"[{self.__class__.__name__}] {message}"."""
        raise NotImplementedError


class SerializableMixin:
    def to_dict(self) -> dict:
        """dict(self.__dict__)."""
        raise NotImplementedError


class Widget(LoggingMixin, SerializableMixin):
    def __init__(self, name):
        raise NotImplementedError


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
