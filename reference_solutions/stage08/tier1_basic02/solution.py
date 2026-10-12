class PlayingCard:
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit

    def __repr__(self) -> str:
        return f"PlayingCard({self.rank!r}, {self.suit!r})"

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"

    def __eq__(self, other) -> bool:
        return isinstance(other, PlayingCard) and self.rank == other.rank and self.suit == other.suit
