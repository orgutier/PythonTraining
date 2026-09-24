"""
Stage 4 -- Data Structures.

Rolled onto the tier-named exercise convention: a minimum of two exercises
per Basic/Mid/Advanced tier. All exercises here are function-based -- this
stage is about manipulating data with functions, so wrapping the work in
`def`s (and a couple of small classes for the dataclass/hashability
material) is exactly the point.

Coverage plan (every item below is exercised by the trainee's own code,
generally 2+ times across these 6 exercises):

  Basic:    list, tuple, dict, set, append(), sort()/sorted(), len(), zip(),
            enumerate(), list comprehension, dict comprehension
  Mid:      dataclasses.dataclass, __eq__, collections module, dataclasses
            module, namedtuple/dataclass records, set operations
            (union/intersection/difference)
  Advanced: collections.defaultdict(), collections.Counter(),
            collections.deque(), __hash__, hashability
"""

STAGE = "stage04"
TOPIC = "Data Structures"
OVERVIEW = (
    "Six exercises, two per tier. Every one is a small, realistic scenario "
    "combining several of that tier's specific tools at once -- from "
    "building a race-results ledger with tuples/zip/sort, through "
    "dataclass/namedtuple equality and set algebra, to the deque/defaultdict/"
    "Counter toolbox and, finally, exactly why __hash__ matters."
)

