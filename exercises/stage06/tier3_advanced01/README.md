# Descriptors Preview: PositiveNumber

`@property` is itself built on a lower-level mechanism called the **descriptor protocol**: any object with `__get__`/`__set__` methods, assigned as a *class* attribute, controls what happens when you read/write that attribute on an instance. Implement a reusable descriptor:

- `PositiveNumber` -- `__set_name__(self, owner, name)` stores `self._name = "_" + name` (already given -- called automatically by Python when the descriptor is assigned in a class body, telling it what attribute name it was bound to); `__get__(self, obj, objtype=None)` returns `getattr(obj, self._name)`; `__set__(self, obj, value)` raises `ValueError` if `value < 0`, else `setattr(obj, self._name, value)`.

Then use it: `Product` has `price = PositiveNumber()` as a class attribute, plus `__init__(self, name, price)` that sets `self.name = name` and `self.price = price` (going through the descriptor, exactly like a `@property` setter would).

See the Study Reference presentation, Topic 6 (Advanced tier), for the theory.
