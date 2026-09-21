"""
The Python Data Model -- NumberRange: A Read-Only Sequence
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the aggregated test suite in
tests/test_week08.py imports directly from here. Need a helper function or
class of your own? Add another .py file next to this one inside
exercises/week08/exercise05/ and import it as a submodule (e.g.
`from exercises.week08.exercise05 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


class NumberRange:
    def __init__(self, start: int, stop: int):
        self.start = start
        self.stop = stop

    def __repr__(self) -> str:
        """f"NumberRange({self.start}, {self.stop})"."""
        raise NotImplementedError

    def __eq__(self, other) -> bool:
        raise NotImplementedError

    def __hash__(self) -> int:
        raise NotImplementedError

    def __len__(self) -> int:
        """max(0, self.stop - self.start)."""
        raise NotImplementedError

    def __getitem__(self, index):
        """self.start + index, or raise IndexError if out of range."""
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    def __contains__(self, value) -> bool:
        """self.start <= value < self.stop -- O(1), not a scan."""
        raise NotImplementedError

    def __bool__(self) -> bool:
        raise NotImplementedError
