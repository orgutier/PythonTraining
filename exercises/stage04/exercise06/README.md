# Records and Hashability

Implement:

- `make_coordinate(x: int, y: int)` -- return `Coordinate(x, y)` (`Coordinate` is already defined above via `collections.namedtuple("Coordinate", ["x", "y"])` -- a lightweight, immutable, hashable record with no class boilerplate).
- `SimpleFraction.__init__(self, numerator: int, denominator: int)` -- raise `ZeroDivisionError` if `denominator == 0`; otherwise, if `denominator < 0`, flip the sign of both (`numerator, denominator = -numerator, -denominator`); then reduce both by their `math.gcd(numerator, denominator)` and store the results.
- `SimpleFraction.__eq__(self, other) -> bool` -- `True` if `other` is a `SimpleFraction` with the same (already-reduced) `numerator` and `denominator`.
- `SimpleFraction.__hash__(self) -> int` -- `hash((self.numerator, self.denominator))`. **This is required**: Python removes the default `__hash__` from any class that defines `__eq__` without also defining `__hash__` -- skip this and `SimpleFraction` instances become unhashable, breaking `set()`/dict-key use, even though `==` still works fine.
- `dedupe_preserving_order(items: list) -> list` -- `list(dict.fromkeys(items))`. `dict.fromkeys` de-duplicates using each item's `__hash__`/`__eq__` while a plain dict's insertion-ordering keeps first-seen order -- this only works because `SimpleFraction`/`Coordinate`/`FrozenPoint` are all hashable.

See the Study Reference presentation, Topic 4, for the theory.
