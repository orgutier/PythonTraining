# Point: repr, str, eq

Implement `Point`, a simple 2D point:

- `__init__(self, x, y)` -- store both.
- `__repr__(self) -> str` -- `f"Point({self.x}, {self.y})"` (unambiguous, developer-facing -- what you'd see in a debugger or an error traceback).
- `__str__(self) -> str` -- `f"({self.x}, {self.y})"` (friendlier, user-facing -- what `print()`/`str()` use).
- `__eq__(self, other) -> bool` -- `True` if `other` is a `Point` with the same `x`/`y`.

`repr()` and `str()` serve different audiences: `repr()` should (ideally) look like valid Python that could recreate the object, while `str()` is free to be whatever reads best to a human. Without `__eq__`, `Point(1, 2) == Point(1, 2)` would be `False` -- the default `__eq__` compares object identity (`is`), not field values.

See the Study Reference presentation, Topic 8 (Basic tier), for the theory.
