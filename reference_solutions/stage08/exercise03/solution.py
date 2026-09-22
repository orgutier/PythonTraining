class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name: str, qty: int) -> None:
        self.items[name] = self.items.get(name, 0) + qty

    def __str__(self) -> str:
        return f"Inventory({len(self.items)} item types)"

    def __len__(self) -> int:
        return len(self.items)

    def __contains__(self, name) -> bool:
        return name in self.items

    def __iter__(self):
        return iter(self.items)

    def __bool__(self) -> bool:
        return len(self.items) > 0
