# Money and Score: Operator Overloading

Implement two small immutable value classes, each supporting `+` and `sum()`:

- `Money.__init__(self, cents: int)` -- store it. `__repr__` -- `f"Money({self.cents})"`. `__eq__` -- same `cents`. `__add__` -- `Money(self.cents + other.cents)` if `other` is `Money`, else `NotImplemented`. `__radd__` -- `self` if `other == 0`, else `NotImplemented`. `__hash__` -- `hash(self.cents)` (required alongside `__eq__` for `Money` to work in a `set`).
- `Score.__init__(self, points: int)` -- same five methods, same shapes, just `points` instead of `cents`.

`__radd__` is what makes `sum([m1, m2, m3])` work: `sum()` starts from `0 + m1`, and `int.__add__(0, m1)` fails (an `int` doesn't know how to add a `Money`), so Python falls back to `m1.__radd__(0)` -- the **reflected** operator, tried only when the left operand's own method returns `NotImplemented`. Writing this twice, independently, for two unrelated classes is the point: any class can opt into `+` and `sum()` this way, with no shared base class required.

See the Study Reference presentation, Topic 8 (Advanced tier), for the theory.
