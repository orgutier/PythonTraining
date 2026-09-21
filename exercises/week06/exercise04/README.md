# Slots and Memory

Implement three classes using `__slots__` instead of the default per-instance `__dict__`:

- `PointSlots` -- `__slots__ = ("x", "y")`; `__init__(self, x, y)` sets both.
- `Vector3DSlots` -- `__slots__ = ("x", "y", "z")`; `__init__(self, x, y, z)` sets all three; `magnitude(self) -> float` returns `(x**2 + y**2 + z**2) ** 0.5`.
- `TemperatureSlots` -- `__slots__ = ("celsius",)`; `__init__(self, celsius)` sets it; `fahrenheit(self) -> float` returns `self.celsius * 9 / 5 + 32`.

`__slots__` tells Python to skip creating a per-instance `__dict__` and allocate fixed storage for only the named attributes instead -- less memory per instance, and it also means trying to set *any other* attribute raises `AttributeError` (the tests check both effects).

See the Study Reference presentation, Topic 6, for the theory.
