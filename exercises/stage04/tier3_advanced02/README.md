# Hashable Records: Frozen Dataclasses and Manual __hash__

Two ways a class can become hashable -- automatically, and by hand -- and why it matters. `Point`, `FrozenPoint`, and `SimpleFraction`'s `__init__` are already defined for you.

- `Point.distance_from_origin(self) -> float` and `FrozenPoint.distance_from_origin(self) -> float` -- both `(self.x ** 2 + self.y ** 2) ** 0.5`. `Point` is a plain `@dataclasses.dataclass` (`eq=True`, `frozen=False` by default) -- dataclass therefore sets `Point.__hash__ = None` automatically, so `hash(Point(1, 2))` raises `TypeError`: **mutable objects that support `==` are unsafe to hash**, since mutating one after it's in a set/dict would silently corrupt that container. `FrozenPoint` is `@dataclasses.dataclass(frozen=True)`, so dataclass generates **both** `__eq__` *and* a working `__hash__` from the fields, and instances work fine in a `set`.
- `SimpleFraction.__eq__(self, other) -> bool` -- `True` if `other` is a `SimpleFraction` with the same (already-reduced, by the given `__init__`) `numerator` and `denominator`.
- `SimpleFraction.__hash__(self) -> int` -- `hash((self.numerator, self.denominator))`. This one you have to write **by hand**: `SimpleFraction` isn't a dataclass, so nothing generates `__hash__` for it automatically. Python actively **removes** the default (identity-based) `__hash__` from any plain class that defines `__eq__` without also defining `__hash__` -- skip this method and every `SimpleFraction` becomes unhashable, even though `==` still works.
- `dedupe_preserving_order(items: list) -> list` -- `list(dict.fromkeys(items))`. `dict.fromkeys` de-duplicates using each item's `__hash__`/`__eq__` while keeping first-seen order -- this only works at all because `SimpleFraction` and `FrozenPoint` are both hashable.

See the Study Reference presentation, Topic 4 (Advanced tier), for the theory.
