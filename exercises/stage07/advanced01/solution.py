"""
OOP II -- Mixins
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage07_advanced01.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage07/advanced01/ and import it as a submodule (e.g.
`from exercises.stage07.advanced01 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


class LoggingMixin:
    def log(self, message: str) -> str:
        """f"[{self.__class__.__name__}] {message}"."""
        raise NotImplementedError


class SerializableMixin:
    def to_dict(self) -> dict:
        """dict(self.__dict__)."""
        raise NotImplementedError


class Widget(LoggingMixin, SerializableMixin):
    def __init__(self, name):
        raise NotImplementedError
