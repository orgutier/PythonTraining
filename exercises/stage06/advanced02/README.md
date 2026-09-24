# Descriptors Preview: Typed

A second reusable descriptor, this time enforcing a **type** instead of a numeric range:

- `Typed` -- same shape as the previous exercise's `PositiveNumber`, but `__init__(self, expected_type)` stores the type to enforce, `__set_name__`/`__get__` work the same way, and `__set__` raises `TypeError` (not `ValueError`) if `not isinstance(value, self.expected_type)`, else `setattr(obj, self._name, value)`.

Then use it: `Person` has `name = Typed(str)` and `age = Typed(int)` as class attributes, plus `__init__(self, name, age)` that sets both (going through the descriptors). The same descriptor **class** (`Typed`) is reused twice on `Person`, each time configured with a different `expected_type` -- that's the point of writing it as a reusable, general-purpose descriptor rather than one-off validation code per attribute.

See the Study Reference presentation, Topic 6 (Advanced tier), for the theory.
