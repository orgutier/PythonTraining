# Vector: The Flagship Dunder Class

Implement `Vector`, a 2D vector with eight dunder methods:

- `__init__(self, x, y)` -- store both.
- `__repr__(self) -> str` -- `f"Vector({self.x}, {self.y})"` (unambiguous, developer-facing -- what you'd see in a debugger).
- `__str__(self) -> str` -- `f"({self.x}, {self.y})"` (friendlier, user-facing -- what `print()`/`str()` use).
- `__eq__(self, other) -> bool` -- `True` if `other` is a `Vector` with the same `x`/`y`.
- `__add__(self, other)` -- if `other` is a `Vector`, return a new `Vector(self.x + other.x, self.y + other.y)`; otherwise return `NotImplemented` (not raise -- that lets Python try the other object's `__radd__`, or fail with a clear `TypeError` itself, instead of your code failing with a confusing one).
- `__radd__(self, other)` -- return `self` if `other == 0`, else `NotImplemented`. This is exactly what `sum([v1, v2, v3])` needs: `sum()` starts from `0 + v1`, and `int.__add__(0, v1)` fails, so Python falls back to `v1.__radd__(0)`.
- `__hash__(self) -> int` -- `hash((self.x, self.y))` (required alongside `__eq__` for `Vector` to work in a `set`).
- `__bool__(self) -> bool` -- `False` only for the zero vector (`x == 0 and y == 0`).
- `__getitem__(self, index)` -- `(self.x, self.y)[index]`, so `v[0]` is `x` and `v[1]` is `y`.

See the Study Reference presentation, Topic 8, for the theory.
