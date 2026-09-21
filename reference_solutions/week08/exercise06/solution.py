class Money:
    def __init__(self, cents: int):
        self.cents = cents

    def __repr__(self) -> str:
        return f"Money({self.cents})"

    def __eq__(self, other) -> bool:
        return isinstance(other, Money) and self.cents == other.cents

    def __add__(self, other):
        if isinstance(other, Money):
            return Money(self.cents + other.cents)
        return NotImplemented

    def __radd__(self, other):
        if other == 0:
            return self
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self.cents)


class Score:
    def __init__(self, points: int):
        self.points = points

    def __repr__(self) -> str:
        return f"Score({self.points})"

    def __eq__(self, other) -> bool:
        return isinstance(other, Score) and self.points == other.points

    def __add__(self, other):
        if isinstance(other, Score):
            return Score(self.points + other.points)
        return NotImplemented

    def __radd__(self, other):
        if other == 0:
            return self
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self.points)
