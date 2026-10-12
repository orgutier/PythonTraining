"""
The Python Data Model -- Inventory and Callables
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage08_tier2_mid02.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage08/tier2_mid02/ and import it as a submodule (e.g.
`from exercises.stage08.tier2_mid02 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name: str, qty: int) -> None:
        raise NotImplementedError

    def __contains__(self, name) -> bool:
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    def __bool__(self) -> bool:
        raise NotImplementedError


class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        """x * self.factor."""
        raise NotImplementedError


class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        """x + self.n."""
        raise NotImplementedError


class Toggler:
    def __init__(self):
        self.state = False

    def __call__(self) -> bool:
        """Flip self.state and return the new value."""
        raise NotImplementedError
