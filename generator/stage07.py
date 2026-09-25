"""
Stage 7 -- OOP II.

Rolled onto the tier-named exercise convention: a minimum of two exercises
per Basic/Mid/Advanced tier. Every exercise here is class-based -- Stage
7's whole subject is inheritance/composition/abstraction, which are
inherently class-shaped content.

Coverage plan (every item below is exercised by the trainee's own code,
generally 2+ times across these 6 exercises):

  Basic:    class Child(Parent), super(), isinstance(), typing module,
            polymorphism, duck typing
  Mid:      abc, ABC, @abstractmethod, abc module, composition vs
            inheritance
  Advanced: mixins, Protocol structural typing
"""

STAGE = "stage07"
TOPIC = "OOP II"
OVERVIEW = (
    "Six exercises, two per tier: inheritance/super()/polymorphism "
    "contrasted with duck typing in Basic, abstract base classes "
    "contrasted with composition's runtime flexibility in Mid, and mixins "
    "plus a runtime_checkable Protocol in Advanced."
)

EXERCISES = [
    {
        "name": "tier1_basic01",
        "title": "Animal Sounds: Inheritance and Duck Typing",
        "summary": "class Child(Parent), super(), polymorphism, duck typing (side by side)",
        "readme": (
            "Two different mechanisms for \"the same call does the right "
            "thing for different types\" -- inheritance-based, and "
            "duck-typed. Implement:\n\n"
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
            "Works for any `Animal` subclass -- **polymorphism** through a "
            "shared base class.\n\n"
            "Now the duck-typed version, with **no shared base class at "
            "all**:\n\n"
            "- `Duck.quack(self) -> str` -- `\"Quack!\"`.\n"
            "- `Person.quack(self) -> str` -- `\"I'm quacking like a "
            "duck!\"`. `Duck` and `Person` share nothing in common.\n"
            "- `make_it_quack(obj) -> str` -- `obj.quack()`. This works for "
            "*any* object with a `.quack()` method -- **duck typing**: "
            "\"if it quacks like a duck, treat it like a duck,\" no "
            "inheritance required. Compare it with `describe_animal` "
            "above: both get \"the right behavior for the type passed in\", "
            "but one relies on a shared `Animal` base class and the other "
            "relies on nothing but a matching method name.\n\n"
            "See the Study Reference presentation, Topic 7 (Basic tier), "
            "for the theory."
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
    """animal.speak() -- works for any Animal subclass (polymorphism via inheritance)."""
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
    """obj.quack() -- works for anything with a .quack() method (duck typing, no shared base)."""
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


class Duck:
    def quack(self) -> str:
        return "Quack!"


class Person:
    def quack(self) -> str:
        return "I'm quacking like a duck!"


def make_it_quack(obj) -> str:
    return obj.quack()
''',
        "test": '''\
from exercises.stage07.tier1_basic01.solution import (
    Animal,
    Dog,
    Cat,
    describe_animal,
    Duck,
    Person,
    make_it_quack,
)


def test_dog_speak():
    """Dog overrides Animal.speak()."""
    assert Dog("Rex").speak() == "Rex says Woof!"


def test_cat_speak_and_super_init():
    """Cat.__init__ must call super().__init__(name) before setting its own indoor attribute."""
    cat = Cat("Whiskers")
    assert cat.speak() == "Whiskers says Meow!"
    assert cat.name == "Whiskers"
    assert cat.indoor is True


def test_describe_animal_polymorphism():
    """describe_animal works for any Animal subclass via inheritance-based polymorphism."""
    assert describe_animal(Dog("Rex")) == "Rex says Woof!"
    assert describe_animal(Cat("Whiskers", indoor=False)) == "Whiskers says Meow!"


def test_dog_and_cat_are_animals():
    """Dog/Cat must both be real Animal subclasses."""
    assert isinstance(Dog("Rex"), Animal)
    assert isinstance(Cat("Whiskers"), Animal)


def test_make_it_quack_duck_typing_with_no_shared_base_class():
    """make_it_quack works on Duck and Person alike -- neither shares a base class, only a matching .quack() method."""
    assert make_it_quack(Duck()) == "Quack!"
    assert make_it_quack(Person()) == "I'm quacking like a duck!"
    assert Duck.__bases__ == (object,)
    assert Person.__bases__ == (object,)
''',
    },
    {
        "name": "tier1_basic02",
        "title": "Vehicle Fleet",
        "summary": "super() (three-level chain), isinstance(), typing module, polymorphism",
        "readme": (
            "Implement a three-level inheritance chain where each level "
            "*extends* the one before it, rather than just calling its "
            "`__init__`:\n\n"
            "- `Vehicle.__init__(self, make, model)` -- store both. "
            "`describe(self) -> str` -- `f\"{self.make} {self.model}\"`.\n"
            "- `Car(Vehicle)` -- `__init__(self, make, model, doors)` calls "
            "`super().__init__(make, model)` then stores `self.doors`; "
            "`describe(self) -> str` returns `super().describe() + f\" "
            "({self.doors} doors)\"` -- it calls the **parent's** "
            "`describe()` and appends to it, instead of rewriting the "
            "whole string.\n"
            "- `ElectricCar(Car)` -- `__init__(self, make, model, doors, "
            "battery_kwh)` calls `super().__init__(make, model, doors)` "
            "then stores `self.battery_kwh`; `describe(self) -> str` "
            "returns `super().describe() + f\", {self.battery_kwh}kWh "
            "battery\"`.\n"
            "- `fleet_summary(vehicles: typing.List[Vehicle]) -> str` -- "
            "`\", \".join(v.describe() for v in vehicles)` (note the "
            "`typing.List[Vehicle]` type hint -- polymorphism means this "
            "one function handles a list mixing all three classes).\n"
            "- `is_car(vehicle) -> bool` -- `isinstance(vehicle, Car)` -- "
            "note an `ElectricCar` **is** a `Car` too (it inherits from "
            "it), so this returns `True` for both.\n\n"
            "See the Study Reference presentation, Topic 7 (Basic tier), "
            "for the theory."
        ),
        "stub": '''\
from typing import List


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


def fleet_summary(vehicles: List[Vehicle]) -> str:
    """", ".join(v.describe() for v in vehicles)."""
    raise NotImplementedError


def is_car(vehicle) -> bool:
    """isinstance(vehicle, Car)."""
    raise NotImplementedError
''',
        "reference": '''\
from typing import List


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


def fleet_summary(vehicles: List[Vehicle]) -> str:
    return ", ".join(v.describe() for v in vehicles)


def is_car(vehicle) -> bool:
    return isinstance(vehicle, Car)
''',
        "test": '''\
from exercises.stage07.tier1_basic02.solution import (
    Vehicle,
    Car,
    ElectricCar,
    fleet_summary,
    is_car,
)


def test_vehicle_describe():
    """Vehicle.describe() == f"{make} {model}"."""
    assert Vehicle("Honda", "Civic").describe() == "Honda Civic"


def test_car_describe_extends_vehicle_via_super():
    """Car.describe() must call super().describe() and append to it, not rewrite the whole string."""
    assert Car("Honda", "Civic", 4).describe() == "Honda Civic (4 doors)"


def test_electric_car_describe_extends_car_via_super():
    """ElectricCar.describe() extends Car.describe() via super(), which itself extends Vehicle.describe() -- a three-level chain."""
    car = ElectricCar("Tesla", "Model 3", 4, 75)
    assert car.describe() == "Tesla Model 3 (4 doors), 75kWh battery"


def test_fleet_summary_polymorphism_across_all_three_classes():
    """fleet_summary works across a mixed list of Vehicle/Car/ElectricCar via polymorphism."""
    vehicles = [Vehicle("A", "B"), Car("C", "D", 2), ElectricCar("E", "F", 4, 50)]
    assert fleet_summary(vehicles) == "A B, C D (2 doors), E F (4 doors), 50kWh battery"


def test_is_car():
    """is_car == isinstance(vehicle, Car) -- True for ElectricCar too (it IS a Car), False for a plain Vehicle."""
    assert is_car(Car("C", "D", 2)) is True
    assert is_car(ElectricCar("E", "F", 4, 50)) is True
    assert is_car(Vehicle("A", "B")) is False
''',
    },
    {
        "name": "tier2_mid01",
        "title": "Abstract Base Classes",
        "summary": "abc module, ABC, @abstractmethod",
        "readme": (
            "Implement `Shape(ABC)` with three `@abstractmethod`s, plus "
            "two concrete subclasses:\n\n"
            "- `Shape.area(self) -> float` (`@abstractmethod`).\n"
            "- `Shape.perimeter(self) -> float` (`@abstractmethod`).\n"
            "- `Shape.name(self) -> str` (`@abstractmethod`) -- a short "
            "label like `\"circle\"`.\n"
            "- `Circle(Shape)` -- `__init__(self, radius)`; `area()` = "
            "`3.14159 * radius ** 2`; `perimeter()` = `2 * 3.14159 * "
            "radius`; `name()` = `\"circle\"`.\n"
            "- `Square(Shape)` -- `__init__(self, side)`; `area()` = "
            "`side ** 2`; `perimeter()` = `4 * side`; `name()` = "
            "`\"square\"`.\n\n"
            "`Shape` inherits from `abc.ABC` and declares three abstract "
            "methods -- that makes `Shape` itself impossible to "
            "instantiate directly (`Shape()` raises `TypeError`), and "
            "forces every concrete subclass to implement *all three* "
            "methods before it can be instantiated at all. This is a "
            "stronger guarantee than an ordinary base method that merely "
            "`raise`s if left unoverridden: that only fails if you *call* "
            "it, while `@abstractmethod` fails at **instantiation** time.\n\n"
            "See the Study Reference presentation, Topic 7 (Mid tier), "
            "for the theory."
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
from exercises.stage07.tier2_mid01.solution import Shape, Circle, Square


def test_shape_cannot_be_instantiated():
    """Shape(ABC) with @abstractmethods must raise TypeError on direct instantiation."""
    with pytest.raises(TypeError):
        Shape()


def test_circle_area_and_perimeter():
    """Circle implements all three abstract methods."""
    c = Circle(2)
    assert round(c.area(), 2) == 12.57
    assert round(c.perimeter(), 2) == 12.57
    assert c.name() == "circle"


def test_square_area_and_perimeter():
    """Square implements all three abstract methods."""
    s = Square(4)
    assert s.area() == 16
    assert s.perimeter() == 16
    assert s.name() == "square"


def test_circle_and_square_are_shapes():
    """Circle/Square must both be real Shape subclasses."""
    assert isinstance(Circle(1), Shape)
    assert isinstance(Square(1), Shape)
''',
    },
    {
        "name": "tier2_mid02",
        "title": "Composition and Swappable Engines",
        "summary": "composition vs inheritance",
        "readme": (
            "Two interchangeable engines and a boat that **has an** "
            "engine, rather than **is an** engine -- the point of "
            "composition. Implement:\n\n"
            "- `GasEngine.start(self) -> str` -- "
            "`\"Gas engine roaring to life...\"`.\n"
            "- `ElectricEngine.start(self) -> str` -- "
            "`\"Electric engine humming...\"`.\n"
            "- `Boat.__init__(self, engine)` -- store `self.engine = "
            "engine` (**composition**: `Boat` doesn't extend `GasEngine`/"
            "`ElectricEngine`, it just *holds one*). `start(self) -> str` "
            "-- `self.engine.start()` (delegates to whichever engine it "
            "was given).\n"
            "- `swap_engine(boat, new_engine) -> None` -- "
            "`boat.engine = new_engine`.\n\n"
            "This is what composition buys you that inheritance can't: "
            "`swap_engine` changes a `Boat`'s behavior **at runtime**, "
            "with no class hierarchy to touch at all. Rewriting this with "
            "inheritance would mean either a `GasBoat`/`ElectricBoat` "
            "class pair (can't switch after construction) or multiple "
            "inheritance from both engine classes at once (`Boat` would "
            "*be* both kinds of engine, which doesn't make sense).\n\n"
            "See the Study Reference presentation, Topic 7 (Mid tier), "
            "for the theory."
        ),
        "stub": '''\
class GasEngine:
    def start(self) -> str:
        """"Gas engine roaring to life..."."""
        raise NotImplementedError


class ElectricEngine:
    def start(self) -> str:
        """"Electric engine humming..."."""
        raise NotImplementedError


class Boat:
    def __init__(self, engine):
        """Store self.engine = engine (composition: Boat HAS an engine, doesn't extend one)."""
        raise NotImplementedError

    def start(self) -> str:
        """self.engine.start() -- delegates to whichever engine it holds."""
        raise NotImplementedError


def swap_engine(boat, new_engine) -> None:
    """boat.engine = new_engine -- swap behavior at runtime, no class hierarchy involved."""
    raise NotImplementedError
''',
        "reference": '''\
class GasEngine:
    def start(self) -> str:
        return "Gas engine roaring to life..."


class ElectricEngine:
    def start(self) -> str:
        return "Electric engine humming..."


class Boat:
    def __init__(self, engine):
        self.engine = engine

    def start(self) -> str:
        return self.engine.start()


def swap_engine(boat, new_engine) -> None:
    boat.engine = new_engine
''',
        "test": '''\
from exercises.stage07.tier2_mid02.solution import GasEngine, ElectricEngine, Boat, swap_engine


def test_boat_composition_delegates_to_gas_engine():
    """Boat.start() delegates to whatever engine object it holds (composition, not inheritance)."""
    boat = Boat(GasEngine())
    assert boat.start() == "Gas engine roaring to life..."


def test_boat_composition_delegates_to_electric_engine():
    """The same Boat class works with a completely different engine object, with no shared inheritance needed."""
    boat = Boat(ElectricEngine())
    assert boat.start() == "Electric engine humming..."


def test_swap_engine_changes_behavior_at_runtime():
    """swap_engine replaces boat.engine after construction -- behavior changes without touching any class hierarchy."""
    boat = Boat(GasEngine())
    assert boat.start() == "Gas engine roaring to life..."
    swap_engine(boat, ElectricEngine())
    assert boat.start() == "Electric engine humming..."


def test_boat_is_not_an_engine():
    """Boat must NOT inherit from either engine class -- it holds one, it isn't one."""
    boat = Boat(GasEngine())
    assert not isinstance(boat, GasEngine)
    assert not isinstance(boat, ElectricEngine)
''',
    },
    {
        "name": "tier3_advanced01",
        "title": "Mixins",
        "summary": "mixins (multiple inheritance for composed-in behavior)",
        "readme": (
            "Implement two **mixins** -- small classes meant to be "
            "combined with others via multiple inheritance, each adding "
            "one focused piece of reusable behavior, never instantiated "
            "on their own:\n\n"
            "- `LoggingMixin.log(self, message: str) -> str` -- "
            "`f\"[{self.__class__.__name__}] {message}\"`.\n"
            "- `SerializableMixin.to_dict(self) -> dict` -- "
            "`dict(self.__dict__)`.\n"
            "- `Widget(LoggingMixin, SerializableMixin)` -- "
            "`__init__(self, name)` stores `self.name`. `Widget` gets "
            "both `.log()` and `.to_dict()` for free by combining the two "
            "mixins -- no shared \"is-a\" hierarchy needed beyond the "
            "mixins themselves, just behavior composed in through "
            "multiple inheritance.\n\n"
            "Note `self.__class__.__name__` inside `LoggingMixin.log` -- "
            "because it reads the *actual* class of whatever instance "
            "calls it (`\"Widget\"`), not `\"LoggingMixin\"`, the same "
            "mixin code produces a correctly-labeled message no matter "
            "which class mixes it in.\n\n"
            "See the Study Reference presentation, Topic 7 (Advanced "
            "tier), for the theory."
        ),
        "stub": '''\
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
''',
        "reference": '''\
class LoggingMixin:
    def log(self, message: str) -> str:
        return f"[{self.__class__.__name__}] {message}"


class SerializableMixin:
    def to_dict(self) -> dict:
        return dict(self.__dict__)


class Widget(LoggingMixin, SerializableMixin):
    def __init__(self, name):
        self.name = name
''',
        "test": '''\
from exercises.stage07.tier3_advanced01.solution import LoggingMixin, SerializableMixin, Widget


def test_widget_uses_both_mixins():
    """Widget gets .log() and .to_dict() for free by combining both mixins."""
    w = Widget("gadget")
    assert w.log("created") == "[Widget] created"
    assert w.to_dict() == {"name": "gadget"}


def test_log_reports_the_actual_class_name():
    """LoggingMixin.log must read self.__class__.__name__, so it reports "Widget", not "LoggingMixin"."""
    w = Widget("gadget")
    assert "Widget" in w.log("test")
    assert "LoggingMixin" not in w.log("test")


def test_widget_is_instance_of_both_mixins():
    """Widget must be a real instance of both mixin classes via multiple inheritance."""
    w = Widget("gadget")
    assert isinstance(w, LoggingMixin)
    assert isinstance(w, SerializableMixin)
''',
    },
    {
        "name": "tier3_advanced02",
        "title": "Protocol Structural Typing",
        "summary": "typing.Protocol, @runtime_checkable, isinstance() (structural)",
        "readme": (
            "Implement a `typing.Protocol` and a class that satisfies it "
            "**without ever inheriting from it**:\n\n"
            "- `SupportsArea` (`typing.Protocol`, `@runtime_checkable`) -- "
            "declares `def area(self) -> float: ...` as the interface "
            "(already given).\n"
            "- `Coin.__init__(self, radius)` / `Coin.area(self) -> float` "
            "(`3.14159 * radius ** 2`) -- `Coin` **never inherits from** "
            "`SupportsArea`. It just happens to have a matching `area()` "
            "method.\n"
            "- `total_area(shapes: list) -> float` -- "
            "`sum(s.area() for s in shapes)`.\n"
            "- `supports_area(obj) -> bool` -- "
            "`isinstance(obj, SupportsArea)`. Because `SupportsArea` is "
            "`@runtime_checkable`, this actually works on `Coin` even "
            "though `Coin` never inherits from it -- `isinstance()` "
            "checks the *shape* of the object (does it have an `area()` "
            "method?), not its class hierarchy.\n\n"
            "This is **structural typing**: the formal, type-checker-"
            "friendly version of the duck typing from the first Basic "
            "exercise (`make_it_quack`) -- same underlying idea (match by "
            "shape, not ancestry), but now expressed as a real type "
            "(`SupportsArea`) that both `isinstance()` and a static type "
            "checker can understand.\n\n"
            "See the Study Reference presentation, Topic 7 (Advanced "
            "tier), for the theory."
        ),
        "stub": '''\
from typing import Protocol, runtime_checkable


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
from exercises.stage07.tier3_advanced02.solution import SupportsArea, Coin, total_area, supports_area


def test_total_area():
    """total_area == sum(s.area() for s in shapes)."""
    assert round(total_area([Coin(1), Coin(2)]), 2) == round(3.14159 + 12.56636, 2)


def test_supports_area_structural_typing():
    """supports_area(Coin(...)) is True via structural typing, despite Coin never inheriting from SupportsArea."""
    assert supports_area(Coin(1)) is True
    assert supports_area("not a shape") is False


def test_coin_never_inherits_from_supports_area():
    """Coin must satisfy SupportsArea purely structurally -- SupportsArea must not appear in its base classes."""
    assert SupportsArea not in Coin.__bases__
''',
    },
    {
        "name": "tier4_testing",
        "title": "Testing Without a Framework: Catch the Bug",
        "summary": "manual, framework-free verification -- your own check() helper, no assert, no pytest",
        "readme": (
            "Every other exercise in this stage asked you to implement "
            "something. This one asks you to **verify** something -- with "
            "your own hand-rolled tools, not `pytest`/`unittest` (don't "
            "import either in this file).\n\n"
            "Given, don't modify -- two pairs of implementations, each "
            "pair *supposed* to behave the same way; at least one in each "
            "pair has a bug. Your job is to catch it by testing, not to "
            "fix it:\n\n"
            "```python\n"
            "class Shape:\n"
            "    def area(self):\n"
            "        raise NotImplementedError\n\n"
            "class Square(Shape):\n"
            "    def __init__(self, side):\n"
            "        self.side = side\n\n"
            "    def area(self):\n"
            "        return self.side ** 2\n\n"
            "class SquareBuggy(Shape):\n"
            "    def __init__(self, side):\n"
            "        self.side = side\n\n"
            "    def area(self):\n"
            "        return self.side * 2\n\n"
            "class Duck:\n"
            "    def quack(self):\n"
            "        return \"Quack!\"\n\n"
            "def make_it_quack_correct(obj):\n"
            "    return obj.quack()\n\n"
            "def make_it_quack_buggy(obj):\n"
            "    return obj.quack\n"
            "```\n\n"
            "The spec each pair is supposed to meet:\n\n"
            "- **area** (on a `Shape` subclass) should equal `side ** 2` "
            "for a square.\n"
            "- **make_it_quack** should **call** the object's `.quack()` "
            "method and return its result (a `str`), not the method "
            "object itself.\n\n"
            "Implement:\n\n"
            "- `check(description: str, condition: bool) -> bool` -- "
            "append `(description, condition)` to the given `_check_log` "
            "list, then return `condition`. Unlike `assert`, this must "
            "**never raise** -- a failed check should become a recorded "
            "`False` in the log, not a crash that stops every check after "
            "it from running.\n"
            "- `run_all_checks() -> dict` -- call `check()` **exactly "
            "four times**:\n"
            "  - `Square(4).area()` and `SquareBuggy(4).area()`, each "
            "compared against the spec-computed expected value, `16`.\n"
            "  - `make_it_quack_correct(Duck())` and "
            "`make_it_quack_buggy(Duck())`, each compared against the "
            "spec-computed expected value, `\"Quack!\"`.\n\n"
            "  Then return `{\"total\": ..., \"passed\": ..., \"failed\": "
            "...}` built from `_check_log`.\n\n"
            "See the Study Reference presentation, Topic 7, for the theory."
        ),
        "stub": '''\
class Shape:
    def area(self):
        raise NotImplementedError


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class SquareBuggy(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * 2


class Duck:
    def quack(self):
        return "Quack!"


def make_it_quack_correct(obj):
    return obj.quack()


def make_it_quack_buggy(obj):
    return obj.quack


_check_log = []


def check(description: str, condition: bool) -> bool:
    """Append (description, condition) to _check_log; return condition. Must NEVER raise."""
    raise NotImplementedError


def run_all_checks() -> dict:
    """Call check() exactly 4 times (see README.md), then return {"total": ..., "passed": ..., "failed": [...]}."""
    raise NotImplementedError
''',
        "reference": '''\
class Shape:
    def area(self):
        raise NotImplementedError


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class SquareBuggy(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * 2


class Duck:
    def quack(self):
        return "Quack!"


def make_it_quack_correct(obj):
    return obj.quack()


def make_it_quack_buggy(obj):
    return obj.quack


_check_log = []


def check(description: str, condition: bool) -> bool:
    _check_log.append((description, condition))
    return condition


def run_all_checks() -> dict:
    _check_log.clear()

    check("Square(4).area() == 16", Square(4).area() == 16)
    check("SquareBuggy(4).area() == 16", SquareBuggy(4).area() == 16)

    check("make_it_quack_correct(Duck()) == 'Quack!'", make_it_quack_correct(Duck()) == "Quack!")
    check("make_it_quack_buggy(Duck()) == 'Quack!'", make_it_quack_buggy(Duck()) == "Quack!")

    total = len(_check_log)
    passed = sum(1 for _, ok in _check_log if ok)
    failed = [desc for desc, ok in _check_log if not ok]
    return {"total": total, "passed": passed, "failed": failed}
''',
        "test": '''\
from exercises.stage07.tier4_testing.solution import check, run_all_checks, _check_log


def test_check_records_a_passing_condition_and_returns_it():
    """check(description, True) must append (description, True) to _check_log and return True."""
    _check_log.clear()
    result = check("sample passing check", True)
    assert result is True
    assert _check_log[-1] == ("sample passing check", True)


def test_check_never_raises_on_a_failing_condition():
    """check(description, False) must NOT raise -- unlike assert, it records the failure and returns False."""
    _check_log.clear()
    result = check("sample failing check", False)
    assert result is False
    assert _check_log[-1] == ("sample failing check", False)


def test_run_all_checks_runs_exactly_four_checks():
    """run_all_checks must call check() exactly once per implementation named in README.md -- four total."""
    summary = run_all_checks()
    assert summary["total"] == 4


def test_run_all_checks_catches_both_bugs():
    """Checked against the shared spec-derived value, Square/make_it_quack_correct pass and the _buggy versions fail."""
    summary = run_all_checks()
    assert summary["passed"] == 2
    assert len(summary["failed"]) == 2
''',
    },
]
