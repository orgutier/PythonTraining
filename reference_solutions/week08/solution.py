class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other) -> bool:
        return isinstance(other, Vector) and self.x == other.x and self.y == other.y

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"


class Deck:
    def __init__(self, cards: list):
        self._cards = list(cards)

    def __len__(self) -> int:
        return len(self._cards)

    def __getitem__(self, index: int):
        return self._cards[index]

    def __iter__(self):
        return iter(self._cards)
