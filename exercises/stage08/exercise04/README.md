# Callables

Implement three classes whose instances are directly callable (`instance(...)` works because of `__call__`):

- `Multiplier.__init__(self, factor)` stores it; `__call__(self, x)` returns `x * self.factor`.
- `Adder.__init__(self, n)` stores it; `__call__(self, x)` returns `x + self.n`.
- `Toggler.__init__(self)` sets `self.state = False`; `__call__(self) -> bool` flips `self.state` and returns the new value -- a callable object carrying its own state between calls, the same idea as the `make_counter()` closure from Topic 3, but as a class instead of a closure.

See the Study Reference presentation, Topic 8, for the theory.
