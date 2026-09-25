class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name: str, qty: int) -> None:
        self.items[name] = self.items.get(name, 0) + qty

    def __contains__(self, name) -> bool:
        return name in self.items

    def __iter__(self):
        return iter(self.items)

    def __bool__(self) -> bool:
        return len(self.items) > 0


class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor


class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return x + self.n


class Toggler:
    def __init__(self):
        self.state = False

    def __call__(self) -> bool:
        self.state = not self.state
        return self.state
