"""
Functions -- Decorators
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the aggregated test suite in
tests/test_week03.py imports directly from here. Need a helper function or
class of your own? Add another .py file next to this one inside
exercises/week03/exercise05/ and import it as a submodule (e.g.
`from exercises.week03.exercise05 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import functools


def log_calls(func):
    """Decorator: wrapper.calls counts calls to func. Use functools.wraps(func)."""
    raise NotImplementedError


def count_calls(func):
    """Decorator: wrapper.call_count() (a zero-arg method) returns the call count via a closure. Use functools.wraps(func)."""
    raise NotImplementedError


def uppercase_result(func):
    """Decorator: uppercase func's result if it's a str, else pass it through. Use functools.wraps(func)."""
    raise NotImplementedError
