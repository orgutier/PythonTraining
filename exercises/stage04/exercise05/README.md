# Dataclasses

Implement one method on each of three dataclasses (the `@dataclasses.dataclass` decorators and fields are already there for you -- see how each one changes what `__eq__`/`__hash__` the class gets for free):

- `Point` (plain `@dataclasses.dataclass`, so `eq=True`, `frozen=False` by default) -- implement `distance_from_origin(self) -> float` as `(self.x ** 2 + self.y ** 2) ** 0.5`. Because `eq=True` and `frozen=False`, dataclass sets `Point.__hash__ = None` automatically -- `Point` instances get a real `__eq__` but are **not hashable** (`hash(Point(1, 2))` raises `TypeError`).
- `FrozenPoint` (`@dataclasses.dataclass(frozen=True)`) -- same `distance_from_origin`. Because it's frozen, dataclass generates **both** `__eq__` *and* `__hash__` from the fields -- these instances work fine in a `set` or as dict keys.
- `TaggedItem` (fields `name: str` and `tags: list = dataclasses.field(default_factory=list)`) -- implement `add_tag(self, tag: str) -> None` as `self.tags.append(tag)`. `default_factory=list` is what stops every `TaggedItem` from sharing the *same* mutable list -- the mutable-default-argument bug (Topic 3) applied to dataclass fields.

See the Study Reference presentation, Topic 4, for the theory.
