"""
Stage 6 -- OOP I.

Rolled onto the tier-named exercise convention: a minimum of two exercises
per Basic/Mid/Advanced tier. Every exercise here is naturally class-based --
Stage 6's whole subject is writing classes, so that's exactly the point,
not something to avoid.

Coverage plan (every item below is exercised by the trainee's own code,
generally 2+ times across these 6 exercises):

  Basic:    class, self, __init__, @property, @x.setter, @staticmethod,
            @classmethod, cls, encapsulation, instance vs class attributes
  Mid:      __slots__ memory savings
  Advanced: __get__/__set__ (descriptor preview), descriptors concept
"""

STAGE = "stage06"
TOPIC = "OOP I"
OVERVIEW = (
    "Six exercises, two per tier: validated properties and classmethod "
    "alternate constructors in Basic, __slots__ across four small classes "
    "in Mid, and a hand-rolled descriptor (what @property is built on) "
    "in Advanced."
)

EXERCISES = [
    {
        "name": "tier1_basic01",
        "title": "Bank Account",
        "summary": "class, self, __init__, @property, @x.setter, @staticmethod, encapsulation",
        "readme": (
            "Implement `BankAccount`:\n\n"
            "- `__init__(self, owner: str, balance: float = 0)` -- store "
            "`self.owner = owner` and set the *property* `self.balance = "
            "balance` (going through the setter below, so an invalid "
            "starting balance is rejected the same way a later deposit "
            "would be).\n"
            "- `is_valid_amount(amount) -> bool` (`@staticmethod`) -- "
            "`True` if `amount` is an `int`/`float` (and not a `bool`) and "
            "`amount >= 0`. It's a `@staticmethod` because it doesn't need "
            "`self` at all -- it's just a validation helper that happens "
            "to live on the class.\n"
            "- `balance` (`@property`) -- getter returns `self._balance` "
            "(the real, \"private-by-convention\" storage -- this is what "
            "**encapsulation** means here: callers use `.balance`, never "
            "`._balance` directly).\n"
            "- `balance` setter (`@balance.setter`) -- `raise ValueError` "
            "if `not self.is_valid_amount(value)`, else set "
            "`self._balance = value`.\n"
            "- `deposit(self, amount) -> None` -- `self.balance = "
            "self.balance + amount` (going through the property, so the "
            "setter's validation applies).\n"
            "- `withdraw(self, amount) -> None` -- `raise ValueError` if "
            "`amount > self.balance`, else `self.balance = self.balance - "
            "amount`.\n\n"
            "See the Study Reference presentation, Topic 6 (Basic tier), "
            "for the theory."
        ),
        "stub": '''\
class BankAccount:
    def __init__(self, owner: str, balance: float = 0):
        raise NotImplementedError

    @staticmethod
    def is_valid_amount(amount) -> bool:
        """True if amount is an int/float (not bool) and >= 0."""
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
from exercises.stage06.tier1_basic01.solution import BankAccount


def test_initial_balance_goes_through_the_setter():
    """__init__ must assign self.balance (the property), not self._balance directly."""
    acct = BankAccount("Ada", 100)
    assert acct.balance == 100


def test_deposit():
    """deposit() adds to balance through the property setter."""
    acct = BankAccount("Ada", 100)
    acct.deposit(50)
    assert acct.balance == 150


def test_withdraw():
    """withdraw() subtracts from balance through the property setter."""
    acct = BankAccount("Ada", 100)
    acct.withdraw(30)
    assert acct.balance == 70


def test_withdraw_insufficient_funds_raises():
    """withdraw() must raise ValueError if amount exceeds the current balance."""
    acct = BankAccount("Ada", 100)
    with pytest.raises(ValueError):
        acct.withdraw(200)


def test_negative_balance_raises_at_construction():
    """__init__ must route through the balance setter, so a negative starting balance raises ValueError too."""
    with pytest.raises(ValueError):
        BankAccount("Ada", -5)


def test_is_valid_amount_is_a_staticmethod():
    """is_valid_amount is callable on the class itself (no instance) and rejects non-numeric/negative values."""
    assert BankAccount.is_valid_amount(10) is True
    assert BankAccount.is_valid_amount(-1) is False
    assert BankAccount.is_valid_amount("10") is False
''',
    },
    {
        "name": "tier1_basic02",
        "title": "Employee Registry",
        "summary": "instance vs class attributes, @classmethod, cls, @staticmethod, @property (read-only)",
        "readme": (
            "Implement `Employee`:\n\n"
            "- `company_name = \"Acme Corp\"` and `employee_count = 0` -- "
            "**class** attributes, declared directly in the class body "
            "(already in the stub). Every instance shares the *same* "
            "`company_name` unless overridden on that instance.\n"
            "- `__init__(self, name: str, salary: float)` -- set the "
            "**instance** attributes `self.name` and `self.salary`, then "
            "increment the shared class attribute via `Employee."
            "employee_count += 1` (not `self.employee_count`, which would "
            "create a new *instance* attribute shadowing the class one "
            "instead of incrementing the shared counter).\n"
            "- `annual_bonus` (`@property`, read-only, no setter) -- "
            "`round(self.salary * 0.1, 2)`. A *computed* property: there's "
            "nothing to set, it's derived fresh from `salary` on every "
            "access, which is exactly why it's read-only.\n"
            "- `get_employee_count(cls) -> int` (`@classmethod`) -- return "
            "`cls.employee_count`.\n"
            "- `hire_intern(cls, name: str) -> \"Employee\"` (`@classmethod`) "
            "-- return `cls(name, salary=0)`. This is the classic "
            "\"alternate constructor\" use of `@classmethod`: it receives "
            "the class itself (`cls`) rather than an instance (`self`), "
            "so it can build and return a new instance.\n"
            "- `is_valid_salary(salary) -> bool` (`@staticmethod`) -- "
            "`True` if `salary >= 0`.\n\n"
            "See the Study Reference presentation, Topic 6 (Basic tier), "
            "for the theory."
        ),
        "stub": '''\
class Employee:
    company_name = "Acme Corp"
    employee_count = 0

    def __init__(self, name: str, salary: float):
        raise NotImplementedError

    @property
    def annual_bonus(self) -> float:
        """round(self.salary * 0.1, 2) -- a computed, read-only property."""
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

    @property
    def annual_bonus(self) -> float:
        return round(self.salary * 0.1, 2)

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
from exercises.stage06.tier1_basic02.solution import Employee


def test_instance_attributes_are_per_employee():
    """name/salary are instance attributes -- distinct per Employee."""
    a = Employee("Ada", 90000)
    b = Employee("Grace", 95000)
    assert a.name == "Ada"
    assert b.name == "Grace"
    assert a.salary != b.salary


def test_class_attribute_shared_across_instances():
    """company_name is a class attribute -- the same object for every instance."""
    a = Employee("Ada", 90000)
    b = Employee("Grace", 95000)
    assert a.company_name == "Acme Corp"
    assert b.company_name == "Acme Corp"
    assert a.company_name is b.company_name


def test_employee_count_increments_via_class_not_instance():
    """__init__ must increment Employee.employee_count (the shared class attribute), not create a shadowing instance attribute."""
    before = Employee.get_employee_count()
    Employee("New Hire", 50000)
    after = Employee.get_employee_count()
    assert after == before + 1


def test_annual_bonus_is_computed_from_salary():
    """annual_bonus == round(salary * 0.1, 2), recomputed fresh on every access."""
    e = Employee("Ada", 90000)
    assert e.annual_bonus == 9000.0
    e.salary = 100000
    assert e.annual_bonus == 10000.0


def test_hire_intern_alternate_constructor():
    """hire_intern is a @classmethod that builds and returns a new instance via cls(...)."""
    intern = Employee.hire_intern("Intern Ivy")
    assert intern.name == "Intern Ivy"
    assert intern.salary == 0
    assert isinstance(intern, Employee)


def test_is_valid_salary_is_a_staticmethod():
    """is_valid_salary is callable on the class itself."""
    assert Employee.is_valid_salary(50000) is True
    assert Employee.is_valid_salary(-1) is False
''',
    },
    {
        "name": "tier2_mid01",
        "title": "Slotted Geometry",
        "summary": "__slots__",
        "readme": (
            "Implement two classes using `__slots__` instead of the "
            "default per-instance `__dict__`:\n\n"
            "- `PointSlots` -- `__slots__ = (\"x\", \"y\")`; "
            "`__init__(self, x, y)` sets both.\n"
            "- `Vector3DSlots` -- `__slots__ = (\"x\", \"y\", \"z\")`; "
            "`__init__(self, x, y, z)` sets all three; "
            "`magnitude(self) -> float` returns "
            "`(x**2 + y**2 + z**2) ** 0.5`.\n\n"
            "`__slots__` tells Python to skip creating a per-instance "
            "`__dict__` and allocate fixed storage for only the named "
            "attributes instead -- less memory per instance, and it also "
            "means trying to set *any other* attribute raises "
            "`AttributeError` (the tests check both effects).\n\n"
            "See the Study Reference presentation, Topic 6 (Mid tier), "
            "for the theory."
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
''',
        "test": '''\
import pytest
from exercises.stage06.tier2_mid01.solution import PointSlots, Vector3DSlots


def test_point_slots_basic():
    """__init__ sets x/y via __slots__-declared attributes."""
    p = PointSlots(1, 2)
    assert (p.x, p.y) == (1, 2)


def test_point_slots_has_no_dict():
    """__slots__ replaces the per-instance __dict__ entirely."""
    p = PointSlots(1, 2)
    assert not hasattr(p, "__dict__")


def test_point_slots_rejects_new_attribute():
    """Setting an attribute not named in __slots__ must raise AttributeError."""
    p = PointSlots(1, 2)
    with pytest.raises(AttributeError):
        p.z = 3


def test_vector3d_slots_magnitude():
    """magnitude() == (x**2 + y**2 + z**2) ** 0.5."""
    v = Vector3DSlots(2, 3, 6)
    assert v.magnitude() == 7.0
''',
    },
    {
        "name": "tier2_mid02",
        "title": "Slotted Records",
        "summary": "__slots__ (two more classes)",
        "readme": (
            "Implement two more `__slots__`-based classes:\n\n"
            "- `TemperatureSlots` -- `__slots__ = (\"celsius\",)`; "
            "`__init__(self, celsius)` sets it; `fahrenheit(self) -> float` "
            "returns `self.celsius * 9 / 5 + 32`.\n"
            "- `InventoryItemSlots` -- `__slots__ = (\"name\", \"price\", "
            "\"quantity\")`; `__init__(self, name, price, quantity)` sets "
            "all three; `total_value(self) -> float` returns "
            "`round(self.price * self.quantity, 2)`.\n\n"
            "Same mechanism as the previous exercise, on two different "
            "record shapes: `__slots__` allocates fixed storage for "
            "exactly the named attributes, so both classes skip the "
            "per-instance `__dict__` and reject any attribute not listed.\n\n"
            "See the Study Reference presentation, Topic 6 (Mid tier), "
            "for the theory."
        ),
        "stub": '''\
class TemperatureSlots:
    __slots__ = ("celsius",)

    def __init__(self, celsius):
        raise NotImplementedError

    def fahrenheit(self) -> float:
        """celsius * 9 / 5 + 32."""
        raise NotImplementedError


class InventoryItemSlots:
    __slots__ = ("name", "price", "quantity")

    def __init__(self, name, price, quantity):
        raise NotImplementedError

    def total_value(self) -> float:
        """round(price * quantity, 2)."""
        raise NotImplementedError
''',
        "reference": '''\
class TemperatureSlots:
    __slots__ = ("celsius",)

    def __init__(self, celsius):
        self.celsius = celsius

    def fahrenheit(self) -> float:
        return self.celsius * 9 / 5 + 32


class InventoryItemSlots:
    __slots__ = ("name", "price", "quantity")

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self) -> float:
        return round(self.price * self.quantity, 2)
''',
        "test": '''\
import pytest
from exercises.stage06.tier2_mid02.solution import TemperatureSlots, InventoryItemSlots


def test_temperature_slots_fahrenheit():
    """fahrenheit() == celsius * 9 / 5 + 32."""
    t = TemperatureSlots(0)
    assert t.fahrenheit() == 32.0


def test_inventory_item_slots_total_value():
    """total_value() == round(price * quantity, 2)."""
    item = InventoryItemSlots("Widget", 2.5, 4)
    assert item.total_value() == 10.0


def test_inventory_item_slots_rejects_new_attribute():
    """Setting an attribute not named in __slots__ must raise AttributeError."""
    item = InventoryItemSlots("Widget", 2.5, 4)
    with pytest.raises(AttributeError):
        item.discount = 0.1
''',
    },
    {
        "name": "tier3_advanced01",
        "title": "Descriptors Preview: PositiveNumber",
        "summary": "__get__/__set__, descriptors",
        "readme": (
            "`@property` is itself built on a lower-level mechanism called "
            "the **descriptor protocol**: any object with `__get__`/"
            "`__set__` methods, assigned as a *class* attribute, controls "
            "what happens when you read/write that attribute on an "
            "instance. Implement a reusable descriptor:\n\n"
            "- `PositiveNumber` -- `__set_name__(self, owner, name)` "
            "stores `self._name = \"_\" + name` (already given -- called "
            "automatically by Python when the descriptor is assigned in a "
            "class body, telling it what attribute name it was bound to); "
            "`__get__(self, obj, objtype=None)` returns "
            "`getattr(obj, self._name)`; `__set__(self, obj, value)` "
            "raises `ValueError` if `value < 0`, else `setattr(obj, "
            "self._name, value)`.\n\n"
            "Then use it: `Product` has `price = PositiveNumber()` as a "
            "class attribute, plus `__init__(self, name, price)` that sets "
            "`self.name = name` and `self.price = price` (going through "
            "the descriptor, exactly like a `@property` setter would).\n\n"
            "See the Study Reference presentation, Topic 6 (Advanced "
            "tier), for the theory."
        ),
        "stub": '''\
class PositiveNumber:
    def __set_name__(self, owner, name):
        self._name = "_" + name

    def __get__(self, obj, objtype=None):
        """getattr(obj, self._name)."""
        raise NotImplementedError

    def __set__(self, obj, value):
        """Raise ValueError if value < 0, else setattr(obj, self._name, value)."""
        raise NotImplementedError


class Product:
    price = PositiveNumber()

    def __init__(self, name, price):
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


class Product:
    price = PositiveNumber()

    def __init__(self, name, price):
        self.name = name
        self.price = price
''',
        "test": '''\
import pytest
from exercises.stage06.tier3_advanced01.solution import Product


def test_positive_number_descriptor_get_set():
    """price reads/writes through PositiveNumber's __get__/__set__, just like a @property would."""
    p = Product("Widget", 9.99)
    assert p.price == 9.99
    p.price = 19.99
    assert p.price == 19.99


def test_positive_number_descriptor_rejects_negative():
    """__set__ must raise ValueError for a negative value."""
    p = Product("Widget", 9.99)
    with pytest.raises(ValueError):
        p.price = -1


def test_positive_number_descriptor_rejects_at_construction():
    """__init__ assigns self.price through the descriptor, so construction validates too."""
    with pytest.raises(ValueError):
        Product("Widget", -5)
''',
    },
    {
        "name": "tier3_advanced02",
        "title": "Descriptors Preview: Typed",
        "summary": "__get__/__set__, descriptors (type-checking variant)",
        "readme": (
            "A second reusable descriptor, this time enforcing a **type** "
            "instead of a numeric range:\n\n"
            "- `Typed` -- same shape as the previous exercise's "
            "`PositiveNumber`, but `__init__(self, expected_type)` stores "
            "the type to enforce, `__set_name__`/`__get__` work the same "
            "way, and `__set__` raises `TypeError` (not `ValueError`) if "
            "`not isinstance(value, self.expected_type)`, else "
            "`setattr(obj, self._name, value)`.\n\n"
            "Then use it: `Person` has `name = Typed(str)` and `age = "
            "Typed(int)` as class attributes, plus `__init__(self, name, "
            "age)` that sets both (going through the descriptors). The "
            "same descriptor **class** (`Typed`) is reused twice on "
            "`Person`, each time configured with a different "
            "`expected_type` -- that's the point of writing it as a "
            "reusable, general-purpose descriptor rather than one-off "
            "validation code per attribute.\n\n"
            "See the Study Reference presentation, Topic 6 (Advanced "
            "tier), for the theory."
        ),
        "stub": '''\
class Typed:
    def __init__(self, expected_type):
        self.expected_type = expected_type

    def __set_name__(self, owner, name):
        self._name = "_" + name

    def __get__(self, obj, objtype=None):
        """getattr(obj, self._name)."""
        raise NotImplementedError

    def __set__(self, obj, value):
        """Raise TypeError if value isn't an instance of self.expected_type, else store it."""
        raise NotImplementedError


class Person:
    name = Typed(str)
    age = Typed(int)

    def __init__(self, name, age):
        raise NotImplementedError
''',
        "reference": '''\
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


class Person:
    name = Typed(str)
    age = Typed(int)

    def __init__(self, name, age):
        self.name = name
        self.age = age
''',
        "test": '''\
import pytest
from exercises.stage06.tier3_advanced02.solution import Person


def test_typed_descriptor_get_set():
    """name/age read/write through Typed's __get__/__set__."""
    person = Person("Ada", 30)
    assert person.name == "Ada"
    assert person.age == 30


def test_typed_descriptor_rejects_wrong_type():
    """__set__ must raise TypeError when the value doesn't match expected_type."""
    person = Person("Ada", 30)
    with pytest.raises(TypeError):
        person.age = "thirty"


def test_typed_descriptor_rejects_at_construction():
    """__init__ assigns through the descriptors, so construction validates types too."""
    with pytest.raises(TypeError):
        Person("Ada", "thirty")


def test_same_descriptor_class_reused_with_different_expected_types():
    """Typed is reused for both name (str) and age (int) -- each enforcing its own configured type independently."""
    person = Person("Ada", 30)
    with pytest.raises(TypeError):
        person.name = 123
    person.age = 31
    assert person.age == 31
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
            "Given, don't modify -- two pairs of classes, each pair "
            "*supposed* to behave the same way; at least one class in "
            "each pair has a bug. Your job is to catch it by testing, not "
            "to fix it:\n\n"
            "```python\n"
            "class Temperature:\n"
            "    def __init__(self, celsius):\n"
            "        self.celsius = celsius\n\n"
            "    @property\n"
            "    def fahrenheit(self):\n"
            "        return self.celsius * 9 / 5 + 32\n\n"
            "class TemperatureBuggy:\n"
            "    def __init__(self, celsius):\n"
            "        self.celsius = celsius\n\n"
            "    @property\n"
            "    def fahrenheit(self):\n"
            "        return self.celsius * 9 / 5\n\n"
            "class Counter:\n"
            "    def __init__(self, start=0):\n"
            "        self.value = start\n\n"
            "    @classmethod\n"
            "    def from_string(cls, text):\n"
            "        return cls(int(text))\n\n"
            "class CounterBuggy:\n"
            "    def __init__(self, start=0):\n"
            "        self.value = start\n\n"
            "    @classmethod\n"
            "    def from_string(cls, text):\n"
            "        return cls(text)\n"
            "```\n\n"
            "The spec each pair is supposed to meet:\n\n"
            "- **fahrenheit** should equal `celsius * 9 / 5 + 32`.\n"
            "- **from_string** should build an instance whose `.value` is "
            "the **integer** the string represents, not the string "
            "itself.\n\n"
            "Implement:\n\n"
            "- `check(description: str, condition: bool) -> bool` -- "
            "append `(description, condition)` to the given `_check_log` "
            "list, then return `condition`. Unlike `assert`, this must "
            "**never raise** -- a failed check should become a recorded "
            "`False` in the log, not a crash that stops every check after "
            "it from running.\n"
            "- `run_all_checks() -> dict` -- call `check()` **exactly "
            "four times**:\n"
            "  - `Temperature(100).fahrenheit` and "
            "`TemperatureBuggy(100).fahrenheit`, each compared against "
            "the spec-computed expected value, `212.0`.\n"
            "  - `Counter.from_string(\"5\").value` and "
            "`CounterBuggy.from_string(\"5\").value`, each compared "
            "against the spec-computed expected value, `5` (the `int`, "
            "not the string `\"5\"`).\n\n"
            "  Then return `{\"total\": ..., \"passed\": ..., \"failed\": "
            "...}` built from `_check_log`.\n\n"
            "See the Study Reference presentation, Topic 6, for the theory."
        ),
        "stub": '''\
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32


class TemperatureBuggy:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5


class Counter:
    def __init__(self, start=0):
        self.value = start

    @classmethod
    def from_string(cls, text):
        return cls(int(text))


class CounterBuggy:
    def __init__(self, start=0):
        self.value = start

    @classmethod
    def from_string(cls, text):
        return cls(text)


_check_log = []


def check(description: str, condition: bool) -> bool:
    """Append (description, condition) to _check_log; return condition. Must NEVER raise."""
    raise NotImplementedError


def run_all_checks() -> dict:
    """Call check() exactly 4 times (see README.md), then return {"total": ..., "passed": ..., "failed": [...]}."""
    raise NotImplementedError
''',
        "reference": '''\
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32


class TemperatureBuggy:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5


class Counter:
    def __init__(self, start=0):
        self.value = start

    @classmethod
    def from_string(cls, text):
        return cls(int(text))


class CounterBuggy:
    def __init__(self, start=0):
        self.value = start

    @classmethod
    def from_string(cls, text):
        return cls(text)


_check_log = []


def check(description: str, condition: bool) -> bool:
    _check_log.append((description, condition))
    return condition


def run_all_checks() -> dict:
    _check_log.clear()

    check("Temperature(100).fahrenheit == 212.0", Temperature(100).fahrenheit == 212.0)
    check("TemperatureBuggy(100).fahrenheit == 212.0", TemperatureBuggy(100).fahrenheit == 212.0)

    check("Counter.from_string('5').value == 5", Counter.from_string("5").value == 5)
    check("CounterBuggy.from_string('5').value == 5", CounterBuggy.from_string("5").value == 5)

    total = len(_check_log)
    passed = sum(1 for _, ok in _check_log if ok)
    failed = [desc for desc, ok in _check_log if not ok]
    return {"total": total, "passed": passed, "failed": failed}
''',
        "test": '''\
from exercises.stage06.tier4_testing.solution import check, run_all_checks, _check_log


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
    """run_all_checks must call check() exactly once per class named in README.md -- four total."""
    summary = run_all_checks()
    assert summary["total"] == 4


def test_run_all_checks_catches_both_bugs():
    """Checked against the shared spec-derived value, Temperature/Counter pass and the _buggy versions fail."""
    summary = run_all_checks()
    assert summary["passed"] == 2
    assert len(summary["failed"]) == 2
''',
    },
]
