class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def describe(self) -> str:
        return f"{self.make} {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors

    def describe(self) -> str:
        return super().describe() + f" ({self.doors} doors)"


class ElectricCar(Car):
    def __init__(self, make, model, doors, battery_kwh):
        super().__init__(make, model, doors)
        self.battery_kwh = battery_kwh

    def describe(self) -> str:
        return super().describe() + f", {self.battery_kwh}kWh battery"


def total_description(vehicles: list) -> list:
    return [v.describe() for v in vehicles]


def is_car(vehicle) -> bool:
    return isinstance(vehicle, Car)
