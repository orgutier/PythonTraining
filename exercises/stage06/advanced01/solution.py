"""
OOP I -- Descriptors Preview: PositiveNumber
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage06_advanced01.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage06/advanced01/ and import it as a submodule (e.g.
`from exercises.stage06.advanced01 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


class PositiveNumber:
    def __set_name__(self, owner, name):
        self._name = "_" + name

    def __get__(self, obj, objtype=None):
        """getattr(obj, self._name)."""
        raise NotImplementedError

    def __set__(self, obj, value):
        """Raise ValueError if value < 0, else setattr(obj, self._name, value)."""
        raise NotImplementedError


class Product:
    price = PositiveNumber()

    def __init__(self, name, price):
        raise NotImplementedError
