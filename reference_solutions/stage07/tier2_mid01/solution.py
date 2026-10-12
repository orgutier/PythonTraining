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
        self.radius = radius

    def area(self) -> float:
        return 3.14159 * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * 3.14159 * self.radius

    def name(self) -> str:
        return "circle"


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self) -> float:
        return self.side ** 2

    def perimeter(self) -> float:
        return 4 * self.side

    def name(self) -> str:
        return "square"
