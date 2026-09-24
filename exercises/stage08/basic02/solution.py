"""
The Python Data Model -- PlayingCard: repr, str, eq
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage08_basic02.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage08/basic02/ and import it as a submodule (e.g.
`from exercises.stage08.basic02 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


class PlayingCard:
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit

    def __repr__(self) -> str:
        """f"PlayingCard({self.rank!r}, {self.suit!r})"."""
        raise NotImplementedError

    def __str__(self) -> str:
        """f"{self.rank} of {self.suit}"."""
        raise NotImplementedError

    def __eq__(self, other) -> bool:
        """True if other is a PlayingCard with the same rank/suit."""
        raise NotImplementedError
