"""
OOP II -- Duck Typing and Composition
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the aggregated test suite in
tests/test_week07.py imports directly from here. Need a helper function or
class of your own? Add another .py file next to this one inside
exercises/week07/exercise03/ and import it as a submodule (e.g.
`from exercises.week07.exercise03 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


class Engine:
    def start(self) -> str:
        """"Engine starting..."."""
        raise NotImplementedError


class Boat:
    def __init__(self, engine):
        """Store self.engine = engine (composition: Boat HAS an Engine)."""
        raise NotImplementedError

    def start(self) -> str:
        """self.engine.start()."""
        raise NotImplementedError


class Duck:
    def quack(self) -> str:
        """"Quack!"."""
        raise NotImplementedError


class Person:
    def quack(self) -> str:
        """"I'm quacking like a duck!"."""
        raise NotImplementedError


def make_it_quack(obj) -> str:
    """obj.quack() -- works for anything with a .quack() method (duck typing)."""
    raise NotImplementedError


def is_duck_instance(obj) -> bool:
    """isinstance(obj, Duck)."""
    raise NotImplementedError
