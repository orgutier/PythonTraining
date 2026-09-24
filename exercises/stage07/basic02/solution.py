"""
OOP II -- Vehicle Fleet
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage07_basic02.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage07/basic02/ and import it as a submodule (e.g.
`from exercises.stage07.basic02 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


from typing import List


class Vehicle:
    def __init__(self, make, model):
        raise NotImplementedError

    def describe(self) -> str:
        """f"{self.make} {self.model}"."""
        raise NotImplementedError


class Car(Vehicle):
    def __init__(self, make, model, doors):
        """super().__init__(make, model), then store self.doors."""
        raise NotImplementedError

    def describe(self) -> str:
        """super().describe() + f" ({self.doors} doors)"."""
        raise NotImplementedError


class ElectricCar(Car):
    def __init__(self, make, model, doors, battery_kwh):
        """super().__init__(make, model, doors), then store self.battery_kwh."""
        raise NotImplementedError

    def describe(self) -> str:
        """super().describe() + f", {self.battery_kwh}kWh battery"."""
        raise NotImplementedError


def fleet_summary(vehicles: List[Vehicle]) -> str:
    """", ".join(v.describe() for v in vehicles)."""
    raise NotImplementedError


def is_car(vehicle) -> bool:
    """isinstance(vehicle, Car)."""
    raise NotImplementedError
