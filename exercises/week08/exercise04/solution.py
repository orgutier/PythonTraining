"""
The Python Data Model -- Callables
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the aggregated test suite in
tests/test_week08.py imports directly from here. Need a helper function or
class of your own? Add another .py file next to this one inside
exercises/week08/exercise04/ and import it as a submodule (e.g.
`from exercises.week08.exercise04 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


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
