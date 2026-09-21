# Mixins and Protocols

Implement:

- `LoggingMixin.log(self, message: str) -> str` -- `f"[{self.__class__.__name__}] {message}"`. A **mixin**: a small class meant to be combined with others via multiple inheritance, adding one focused piece of reusable behavior -- never instantiated on its own.
- `SerializableMixin.to_dict(self) -> dict` -- `dict(self.__dict__)`.
- `Widget(LoggingMixin, SerializableMixin)` -- `__init__(self, name)` stores `self.name`. `Widget` gets both `.log()` and `.to_dict()` for free by combining the two mixins -- no shared "is-a" hierarchy needed, just behavior composed in.
- `SupportsArea` (`typing.Protocol`, `@runtime_checkable`) -- declares `def area(self) -> float: ...` as the interface.
- `Coin.__init__(self, radius)` / `Coin.area(self) -> float` (`3.14159 * radius ** 2`) -- `Coin` **never inherits from** `SupportsArea`. It just happens to have a matching `area()` method.
- `total_area(shapes: list) -> float` -- `sum(s.area() for s in shapes)`.
- `supports_area(obj) -> bool` -- `isinstance(obj, SupportsArea)`. Because `SupportsArea` is `@runtime_checkable`, this actually works on `Coin` even though `Coin` never inherits from it -- `isinstance()` checks the *shape* of the object (does it have an `area()` method?), not its class hierarchy. This is **structural typing**: the formal, type-checker-friendly version of the duck typing from Exercise 3.

See the Study Reference presentation, Topic 7, for the theory.
