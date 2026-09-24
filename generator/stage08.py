"""
Stage 8 -- The Python Data Model.

Rolled onto the tier-named exercise convention: a minimum of two exercises
per Basic/Mid/Advanced tier. Every exercise here is built around one or
more small classes -- Stage 8's whole subject is dunder methods, which
only exist on classes.

Coverage plan (every item below is exercised by the trainee's own code,
generally 2+ times across these 6 exercises):

  Basic:    __repr__, __str__, __eq__
  Mid:      __add__, __len__, __getitem__, __iter__, __contains__,
            __call__, __bool__, operator overloading, protocols vs
            explicit inheritance
  Advanced: __enter__, __exit__, __hash__, __radd__
"""

STAGE = "stage08"
TOPIC = "The Python Data Model"
OVERVIEW = (
    "Six exercises, two per tier: the everyday trio (__repr__/__str__/"
    "__eq__) in Basic, a card-deck-style collection protocol plus "
    "callables in Mid, and operator overloading's __radd__/__hash__ "
    "pairing plus three context-manager classes with no shared base class "
    "in Advanced."
)

EXERCISES = [
    {
        "name": "basic01",
        "title": "Point: repr, str, eq",
        "summary": "__repr__, __str__, __eq__",
        "readme": (
            "Implement `Point`, a simple 2D point:\n\n"
            "- `__init__(self, x, y)` -- store both.\n"
            "- `__repr__(self) -> str` -- `f\"Point({self.x}, {self.y})\"` "
            "(unambiguous, developer-facing -- what you'd see in a "
            "debugger or an error traceback).\n"
            "- `__str__(self) -> str` -- `f\"({self.x}, {self.y})\"` "
            "(friendlier, user-facing -- what `print()`/`str()` use).\n"
            "- `__eq__(self, other) -> bool` -- `True` if `other` is a "
            "`Point` with the same `x`/`y`.\n\n"
            "`repr()` and `str()` serve different audiences: `repr()` "
            "should (ideally) look like valid Python that could recreate "
            "the object, while `str()` is free to be whatever reads best "
            "to a human. Without `__eq__`, `Point(1, 2) == Point(1, 2)` "
            "would be `False` -- the default `__eq__` compares object "
            "identity (`is`), not field values.\n\n"
            "See the Study Reference presentation, Topic 8 (Basic tier), "
            "for the theory."
        ),
        "stub": '''\
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        """f"Point({self.x}, {self.y})"."""
        raise NotImplementedError

    def __str__(self) -> str:
        """f"({self.x}, {self.y})"."""
        raise NotImplementedError

    def __eq__(self, other) -> bool:
        """True if other is a Point with the same x/y."""
        raise NotImplementedError
''',
        "reference": '''\
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __eq__(self, other) -> bool:
        return isinstance(other, Point) and self.x == other.x and self.y == other.y
''',
        "test": '''\
from exercises.stage08.basic01.solution import Point


def test_repr_is_unambiguous_and_developer_facing():
    """__repr__ must be f"Point(x, y)" -- what a debugger/traceback would show."""
    assert repr(Point(1, 2)) == "Point(1, 2)"


def test_str_is_friendlier_and_differs_from_repr():
    """__str__ must be f"(x, y)" -- friendlier than __repr__, and distinct from it."""
    assert str(Point(1, 2)) == "(1, 2)"
    assert str(Point(1, 2)) != repr(Point(1, 2))


def test_eq_compares_field_values_not_identity():
    """Without a custom __eq__, two distinct Point objects would never compare equal -- this one must compare x/y."""
    assert Point(1, 2) == Point(1, 2)
    assert Point(1, 2) != Point(3, 4)
    assert Point(1, 2) is not Point(1, 2)
''',
    },
    {
        "name": "basic02",
        "title": "PlayingCard: repr, str, eq",
        "summary": "__repr__, __str__, __eq__ (a second scenario)",
        "readme": (
            "Implement `PlayingCard`, a single playing card:\n\n"
            "- `__init__(self, rank: str, suit: str)` -- store both.\n"
            "- `__repr__(self) -> str` -- "
            "`f\"PlayingCard({self.rank!r}, {self.suit!r})\"` (note the "
            "`!r}` -- it wraps `rank`/`suit` in their own `repr()`, e.g. "
            "`PlayingCard('A', 'Spades')` with the quotes included, so "
            "the result really is valid Python that recreates the "
            "object).\n"
            "- `__str__(self) -> str` -- `f\"{self.rank} of {self.suit}\"` "
            "(e.g. `\"A of Spades\"`).\n"
            "- `__eq__(self, other) -> bool` -- `True` if `other` is a "
            "`PlayingCard` with the same `rank`/`suit`.\n\n"
            "Same three dunders as the previous exercise, on a different "
            "shape of data, to drive home that `__repr__`/`__str__`/"
            "`__eq__` are a pattern you write the same way on every class "
            "that needs it, not something specific to one kind of "
            "object.\n\n"
            "See the Study Reference presentation, Topic 8 (Basic tier), "
            "for the theory."
        ),
        "stub": '''\
class PlayingCard:
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit

    def __repr__(self) -> str:
        """f"PlayingCard({self.rank!r}, {self.suit!r})"."""
        raise NotImplementedError

    def __str__(self) -> str:
        """f"{self.rank} of {self.suit}"."""
        raise NotImplementedError

    def __eq__(self, other) -> bool:
        """True if other is a PlayingCard with the same rank/suit."""
        raise NotImplementedError
''',
        "reference": '''\
class PlayingCard:
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit

    def __repr__(self) -> str:
        return f"PlayingCard({self.rank!r}, {self.suit!r})"

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"

    def __eq__(self, other) -> bool:
        return isinstance(other, PlayingCard) and self.rank == other.rank and self.suit == other.suit
''',
        "test": '''\
from exercises.stage08.basic02.solution import PlayingCard


def test_repr_uses_bang_r_formatting():
    """__repr__ must use !r on rank/suit, so the result is valid Python (quoted strings) that recreates the object."""
    assert repr(PlayingCard("A", "Spades")) == "PlayingCard('A', 'Spades')"


def test_str_is_human_friendly():
    """__str__ must be f"{rank} of {suit}"."""
    assert str(PlayingCard("A", "Spades")) == "A of Spades"


def test_eq_compares_rank_and_suit():
    """__eq__ must compare BOTH rank and suit, not just one."""
    assert PlayingCard("A", "Spades") == PlayingCard("A", "Spades")
    assert PlayingCard("A", "Spades") != PlayingCard("A", "Hearts")
    assert PlayingCard("A", "Spades") != PlayingCard("K", "Spades")
''',
    },
    {
        "name": "mid01",
        "title": "Deck: A Collection Protocol",
        "summary": "__len__, __getitem__, __iter__, __contains__, __add__, operator overloading, protocols",
        "readme": (
            "Implement `Deck`, a thin wrapper around a list of cards that "
            "behaves like a built-in collection -- purely by implementing "
            "the right dunders, with **no inheritance from any collection "
            "base class**:\n\n"
            "- `__init__(self, cards: list)` -- store `self.cards = "
            "list(cards)` (a copy, so mutating the caller's original list "
            "later doesn't affect the deck).\n"
            "- `__len__(self) -> int` -- `len(self.cards)`.\n"
            "- `__getitem__(self, index)` -- `self.cards[index]` (this "
            "alone makes `deck[0]` and slicing like `deck[:3]` work).\n"
            "- `__iter__(self)` -- `iter(self.cards)` (an explicit "
            "iterator, even though `__getitem__` alone would let "
            "old-style iteration work too).\n"
            "- `__contains__(self, card) -> bool` -- `card in "
            "self.cards`.\n"
            "- `__add__(self, other)` -- if `other` is a `Deck`, return a "
            "new `Deck(self.cards + other.cards)` (concatenation); else "
            "`NotImplemented`. This is **operator overloading**: `+` on "
            "`Deck` does nothing magical, it's just Python calling "
            "`__add__`.\n\n"
            "`Deck` supports `len()`, indexing, slicing, `for x in deck`, "
            "`in`, and `+` -- all of that from five small methods, none of "
            "which required subclassing `list` or any other built-in "
            "type. That's the **protocol** idea: Python's `with`/`len()`/"
            "`for`/`in`/`+` machinery looks for matching dunder methods "
            "*at runtime*, not for a specific base class.\n\n"
            "See the Study Reference presentation, Topic 8 (Mid tier), "
            "for the theory."
        ),
        "stub": '''\
class Deck:
    def __init__(self, cards: list):
        self.cards = list(cards)

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
from exercises.stage08.mid01.solution import Deck


def test_init_copies_the_input_list():
    """__init__ must store list(cards) -- a copy, not the same list object."""
    original = ["A", "K"]
    d = Deck(original)
    original.append("Q")
    assert list(d) == ["A", "K"]


def test_len_and_getitem():
    """__len__ and __getitem__ make len(deck) and indexing/slicing work."""
    d = Deck(["A", "K", "Q"])
    assert len(d) == 3
    assert d[0] == "A"
    assert d[1:] == ["K", "Q"]


def test_deck_iter():
    """__iter__ makes list(deck)/for-loops work."""
    d = Deck(["A", "K", "Q"])
    assert list(d) == ["A", "K", "Q"]


def test_deck_contains():
    """__contains__ makes the `in` operator work."""
    d = Deck(["A", "K", "Q"])
    assert "K" in d
    assert "J" not in d


def test_add_concatenates_via_operator_overloading():
    """__add__ must return a NEW Deck concatenating both cards lists -- this is what makes `+` work on Deck instances."""
    d1 = Deck(["A", "K"])
    d2 = Deck(["Q", "J"])
    combined = d1 + d2
    assert list(combined) == ["A", "K", "Q", "J"]
    assert isinstance(combined, Deck)


def test_deck_has_no_special_base_class():
    """Deck supports len()/indexing/iteration/`in`/`+` via dunders alone -- no collection base class needed (protocols vs explicit inheritance)."""
    assert Deck.__bases__ == (object,)
''',
    },
    {
        "name": "mid02",
        "title": "Inventory and Callables",
        "summary": "__contains__, __iter__, __bool__ (reinforced), __call__",
        "readme": (
            "Two more dunder protocols on unrelated classes. First, "
            "`Inventory`, a small wrapper around a `{item_name: "
            "quantity}` dict:\n\n"
            "- `__init__(self)` -- `self.items = {}`.\n"
            "- `add_item(self, name: str, qty: int) -> None` -- "
            "`self.items[name] = self.items.get(name, 0) + qty`.\n"
            "- `__contains__(self, name) -> bool` -- `name in "
            "self.items`.\n"
            "- `__iter__(self)` -- `iter(self.items)` (iterating an "
            "`Inventory` yields item *names*, same as iterating a plain "
            "dict would).\n"
            "- `__bool__(self) -> bool` -- `len(self.items) > 0` (an "
            "empty inventory is falsy).\n\n"
            "Second, three classes whose instances are directly callable "
            "(`instance(...)` works because of `__call__`):\n\n"
            "- `Multiplier.__init__(self, factor)` stores it; "
            "`__call__(self, x)` returns `x * self.factor`.\n"
            "- `Adder.__init__(self, n)` stores it; `__call__(self, x)` "
            "returns `x + self.n`.\n"
            "- `Toggler.__init__(self)` sets `self.state = False`; "
            "`__call__(self) -> bool` flips `self.state` and returns the "
            "new value -- a callable object carrying its own state "
            "between calls, the same idea as a closure, but as a class "
            "instead.\n\n"
            "See the Study Reference presentation, Topic 8 (Mid tier), "
            "for the theory."
        ),
        "stub": '''\
class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name: str, qty: int) -> None:
        raise NotImplementedError

    def __contains__(self, name) -> bool:
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    def __bool__(self) -> bool:
        raise NotImplementedError


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
class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name: str, qty: int) -> None:
        self.items[name] = self.items.get(name, 0) + qty

    def __contains__(self, name) -> bool:
        return name in self.items

    def __iter__(self):
        return iter(self.items)

    def __bool__(self) -> bool:
        return len(self.items) > 0


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
from exercises.stage08.mid02.solution import Inventory, Multiplier, Adder, Toggler


def test_empty_inventory_is_falsy():
    """__bool__ makes an empty Inventory falsy."""
    inv = Inventory()
    assert bool(inv) is False


def test_add_item_makes_inventory_truthy():
    """Adding an item makes __bool__ return True."""
    inv = Inventory()
    inv.add_item("bolt", 10)
    assert bool(inv) is True


def test_add_item_accumulates():
    """add_item must accumulate quantities for the same name, not overwrite."""
    inv = Inventory()
    inv.add_item("bolt", 10)
    inv.add_item("bolt", 5)
    assert inv.items["bolt"] == 15


def test_contains():
    """__contains__ makes the `in` operator work against item names."""
    inv = Inventory()
    inv.add_item("bolt", 10)
    assert "bolt" in inv
    assert "screw" not in inv


def test_iter_yields_names():
    """__iter__ must yield item NAMES, same as iterating a plain dict."""
    inv = Inventory()
    inv.add_item("bolt", 10)
    inv.add_item("nut", 20)
    assert set(inv) == {"bolt", "nut"}


def test_multiplier_and_adder_are_callable():
    """__call__ makes instances directly callable like a function."""
    double = Multiplier(2)
    add5 = Adder(5)
    assert double(5) == 10
    assert add5(10) == 15
    assert callable(double)
    assert callable(add5)


def test_toggler_carries_state_across_calls():
    """Toggler's __call__ must flip and return its own state each call, like a stateful closure."""
    toggle = Toggler()
    assert toggle() is True
    assert toggle() is False
    assert toggle() is True
''',
    },
    {
        "name": "advanced01",
        "title": "Money and Score: Operator Overloading",
        "summary": "__repr__/__eq__ (reinforced), __add__, __radd__, __hash__",
        "readme": (
            "Implement two small immutable value classes, each supporting "
            "`+` and `sum()`:\n\n"
            "- `Money.__init__(self, cents: int)` -- store it. `__repr__` "
            "-- `f\"Money({self.cents})\"`. `__eq__` -- same `cents`. "
            "`__add__` -- `Money(self.cents + other.cents)` if `other` is "
            "`Money`, else `NotImplemented`. `__radd__` -- `self` if "
            "`other == 0`, else `NotImplemented`. `__hash__` -- "
            "`hash(self.cents)` (required alongside `__eq__` for `Money` "
            "to work in a `set`).\n"
            "- `Score.__init__(self, points: int)` -- same five methods, "
            "same shapes, just `points` instead of `cents`.\n\n"
            "`__radd__` is what makes `sum([m1, m2, m3])` work: `sum()` "
            "starts from `0 + m1`, and `int.__add__(0, m1)` fails (an "
            "`int` doesn't know how to add a `Money`), so Python falls "
            "back to `m1.__radd__(0)` -- the **reflected** operator, "
            "tried only when the left operand's own method returns "
            "`NotImplemented`. Writing this twice, independently, for two "
            "unrelated classes is the point: any class can opt into `+` "
            "and `sum()` this way, with no shared base class required.\n\n"
            "See the Study Reference presentation, Topic 8 (Advanced "
            "tier), for the theory."
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
from exercises.stage08.advanced01.solution import Money, Score


def test_money_add_and_eq():
    """Money.__add__ combines cents; __eq__ compares by value."""
    assert Money(100) + Money(50) == Money(150)


def test_money_sum_uses_radd():
    """sum() starts from 0 + Money(...), which needs __radd__ to succeed."""
    assert sum([Money(100), Money(200), Money(300)]) == Money(600)


def test_money_hash_required_alongside_eq():
    """Money must be hashable (via __hash__) since it defines __eq__, or it couldn't go in a set."""
    assert len({Money(100), Money(100), Money(200)}) == 2


def test_score_add_and_sum_independently_of_money():
    """Score implements the same pattern independently -- no shared base class with Money."""
    assert Score(10) + Score(5) == Score(15)
    assert sum([Score(1), Score(2), Score(3)]) == Score(6)


def test_money_repr():
    """__repr__ == f"Money({cents})"."""
    assert repr(Money(500)) == "Money(500)"
''',
    },
    {
        "name": "advanced02",
        "title": "Context Managers as a Protocol",
        "summary": "__enter__, __exit__",
        "readme": (
            "Implement three unrelated classes that all work in a `with` "
            "statement -- **none of them inherit from any special base "
            "class**. `with` works purely by looking for `__enter__`/"
            "`__exit__` *at runtime*: this is a **protocol** (structural, "
            "duck-typed), not explicit inheritance (unlike, say, Java's "
            "`Closeable` interface, which a class must formally "
            "implement):\n\n"
            "- `ResourceGuard` -- `__enter__` sets `self.active = True` "
            "and returns `self`; `__exit__(self, exc_type, exc_val, "
            "exc_tb)` sets `self.active = False` and returns `False`.\n"
            "- `Transaction` -- `__enter__` sets `self.committed = False` "
            "and `self.rolled_back = False`, returns `self`; `__exit__` "
            "sets `self.committed = True` if `exc_type is None` (the "
            "block finished cleanly), else sets `self.rolled_back = "
            "True` -- either way, returns `False` (never swallow the "
            "exception).\n"
            "- `SuppressAll` -- `__enter__` returns `None`; `__exit__` "
            "**always** returns `True`, suppressing *any* exception "
            "raised inside the block, regardless of type.\n\n"
            "See the Study Reference presentation, Topic 8 (Advanced "
            "tier), for the theory."
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
from exercises.stage08.advanced02.solution import ResourceGuard, Transaction, SuppressAll


def test_resource_guard_active_during_block():
    """__enter__ sets active True and returns self; __exit__ sets it back to False."""
    guard = ResourceGuard()
    with guard:
        assert guard.active is True
    assert guard.active is False


def test_transaction_commits_on_success():
    """__exit__ sets committed=True when the block finishes with no exception (exc_type is None)."""
    with Transaction() as tx:
        pass
    assert tx.committed is True
    assert tx.rolled_back is False


def test_transaction_rolls_back_on_exception():
    """__exit__ sets rolled_back=True when the block raises, and must return False so the exception still propagates."""
    with pytest.raises(RuntimeError):
        with Transaction() as tx:
            raise RuntimeError("boom")
    assert tx.rolled_back is True
    assert tx.committed is False


def test_suppress_all_swallows_any_exception():
    """__exit__ must always return True, suppressing any exception type raised inside the block."""
    with SuppressAll():
        raise ValueError("this never propagates")
    with SuppressAll():
        raise KeyError("neither does this")


def test_no_special_base_class_required_for_with_statement():
    """None of the three classes inherit from any special base -- `with` works purely via the __enter__/__exit__ protocol."""
    assert ResourceGuard.__bases__ == (object,)
    assert Transaction.__bases__ == (object,)
    assert SuppressAll.__bases__ == (object,)
''',
    },
]
