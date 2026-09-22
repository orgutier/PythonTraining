# NumberRange: A Read-Only Sequence

Implement `NumberRange`, a simplified, immutable version of the builtin `range`:

- `__init__(self, start: int, stop: int)` -- store both.
- `__repr__(self) -> str` -- `f"NumberRange({self.start}, {self.stop})"`.
- `__eq__(self, other) -> bool` -- `True` if `other` is a `NumberRange` with the same `start`/`stop`.
- `__hash__(self) -> int` -- `hash((self.start, self.stop))`.
- `__len__(self) -> int` -- `max(0, self.stop - self.start)`.
- `__getitem__(self, index)` -- `raise IndexError` if `index < 0 or index >= len(self)`, else `self.start + index`.
- `__iter__(self)` -- `iter(range(self.start, self.stop))`.
- `__contains__(self, value) -> bool` -- `self.start <= value < self.stop` (an O(1) check, not a linear scan -- one advantage of implementing `__contains__` yourself instead of relying on the default that falls back to iterating).
- `__bool__(self) -> bool` -- `len(self) > 0`.

See the Study Reference presentation, Topic 8, for the theory.
