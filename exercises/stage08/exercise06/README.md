# Money and Score: Operator Overloading

Implement two small immutable value classes, each supporting `+` and `sum()`:

- `Money.__init__(self, cents: int)` -- store it. `__repr__` -- `f"Money({self.cents})"`. `__eq__` -- same `cents`. `__add__` -- `Money(self.cents + other.cents)` if `other` is `Money`, else `NotImplemented`. `__radd__` -- `self` if `other == 0`, else `NotImplemented`. `__hash__` -- `hash(self.cents)`.
- `Score.__init__(self, points: int)` -- same five methods, same shapes, just `points` instead of `cents`.

This is **operator overloading**: `+` on `Money`/`Score` doesn't do anything magical -- it's just Python calling `__add__`/`__radd__`, the same mechanism as `Vector` in Exercise 1. Writing it twice, independently, for two unrelated classes is the point: any class can opt into `+` this way, with no shared base class required.

See the Study Reference presentation, Topic 8, for the theory.
