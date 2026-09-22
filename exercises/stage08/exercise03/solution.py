"""
The Python Data Model -- Inventory: Mapping-ish Container
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage08_exercise03.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage08/exercise03/ and import it as a submodule (e.g.
`from exercises.stage08.exercise03 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name: str, qty: int) -> None:
        raise NotImplementedError

    def __str__(self) -> str:
        """f"Inventory({len(self.items)} item types)"."""
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def __contains__(self, name) -> bool:
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    def __bool__(self) -> bool:
        raise NotImplementedError