EXERCISES = [
    {
        "name": "basic01",
        "title": "Race Results Ledger",
        "summary": "list, tuple, append(), sort()/sorted(), zip(), enumerate(), len()",
        "readme": (
            "A local 5K's raw results arrive as two parallel lists. Given, "
            "don't modify:\n\n"
            "```python\n"
            'raw_names = ["Ava", "Ben", "Cy", "Dee", "Emi"]\n'
            "raw_times = [54.2, 49.8, 61.0, 49.8, 57.3]  # seconds\n"
            "```\n\n"
            "Implement:\n\n"
            "- `build_results(names: list[str], times: list[float]) -> list[tuple]` "
            "-- start with `results = []`, then use a `for` loop over "
            "`zip(names, times)` that `.append()`s each `(name, time)` "
            "**tuple** onto `results` one at a time (don't just return "
            "`list(zip(...))` directly -- the point here is the explicit "
            "loop + `.append()`, not the shortcut).\n"
            "- `rank_by_time(results: list[tuple]) -> list[tuple]` -- "
            "`sorted(results, key=lambda r: r[1])` (fastest time first; "
            "`sorted()` returns a **new** list, it never touches `results`).\n"
            "- `fastest_n(ranked_results: list[tuple], n: int) -> list[tuple]` "
            "-- `ranked_results[:n]`.\n"
            "- `podium_labels(fastest: list[tuple]) -> list[str]` -- "
            '`[f"{i+1}. {name} ({time}s)" for i, (name, time) in '
            "enumerate(fastest)]` (a list comprehension over "
            "`enumerate()`, unpacking each tuple as it goes).\n"
            "- `racer_count(names: list[str]) -> int` -- `len(names)`.\n\n"
            "See the Study Reference presentation, Topic 4 (Basic tier), "
            "for the theory."
        ),
        "stub": '''\
def build_results(names: list[str], times: list[float]) -> list[tuple]:
    """[] then a for-loop over zip(names, times) .append()-ing each (name, time) tuple."""
    raise NotImplementedError


def rank_by_time(results: list[tuple]) -> list[tuple]:
    """sorted(results, key=lambda r: r[1]) -- fastest first, returns a NEW list."""
    raise NotImplementedError


def fastest_n(ranked_results: list[tuple], n: int) -> list[tuple]:
    """ranked_results[:n]."""
    raise NotImplementedError


def podium_labels(fastest: list[tuple]) -> list[str]:
    """[f"{i+1}. {name} ({time}s)" for i, (name, time) in enumerate(fastest)]."""
    raise NotImplementedError


def racer_count(names: list[str]) -> int:
    """len(names)."""
    raise NotImplementedError
''',
        "reference": '''\
def build_results(names: list[str], times: list[float]) -> list[tuple]:
    results = []
    for name, time in zip(names, times):
        results.append((name, time))
    return results


def rank_by_time(results: list[tuple]) -> list[tuple]:
    return sorted(results, key=lambda r: r[1])


def fastest_n(ranked_results: list[tuple], n: int) -> list[tuple]:
    return ranked_results[:n]


def podium_labels(fastest: list[tuple]) -> list[str]:
    return [f"{i+1}. {name} ({time}s)" for i, (name, time) in enumerate(fastest)]


def racer_count(names: list[str]) -> int:
    return len(names)
''',
        "test": '''\
from exercises.stage04.basic01.solution import (
    build_results,
    rank_by_time,
    fastest_n,
    podium_labels,
    racer_count,
)

NAMES = ["Ava", "Ben", "Cy", "Dee", "Emi"]
TIMES = [54.2, 49.8, 61.0, 49.8, 57.3]


def test_build_results_via_append_and_zip():
    """build_results must loop over zip(names, times), .append()-ing (name, time) tuples -- not just wrap zip() in list()."""
    results = build_results(NAMES, TIMES)
    assert results == [("Ava", 54.2), ("Ben", 49.8), ("Cy", 61.0), ("Dee", 49.8), ("Emi", 57.3)]
    assert isinstance(results[0], tuple)


def test_rank_by_time_does_not_mutate_input():
    """rank_by_time uses sorted(), which returns a new list and leaves the original untouched."""
    results = build_results(NAMES, TIMES)
    ranked = rank_by_time(results)
    assert ranked[0] == ("Ben", 49.8)
    assert results[0] == ("Ava", 54.2)


def test_fastest_n_slices_ranked_results():
    """fastest_n(ranked_results, n) == ranked_results[:n]."""
    ranked = rank_by_time(build_results(NAMES, TIMES))
    assert fastest_n(ranked, 3) == [("Ben", 49.8), ("Dee", 49.8), ("Ava", 54.2)]


def test_podium_labels_uses_enumerate_in_a_comprehension():
    """podium_labels builds one f-string label per entry via enumerate() inside a list comprehension."""
    fastest = fastest_n(rank_by_time(build_results(NAMES, TIMES)), 3)
    assert podium_labels(fastest) == ["1. Ben (49.8s)", "2. Dee (49.8s)", "3. Ava (54.2s)"]


def test_racer_count():
    """racer_count == len(names)."""
    assert racer_count(NAMES) == 5
''',
    },
    {
        "name": "basic02",
        "title": "Inventory Category Summary",
        "summary": "dict, set, dict comprehension, list comprehension, zip(), len()",
        "readme": (
            "A store's product catalog arrives as two parallel lists. "
            "Given, don't modify:\n\n"
            "```python\n"
            'product_names = ["Widget", "Gadget", "Gizmo", "Widget", "Sprocket"]\n'
            'product_categories = ["tools", "electronics", "electronics", "tools", "tools"]\n'
            "```\n\n"
            "Implement:\n\n"
            "- `category_by_product(names: list[str], categories: list[str]) -> dict` "
            "-- `{name: cat for name, cat in zip(names, categories)}` (a "
            "**dict comprehension**). Since `\"Widget\"` appears twice in the "
            "data, the resulting dict has only one `\"Widget\"` key -- later "
            "entries silently overwrite earlier ones with the same key, which "
            "is exactly what a real dict does.\n"
            "- `unique_categories(categories: list[str]) -> set` -- "
            "`set(categories)`.\n"
            "- `products_in_category(names: list[str], categories: list[str], "
            "target: str) -> list[str]` -- "
            "`[name for name, cat in zip(names, categories) if cat == target]` "
            "(a **list comprehension** with an `if` filter). Compare its "
            "result for `\"tools\"` against `category_by_product`'s: the list "
            "comprehension keeps **every** match (so `\"Widget\"` appears "
            "twice), while the dict comprehension above collapsed the "
            "duplicate -- same source data, two different container "
            "semantics.\n"
            "- `category_counts(categories: list[str]) -> dict` -- "
            "`{cat: categories.count(cat) for cat in set(categories)}` "
            "(another dict comprehension, this time over a `set` to avoid "
            "counting each category more than once).\n"
            "- `product_count(names: list[str]) -> int` -- `len(names)`.\n\n"
            "See the Study Reference presentation, Topic 4 (Basic tier), "
            "for the theory."
        ),
        "stub": '''\
def category_by_product(names: list[str], categories: list[str]) -> dict:
    """{name: cat for name, cat in zip(names, categories)} -- a dict comprehension."""
    raise NotImplementedError


def unique_categories(categories: list[str]) -> set:
    """set(categories)."""
    raise NotImplementedError


def products_in_category(names: list[str], categories: list[str], target: str) -> list[str]:
    """[name for name, cat in zip(names, categories) if cat == target] -- a filtered list comprehension."""
    raise NotImplementedError


def category_counts(categories: list[str]) -> dict:
    """{cat: categories.count(cat) for cat in set(categories)}."""
    raise NotImplementedError


def product_count(names: list[str]) -> int:
    """len(names)."""
    raise NotImplementedError
''',
        "reference": '''\
def category_by_product(names: list[str], categories: list[str]) -> dict:
    return {name: cat for name, cat in zip(names, categories)}


def unique_categories(categories: list[str]) -> set:
    return set(categories)


def products_in_category(names: list[str], categories: list[str], target: str) -> list[str]:
    return [name for name, cat in zip(names, categories) if cat == target]


def category_counts(categories: list[str]) -> dict:
    return {cat: categories.count(cat) for cat in set(categories)}


def product_count(names: list[str]) -> int:
    return len(names)
''',
        "test": '''\
from exercises.stage04.basic02.solution import (
    category_by_product,
    unique_categories,
    products_in_category,
    category_counts,
    product_count,
)

NAMES = ["Widget", "Gadget", "Gizmo", "Widget", "Sprocket"]
CATEGORIES = ["tools", "electronics", "electronics", "tools", "tools"]


def test_category_by_product_dict_comprehension_collapses_duplicate_key():
    """category_by_product is a dict comprehension -- the second "Widget" entry silently overwrites the first."""
    result = category_by_product(NAMES, CATEGORIES)
    assert result == {"Widget": "tools", "Gadget": "electronics", "Gizmo": "electronics", "Sprocket": "tools"}
    assert len(result) == 4


def test_unique_categories():
    """unique_categories == set(categories)."""
    assert unique_categories(CATEGORIES) == {"tools", "electronics"}


def test_products_in_category_list_comprehension_keeps_all_matches():
    """products_in_category is a filtered list comprehension -- unlike the dict version, both "Widget" entries survive."""
    result = products_in_category(NAMES, CATEGORIES, "tools")
    assert result == ["Widget", "Widget", "Sprocket"]


def test_category_counts():
    """category_counts is a dict comprehension over set(categories), counting each category via .count()."""
    assert category_counts(CATEGORIES) == {"tools": 3, "electronics": 2}


def test_product_count():
    """product_count == len(names)."""
    assert product_count(NAMES) == 5
''',
    },
    {
        "name": "mid01",
        "title": "Player Records: Dataclass vs. namedtuple",
        "summary": "dataclasses.dataclass, __eq__, collections module (namedtuple), dataclasses module, records",
        "readme": (
            "Two ways to model the same lightweight record: a mutable "
            "`@dataclasses.dataclass` and an immutable `collections.namedtuple`. "
            "Both are already defined for you:\n\n"
            "```python\n"
            "@dataclasses.dataclass\n"
            "class Player:\n"
            "    name: str\n"
            "    position: str\n\n"
            'PlayerRecord = collections.namedtuple("PlayerRecord", ["name", "position"])\n'
            "```\n\n"
            "Implement:\n\n"
            "- `convert_to_record(player: Player) -> PlayerRecord` -- "
            "`PlayerRecord(player.name, player.position)`.\n"
            "- `players_are_equal(a: Player, b: Player) -> bool` -- "
            "`a == b`. `@dataclasses.dataclass` auto-generates `__eq__` from "
            "the fields, so two **different** `Player` objects with the same "
            "`name`/`position` compare equal, even though `a is b` is "
            "`False`.\n"
            "- `records_are_equal(a: PlayerRecord, b: PlayerRecord) -> bool` "
            "-- `a == b`. `namedtuple` gets field-based equality for free "
            "too, inherited from being a plain `tuple` subclass -- no "
            "`@dataclass` decorator needed here at all.\n\n"
            "The point of putting these side by side: both "
            "`@dataclasses.dataclass` and `collections.namedtuple` are ways "
            "to define a record type without hand-writing `__init__`/"
            "`__repr__`/`__eq__` yourself, from two different standard-"
            "library modules (`dataclasses` and `collections`).\n\n"
            "See the Study Reference presentation, Topic 4 (Mid tier), for "
            "the theory."
        ),
        "stub": '''\
import collections
import dataclasses


@dataclasses.dataclass
class Player:
    name: str
    position: str


PlayerRecord = collections.namedtuple("PlayerRecord", ["name", "position"])


def convert_to_record(player: Player) -> PlayerRecord:
    """PlayerRecord(player.name, player.position)."""
    raise NotImplementedError


def players_are_equal(a: Player, b: Player) -> bool:
    """a == b -- relies on @dataclasses.dataclass's auto-generated __eq__ (field-based, not identity)."""
    raise NotImplementedError


def records_are_equal(a: PlayerRecord, b: PlayerRecord) -> bool:
    """a == b -- namedtuple's field-based equality, inherited from tuple."""
    raise NotImplementedError
''',
        "reference": '''\
import collections
import dataclasses


@dataclasses.dataclass
class Player:
    name: str
    position: str


PlayerRecord = collections.namedtuple("PlayerRecord", ["name", "position"])


def convert_to_record(player: Player) -> PlayerRecord:
    return PlayerRecord(player.name, player.position)


def players_are_equal(a: Player, b: Player) -> bool:
    return a == b


def records_are_equal(a: PlayerRecord, b: PlayerRecord) -> bool:
    return a == b
''',
        "test": '''\
from exercises.stage04.mid01.solution import (
    Player,
    PlayerRecord,
    convert_to_record,
    players_are_equal,
    records_are_equal,
)


def test_convert_to_record():
    """convert_to_record(player) == PlayerRecord(player.name, player.position)."""
    record = convert_to_record(Player("Ava", "guard"))
    assert record == PlayerRecord("Ava", "guard")


def test_players_are_equal_uses_dataclass_generated_eq_not_identity():
    """@dataclasses.dataclass generates __eq__ from fields -- two distinct objects with equal fields compare equal."""
    a = Player("Ava", "guard")
    b = Player("Ava", "guard")
    assert a is not b
    assert players_are_equal(a, b) is True


def test_players_are_equal_false_for_different_fields():
    """players_are_equal must actually compare fields, not always return True."""
    assert players_are_equal(Player("Ava", "guard"), Player("Ben", "forward")) is False


def test_records_are_equal_uses_namedtuple_field_equality():
    """namedtuple equality is field-based (inherited from tuple), with no @dataclass decorator involved."""
    a = PlayerRecord("Ava", "guard")
    b = PlayerRecord("Ava", "guard")
    assert records_are_equal(a, b) is True
    assert records_are_equal(a, PlayerRecord("Ben", "forward")) is False
''',
    },
    {
        "name": "mid02",
        "title": "League Membership Analyzer",
        "summary": "set operations: union, intersection, difference",
        "readme": (
            "Two conferences' rosters, as sets of player names. Given, "
            "don't modify:\n\n"
            "```python\n"
            'east_team_names = {"Ava", "Ben", "Cy", "Dee"}\n'
            'west_team_names = {"Cy", "Dee", "Emi", "Finn"}\n'
            "```\n\n"
            "Implement:\n\n"
            "- `both_conferences(east: set, west: set) -> set` -- `east & "
            "west` (**intersection**: players rostered on both sides -- a "
            "trade mid-season, or a data error worth flagging).\n"
            "- `all_players(east: set, west: set) -> set` -- `east | west` "
            "(**union**: every player across both rosters).\n"
            "- `east_only(east: set, west: set) -> set` -- `east - west` "
            "(**difference**: on the East roster and nowhere else).\n"
            "- `west_only(east: set, west: set) -> set` -- `west - east` "
            "(the same **difference** operator, the other direction -- note "
            "it is not symmetric: `east - west != west - east` in general).\n"
            "- `symmetric_difference_manual(east: set, west: set) -> set` -- "
            "build it by hand from the three operators above: "
            "`(east - west) | (west - east)` (players on exactly one "
            "roster, not both). This should come out identical to Python's "
            "built-in `east ^ west` -- the exercise is proving that to "
            "yourself by composing union+difference, not reaching for `^` "
            "directly.\n\n"
            "See the Study Reference presentation, Topic 4 (Mid tier), for "
            "the theory."
        ),
        "stub": '''\
def both_conferences(east: set, west: set) -> set:
    """east & west -- intersection."""
    raise NotImplementedError


def all_players(east: set, west: set) -> set:
    """east | west -- union."""
    raise NotImplementedError


def east_only(east: set, west: set) -> set:
    """east - west -- difference."""
    raise NotImplementedError


def west_only(east: set, west: set) -> set:
    """west - east -- difference, other direction."""
    raise NotImplementedError


def symmetric_difference_manual(east: set, west: set) -> set:
    """(east - west) | (west - east) -- built from difference + union, not the `^` operator."""
    raise NotImplementedError
''',
        "reference": '''\
def both_conferences(east: set, west: set) -> set:
    return east & west


def all_players(east: set, west: set) -> set:
    return east | west


def east_only(east: set, west: set) -> set:
    return east - west


def west_only(east: set, west: set) -> set:
    return west - east


def symmetric_difference_manual(east: set, west: set) -> set:
    return (east - west) | (west - east)
''',
        "test": '''\
from exercises.stage04.mid02.solution import (
    both_conferences,
    all_players,
    east_only,
    west_only,
    symmetric_difference_manual,
)

EAST = {"Ava", "Ben", "Cy", "Dee"}
WEST = {"Cy", "Dee", "Emi", "Finn"}


def test_both_conferences_intersection():
    """both_conferences == east & west."""
    assert both_conferences(EAST, WEST) == {"Cy", "Dee"}


def test_all_players_union():
    """all_players == east | west."""
    assert all_players(EAST, WEST) == {"Ava", "Ben", "Cy", "Dee", "Emi", "Finn"}


def test_east_only_difference():
    """east_only == east - west."""
    assert east_only(EAST, WEST) == {"Ava", "Ben"}


def test_west_only_difference_is_not_symmetric_with_east_only():
    """west_only == west - east, which differs from east - west -- difference is directional."""
    assert west_only(EAST, WEST) == {"Emi", "Finn"}
    assert west_only(EAST, WEST) != east_only(EAST, WEST)


def test_symmetric_difference_manual_matches_builtin_xor():
    """symmetric_difference_manual, built from (east - west) | (west - east), must equal Python's east ^ west."""
    result = symmetric_difference_manual(EAST, WEST)
    assert result == {"Ava", "Ben", "Emi", "Finn"}
    assert result == (EAST ^ WEST)
''',
    },
    {
        "name": "advanced01",
        "title": "Log Aggregator",
        "summary": "collections.defaultdict(), collections.Counter() x2, collections.deque() x2",
        "readme": (
            "Raw log lines from a service, each shaped `\"LEVEL:tag\"`. "
            "Given, don't modify:\n\n"
            "```python\n"
            "log_entries = [\n"
            '    "ERROR:disk", "INFO:boot", "ERROR:disk", "WARN:mem",\n'
            '    "ERROR:net", "INFO:boot", "ERROR:disk",\n'
            "]\n"
            "```\n\n"
            "Implement:\n\n"
            "- `entries_by_level(entries: list[str]) -> dict` -- bucket "
            "whole entries by their `LEVEL` prefix (`entry.split(\":\")[0]`) "
            "using a `collections.defaultdict(list)` (`.append()` each entry "
            "onto `groups[level]`); return `dict(sorted(groups.items()))` "
            "so the result is a plain dict with sorted keys.\n"
            "- `level_counts(entries: list[str]) -> dict` -- extract each "
            "entry's level, then `dict(collections.Counter(levels))`.\n"
            "- `most_common_level(entries: list[str]) -> tuple` -- "
            "`collections.Counter(levels).most_common(1)[0]` (a "
            "`(level, count)` tuple for the single most frequent level).\n"
            "- `last_n_entries(entries: list[str], n: int) -> list[str]` -- "
            "push every entry, one at a time, onto a "
            "`collections.deque(maxlen=n)` (via `.append()`); once it's "
            "full, older items automatically fall off the left. Return "
            "`list(the_deque)`.\n"
            "- `rotate_entries(entries: list[str], k: int) -> list[str]` -- "
            "build a `collections.deque(entries)`, call `.rotate(k)`, "
            "return `list(the_deque)`.\n\n"
            "See the Study Reference presentation, Topic 4 (Advanced tier), "
            "for the theory."
        ),
        "stub": '''\
import collections


def entries_by_level(entries: list[str]) -> dict:
    """Bucket entries by their LEVEL prefix using collections.defaultdict(list); return dict(sorted(...))."""
    raise NotImplementedError


def level_counts(entries: list[str]) -> dict:
    """dict(collections.Counter(levels)) -- levels extracted from each entry's prefix."""
    raise NotImplementedError


def most_common_level(entries: list[str]) -> tuple:
    """collections.Counter(levels).most_common(1)[0]."""
    raise NotImplementedError


def last_n_entries(entries: list[str], n: int) -> list[str]:
    """Push each entry onto a collections.deque(maxlen=n); return list(it)."""
    raise NotImplementedError


def rotate_entries(entries: list[str], k: int) -> list[str]:
    """collections.deque(entries), .rotate(k), then list(it)."""
    raise NotImplementedError
''',
        "reference": '''\
import collections


def entries_by_level(entries: list[str]) -> dict:
    groups = collections.defaultdict(list)
    for entry in entries:
        level = entry.split(":")[0]
        groups[level].append(entry)
    return dict(sorted(groups.items()))


def level_counts(entries: list[str]) -> dict:
    levels = [entry.split(":")[0] for entry in entries]
    return dict(collections.Counter(levels))


def most_common_level(entries: list[str]) -> tuple:
    levels = [entry.split(":")[0] for entry in entries]
    return collections.Counter(levels).most_common(1)[0]


def last_n_entries(entries: list[str], n: int) -> list[str]:
    window = collections.deque(maxlen=n)
    for entry in entries:
        window.append(entry)
    return list(window)


def rotate_entries(entries: list[str], k: int) -> list[str]:
    d = collections.deque(entries)
    d.rotate(k)
    return list(d)
''',
        "test": '''\
from exercises.stage04.advanced01.solution import (
    entries_by_level,
    level_counts,
    most_common_level,
    last_n_entries,
    rotate_entries,
)

ENTRIES = ["ERROR:disk", "INFO:boot", "ERROR:disk", "WARN:mem", "ERROR:net", "INFO:boot", "ERROR:disk"]


def test_entries_by_level_uses_defaultdict():
    """entries_by_level buckets whole entries under their LEVEL prefix via collections.defaultdict(list)."""
    result = entries_by_level(ENTRIES)
    assert result == {
        "ERROR": ["ERROR:disk", "ERROR:disk", "ERROR:net", "ERROR:disk"],
        "INFO": ["INFO:boot", "INFO:boot"],
        "WARN": ["WARN:mem"],
    }


def test_level_counts_uses_counter():
    """level_counts == dict(collections.Counter(levels))."""
    assert level_counts(ENTRIES) == {"ERROR": 4, "INFO": 2, "WARN": 1}


def test_most_common_level_uses_counter_most_common():
    """most_common_level == collections.Counter(levels).most_common(1)[0]."""
    assert most_common_level(ENTRIES) == ("ERROR", 4)


def test_last_n_entries_uses_bounded_deque():
    """last_n_entries pushes onto a collections.deque(maxlen=n), keeping only the most recent n."""
    assert last_n_entries(ENTRIES, 3) == ["ERROR:net", "INFO:boot", "ERROR:disk"]


def test_rotate_entries_uses_deque_rotate():
    """rotate_entries builds a collections.deque(entries) and calls .rotate(k)."""
    assert rotate_entries(ENTRIES, 2) == [
        "INFO:boot", "ERROR:disk", "ERROR:disk", "INFO:boot", "ERROR:disk", "WARN:mem", "ERROR:net",
    ]
''',
    },
    {
        "name": "advanced02",
        "title": "Hashable Records: Frozen Dataclasses and Manual __hash__",
        "summary": "__hash__, hashability -- automatic (frozen dataclass) and manual (__eq__ + __hash__ pair)",
        "readme": (
            "Two ways a class can become hashable -- automatically, and by "
            "hand -- and why it matters. `Point`, `FrozenPoint`, and "
            "`SimpleFraction`'s `__init__` are already defined for you.\n\n"
            "- `Point.distance_from_origin(self) -> float` and "
            "`FrozenPoint.distance_from_origin(self) -> float` -- both "
            "`(self.x ** 2 + self.y ** 2) ** 0.5`. `Point` is a plain "
            "`@dataclasses.dataclass` (`eq=True`, `frozen=False` by "
            "default) -- dataclass therefore sets `Point.__hash__ = None` "
            "automatically, so `hash(Point(1, 2))` raises `TypeError`: "
            "**mutable objects that support `==` are unsafe to hash**, "
            "since mutating one after it's in a set/dict would silently "
            "corrupt that container. `FrozenPoint` is "
            "`@dataclasses.dataclass(frozen=True)`, so dataclass generates "
            "**both** `__eq__` *and* a working `__hash__` from the fields, "
            "and instances work fine in a `set`.\n"
            "- `SimpleFraction.__eq__(self, other) -> bool` -- `True` if "
            "`other` is a `SimpleFraction` with the same (already-reduced, "
            "by the given `__init__`) `numerator` and `denominator`.\n"
            "- `SimpleFraction.__hash__(self) -> int` -- "
            "`hash((self.numerator, self.denominator))`. This one you have "
            "to write **by hand**: `SimpleFraction` isn't a dataclass, so "
            "nothing generates `__hash__` for it automatically. Python "
            "actively **removes** the default (identity-based) `__hash__` "
            "from any plain class that defines `__eq__` without also "
            "defining `__hash__` -- skip this method and every "
            "`SimpleFraction` becomes unhashable, even though `==` still "
            "works.\n"
            "- `dedupe_preserving_order(items: list) -> list` -- "
            "`list(dict.fromkeys(items))`. `dict.fromkeys` de-duplicates "
            "using each item's `__hash__`/`__eq__` while keeping first-seen "
            "order -- this only works at all because `SimpleFraction` and "
            "`FrozenPoint` are both hashable.\n\n"
            "See the Study Reference presentation, Topic 4 (Advanced tier), "
            "for the theory."
        ),
        "stub": '''\
import dataclasses
import math


@dataclasses.dataclass
class Point:
    x: int
    y: int

    def distance_from_origin(self) -> float:
        """(x**2 + y**2) ** 0.5. Point is NOT hashable (mutable + eq=True -> __hash__ is None)."""
        raise NotImplementedError


@dataclasses.dataclass(frozen=True)
class FrozenPoint:
    x: int
    y: int

    def distance_from_origin(self) -> float:
        """(x**2 + y**2) ** 0.5. frozen=True gives FrozenPoint a working, auto-generated __hash__."""
        raise NotImplementedError


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
        """True if other is a SimpleFraction with the same reduced numerator/denominator."""
        raise NotImplementedError

    def __hash__(self) -> int:
        """hash((self.numerator, self.denominator)) -- must be written BY HAND; nothing generates it for a plain class."""
        raise NotImplementedError


def dedupe_preserving_order(items: list) -> list:
    """Remove duplicates, preserving first-seen order: list(dict.fromkeys(items))."""
    raise NotImplementedError
''',
        "reference": '''\
import dataclasses
import math


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
from exercises.stage04.advanced02.solution import (
    Point,
    FrozenPoint,
    SimpleFraction,
    dedupe_preserving_order,
)


def test_point_distance():
    """Point.distance_from_origin() == (x**2 + y**2) ** 0.5."""
    assert Point(3, 4).distance_from_origin() == 5.0


def test_point_is_not_hashable():
    """Point is a plain (mutable) dataclass with eq=True -- dataclass sets __hash__ = None, so hash() must raise TypeError."""
    with pytest.raises(TypeError):
        hash(Point(1, 2))


def test_frozen_point_distance_and_is_hashable():
    """FrozenPoint.distance_from_origin() works, and frozen=True gives it a working auto-generated __hash__."""
    assert FrozenPoint(3, 4).distance_from_origin() == 5.0
    points = {FrozenPoint(1, 2), FrozenPoint(1, 2), FrozenPoint(3, 4)}
    assert len(points) == 2


def test_simple_fraction_eq_compares_reduced_values():
    """SimpleFraction.__eq__ must compare reduced numerator/denominator, not object identity."""
    assert SimpleFraction(2, 4) == SimpleFraction(1, 2)
    assert SimpleFraction(1, 2) != SimpleFraction(1, 3)


def test_simple_fraction_is_hashable_via_hand_written_hash():
    """SimpleFraction.__hash__ must be written by hand (hash((numerator, denominator))) -- without it, defining __eq__ alone makes it unhashable."""
    fractions = {SimpleFraction(1, 2), SimpleFraction(2, 4), SimpleFraction(1, 3)}
    assert len(fractions) == 2


def test_dedupe_preserving_order_relies_on_hashability():
    """dedupe_preserving_order (dict.fromkeys) only works because SimpleFraction/FrozenPoint are both hashable."""
    items = [
        SimpleFraction(1, 2),
        SimpleFraction(2, 4),
        FrozenPoint(1, 1),
        SimpleFraction(1, 3),
        FrozenPoint(1, 1),
    ]
    result = dedupe_preserving_order(items)
    assert result == [SimpleFraction(1, 2), FrozenPoint(1, 1), SimpleFraction(1, 3)]
    assert len(result) == 3


def test_dedupe_preserving_order_with_plain_values():
    """dedupe_preserving_order also works on ordinary hashable values like ints."""
    assert dedupe_preserving_order([1, 2, 1, 3, 2]) == [1, 2, 3]
''',
    },
]
