"""
Functions -- Call-Counting Decorator + Validated Config
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage03_mid02.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage03/mid02/ and import it as a submodule (e.g.
`from exercises.stage03.mid02 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


def count_calls(fn):
    """Decorator: wrapper.calls counts calls to fn, starting at 0."""
    raise NotImplementedError


def greet(name):
    """"Hello, " + name -- deliberately NOT decorated with @count_calls here; see README."""
    raise NotImplementedError


def make_validator(*, min_value, max_value=100):
    """Keyword-only min_value/max_value. Return a validate(n) closure: min_value <= n <= max_value."""
    raise NotImplementedError
