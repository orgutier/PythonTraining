"""
The Python Data Model -- Deck: A Collection Protocol
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the aggregated test suite in
tests/test_week08.py imports directly from here. Need a helper function or
class of your own? Add another .py file next to this one inside
exercises/week08/exercise02/ and import it as a submodule (e.g.
`from exercises.week08.exercise02 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


class Deck:
    def __init__(self, cards: list):
        self.cards = list(cards)

    def __repr__(self) -> str:
        """f"Deck({self.cards!r})"."""
        raise NotImplementedError

    def __str__(self) -> str:
        """f"Deck of {len(self.cards)} cards"."""
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def __getitem__(self, index):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    def __contains__(self, card) -> bool:
        raise NotImplementedError

    def __add__(self, other):
        """New Deck(self.cards + other.cards) if other is a Deck, else NotImplemented."""
        raise NotImplementedError
