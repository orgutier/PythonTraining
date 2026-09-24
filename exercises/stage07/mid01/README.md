# Abstract Base Classes

Implement `Shape(ABC)` with three `@abstractmethod`s, plus two concrete subclasses:

- `Shape.area(self) -> float` (`@abstractmethod`).
- `Shape.perimeter(self) -> float` (`@abstractmethod`).
- `Shape.name(self) -> str` (`@abstractmethod`) -- a short label like `"circle"`.
- `Circle(Shape)` -- `__init__(self, radius)`; `area()` = `3.14159 * radius ** 2`; `perimeter()` = `2 * 3.14159 * radius`; `name()` = `"circle"`.
- `Square(Shape)` -- `__init__(self, side)`; `area()` = `side ** 2`; `perimeter()` = `4 * side`; `name()` = `"square"`.

`Shape` inherits from `abc.ABC` and declares three abstract methods -- that makes `Shape` itself impossible to instantiate directly (`Shape()` raises `TypeError`), and forces every concrete subclass to implement *all three* methods before it can be instantiated at all. This is a stronger guarantee than an ordinary base method that merely `raise`s if left unoverridden: that only fails if you *call* it, while `@abstractmethod` fails at **instantiation** time.

See the Study Reference presentation, Topic 7 (Mid tier), for the theory.
