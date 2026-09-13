"""
Week 7 - OOP II
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in tests/test_week07.py
imports directly from here.
"""


import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        ...


class Circle(Shape):
    def __init__(self, radius: float):
        raise NotImplementedError

    def area(self) -> float:
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        raise NotImplementedError

    def area(self) -> float:
        raise NotImplementedError
