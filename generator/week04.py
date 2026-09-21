"""
Week 4 -- Data Structures.

Coverage plan (each item exercised by the trainee's own code >=3 times):
  keywords: list, tuple, dict, set, append(), sort()/sorted(), len(),
            zip(), enumerate(), list comprehension, dict comprehension
  dunders:  __hash__, __eq__
  modules:  collections, dataclasses
  methods:  collections.defaultdict(), collections.Counter(),
            collections.deque(), dataclasses.dataclass
  concepts: hashability, namedtuple / dataclass records,
            set operations (union/intersection/difference)
"""

WEEK = "week04"
TOPIC = "Data Structures"
OVERVIEW = (
    "Six exercises covering every builtin container, comprehension style, "
    "and collections/dataclasses tool from Topic 4 at least three times "
    "each, finishing with hand-written __eq__/__hash__ so hashability stops "
    "being an abstract warning and becomes something you had to get right."
)

EXERCISES = [
    {
        "name": "exercise01",
        "title": "List and Tuple Basics",
        "summary": "list, tuple, append(), sort()/sorted(), zip(), enumerate(), len()",
        "readme": (
            "Implement:\n\n"
            "- `build_shopping_list(items: list[str]) -> list[str]` -- start "
            "with `[]` and `.append()` each item from `items` onto it in a "
            "`for` loop (don't just return `items`/`list(items)`).\n"
            "- `unique_sorted(numbers: list[int]) -> list[int]` -- "
            "`sorted(set(numbers))`.\n"
            "- `sort_in_place(items: list) -> None` -- `items.sort()` (the "
            "**method**, which mutates in place and returns `None` -- different "
            "from the `sorted()` builtin used above, which returns a new list).\n"
            "- `as_tuple_pairs(names: list[str], ages: list[int]) -> list[tuple]` "
            "-- `list(zip(names, ages))`.\n"
            "- `zip_and_sum(list1: list[int], list2: list[int]) -> list[int]` -- "
            "`[a + b for a, b in zip(list1, list2)]`.\n"
            "- `label_each(items: list[str]) -> list[str]` -- "
            "`[f\"{i}:{v}\" for i, v in enumerate(items)]`.\n"
            "- `count_items(items: list) -> int` -- `len(items)`.\n\n"
            "See the Study Reference presentation, Topic 4, for the theory."
        ),
        "stub": '''\
def build_shopping_list(items: list[str]) -> list[str]:
    """Build a new list by .append()-ing each item in a loop."""
    raise NotImplementedError


def unique_sorted(numbers: list[int]) -> list[int]:
    """sorted(set(numbers))."""
    raise NotImplementedError


def sort_in_place(items: list) -> None:
    """items.sort() -- mutate in place, return None."""
    raise NotImplementedError


def as_tuple_pairs(names: list[str], ages: list[int]) -> list[tuple]:
    """list(zip(names, ages))."""
    raise NotImplementedError


def zip_and_sum(list1: list[int], list2: list[int]) -> list[int]:
    """[a + b for a, b in zip(list1, list2)]."""
    raise NotImplementedError


def label_each(items: list[str]) -> list[str]:
    """[f"{i}:{v}" for i, v in enumerate(items)]."""
    raise NotImplementedError


def count_items(items: list) -> int:
    """len(items)."""
    raise NotImplementedError
''',
        "reference": '''\
def build_shopping_list(items: list[str]) -> list[str]:
    result = []
    for item in items:
        result.append(item)
    return result


def unique_sorted(numbers: list[int]) -> list[int]:
    return sorted(set(numbers))


def sort_in_place(items: list) -> None:
    items.sort()


def as_tuple_pairs(names: list[str], ages: list[int]) -> list[tuple]:
    return list(zip(names, ages))


def zip_and_sum(list1: list[int], list2: list[int]) -> list[int]:
    return [a + b for a, b in zip(list1, list2)]


def label_each(items: list[str]) -> list[str]:
    return [f"{i}:{v}" for i, v in enumerate(items)]


def count_items(items: list) -> int:
    return len(items)
''',
        "test": '''\
from exercises.week04.exercise01.solution import (
    build_shopping_list,
    unique_sorted,
    sort_in_place,
    as_tuple_pairs,
    zip_and_sum,
    label_each,
    count_items,
)


def test_build_shopping_list():
    assert build_shopping_list(["milk", "eggs"]) == ["milk", "eggs"]


def test_unique_sorted():
    assert unique_sorted([3, 1, 2, 1, 3]) == [1, 2, 3]


def test_sort_in_place():
    items = [3, 1, 2]
    result = sort_in_place(items)
    assert result is None
    assert items == [1, 2, 3]


def test_as_tuple_pairs():
    assert as_tuple_pairs(["a", "b"], [1, 2]) == [("a", 1), ("b", 2)]


def test_zip_and_sum():
    assert zip_and_sum([1, 2, 3], [10, 20, 30]) == [11, 22, 33]


def test_label_each():
    assert label_each(["a", "b"]) == ["0:a", "1:b"]


def test_count_items():
    assert count_items([1, 2, 3]) == 3
''',
    },
    {
        "name": "exercise02",
        "title": "Dict and Set Operations",
        "summary": "dict comprehension x3, enumerate/zip reinforced, set operations x3",
        "readme": (
            "Implement:\n\n"
            "- `word_lengths(words: list[str]) -> dict` -- "
            "`{w: len(w) for w in words}`.\n"
            "- `index_lookup(items: list[str]) -> dict` -- "
            "`{item: i for i, item in enumerate(items)}`.\n"
            "- `numbered_pairs(items: list[str]) -> list[tuple]` -- "
            "`list(enumerate(items))`.\n"
            "- `pair_and_dict(keys: list[str], values: list) -> dict` -- "
            "`dict(zip(keys, values))`.\n"
            "- `common_elements(a: set, b: set) -> set` -- `a & b` "
            "(intersection).\n"
            "- `unique_to_first(a: set, b: set) -> set` -- `a - b` "
            "(difference).\n"
            "- `all_elements(a: set, b: set) -> set` -- `a | b` (union).\n\n"
            "See the Study Reference presentation, Topic 4, for the theory."
        ),
        "stub": '''\
def word_lengths(words: list[str]) -> dict:
    """{w: len(w) for w in words}."""
    raise NotImplementedError


def index_lookup(items: list[str]) -> dict:
    """{item: i for i, item in enumerate(items)}."""
    raise NotImplementedError


def numbered_pairs(items: list[str]) -> list[tuple]:
    """list(enumerate(items))."""
    raise NotImplementedError


def pair_and_dict(keys: list[str], values: list) -> dict:
    """dict(zip(keys, values))."""
    raise NotImplementedError


def common_elements(a: set, b: set) -> set:
    """a & b -- intersection."""
    raise NotImplementedError


def unique_to_first(a: set, b: set) -> set:
    """a - b -- difference."""
    raise NotImplementedError


def all_elements(a: set, b: set) -> set:
    """a | b -- union."""
    raise NotImplementedError
''',
        "reference": '''\
def word_lengths(words: list[str]) -> dict:
    return {w: len(w) for w in words}


def index_lookup(items: list[str]) -> dict:
    return {item: i for i, item in enumerate(items)}


def numbered_pairs(items: list[str]) -> list[tuple]:
    return list(enumerate(items))


def pair_and_dict(keys: list[str], values: list) -> dict:
    return dict(zip(keys, values))


def common_elements(a: set, b: set) -> set:
    return a & b


def unique_to_first(a: set, b: set) -> set:
    return a - b


def all_elements(a: set, b: set) -> set:
    return a | b
''',
        "test": '''\
from exercises.week04.exercise02.solution import (
    word_lengths,
    index_lookup,
    numbered_pairs,
    pair_and_dict,
    common_elements,
    unique_to_first,
    all_elements,
)


def test_word_lengths():
    assert word_lengths(["a", "bb"]) == {"a": 1, "bb": 2}


def test_index_lookup():
    assert index_lookup(["a", "b"]) == {"a": 0, "b": 1}


def test_numbered_pairs():
    assert numbered_pairs(["a", "b"]) == [(0, "a"), (1, "b")]


def test_pair_and_dict():
    assert pair_and_dict(["x", "y"], [1, 2]) == {"x": 1, "y": 2}


def test_common_elements():
    assert common_elements({1, 2, 3}, {2, 3, 4}) == {2, 3}


def test_unique_to_first():
    assert unique_to_first({1, 2, 3}, {2, 3, 4}) == {1}


def test_all_elements():
    assert all_elements({1, 2}, {2, 3}) == {1, 2, 3}
''',
    },
    {
        "name": "exercise03",
        "title": "Comprehensions",
        "summary": "list comprehension x3 (incl. filtering and nesting)",
        "readme": (
            "Implement:\n\n"
            "- `squares(n: int) -> list[int]` -- `[x ** 2 for x in range(n)]`.\n"
            "- `evens_squared_dict(n: int) -> dict` -- "
            "`{x: x ** 2 for x in range(n) if x % 2 == 0}` (a dict comprehension "
            "with an `if` filter).\n"
            "- `flatten(matrix: list[list[int]]) -> list[int]` -- a **nested** "
            "list comprehension: `[x for row in matrix for x in row]` (flattens "
            "a list of lists into one list, left-to-right, top-to-bottom).\n\n"
            "See the Study Reference presentation, Topic 4, for the theory."
        ),
        "stub": '''\
def squares(n: int) -> list[int]:
    """[x ** 2 for x in range(n)]."""
    raise NotImplementedError


def evens_squared_dict(n: int) -> dict:
    """{x: x ** 2 for x in range(n) if x % 2 == 0}."""
    raise NotImplementedError


def flatten(matrix: list[list[int]]) -> list[int]:
    """Nested comprehension: [x for row in matrix for x in row]."""
    raise NotImplementedError
''',
        "reference": '''\
def squares(n: int) -> list[int]:
    return [x ** 2 for x in range(n)]


def evens_squared_dict(n: int) -> dict:
    return {x: x ** 2 for x in range(n) if x % 2 == 0}


def flatten(matrix: list[list[int]]) -> list[int]:
    return [x for row in matrix for x in row]
''',
        "test": '''\
from exercises.week04.exercise03.solution import squares, evens_squared_dict, flatten


def test_squares():
    assert squares(5) == [0, 1, 4, 9, 16]


def test_evens_squared_dict():
    assert evens_squared_dict(6) == {0: 0, 2: 4, 4: 16}


def test_flatten():
    assert flatten([[1, 2], [3, 4], [5]]) == [1, 2, 3, 4, 5]
''',
    },
    {
        "name": "exercise04",
        "title": "Collections Toolbox",
        "summary": "collections.defaultdict() x1, Counter() x2, deque() x2",
        "readme": (
            "Implement:\n\n"
            "- `group_by_first_letter(words: list[str]) -> dict` -- use "
            "`collections.defaultdict(list)` to bucket each word under its "
            "first letter (`.append()` each word to its bucket); return "
            "`dict(sorted(groups.items()))` so the result is a plain dict "
            "with sorted keys.\n"
            "- `count_occurrences(items: list) -> dict` -- "
            "`dict(collections.Counter(items))`.\n"
            "- `most_common_n(items: list, n: int) -> list[tuple]` -- "
            "`collections.Counter(items).most_common(n)`.\n"
            "- `sliding_window_last_n(numbers: list[int], maxlen: int) -> list[int]` "
            "-- push every number, one at a time, onto a `collections.deque(maxlen=maxlen)` "
            "(via `.append()`); once it's full, older items fall off the left "
            "automatically. Return `list(the_deque)` at the end.\n"
            "- `rotate_queue(items: list, k: int) -> list` -- build a "
            "`collections.deque(items)`, call `.rotate(k)`, return `list(the_deque)`.\n\n"
            "See the Study Reference presentation, Topic 4, for the theory."
        ),
        "stub": '''\
import collections


def group_by_first_letter(words: list[str]) -> dict:
    """Bucket words by first letter using collections.defaultdict(list)."""
    raise NotImplementedError


def count_occurrences(items: list) -> dict:
    """dict(collections.Counter(items))."""
    raise NotImplementedError


def most_common_n(items: list, n: int) -> list:
    """collections.Counter(items).most_common(n)."""
    raise NotImplementedError


def sliding_window_last_n(numbers: list[int], maxlen: int) -> list[int]:
    """Push each number onto a collections.deque(maxlen=maxlen); return list(it)."""
    raise NotImplementedError


def rotate_queue(items: list, k: int) -> list:
    """collections.deque(items), .rotate(k), then list(it)."""
    raise NotImplementedError
''',
        "reference": '''\
import collections


def group_by_first_letter(words: list[str]) -> dict:
    groups = collections.defaultdict(list)
    for word in words:
        groups[word[0]].append(word)
    return dict(sorted(groups.items()))


def count_occurrences(items: list) -> dict:
    return dict(collections.Counter(items))


def most_common_n(items: list, n: int) -> list:
    return collections.Counter(items).most_common(n)


def sliding_window_last_n(numbers: list[int], maxlen: int) -> list[int]:
    window = collections.deque(maxlen=maxlen)
    for n in numbers:
        window.append(n)
    return list(window)


def rotate_queue(items: list, k: int) -> list:
    d = collections.deque(items)
    d.rotate(k)
    return list(d)
''',
        "test": '''\
from exercises.week04.exercise04.solution import (
    group_by_first_letter,
    count_occurrences,
    most_common_n,
    sliding_window_last_n,
    rotate_queue,
)


def test_group_by_first_letter():
    result = group_by_first_letter(["apple", "avocado", "banana", "cherry"])
    assert result == {"a": ["apple", "avocado"], "b": ["banana"], "c": ["cherry"]}


def test_count_occurrences():
    assert count_occurrences(["a", "b", "a", "c", "a"]) == {"a": 3, "b": 1, "c": 1}


def test_most_common_n():
    assert most_common_n(["a", "b", "a", "c", "a", "b"], 2) == [("a", 3), ("b", 2)]


def test_sliding_window_last_n():
    assert sliding_window_last_n([1, 2, 3, 4, 5], 3) == [3, 4, 5]


def test_rotate_queue():
    assert rotate_queue([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
''',
    },
    {
        "name": "exercise05",
        "title": "Dataclasses",
        "summary": "dataclasses module/@dataclass x3, __eq__/__hash__ via dataclass mechanics",
        "readme": (
            "Implement one method on each of three dataclasses (the "
            "`@dataclasses.dataclass` decorators and fields are already there "
            "for you -- see how each one changes what `__eq__`/`__hash__` the "
            "class gets for free):\n\n"
            "- `Point` (plain `@dataclasses.dataclass`, so `eq=True`, "
            "`frozen=False` by default) -- implement "
            "`distance_from_origin(self) -> float` as "
            "`(self.x ** 2 + self.y ** 2) ** 0.5`. Because `eq=True` and "
            "`frozen=False`, dataclass sets `Point.__hash__ = None` "
            "automatically -- `Point` instances get a real `__eq__` but are "
            "**not hashable** (`hash(Point(1, 2))` raises `TypeError`).\n"
            "- `FrozenPoint` (`@dataclasses.dataclass(frozen=True)`) -- same "
            "`distance_from_origin`. Because it's frozen, dataclass generates "
            "**both** `__eq__` *and* `__hash__` from the fields -- these "
            "instances work fine in a `set` or as dict keys.\n"
            "- `TaggedItem` (fields `name: str` and "
            "`tags: list = dataclasses.field(default_factory=list)`) -- "
            "implement `add_tag(self, tag: str) -> None` as "
            "`self.tags.append(tag)`. `default_factory=list` is what stops "
            "every `TaggedItem` from sharing the *same* mutable list -- the "
            "mutable-default-argument bug (Topic 3) applied to dataclass "
            "fields.\n\n"
            "See the Study Reference presentation, Topic 4, for the theory."
        ),
        "stub": '''\
import dataclasses


@dataclasses.dataclass
class Point:
    x: int
    y: int

    def distance_from_origin(self) -> float:
        """(x**2 + y**2) ** 0.5."""
        raise NotImplementedError


@dataclasses.dataclass(frozen=True)
class FrozenPoint:
    x: int
    y: int

    def distance_from_origin(self) -> float:
        """(x**2 + y**2) ** 0.5."""
        raise NotImplementedError


@dataclasses.dataclass
class TaggedItem:
    name: str
    tags: list = dataclasses.field(default_factory=list)

    def add_tag(self, tag: str) -> None:
        """self.tags.append(tag)."""
        raise NotImplementedError
''',
        "reference": '''\
import dataclasses


@dataclasses.dataclass
class Point:
    x: int
    y: int

    def distance_from_origin(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5


@dataclasses.dataclass(frozen=True)
class FrozenPoint:
    x: int
    y: int

    def distance_from_origin(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5


@dataclasses.dataclass
class TaggedItem:
    name: str
    tags: list = dataclasses.field(default_factory=list)

    def add_tag(self, tag: str) -> None:
        self.tags.append(tag)
''',
        "test": '''\
import pytest
from exercises.week04.exercise05.solution import Point, FrozenPoint, TaggedItem


def test_point_distance_and_eq():
    assert Point(3, 4).distance_from_origin() == 5.0
    assert Point(1, 2) == Point(1, 2)


def test_point_is_not_hashable():
    with pytest.raises(TypeError):
        hash(Point(1, 2))


def test_frozen_point_distance_and_eq():
    assert FrozenPoint(3, 4).distance_from_origin() == 5.0
    assert FrozenPoint(1, 2) == FrozenPoint(1, 2)


def test_frozen_point_is_hashable():
    points = {FrozenPoint(1, 2), FrozenPoint(1, 2), FrozenPoint(3, 4)}
    assert len(points) == 2


def test_tagged_item_add_tag():
    item = TaggedItem("shirt")
    item.add_tag("clothing")
    assert item.tags == ["clothing"]


def test_tagged_item_default_factory_is_independent_per_instance():
    item1 = TaggedItem("shirt")
    item2 = TaggedItem("shoe")
    item1.add_tag("clothing")
    assert item2.tags == []
''',
    },
    {
        "name": "exercise06",
        "title": "Records and Hashability",
        "summary": "collections.namedtuple, hand-written __eq__/__hash__, hashability",
        "readme": (
            "Implement:\n\n"
            "- `make_coordinate(x: int, y: int)` -- return `Coordinate(x, y)` "
            "(`Coordinate` is already defined above via "
            "`collections.namedtuple(\"Coordinate\", [\"x\", \"y\"])` -- a "
            "lightweight, immutable, hashable record with no class boilerplate).\n"
            "- `SimpleFraction.__init__(self, numerator: int, denominator: int)` "
            "-- raise `ZeroDivisionError` if `denominator == 0`; otherwise, if "
            "`denominator < 0`, flip the sign of both (`numerator, denominator = "
            "-numerator, -denominator`); then reduce both by their "
            "`math.gcd(numerator, denominator)` and store the results.\n"
            "- `SimpleFraction.__eq__(self, other) -> bool` -- `True` if `other` "
            "is a `SimpleFraction` with the same (already-reduced) `numerator` "
            "and `denominator`.\n"
            "- `SimpleFraction.__hash__(self) -> int` -- "
            "`hash((self.numerator, self.denominator))`. **This is required**: "
            "Python removes the default `__hash__` from any class that defines "
            "`__eq__` without also defining `__hash__` -- skip this and "
            "`SimpleFraction` instances become unhashable, breaking `set()`/"
            "dict-key use, even though `==` still works fine.\n"
            "- `dedupe_preserving_order(items: list) -> list` -- "
            "`list(dict.fromkeys(items))`. `dict.fromkeys` de-duplicates using "
            "each item's `__hash__`/`__eq__` while a plain dict's "
            "insertion-ordering keeps first-seen order -- this only works "
            "because `SimpleFraction`/`Coordinate`/`FrozenPoint` are all "
            "hashable.\n\n"
            "See the Study Reference presentation, Topic 4, for the theory."
        ),
        "stub": '''\
import collections
import math

Coordinate = collections.namedtuple("Coordinate", ["x", "y"])


def make_coordinate(x: int, y: int):
    """Return Coordinate(x, y)."""
    raise NotImplementedError


class SimpleFraction:
    def __init__(self, numerator: int, denominator: int):
        """Reduce to lowest terms via math.gcd; raise ZeroDivisionError if denominator == 0."""
        raise NotImplementedError

    def __eq__(self, other) -> bool:
        """True if other is a SimpleFraction with the same reduced numerator/denominator."""
        raise NotImplementedError

    def __hash__(self) -> int:
        """hash((self.numerator, self.denominator)) -- required alongside __eq__."""
        raise NotImplementedError


def dedupe_preserving_order(items: list) -> list:
    """Remove duplicates, preserving first-seen order: list(dict.fromkeys(items))."""
    raise NotImplementedError
''',
        "reference": '''\
import collections
import math

Coordinate = collections.namedtuple("Coordinate", ["x", "y"])


def make_coordinate(x: int, y: int):
    return Coordinate(x, y)


class SimpleFraction:
    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ZeroDivisionError("denominator cannot be 0")
        if denominator < 0:
            numerator, denominator = -numerator, -denominator
        g = math.gcd(numerator, denominator)
        self.numerator = numerator // g
        self.denominator = denominator // g

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, SimpleFraction)
            and self.numerator == other.numerator
            and self.denominator == other.denominator
        )

    def __hash__(self) -> int:
        return hash((self.numerator, self.denominator))


def dedupe_preserving_order(items: list) -> list:
    return list(dict.fromkeys(items))
''',
        "test": '''\
import pytest
from exercises.week04.exercise06.solution import (
    Coordinate,
    make_coordinate,
    SimpleFraction,
    dedupe_preserving_order,
)


def test_make_coordinate():
    c = make_coordinate(1, 2)
    assert c == Coordinate(1, 2)
    assert c.x == 1 and c.y == 2


def test_simple_fraction_reduces():
    assert SimpleFraction(2, 4) == SimpleFraction(1, 2)


def test_simple_fraction_normalizes_negative_denominator():
    assert SimpleFraction(1, -2) == SimpleFraction(-1, 2)


def test_simple_fraction_zero_denominator_raises():
    with pytest.raises(ZeroDivisionError):
        SimpleFraction(1, 0)


def test_simple_fraction_is_hashable():
    fractions = {SimpleFraction(1, 2), SimpleFraction(2, 4), SimpleFraction(1, 3)}
    assert len(fractions) == 2


def test_dedupe_preserving_order_with_hashable_records():
    items = [
        SimpleFraction(1, 2),
        SimpleFraction(2, 4),
        Coordinate(1, 1),
        SimpleFraction(1, 3),
        Coordinate(1, 1),
    ]
    result = dedupe_preserving_order(items)
    assert result == [SimpleFraction(1, 2), Coordinate(1, 1), SimpleFraction(1, 3)]


def test_dedupe_preserving_order_with_plain_values():
    assert dedupe_preserving_order([1, 2, 1, 3, 2]) == [1, 2, 3]
''',
    },
]
