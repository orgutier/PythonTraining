"""
OOP II -- Abstract Base Classes
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage07_mid01.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage07/mid01/ and import it as a submodule (e.g.
`from exercises.stage07.mid01 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def perimeter(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, radius):
        raise NotImplementedError

    def area(self) -> float:
        raise NotImplementedError

    def perimeter(self) -> float:
        raise NotImplementedError

    def name(self) -> str:
        raise NotImplementedError


class Square(Shape):
    def __init__(self, side):
        raise NotImplementedError

    def area(self) -> float:
        raise NotImplementedError

    def perimeter(self) -> float:
        raise NotImplementedError

    def name(self) -> str:
        raise NotImplementedError
