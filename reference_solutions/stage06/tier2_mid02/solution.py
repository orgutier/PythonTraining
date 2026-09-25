class TemperatureSlots:
    __slots__ = ("celsius",)

    def __init__(self, celsius):
        self.celsius = celsius

    def fahrenheit(self) -> float:
        return self.celsius * 9 / 5 + 32


class InventoryItemSlots:
    __slots__ = ("name", "price", "quantity")

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self) -> float:
        return round(self.price * self.quantity, 2)
