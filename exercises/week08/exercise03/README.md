# Inventory: Mapping-ish Container

Implement `Inventory`, a small wrapper around a `{item_name: quantity}` dict:

- `__init__(self)` -- `self.items = {}`.
- `add_item(self, name: str, qty: int) -> None` -- `self.items[name] = self.items.get(name, 0) + qty`.
- `__str__(self) -> str` -- `f"Inventory({len(self.items)} item types)"`.
- `__len__(self) -> int` -- `len(self.items)` (how many *distinct* item types, not total quantity).
- `__contains__(self, name) -> bool` -- `name in self.items`.
- `__iter__(self)` -- `iter(self.items)` (iterating an `Inventory` yields item *names*, same as iterating a plain dict would).
- `__bool__(self) -> bool` -- `len(self.items) > 0` (an empty inventory is falsy).

See the Study Reference presentation, Topic 8, for the theory.
