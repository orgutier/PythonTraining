"""
Week 7 -- OOP II.

Coverage plan (each item exercised by the trainee's own code >=3 times):
  keywords: class Child(Parent), super(), isinstance(), abc, ABC,
            @abstractmethod
  modules:  abc, typing
  concepts: polymorphism, duck typing, composition vs inheritance, mixins,
            Protocol structural typing
"""

WEEK = "week07"
TOPIC = "OOP II"
OVERVIEW = (
    "Five exercises covering inheritance, composition, duck typing, "
    "abstract base classes, mixins, and typing.Protocol from Topic 7 at "
    "least three times each -- ending with a runtime_checkable Protocol so "
    "isinstance() and structural typing meet in the same exercise."
)

EXERCISES = [
    {
        "name": "exercise01",
        "title": "Inheritance Basics",
        "summary": "class Child(Parent), a first super(), polymorphism",
        "readme": (
            "Implement:\n\n"
            "- `Animal.__init__(self, name: str)` -- store `self.name`.\n"
            "- `Animal.speak(self) -> str` -- `raise NotImplementedError` "
            "(the base class defines the *interface*, not a default "
            "behavior -- every subclass must override this).\n"
            "- `Dog(Animal)` -- `speak(self) -> str` returns "
            "`f\"{self.name} says Woof!\"`.\n"
            "- `Cat(Animal)` -- `__init__(self, name, indoor=True)` calls "
            "`super().__init__(name)` then stores `self.indoor`; "
            "`speak(self) -> str` returns `f\"{self.name} says Meow!\"`.\n"
            "- `describe_animal(animal) -> str` -- `return animal.speak()`. "
            "This function doesn't care whether `animal` is a `Dog`, a `Cat`, "
            "or anything else with a `.speak()` method -- that's "
            "**polymorphism**: the same call (`animal.speak()`) does the "
            "right thing for whatever type is actually passed in.\n\n"
            "See the Study Reference presentation, Topic 7, for the theory."
        ),
        "stub": '''\
class Animal:
    def __init__(self, name: str):
        raise NotImplementedError

    def speak(self) -> str:
        """Base class defines the interface; subclasses must override."""
        raise NotImplementedError


class Dog(Animal):
    def speak(self) -> str:
        """f"{self.name} says Woof!"."""
        raise NotImplementedError


class Cat(Animal):
    def __init__(self, name: str, indoor: bool = True):
        """super().__init__(name), then store self.indoor."""
        raise NotImplementedError

    def speak(self) -> str:
        """f"{self.name} says Meow!"."""
        raise NotImplementedError


def describe_animal(animal) -> str:
    """animal.speak() -- works for any Animal subclass (polymorphism)."""
    raise NotImplementedError
''',
        "reference": '''\
class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        raise NotImplementedError


class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name} says Woof!"


class Cat(Animal):
    def __init__(self, name: str, indoor: bool = True):
        super().__init__(name)
        self.indoor = indoor

    def speak(self) -> str:
        return f"{self.name} says Meow!"


def describe_animal(animal) -> str:
    return animal.speak()
''',
        "test": '''\
from exercises.week07.exercise01.solution import Animal, Dog, Cat, describe_animal


def test_dog_speak():
    assert Dog("Rex").speak() == "Rex says Woof!"


def test_cat_speak_and_super_init():
    cat = Cat("Whiskers")
    assert cat.speak() == "Whiskers says Meow!"
    assert cat.name == "Whiskers"
    assert cat.indoor is True


def test_describe_animal_polymorphism():
    assert describe_animal(Dog("Rex")) == "Rex says Woof!"
    assert describe_animal(Cat("Whiskers", indoor=False)) == "Whiskers says Meow!"


def test_dog_and_cat_are_animals():
    assert isinstance(Dog("Rex"), Animal)
    assert isinstance(Cat("Whiskers"), Animal)
''',
    },
    {
        "name": "exercise02",
        "title": "super() and Polymorphism",
        "summary": "super() x3 (three-level chain), isinstance(), polymorphism again",
        "readme": (
            "Implement a three-level inheritance chain where each level "
            "*extends* the one before it, rather than just calling its "
            "`__init__`:\n\n"
            "- `Vehicle.__init__(self, make, model)` -- store both. "
            "`describe(self) -> str` -- `f\"{self.make} {self.model}\"`.\n"
            "- `Car(Vehicle)` -- `__init__(self, make, model, doors)` calls "
            "`super().__init__(make, model)` then stores `self.doors`; "
            "`describe(self) -> str` returns `super().describe() + f\" "
            "({self.doors} doors)\"` -- it calls the **parent's** `describe()` "
            "and appends to it, instead of rewriting the whole string.\n"
            "- `ElectricCar(Car)` -- `__init__(self, make, model, doors, "
            "battery_kwh)` calls `super().__init__(make, model, doors)` then "
            "stores `self.battery_kwh`; `describe(self) -> str` returns "
            "`super().describe() + f\", {self.battery_kwh}kWh battery\"`.\n"
            "- `total_description(vehicles: list) -> list[str]` -- "
            "`[v.describe() for v in vehicles]` (polymorphism again: works "
            "across all three classes in one list).\n"
            "- `is_car(vehicle) -> bool` -- `isinstance(vehicle, Car)` -- note "
            "an `ElectricCar` **is** a `Car` too (it inherits from it), so "
            "this returns `True` for both.\n\n"
            "See the Study Reference presentation, Topic 7, for the theory."
        ),
        "stub": '''\
class Vehicle:
    def __init__(self, make, model):
        raise NotImplementedError

    def describe(self) -> str:
        """f"{self.make} {self.model}"."""
        raise NotImplementedError


class Car(Vehicle):
    def __init__(self, make, model, doors):
        """super().__init__(make, model), then store self.doors."""
        raise NotImplementedError

    def describe(self) -> str:
        """super().describe() + f" ({self.doors} doors)"."""
        raise NotImplementedError


class ElectricCar(Car):
    def __init__(self, make, model, doors, battery_kwh):
        """super().__init__(make, model, doors), then store self.battery_kwh."""
        raise NotImplementedError

    def describe(self) -> str:
        """super().describe() + f", {self.battery_kwh}kWh battery"."""
        raise NotImplementedError


def total_description(vehicles: list) -> list:
    """[v.describe() for v in vehicles]."""
    raise NotImplementedError


def is_car(vehicle) -> bool:
    """isinstance(vehicle, Car)."""
    raise NotImplementedError
''',
        "reference": '''\
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def describe(self) -> str:
        return f"{self.make} {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors

    def describe(self) -> str:
        return super().describe() + f" ({self.doors} doors)"


class ElectricCar(Car):
    def __init__(self, make, model, doors, battery_kwh):
        super().__init__(make, model, doors)
        self.battery_kwh = battery_kwh

    def describe(self) -> str:
        return super().describe() + f", {self.battery_kwh}kWh battery"


def total_description(vehicles: list) -> list:
    return [v.describe() for v in vehicles]


def is_car(vehicle) -> bool:
    return isinstance(vehicle, Car)
''',
        "test": '''\
from exercises.week07.exercise02.solution import (
    Vehicle,
    Car,
    ElectricCar,
    total_description,
    is_car,
)


def test_vehicle_describe():
    assert Vehicle("Honda", "Civic").describe() == "Honda Civic"


def test_car_describe_extends_vehicle():
    assert Car("Honda", "Civic", 4).describe() == "Honda Civic (4 doors)"


def test_electric_car_describe_extends_car():
    car = ElectricCar("Tesla", "Model 3", 4, 75)
    assert car.describe() == "Tesla Model 3 (4 doors), 75kWh battery"


def test_total_description_polymorphism():
    vehicles = [Vehicle("A", "B"), Car("C", "D", 2), ElectricCar("E", "F", 4, 50)]
    result = total_description(vehicles)
    assert result == [
        "A B",
        "C D (2 doors)",
        "E F (4 doors), 50kWh battery",
    ]


def test_is_car():
    assert is_car(Car("C", "D", 2)) is True
    assert is_car(ElectricCar("E", "F", 4, 50)) is True
    assert is_car(Vehicle("A", "B")) is False
''',
    },
    {
        "name": "exercise03",
        "title": "Duck Typing and Composition",
        "summary": "duck typing, composition vs inheritance, isinstance()",
        "readme": (
            "Implement:\n\n"
            "- `Engine.start(self) -> str` -- `\"Engine starting...\"`.\n"
            "- `Boat.__init__(self, engine)` -- store `self.engine = engine` "
            "(a `Boat` **has an** `Engine` -- **composition**, not "
            "inheritance: `Boat` doesn't extend `Engine`, it just holds one). "
            "`start(self) -> str` -- `self.engine.start()`.\n"
            "- `Duck.quack(self) -> str` -- `\"Quack!\"`.\n"
            "- `Person.quack(self) -> str` -- `\"I'm quacking like a duck!\"`. "
            "`Duck` and `Person` share **no** base class in common.\n"
            "- `make_it_quack(obj) -> str` -- `obj.quack()`. This works for "
            "*any* object with a `.quack()` method, `Duck` or `Person` or "
            "anything else -- **duck typing**: \"if it quacks like a duck, "
            "treat it like a duck,\" no shared inheritance required.\n"
            "- `is_duck_instance(obj) -> bool` -- `isinstance(obj, Duck)`. "
            "Unlike `make_it_quack`, this one *does* care about the actual "
            "type -- contrast the two.\n\n"
            "See the Study Reference presentation, Topic 7, for the theory."
        ),
        "stub": '''\
class Engine:
    def start(self) -> str:
        """"Engine starting..."."""
        raise NotImplementedError


class Boat:
    def __init__(self, engine):
        """Store self.engine = engine (composition: Boat HAS an Engine)."""
        raise NotImplementedError

    def start(self) -> str:
        """self.engine.start()."""
        raise NotImplementedError


class Duck:
    def quack(self) -> str:
        """"Quack!"."""
        raise NotImplementedError


class Person:
    def quack(self) -> str:
        """"I'm quacking like a duck!"."""
        raise NotImplementedError


def make_it_quack(obj) -> str:
    """obj.quack() -- works for anything with a .quack() method (duck typing)."""
    raise NotImplementedError


def is_duck_instance(obj) -> bool:
    """isinstance(obj, Duck)."""
    raise NotImplementedError
''',
        "reference": '''\
class Engine:
    def start(self) -> str:
        return "Engine starting..."


class Boat:
    def __init__(self, engine):
        self.engine = engine

    def start(self) -> str:
        return self.engine.start()


class Duck:
    def quack(self) -> str:
        return "Quack!"


class Person:
    def quack(self) -> str:
        return "I'm quacking like a duck!"


def make_it_quack(obj) -> str:
    return obj.quack()


def is_duck_instance(obj) -> bool:
    return isinstance(obj, Duck)
''',
        "test": '''\
from exercises.week07.exercise03.solution import (
    Engine,
    Boat,
    Duck,
    Person,
    make_it_quack,
    is_duck_instance,
)


def test_boat_composition_delegates_to_engine():
    boat = Boat(Engine())
    assert boat.start() == "Engine starting..."


def test_make_it_quack_duck():
    assert make_it_quack(Duck()) == "Quack!"


def test_make_it_quack_person_duck_typing():
    assert make_it_quack(Person()) == "I'm quacking like a duck!"


def test_is_duck_instance():
    assert is_duck_instance(Duck()) is True
    assert is_duck_instance(Person()) is False
''',
    },
    {
        "name": "exercise04",
        "title": "Abstract Base Classes",
        "summary": "abc module, ABC, @abstractmethod x3",
        "readme": (
            "Implement `Shape(ABC)` with three `@abstractmethod`s, plus two "
            "concrete subclasses:\n\n"
            "- `Shape.area(self) -> float` (`@abstractmethod`).\n"
            "- `Shape.perimeter(self) -> float` (`@abstractmethod`).\n"
            "- `Shape.name(self) -> str` (`@abstractmethod`) -- a short label "
            "like `\"circle\"`.\n"
            "- `Circle(Shape)` -- `__init__(self, radius)`; `area()` = "
            "`3.14159 * radius ** 2`; `perimeter()` = `2 * 3.14159 * radius`; "
            "`name()` = `\"circle\"`.\n"
            "- `Square(Shape)` -- `__init__(self, side)`; `area()` = "
            "`side ** 2`; `perimeter()` = `4 * side`; `name()` = `\"square\"`.\n\n"
            "`Shape` inherits from `abc.ABC` and declares three abstract "
            "methods -- that makes `Shape` itself impossible to instantiate "
            "directly (`Shape()` raises `TypeError`), and forces every "
            "concrete subclass to implement *all three* methods before it "
            "can be instantiated at all. This is a stronger guarantee than "
            "`Animal.speak()` in Exercise 1, which only fails if you *call* "
            "the unoverridden method.\n\n"
            "See the Study Reference presentation, Topic 7, for the theory."
        ),
        "stub": '''\
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
''',
        "reference": '''\
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
''',
        "test": '''\
import pytest
from exercises.week07.exercise04.solution import Shape, Circle, Square


def test_shape_cannot_be_instantiated():
    with pytest.raises(TypeError):
        Shape()


def test_circle_area_and_perimeter():
    c = Circle(2)
    assert round(c.area(), 2) == 12.57
    assert round(c.perimeter(), 2) == 12.57
    assert c.name() == "circle"


def test_square_area_and_perimeter():
    s = Square(4)
    assert s.area() == 16
    assert s.perimeter() == 16
    assert s.name() == "square"


def test_circle_and_square_are_shapes():
    assert isinstance(Circle(1), Shape)
    assert isinstance(Square(1), Shape)
''',
    },
    {
        "name": "exercise05",
        "title": "Mixins and Protocols",
        "summary": "mixins, typing.Protocol structural typing, isinstance()",
        "readme": (
            "Implement:\n\n"
            "- `LoggingMixin.log(self, message: str) -> str` -- "
            "`f\"[{self.__class__.__name__}] {message}\"`. A **mixin**: a "
            "small class meant to be combined with others via multiple "
            "inheritance, adding one focused piece of reusable behavior -- "
            "never instantiated on its own.\n"
            "- `SerializableMixin.to_dict(self) -> dict` -- `dict(self.__dict__)`.\n"
            "- `Widget(LoggingMixin, SerializableMixin)` -- `__init__(self, "
            "name)` stores `self.name`. `Widget` gets both `.log()` and "
            "`.to_dict()` for free by combining the two mixins -- no shared "
            "\"is-a\" hierarchy needed, just behavior composed in.\n"
            "- `SupportsArea` (`typing.Protocol`, `@runtime_checkable`) -- "
            "declares `def area(self) -> float: ...` as the interface.\n"
            "- `Coin.__init__(self, radius)` / `Coin.area(self) -> float` "
            "(`3.14159 * radius ** 2`) -- `Coin` **never inherits from** "
            "`SupportsArea`. It just happens to have a matching `area()` "
            "method.\n"
            "- `total_area(shapes: list) -> float` -- "
            "`sum(s.area() for s in shapes)`.\n"
            "- `supports_area(obj) -> bool` -- `isinstance(obj, SupportsArea)`. "
            "Because `SupportsArea` is `@runtime_checkable`, this actually "
            "works on `Coin` even though `Coin` never inherits from it -- "
            "`isinstance()` checks the *shape* of the object (does it have "
            "an `area()` method?), not its class hierarchy. This is "
            "**structural typing**: the formal, type-checker-friendly "
            "version of the duck typing from Exercise 3.\n\n"
            "See the Study Reference presentation, Topic 7, for the theory."
        ),
        "stub": '''\
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
''',
        "reference": '''\
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
''',
        "test": '''\
from exercises.week07.exercise05.solution import (
    LoggingMixin,
    SerializableMixin,
    Widget,
    SupportsArea,
    Coin,
    total_area,
    supports_area,
)


def test_widget_uses_both_mixins():
    w = Widget("gadget")
    assert w.log("created") == "[Widget] created"
    assert w.to_dict() == {"name": "gadget"}


def test_widget_is_instance_of_both_mixins():
    w = Widget("gadget")
    assert isinstance(w, LoggingMixin)
    assert isinstance(w, SerializableMixin)


def test_total_area():
    assert round(total_area([Coin(1), Coin(2)]), 2) == round(3.14159 + 12.56636, 2)


def test_supports_area_structural_typing():
    assert supports_area(Coin(1)) is True
    assert supports_area("not a shape") is False


def test_coin_never_inherits_from_supports_area():
    assert SupportsArea not in Coin.__bases__
''',
    },
]
