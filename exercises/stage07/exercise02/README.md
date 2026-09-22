# super() and Polymorphism

Implement a three-level inheritance chain where each level *extends* the one before it, rather than just calling its `__init__`:

- `Vehicle.__init__(self, make, model)` -- store both. `describe(self) -> str` -- `f"{self.make} {self.model}"`.
- `Car(Vehicle)` -- `__init__(self, make, model, doors)` calls `super().__init__(make, model)` then stores `self.doors`; `describe(self) -> str` returns `super().describe() + f" ({self.doors} doors)"` -- it calls the **parent's** `describe()` and appends to it, instead of rewriting the whole string.
- `ElectricCar(Car)` -- `__init__(self, make, model, doors, battery_kwh)` calls `super().__init__(make, model, doors)` then stores `self.battery_kwh`; `describe(self) -> str` returns `super().describe() + f", {self.battery_kwh}kWh battery"`.
- `total_description(vehicles: list) -> list[str]` -- `[v.describe() for v in vehicles]` (polymorphism again: works across all three classes in one list).
- `is_car(vehicle) -> bool` -- `isinstance(vehicle, Car)` -- note an `ElectricCar` **is** a `Car` too (it inherits from it), so this returns `True` for both.

See the Study Reference presentation, Topic 7, for the theory.
