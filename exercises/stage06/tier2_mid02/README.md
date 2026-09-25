# Slotted Records

Implement two more `__slots__`-based classes:

- `TemperatureSlots` -- `__slots__ = ("celsius",)`; `__init__(self, celsius)` sets it; `fahrenheit(self) -> float` returns `self.celsius * 9 / 5 + 32`.
- `InventoryItemSlots` -- `__slots__ = ("name", "price", "quantity")`; `__init__(self, name, price, quantity)` sets all three; `total_value(self) -> float` returns `round(self.price * self.quantity, 2)`.

Same mechanism as the previous exercise, on two different record shapes: `__slots__` allocates fixed storage for exactly the named attributes, so both classes skip the per-instance `__dict__` and reject any attribute not listed.

See the Study Reference presentation, Topic 6 (Mid tier), for the theory.
