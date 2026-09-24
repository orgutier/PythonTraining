# Protocol Structural Typing

Implement a `typing.Protocol` and a class that satisfies it **without ever inheriting from it**:

- `SupportsArea` (`typing.Protocol`, `@runtime_checkable`) -- declares `def area(self) -> float: ...` as the interface (already given).
- `Coin.__init__(self, radius)` / `Coin.area(self) -> float` (`3.14159 * radius ** 2`) -- `Coin` **never inherits from** `SupportsArea`. It just happens to have a matching `area()` method.
- `total_area(shapes: list) -> float` -- `sum(s.area() for s in shapes)`.
- `supports_area(obj) -> bool` -- `isinstance(obj, SupportsArea)`. Because `SupportsArea` is `@runtime_checkable`, this actually works on `Coin` even though `Coin` never inherits from it -- `isinstance()` checks the *shape* of the object (does it have an `area()` method?), not its class hierarchy.

This is **structural typing**: the formal, type-checker-friendly version of the duck typing from the first Basic exercise (`make_it_quack`) -- same underlying idea (match by shape, not ancestry), but now expressed as a real type (`SupportsArea`) that both `isinstance()` and a static type checker can understand.

See the Study Reference presentation, Topic 7 (Advanced tier), for the theory.
