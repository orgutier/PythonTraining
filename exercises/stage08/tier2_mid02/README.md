# Inventory and Callables

Two more dunder protocols on unrelated classes. First, `Inventory`, a small wrapper around a `{item_name: quantity}` dict:

- `__init__(self)` -- `self.items = {}`.
- `add_item(self, name: str, qty: int) -> None` -- `self.items[name] = self.items.get(name, 0) + qty`.
- `__contains__(self, name) -> bool` -- `name in self.items`.
- `__iter__(self)` -- `iter(self.items)` (iterating an `Inventory` yields item *names*, same as iterating a plain dict would).
- `__bool__(self) -> bool` -- `len(self.items) > 0` (an empty inventory is falsy).

Second, three classes whose instances are directly callable (`instance(...)` works because of `__call__`):

- `Multiplier.__init__(self, factor)` stores it; `__call__(self, x)` returns `x * self.factor`.
- `Adder.__init__(self, n)` stores it; `__call__(self, x)` returns `x + self.n`.
- `Toggler.__init__(self)` sets `self.state = False`; `__call__(self) -> bool` flips `self.state` and returns the new value -- a callable object carrying its own state between calls, the same idea as a closure, but as a class instead.

See the Study Reference presentation, Topic 8 (Mid tier), for the theory.
