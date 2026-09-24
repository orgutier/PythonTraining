class Deck:
    def __init__(self, cards: list):
        self.cards = list(cards)

    def __len__(self) -> int:
        return len(self.cards)

    def __getitem__(self, index):
        return self.cards[index]

    def __iter__(self):
        return iter(self.cards)

    def __contains__(self, card) -> bool:
        return card in self.cards

    def __add__(self, other):
        if isinstance(other, Deck):
            return Deck(self.cards + other.cards)
        return NotImplemented
