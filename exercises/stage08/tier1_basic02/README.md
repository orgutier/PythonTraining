# PlayingCard: repr, str, eq

Implement `PlayingCard`, a single playing card:

- `__init__(self, rank: str, suit: str)` -- store both.
- `__repr__(self) -> str` -- `f"PlayingCard({self.rank!r}, {self.suit!r})"` (note the `!r}` -- it wraps `rank`/`suit` in their own `repr()`, e.g. `PlayingCard('A', 'Spades')` with the quotes included, so the result really is valid Python that recreates the object).
- `__str__(self) -> str` -- `f"{self.rank} of {self.suit}"` (e.g. `"A of Spades"`).
- `__eq__(self, other) -> bool` -- `True` if `other` is a `PlayingCard` with the same `rank`/`suit`.

Same three dunders as the previous exercise, on a different shape of data, to drive home that `__repr__`/`__str__`/`__eq__` are a pattern you write the same way on every class that needs it, not something specific to one kind of object.

See the Study Reference presentation, Topic 8 (Basic tier), for the theory.
