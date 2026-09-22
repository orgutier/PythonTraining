"""
Stage 8 -- The Python Data Model.

Coverage plan (each dunder exercised by the trainee's own code >=3 times):
  dunders:  __repr__, __str__, __eq__, __add__, __len__, __getitem__,
            __iter__, __contains__, __call__, __bool__, __enter__,
            __exit__, __hash__, __radd__
  concepts: operator overloading, protocols vs explicit inheritance
"""

STAGE = "stage08"
TOPIC = "The Python Data Model"
OVERVIEW = (
    "Seven exercises, each built around one or more small classes, cover "
    "every dunder method from Topic 8 at least three times -- from the "
    "everyday (__repr__/__eq__) to the ones most trainees never write by "
    "hand until now (__radd__, the __enter__/__exit__ protocol)."
)

EXERCISES = [
    {
        "name": "exercise01",
        "title": "Vector: The Flagship Dunder Class",
        "summary": "__repr__, __str__, __eq__, __add__, __radd__, __hash__, __bool__, __getitem__",
        "readme": (
            "Implement `Vector`, a 2D vector with eight dunder methods:\n\n"
            "- `__init__(self, x, y)` -- store both.\n"
            "- `__repr__(self) -> str` -- `f\"Vector({self.x}, {self.y})\"` "
            "(unambiguous, developer-facing -- what you'd see in a debugger).\n"
            "- `__str__(self) -> str` -- `f\"({self.x}, {self.y})\"` "
            "(friendlier, user-facing -- what `print()`/`str()` use).\n"
            "- `__eq__(self, other) -> bool` -- `True` if `other` is a "
            "`Vector` with the same `x`/`y`.\n"
            "- `__add__(self, other)` -- if `other` is a `Vector`, return a "
            "new `Vector(self.x + other.x, self.y + other.y)`; otherwise "
            "return `NotImplemented` (not raise -- that lets Python try the "
            "other object's `__radd__`, or fail with a clear `TypeError` "
            "itself, instead of your code failing with a confusing one).\n"
            "- `__radd__(self, other)` -- return `self` if `other == 0`, else "
            "`NotImplemented`. This is exactly what `sum([v1, v2, v3])` "
            "needs: `sum()` starts from `0 + v1`, and `int.__add__(0, v1)` "
            "fails, so Python falls back to `v1.__radd__(0)`.\n"
            "- `__hash__(self) -> int` -- `hash((self.x, self.y))` (required "
            "alongside `__eq__` for `Vector` to work in a `set`).\n"
            "- `__bool__(self) -> bool` -- `False` only for the zero vector "
            "(`x == 0 and y == 0`).\n"
            "- `__getitem__(self, index)` -- `(self.x, self.y)[index]`, so "
            "`v[0]` is `x` and `v[1]` is `y`.\n\n"
            "See the Study Reference presentation, Topic 8, for the theory."
        ),
        "stub": '''\
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        """f"Vector({self.x}, {self.y})"."""
        raise NotImplementedError

    def __str__(self) -> str:
        """f"({self.x}, {self.y})"."""
        raise NotImplementedError

    def __eq__(self, other) -> bool:
        """True if other is a Vector with the same x/y."""
        raise NotImplementedError

    def __add__(self, other):
        """New Vector(x+x, y+y) if other is a Vector, else NotImplemented."""
        raise NotImplementedError

    def __radd__(self, other):
        """self if other == 0 (for sum()), else NotImplemented."""
        raise NotImplementedError

    def __hash__(self) -> int:
        """hash((self.x, self.y))."""
        raise NotImplementedError

    def __bool__(self) -> bool:
        """False only for the zero vector."""
        raise NotImplementedError

    def __getitem__(self, index):
        """(self.x, self.y)[index]."""
        raise NotImplementedError
''',
        "reference": '''\
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __eq__(self, other) -> bool:
        return isinstance(other, Vector) and self.x == other.x and self.y == other.y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __radd__(self, other):
        if other == 0:
            return self
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __bool__(self) -> bool:
        return not (self.x == 0 and self.y == 0)

    def __getitem__(self, index):
        return (self.x, self.y)[index]
''',
        "test": '''\
from exercises.stage08.exercise01.solution import Vector


def test_vector_repr():
    assert repr(Vector(1, 2)) == "Vector(1, 2)"


def test_str():
    assert str(Vector(1, 2)) == "(1, 2)"


def test_eq():
    assert Vector(1, 2) == Vector(1, 2)
    assert Vector(1, 2) != Vector(3, 4)


def test_add():
    assert Vector(1, 2) + Vector(3, 4) == Vector(4, 6)


def test_radd_via_sum():
    total = sum([Vector(1, 1), Vector(2, 2), Vector(3, 3)])
    assert total == Vector(6, 6)


def test_hash_and_set():
    vectors = {Vector(1, 2), Vector(1, 2), Vector(3, 4)}
    assert len(vectors) == 2


def test_vector_bool():
    assert bool(Vector(0, 0)) is False
    assert bool(Vector(1, 0)) is True


def test_vector_getitem():
    v = Vector(5, 7)
    assert v[0] == 5
    assert v[1] == 7
''',
    },
    {
        "name": "exercise02",
        "title": "Deck: A Collection Protocol",
        "summary": "__repr__, __str__, __len__, __getitem__, __iter__, __contains__, __add__",
        "readme": (
            "Implement `Deck`, a thin wrapper around a list of cards that "
            "behaves like a built-in collection:\n\n"
            "- `__init__(self, cards: list)` -- store `self.cards = "
            "list(cards)` (a copy, so mutating the caller's original list "
            "later doesn't affect the deck).\n"
            "- `__repr__(self) -> str` -- `f\"Deck({self.cards!r})\"`.\n"
            "- `__str__(self) -> str` -- `f\"Deck of {len(self.cards)} "
            "cards\"`.\n"
            "- `__len__(self) -> int` -- `len(self.cards)`.\n"
            "- `__getitem__(self, index)` -- `self.cards[index]` (this alone "
            "makes `deck[0]` and slicing like `deck[:3]` work).\n"
            "- `__iter__(self)` -- `iter(self.cards)` (an explicit iterator, "
            "even though `__getitem__` alone would let old-style iteration "
            "work too).\n"
            "- `__contains__(self, card) -> bool` -- `card in self.cards`.\n"
            "- `__add__(self, other)` -- if `other` is a `Deck`, return a new "
            "`Deck(self.cards + other.cards)` (concatenation); else "
            "`NotImplemented`.\n\n"
            "See the Study Reference presentation, Topic 8, for the theory."
        ),
        "stub": '''\
class Deck:
    def __init__(self, cards: list):
        self.cards = list(cards)

    def __repr__(self) -> str:
        """f"Deck({self.cards!r})"."""
        raise NotImplementedError

    def __str__(self) -> str:
        """f"Deck of {len(self.cards)} cards"."""
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def __getitem__(self, index):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    def __contains__(self, card) -> bool:
        raise NotImplementedError

    def __add__(self, other):
        """New Deck(self.cards + other.cards) if other is a Deck, else NotImplemented."""
        raise NotImplementedError
''',
        "reference": '''\
class Deck:
    def __init__(self, cards: list):
        self.cards = list(cards)

    def __repr__(self) -> str:
        return f"Deck({self.cards!r})"

    def __str__(self) -> str:
        return f"Deck of {len(self.cards)} cards"

    def __len__(self) -> int:
        return len(self.cards)

    def __getitem__(self, index):
        return self.cards[index]

    def __iter__(self):
        return iter(self.cards)

    def __contains__(self, card) -> bool:
        return card in self.cards

    def __add__(self, other):
        if isinstance(other, Deck):
            return Deck(self.cards + other.cards)
        return NotImplemented
''',
        "test": '''\
from exercises.stage08.exercise02.solution import Deck


def test_repr_and_str():
    d = Deck(["A", "K"])
    assert repr(d) == "Deck(['A', 'K'])"
    assert str(d) == "Deck of 2 cards"


def test_len_and_getitem():
    d = Deck(["A", "K", "Q"])
    assert len(d) == 3
    assert d[0] == "A"
    assert d[1:] == ["K", "Q"]


def test_deck_iter():
    d = Deck(["A", "K", "Q"])
    assert list(d) == ["A", "K", "Q"]


def test_deck_contains():
    d = Deck(["A", "K", "Q"])
    assert "K" in d
    assert "J" not in d


def test_add_concatenates():
    d1 = Deck(["A", "K"])
    d2 = Deck(["Q", "J"])
    combined = d1 + d2
    assert list(combined) == ["A", "K", "Q", "J"]
''',
    },
    {
        "name": "exercise03",
        "title": "Inventory: Mapping-ish Container",
        "summary": "__str__, __len__, __contains__, __iter__, __bool__",
        "readme": (
            "Implement `Inventory`, a small wrapper around a "
            "`{item_name: quantity}` dict:\n\n"
            "- `__init__(self)` -- `self.items = {}`.\n"
            "- `add_item(self, name: str, qty: int) -> None` -- "
            "`self.items[name] = self.items.get(name, 0) + qty`.\n"
            "- `__str__(self) -> str` -- `f\"Inventory({len(self.items)} "
            "item types)\"`.\n"
            "- `__len__(self) -> int` -- `len(self.items)` (how many "
            "*distinct* item types, not total quantity).\n"
            "- `__contains__(self, name) -> bool` -- `name in self.items`.\n"
            "- `__iter__(self)` -- `iter(self.items)` (iterating an "
            "`Inventory` yields item *names*, same as iterating a plain "
            "dict would).\n"
            "- `__bool__(self) -> bool` -- `len(self.items) > 0` (an empty "
            "inventory is falsy).\n\n"
            "See the Study Reference presentation, Topic 8, for the theory."
        ),
        "stub": '''\
class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name: str, qty: int) -> None:
        raise NotImplementedError

    def __str__(self) -> str:
        """f"Inventory({len(self.items)} item types)"."""
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def __contains__(self, name) -> bool:
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    def __bool__(self) -> bool:
        raise NotImplementedError
''',
        "reference": '''\
class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name: str, qty: int) -> None:
        self.items[name] = self.items.get(name, 0) + qty

    def __str__(self) -> str:
        return f"Inventory({len(self.items)} item types)"

    def __len__(self) -> int:
        return len(self.items)

    def __contains__(self, name) -> bool:
        return name in self.items

    def __iter__(self):
        return iter(self.items)

    def __bool__(self) -> bool:
        return len(self.items) > 0
''',
        "test": '''\
from exercises.stage08.exercise03.solution import Inventory


def test_empty_inventory_is_falsy():
    inv = Inventory()
    assert bool(inv) is False
    assert len(inv) == 0


def test_add_item_and_str():
    inv = Inventory()
    inv.add_item("bolt", 10)
    inv.add_item("nut", 20)
    assert str(inv) == "Inventory(2 item types)"
    assert bool(inv) is True


def test_add_item_accumulates():
    inv = Inventory()
    inv.add_item("bolt", 10)
    inv.add_item("bolt", 5)
    assert inv.items["bolt"] == 15


def test_contains():
    inv = Inventory()
    inv.add_item("bolt", 10)
    assert "bolt" in inv
    assert "screw" not in inv


def test_iter_yields_names():
    inv = Inventory()
    inv.add_item("bolt", 10)
    inv.add_item("nut", 20)
    assert set(inv) == {"bolt", "nut"}
''',
    },
    {
        "name": "exercise04",
        "title": "Callables",
        "summary": "__call__ x3",
        "readme": (
            "Implement three classes whose instances are directly callable "
            "(`instance(...)` works because of `__call__`):\n\n"
            "- `Multiplier.__init__(self, factor)` stores it; "
            "`__call__(self, x)` returns `x * self.factor`.\n"
            "- `Adder.__init__(self, n)` stores it; `__call__(self, x)` "
            "returns `x + self.n`.\n"
            "- `Toggler.__init__(self)` sets `self.state = False`; "
            "`__call__(self) -> bool` flips `self.state` and returns the "
            "new value -- a callable object carrying its own state between "
            "calls, the same idea as the `make_counter()` closure from "
            "Topic 3, but as a class instead of a closure.\n\n"
            "See the Study Reference presentation, Topic 8, for the theory."
        ),
        "stub": '''\
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        """x * self.factor."""
        raise NotImplementedError


class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        """x + self.n."""
        raise NotImplementedError


class Toggler:
    def __init__(self):
        self.state = False

    def __call__(self) -> bool:
        """Flip self.state and return the new value."""
        raise NotImplementedError
''',
        "reference": '''\
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor


class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return x + self.n


class Toggler:
    def __init__(self):
        self.state = False

    def __call__(self) -> bool:
        self.state = not self.state
        return self.state
''',
        "test": '''\
from exercises.stage08.exercise04.solution import Multiplier, Adder, Toggler


def test_multiplier():
    double = Multiplier(2)
    assert double(5) == 10


def test_adder():
    add5 = Adder(5)
    assert add5(10) == 15


def test_toggler_carries_state():
    toggle = Toggler()
    assert toggle() is True
    assert toggle() is False
    assert toggle() is True


def test_instances_are_callable():
    assert callable(Multiplier(2))
    assert callable(Adder(1))
    assert callable(Toggler())
''',
    },
    {
        "name": "exercise05",
        "title": "NumberRange: A Read-Only Sequence",
        "summary": "__repr__, __eq__, __len__, __getitem__, __iter__, __contains__, __bool__, __hash__",
        "readme": (
            "Implement `NumberRange`, a simplified, immutable version of the "
            "builtin `range`:\n\n"
            "- `__init__(self, start: int, stop: int)` -- store both.\n"
            "- `__repr__(self) -> str` -- `f\"NumberRange({self.start}, "
            "{self.stop})\"`.\n"
            "- `__eq__(self, other) -> bool` -- `True` if `other` is a "
            "`NumberRange` with the same `start`/`stop`.\n"
            "- `__hash__(self) -> int` -- `hash((self.start, self.stop))`.\n"
            "- `__len__(self) -> int` -- `max(0, self.stop - self.start)`.\n"
            "- `__getitem__(self, index)` -- `raise IndexError` if `index < 0 "
            "or index >= len(self)`, else `self.start + index`.\n"
            "- `__iter__(self)` -- `iter(range(self.start, self.stop))`.\n"
            "- `__contains__(self, value) -> bool` -- `self.start <= value < "
            "self.stop` (an O(1) check, not a linear scan -- one advantage "
            "of implementing `__contains__` yourself instead of relying on "
            "the default that falls back to iterating).\n"
            "- `__bool__(self) -> bool` -- `len(self) > 0`.\n\n"
            "See the Study Reference presentation, Topic 8, for the theory."
        ),
        "stub": '''\
class NumberRange:
    def __init__(self, start: int, stop: int):
        self.start = start
        self.stop = stop

    def __repr__(self) -> str:
        """f"NumberRange({self.start}, {self.stop})"."""
        raise NotImplementedError

    def __eq__(self, other) -> bool:
        raise NotImplementedError

    def __hash__(self) -> int:
        raise NotImplementedError

    def __len__(self) -> int:
        """max(0, self.stop - self.start)."""
        raise NotImplementedError

    def __getitem__(self, index):
        """self.start + index, or raise IndexError if out of range."""
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    def __contains__(self, value) -> bool:
        """self.start <= value < self.stop -- O(1), not a scan."""
        raise NotImplementedError

    def __bool__(self) -> bool:
        raise NotImplementedError
''',
        "reference": '''\
class NumberRange:
    def __init__(self, start: int, stop: int):
        self.start = start
        self.stop = stop

    def __repr__(self) -> str:
        return f"NumberRange({self.start}, {self.stop})"

    def __eq__(self, other) -> bool:
        return isinstance(other, NumberRange) and self.start == other.start and self.stop == other.stop

    def __hash__(self) -> int:
        return hash((self.start, self.stop))

    def __len__(self) -> int:
        return max(0, self.stop - self.start)

    def __getitem__(self, index):
        if index < 0 or index >= len(self):
            raise IndexError("NumberRange index out of range")
        return self.start + index

    def __iter__(self):
        return iter(range(self.start, self.stop))

    def __contains__(self, value) -> bool:
        return self.start <= value < self.stop

    def __bool__(self) -> bool:
        return len(self) > 0
''',
        "test": '''\
import pytest
from exercises.stage08.exercise05.solution import NumberRange


def test_number_range_repr():
    assert repr(NumberRange(1, 5)) == "NumberRange(1, 5)"


def test_number_range_eq_and_hash():
    assert NumberRange(1, 5) == NumberRange(1, 5)
    assert len({NumberRange(1, 5), NumberRange(1, 5), NumberRange(2, 6)}) == 2


def test_number_range_len():
    assert len(NumberRange(1, 5)) == 4
    assert len(NumberRange(5, 5)) == 0


def test_number_range_getitem():
    r = NumberRange(10, 15)
    assert r[0] == 10
    assert r[4] == 14
    with pytest.raises(IndexError):
        r[5]


def test_number_range_iter():
    assert list(NumberRange(1, 5)) == [1, 2, 3, 4]


def test_number_range_contains():
    r = NumberRange(1, 5)
    assert 3 in r
    assert 5 not in r


def test_number_range_bool():
    assert bool(NumberRange(1, 5)) is True
    assert bool(NumberRange(5, 5)) is False
''',
    },
    {
        "name": "exercise06",
        "title": "Money and Score: Operator Overloading",
        "summary": "__repr__, __eq__, __add__, __radd__, __hash__ across two classes",
        "readme": (
            "Implement two small immutable value classes, each supporting "
            "`+` and `sum()`:\n\n"
            "- `Money.__init__(self, cents: int)` -- store it. `__repr__` -- "
            "`f\"Money({self.cents})\"`. `__eq__` -- same `cents`. `__add__` "
            "-- `Money(self.cents + other.cents)` if `other` is `Money`, "
            "else `NotImplemented`. `__radd__` -- `self` if `other == 0`, "
            "else `NotImplemented`. `__hash__` -- `hash(self.cents)`.\n"
            "- `Score.__init__(self, points: int)` -- same five methods, "
            "same shapes, just `points` instead of `cents`.\n\n"
            "This is **operator overloading**: `+` on `Money`/`Score` "
            "doesn't do anything magical -- it's just Python calling "
            "`__add__`/`__radd__`, the same mechanism as `Vector` in "
            "Exercise 1. Writing it twice, independently, for two unrelated "
            "classes is the point: any class can opt into `+` this way, "
            "with no shared base class required.\n\n"
            "See the Study Reference presentation, Topic 8, for the theory."
        ),
        "stub": '''\
class Money:
    def __init__(self, cents: int):
        self.cents = cents

    def __repr__(self) -> str:
        raise NotImplementedError

    def __eq__(self, other) -> bool:
        raise NotImplementedError

    def __add__(self, other):
        raise NotImplementedError

    def __radd__(self, other):
        raise NotImplementedError

    def __hash__(self) -> int:
        raise NotImplementedError


class Score:
    def __init__(self, points: int):
        self.points = points

    def __repr__(self) -> str:
        raise NotImplementedError

    def __eq__(self, other) -> bool:
        raise NotImplementedError

    def __add__(self, other):
        raise NotImplementedError

    def __radd__(self, other):
        raise NotImplementedError

    def __hash__(self) -> int:
        raise NotImplementedError
''',
        "reference": '''\
class Money:
    def __init__(self, cents: int):
        self.cents = cents

    def __repr__(self) -> str:
        return f"Money({self.cents})"

    def __eq__(self, other) -> bool:
        return isinstance(other, Money) and self.cents == other.cents

    def __add__(self, other):
        if isinstance(other, Money):
            return Money(self.cents + other.cents)
        return NotImplemented

    def __radd__(self, other):
        if other == 0:
            return self
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self.cents)


class Score:
    def __init__(self, points: int):
        self.points = points

    def __repr__(self) -> str:
        return f"Score({self.points})"

    def __eq__(self, other) -> bool:
        return isinstance(other, Score) and self.points == other.points

    def __add__(self, other):
        if isinstance(other, Score):
            return Score(self.points + other.points)
        return NotImplemented

    def __radd__(self, other):
        if other == 0:
            return self
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self.points)
''',
        "test": '''\
from exercises.stage08.exercise06.solution import Money, Score


def test_money_add_and_eq():
    assert Money(100) + Money(50) == Money(150)


def test_money_sum():
    assert sum([Money(100), Money(200), Money(300)]) == Money(600)


def test_money_hash():
    assert len({Money(100), Money(100), Money(200)}) == 2


def test_score_add_and_eq():
    assert Score(10) + Score(5) == Score(15)


def test_score_sum():
    assert sum([Score(1), Score(2), Score(3)]) == Score(6)


def test_money_repr():
    assert repr(Money(500)) == "Money(500)"
''',
    },
    {
        "name": "exercise07",
        "title": "Context Managers as a Protocol",
        "summary": "__enter__/__exit__ x3, protocols vs explicit inheritance",
        "readme": (
            "Implement three unrelated classes that all work in a `with` "
            "statement -- **none of them inherit from any special base "
            "class**. `with` works purely by looking for `__enter__`/"
            "`__exit__` *at runtime*: this is a **protocol** (structural, "
            "duck-typed), not explicit inheritance (unlike, say, Java's "
            "`Closeable` interface, which a class must formally implement):\n\n"
            "- `ResourceGuard` -- `__enter__` sets `self.active = True` and "
            "returns `self`; `__exit__(self, exc_type, exc_val, exc_tb)` "
            "sets `self.active = False` and returns `False`.\n"
            "- `Transaction` -- `__enter__` sets `self.committed = False` and "
            "`self.rolled_back = False`, returns `self`; `__exit__` sets "
            "`self.committed = True` if `exc_type is None` (the block "
            "finished cleanly), else sets `self.rolled_back = True` -- "
            "either way, returns `False` (never swallow the exception).\n"
            "- `SuppressAll` -- `__enter__` returns `None`; `__exit__` "
            "**always** returns `True`, suppressing *any* exception raised "
            "inside the block, regardless of type.\n\n"
            "See the Study Reference presentation, Topic 8, for the theory."
        ),
        "stub": '''\
class ResourceGuard:
    def __enter__(self):
        """Set self.active = True; return self."""
        raise NotImplementedError

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Set self.active = False; return False."""
        raise NotImplementedError


class Transaction:
    def __enter__(self):
        """Set self.committed = self.rolled_back = False; return self."""
        raise NotImplementedError

    def __exit__(self, exc_type, exc_val, exc_tb):
        """committed=True if exc_type is None, else rolled_back=True. Return False."""
        raise NotImplementedError


class SuppressAll:
    def __enter__(self):
        raise NotImplementedError

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Always return True -- suppress any exception."""
        raise NotImplementedError
''',
        "reference": '''\
class ResourceGuard:
    def __enter__(self):
        self.active = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.active = False
        return False


class Transaction:
    def __enter__(self):
        self.committed = False
        self.rolled_back = False
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.committed = True
        else:
            self.rolled_back = True
        return False


class SuppressAll:
    def __enter__(self):
        return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        return True
''',
        "test": '''\
import pytest
from exercises.stage08.exercise07.solution import ResourceGuard, Transaction, SuppressAll


def test_resource_guard_active_during_block():
    guard = ResourceGuard()
    with guard:
        assert guard.active is True
    assert guard.active is False


def test_transaction_commits_on_success():
    with Transaction() as tx:
        pass
    assert tx.committed is True
    assert tx.rolled_back is False


def test_transaction_rolls_back_on_exception():
    with pytest.raises(RuntimeError):
        with Transaction() as tx:
            raise RuntimeError("boom")
    assert tx.rolled_back is True
    assert tx.committed is False


def test_suppress_all_swallows_any_exception():
    with SuppressAll():
        raise ValueError("this never propagates")
    with SuppressAll():
        raise KeyError("neither does this")


def test_no_special_base_class():
    assert ResourceGuard.__bases__ == (object,)
    assert Transaction.__bases__ == (object,)
    assert SuppressAll.__bases__ == (object,)
''',
    },
]
