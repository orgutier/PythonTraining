# Descriptors Preview

`@property` is itself built on a lower-level mechanism called the **descriptor protocol**: any object with `__get__`/`__set__` methods, assigned as a *class* attribute, controls what happens when you read/write that attribute on an instance. Implement two reusable descriptors:

- `PositiveNumber` -- `__set_name__(self, owner, name)` stores `self._name = "_" + name` (called automatically by Python when the descriptor is assigned in a class body, telling it what attribute name it was bound to); `__get__(self, obj, objtype=None)` returns `getattr(obj, self._name)`; `__set__(self, obj, value)` raises `ValueError` if `value < 0`, else `setattr(obj, self._name, value)`.
- `Typed` -- same shape, but `__init__(self, expected_type)` stores the type to enforce, and `__set__` raises `TypeError` (not `ValueError`) if `not isinstance(value, self.expected_type)`.

Then use them: `Product` has `price = PositiveNumber()` as a class attribute, plus `__init__(self, name, price)` that sets `self.name = name` and `self.price = price` (going through the descriptor). `Person` has `name = Typed(str)` and `age = Typed(int)`, plus a matching `__init__`.

See the Study Reference presentation, Topic 6, for the theory.
