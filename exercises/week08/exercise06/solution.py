"""
The Python Data Model -- Money and Score: Operator Overloading
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_week08_exercise06.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/week08/exercise06/ and import it as a submodule (e.g.
`from exercises.week08.exercise06 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


class Money:
    def __init__(self, cents: int):
        self.cents = cents

    def __repr__(self) -> str:
        raise NotImplementedError

    def __eq__(self, other) -> bool:
        raise NotImplementedError

    def __add__(self, other):
        raise NotImplementedError

    def __radd__(self, other):
        raise NotImplementedError

    def __hash__(self) -> int:
        raise NotImplementedError


class Score:
    def __init__(self, points: int):
        self.points = points

    def __repr__(self) -> str:
        raise NotImplementedError

    def __eq__(self, other) -> bool:
        raise NotImplementedError

    def __add__(self, other):
        raise NotImplementedError

    def __radd__(self, other):
        raise NotImplementedError

    def __hash__(self) -> int:
        raise NotImplementedError
