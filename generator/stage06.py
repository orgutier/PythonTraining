"""
Stage 6 -- OOP I.

Coverage plan (each item exercised by the trainee's own code >=3 times):
  keywords: class, self, __init__, @property, @x.setter, @staticmethod,
            @classmethod, cls
  dunders:  __init__, __get__/__set__ (preview)
  concepts: encapsulation, instance vs class attributes,
            __slots__ memory savings, descriptors
"""

STAGE = "stage06"
TOPIC = "OOP I"
OVERVIEW = (
    "Five exercises covering class fundamentals from Topic 6 at least "
    "three times each: properties with validating setters, the "
    "class-vs-instance-attribute distinction via classmethod alternate "
    "constructors, __slots__, and a hand-rolled descriptor as a preview of "
    "what @property is built on."
)

EXERCISES = [
    {
        "name": "exercise01",
        "title": "Bank Account",
        "summary": "class, self, __init__, @property, @x.setter, @staticmethod, encapsulation",
        "readme": (
            "Implement `BankAccount`:\n\n"
            "- `__init__(self, owner: str, balance: float = 0)` -- store "
            "`self.owner = owner` and set the *property* `self.balance = "
            "balance` (going through the setter below, so an invalid starting "
            "balance is rejected the same way a later deposit would be).\n"
            "- `is_valid_amount(amount) -> bool` (`@staticmethod`) -- `True` "
            "if `amount` is an `int`/`float` and `amount >= 0`. It's a "
            "`@staticmethod` because it doesn't need `self` at all -- it's "
            "just a validation helper that happens to live on the class.\n"
            "- `balance` (`@property`) -- getter returns `self._balance` (the "
            "real, \"private-by-convention\" storage -- this is what "
            "*encapsulation* means here: callers use `.balance`, never "
            "`._balance` directly).\n"
            "- `balance` setter (`@balance.setter`) -- `raise ValueError` if "
            "`not self.is_valid_amount(value)`, else set `self._balance = "
            "value`.\n"
            "- `deposit(self, amount) -> None` -- `self.balance = self.balance "
            "+ amount` (going through the property, so the setter's "
            "validation applies).\n"
            "- `withdraw(self, amount) -> None` -- `raise ValueError` if "
            "`amount > self.balance`, else `self.balance = self.balance - "
            "amount`.\n\n"
            "See the Study Reference presentation, Topic 6, for the theory."
        ),
        "stub": '''\
class BankAccount:
    def __init__(self, owner: str, balance: float = 0):
        raise NotImplementedError

    @staticmethod
    def is_valid_amount(amount) -> bool:
        """True if amount is an int/float and >= 0."""
        raise NotImplementedError

    @property
    def balance(self) -> float:
        """Return self._balance."""
        raise NotImplementedError

    @balance.setter
    def balance(self, value) -> None:
        """Validate with is_valid_amount, then set self._balance."""
        raise NotImplementedError

    def deposit(self, amount) -> None:
        """self.balance += amount, through the property."""
        raise NotImplementedError

    def withdraw(self, amount) -> None:
        """Raise ValueError if amount > self.balance, else self.balance -= amount."""
        raise NotImplementedError
''',
        "reference": '''\
class BankAccount:
    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        self.balance = balance

    @staticmethod
    def is_valid_amount(amount) -> bool:
        return isinstance(amount, (int, float)) and not isinstance(amount, bool) and amount >= 0

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, value) -> None:
        if not self.is_valid_amount(value):
            raise ValueError(f"invalid balance: {value!r}")
        self._balance = value

    def deposit(self, amount) -> None:
        self.balance = self.balance + amount

    def withdraw(self, amount) -> None:
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance = self.balance - amount
''',
        "test": '''\
import pytest
from exercises.stage06.exercise01.solution import BankAccount


def test_initial_balance():
    acct = BankAccount("Ada", 100)
    assert acct.balance == 100


def test_deposit():
    acct = BankAccount("Ada", 100)
    acct.deposit(50)
    assert acct.balance == 150


def test_withdraw():
    acct = BankAccount("Ada", 100)
    acct.withdraw(30)
    assert acct.balance == 70


def test_withdraw_insufficient_funds_raises():
    acct = BankAccount("Ada", 100)
    with pytest.raises(ValueError):
        acct.withdraw(200)


def test_negative_balance_raises():
    with pytest.raises(ValueError):
        BankAccount("Ada", -5)


def test_is_valid_amount():
    assert BankAccount.is_valid_amount(10) is True
    assert BankAccount.is_valid_amount(-1) is False
    assert BankAccount.is_valid_amount("10") is False
''',
    },
    {
        "name": "exercise02",
        "title": "Employee Registry",
        "summary": "class vs instance attributes, @classmethod x2, cls x2, @staticmethod",
        "readme": (
            "Implement `Employee`:\n\n"
            "- `company_name = \"Acme Corp\"` and `employee_count = 0` -- "
            "**class** attributes, declared directly in the class body (already "
            "in the stub). Every instance shares the *same* `company_name` "
            "unless overridden on that instance.\n"
            "- `__init__(self, name: str, salary: float)` -- set the "
            "**instance** attributes `self.name` and `self.salary`, then "
            "increment the shared class attribute via `Employee.employee_count "
            "+= 1` (not `self.employee_count`, which would create a new "
            "*instance* attribute shadowing the class one instead of "
            "incrementing the shared counter).\n"
            "- `get_employee_count(cls) -> int` (`@classmethod`) -- return "
            "`cls.employee_count`.\n"
            "- `hire_intern(cls, name: str) -> \"Employee\"` (`@classmethod`) -- "
            "return `cls(name, salary=0)`. This is the classic \"alternate "
            "constructor\" use of `@classmethod`: it receives the class "
            "itself (`cls`) rather than an instance (`self`), so it can build "
            "and return a new instance.\n"
            "- `is_valid_salary(salary) -> bool` (`@staticmethod`) -- `True` "
            "if `salary >= 0`.\n\n"
            "See the Study Reference presentation, Topic 6, for the theory."
        ),
        "stub": '''\
class Employee:
    company_name = "Acme Corp"
    employee_count = 0

    def __init__(self, name: str, salary: float):
        raise NotImplementedError

    @classmethod
    def get_employee_count(cls) -> int:
        """cls.employee_count."""
        raise NotImplementedError

    @classmethod
    def hire_intern(cls, name: str) -> "Employee":
        """cls(name, salary=0) -- an alternate constructor."""
        raise NotImplementedError

    @staticmethod
    def is_valid_salary(salary) -> bool:
        """salary >= 0."""
        raise NotImplementedError
''',
        "reference": '''\
class Employee:
    company_name = "Acme Corp"
    employee_count = 0

    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    @classmethod
    def get_employee_count(cls) -> int:
        return cls.employee_count

    @classmethod
    def hire_intern(cls, name: str) -> "Employee":
        return cls(name, salary=0)

    @staticmethod
    def is_valid_salary(salary) -> bool:
        return salary >= 0
''',
        "test": '''\
from exercises.stage06.exercise02.solution import Employee


def test_instance_attributes_are_per_employee():
    a = Employee("Ada", 90000)
    b = Employee("Grace", 95000)
    assert a.name == "Ada"
    assert b.name == "Grace"
    assert a.salary != b.salary


def test_class_attribute_shared_across_instances():
    a = Employee("Ada", 90000)
    b = Employee("Grace", 95000)
    assert a.company_name == "Acme Corp"
    assert b.company_name == "Acme Corp"
    assert a.company_name is b.company_name


def test_employee_count_increments():
    before = Employee.get_employee_count()
    Employee("New Hire", 50000)
    after = Employee.get_employee_count()
    assert after == before + 1


def test_hire_intern_alternate_constructor():
    intern = Employee.hire_intern("Intern Ivy")
    assert intern.name == "Intern Ivy"
    assert intern.salary == 0
    assert isinstance(intern, Employee)


def test_is_valid_salary():
    assert Employee.is_valid_salary(50000) is True
    assert Employee.is_valid_salary(-1) is False
''',
    },
    {
        "name": "exercise03",
        "title": "Rectangle Properties",
        "summary": "@property x3, @x.setter x2 more",
        "readme": (
            "Implement `Rectangle`:\n\n"
            "- `__init__(self, width: float, height: float)` -- set both "
            "*through the properties* below (`self.width = width`, "
            "`self.height = height`), so construction validates them the "
            "same way a later assignment would.\n"
            "- `width` / `height` (`@property` + `@width.setter` / "
            "`@height.setter`) -- getters return `self._width`/`self._height`; "
            "setters `raise ValueError` for any value `<= 0`, else store it.\n"
            "- `area` (`@property`, read-only, no setter) -- `self.width * "
            "self.height`.\n"
            "- `perimeter` (`@property`, read-only) -- "
            "`2 * (self.width + self.height)`.\n"
            "- `is_square` (`@property`, read-only) -- `self.width == "
            "self.height`.\n\n"
            "`area`/`perimeter`/`is_square` are *computed* properties -- there's "
            "nothing to set, they're derived fresh from `width`/`height` on "
            "every access, which is exactly why they're read-only (no setter "
            "defined at all).\n\n"
            "See the Study Reference presentation, Topic 6, for the theory."
        ),
        "stub": '''\
class Rectangle:
    def __init__(self, width: float, height: float):
        raise NotImplementedError

    @property
    def width(self) -> float:
        raise NotImplementedError

    @width.setter
    def width(self, value) -> None:
        """Raise ValueError if value <= 0, else store it."""
        raise NotImplementedError

    @property
    def height(self) -> float:
        raise NotImplementedError

    @height.setter
    def height(self, value) -> None:
        """Raise ValueError if value <= 0, else store it."""
        raise NotImplementedError

    @property
    def area(self) -> float:
        """width * height (read-only, no setter)."""
        raise NotImplementedError

    @property
    def perimeter(self) -> float:
        """2 * (width + height) (read-only)."""
        raise NotImplementedError

    @property
    def is_square(self) -> bool:
        """width == height (read-only)."""
        raise NotImplementedError
''',
        "reference": '''\
class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value) -> None:
        if value <= 0:
            raise ValueError("width must be positive")
        self._width = value

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value) -> None:
        if value <= 0:
            raise ValueError("height must be positive")
        self._height = value

    @property
    def area(self) -> float:
        return self.width * self.height

    @property
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    @property
    def is_square(self) -> bool:
        return self.width == self.height
''',
        "test": '''\
import pytest
from exercises.stage06.exercise03.solution import Rectangle


def test_area():
    assert Rectangle(4, 5).area == 20


def test_perimeter():
    assert Rectangle(4, 5).perimeter == 18


def test_is_square():
    assert Rectangle(4, 4).is_square is True
    assert Rectangle(4, 5).is_square is False


def test_width_setter_validates():
    rect = Rectangle(4, 5)
    with pytest.raises(ValueError):
        rect.width = -1


def test_height_setter_validates():
    with pytest.raises(ValueError):
        Rectangle(4, -5)


def test_changing_width_updates_area():
    rect = Rectangle(4, 5)
    rect.width = 10
    assert rect.area == 50
''',
    },
    {
        "name": "exercise04",
        "title": "Slots and Memory",
        "summary": "__slots__ x3",
        "readme": (
            "Implement three classes using `__slots__` instead of the default "
            "per-instance `__dict__`:\n\n"
            "- `PointSlots` -- `__slots__ = (\"x\", \"y\")`; `__init__(self, x, "
            "y)` sets both.\n"
            "- `Vector3DSlots` -- `__slots__ = (\"x\", \"y\", \"z\")`; "
            "`__init__(self, x, y, z)` sets all three; `magnitude(self) -> "
            "float` returns `(x**2 + y**2 + z**2) ** 0.5`.\n"
            "- `TemperatureSlots` -- `__slots__ = (\"celsius\",)`; "
            "`__init__(self, celsius)` sets it; `fahrenheit(self) -> float` "
            "returns `self.celsius * 9 / 5 + 32`.\n\n"
            "`__slots__` tells Python to skip creating a per-instance "
            "`__dict__` and allocate fixed storage for only the named "
            "attributes instead -- less memory per instance, and it also "
            "means trying to set *any other* attribute raises `AttributeError` "
            "(the tests check both effects).\n\n"
            "See the Study Reference presentation, Topic 6, for the theory."
        ),
        "stub": '''\
class PointSlots:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        raise NotImplementedError


class Vector3DSlots:
    __slots__ = ("x", "y", "z")

    def __init__(self, x, y, z):
        raise NotImplementedError

    def magnitude(self) -> float:
        """(x**2 + y**2 + z**2) ** 0.5."""
        raise NotImplementedError


class TemperatureSlots:
    __slots__ = ("celsius",)

    def __init__(self, celsius):
        raise NotImplementedError

    def fahrenheit(self) -> float:
        """celsius * 9 / 5 + 32."""
        raise NotImplementedError
''',
        "reference": '''\
class PointSlots:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Vector3DSlots:
    __slots__ = ("x", "y", "z")

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def magnitude(self) -> float:
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5


class TemperatureSlots:
    __slots__ = ("celsius",)

    def __init__(self, celsius):
        self.celsius = celsius

    def fahrenheit(self) -> float:
        return self.celsius * 9 / 5 + 32
''',
        "test": '''\
import pytest
from exercises.stage06.exercise04.solution import PointSlots, Vector3DSlots, TemperatureSlots


def test_point_slots_basic():
    p = PointSlots(1, 2)
    assert (p.x, p.y) == (1, 2)


def test_point_slots_has_no_dict():
    p = PointSlots(1, 2)
    assert not hasattr(p, "__dict__")


def test_point_slots_rejects_new_attribute():
    p = PointSlots(1, 2)
    with pytest.raises(AttributeError):
        p.z = 3


def test_vector3d_slots_magnitude():
    v = Vector3DSlots(2, 3, 6)
    assert v.magnitude() == 7.0


def test_temperature_slots_fahrenheit():
    t = TemperatureSlots(0)
    assert t.fahrenheit() == 32.0
''',
    },
    {
        "name": "exercise05",
        "title": "Descriptors Preview",
        "summary": "__get__/__set__ x2, descriptors concept",
        "readme": (
            "`@property` is itself built on a lower-level mechanism called "
            "the **descriptor protocol**: any object with `__get__`/`__set__` "
            "methods, assigned as a *class* attribute, controls what happens "
            "when you read/write that attribute on an instance. Implement two "
            "reusable descriptors:\n\n"
            "- `PositiveNumber` -- `__set_name__(self, owner, name)` stores "
            "`self._name = \"_\" + name` (called automatically by Python when "
            "the descriptor is assigned in a class body, telling it what "
            "attribute name it was bound to); `__get__(self, obj, objtype=None)` "
            "returns `getattr(obj, self._name)`; `__set__(self, obj, value)` "
            "raises `ValueError` if `value < 0`, else `setattr(obj, self._name, "
            "value)`.\n"
            "- `Typed` -- same shape, but `__init__(self, expected_type)` "
            "stores the type to enforce, and `__set__` raises `TypeError` "
            "(not `ValueError`) if `not isinstance(value, self.expected_type)`.\n\n"
            "Then use them: `Product` has `price = PositiveNumber()` as a "
            "class attribute, plus `__init__(self, name, price)` that sets "
            "`self.name = name` and `self.price = price` (going through the "
            "descriptor). `Person` has `name = Typed(str)` and `age = "
            "Typed(int)`, plus a matching `__init__`.\n\n"
            "See the Study Reference presentation, Topic 6, for the theory."
        ),
        "stub": '''\
class PositiveNumber:
    def __set_name__(self, owner, name):
        self._name = "_" + name

    def __get__(self, obj, objtype=None):
        raise NotImplementedError

    def __set__(self, obj, value):
        """Raise ValueError if value < 0, else store it."""
        raise NotImplementedError


class Typed:
    def __init__(self, expected_type):
        self.expected_type = expected_type

    def __set_name__(self, owner, name):
        self._name = "_" + name

    def __get__(self, obj, objtype=None):
        raise NotImplementedError

    def __set__(self, obj, value):
        """Raise TypeError if value isn't an instance of self.expected_type, else store it."""
        raise NotImplementedError


class Product:
    price = PositiveNumber()

    def __init__(self, name, price):
        raise NotImplementedError


class Person:
    name = Typed(str)
    age = Typed(int)

    def __init__(self, name, age):
        raise NotImplementedError
''',
        "reference": '''\
class PositiveNumber:
    def __set_name__(self, owner, name):
        self._name = "_" + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self._name)

    def __set__(self, obj, value):
        if value < 0:
            raise ValueError(f"{self._name[1:]} must be >= 0")
        setattr(obj, self._name, value)


class Typed:
    def __init__(self, expected_type):
        self.expected_type = expected_type

    def __set_name__(self, owner, name):
        self._name = "_" + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self._name)

    def __set__(self, obj, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"{self._name[1:]} must be a {self.expected_type.__name__}")
        setattr(obj, self._name, value)


class Product:
    price = PositiveNumber()

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Person:
    name = Typed(str)
    age = Typed(int)

    def __init__(self, name, age):
        self.name = name
        self.age = age
''',
        "test": '''\
import pytest
from exercises.stage06.exercise05.solution import Product, Person


def test_positive_number_descriptor_get_set():
    p = Product("Widget", 9.99)
    assert p.price == 9.99
    p.price = 19.99
    assert p.price == 19.99


def test_positive_number_descriptor_rejects_negative():
    p = Product("Widget", 9.99)
    with pytest.raises(ValueError):
        p.price = -1


def test_positive_number_descriptor_rejects_at_construction():
    with pytest.raises(ValueError):
        Product("Widget", -5)


def test_typed_descriptor_get_set():
    person = Person("Ada", 30)
    assert person.name == "Ada"
    assert person.age == 30


def test_typed_descriptor_rejects_wrong_type():
    person = Person("Ada", 30)
    with pytest.raises(TypeError):
        person.age = "thirty"


def test_typed_descriptor_rejects_at_construction():
    with pytest.raises(TypeError):
        Person("Ada", "thirty")
''',
    },
]
