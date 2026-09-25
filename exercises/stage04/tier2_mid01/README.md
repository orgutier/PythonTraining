# Player Records: Dataclass vs. namedtuple

Two ways to model the same lightweight record: a mutable `@dataclasses.dataclass` and an immutable `collections.namedtuple`. Both are already defined for you:

```python
@dataclasses.dataclass
class Player:
    name: str
    position: str

PlayerRecord = collections.namedtuple("PlayerRecord", ["name", "position"])
```

Implement:

- `convert_to_record(player: Player) -> PlayerRecord` -- `PlayerRecord(player.name, player.position)`.
- `players_are_equal(a: Player, b: Player) -> bool` -- `a == b`. `@dataclasses.dataclass` auto-generates `__eq__` from the fields, so two **different** `Player` objects with the same `name`/`position` compare equal, even though `a is b` is `False`.
- `records_are_equal(a: PlayerRecord, b: PlayerRecord) -> bool` -- `a == b`. `namedtuple` gets field-based equality for free too, inherited from being a plain `tuple` subclass -- no `@dataclass` decorator needed here at all.

The point of putting these side by side: both `@dataclasses.dataclass` and `collections.namedtuple` are ways to define a record type without hand-writing `__init__`/`__repr__`/`__eq__` yourself, from two different standard-library modules (`dataclasses` and `collections`).

See the Study Reference presentation, Topic 4 (Mid tier), for the theory.
