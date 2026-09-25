"""
Functions -- functools Toolkit
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage03_tier3_advanced01.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage03/tier3_advanced01/ and import it as a submodule (e.g.
`from exercises.stage03.tier3_advanced01 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import functools


def logged(fn):
    """Decorator: functools.wraps(fn)-preserving passthrough wrapper."""
    raise NotImplementedError


def multiply(a, b):
    """Multiply two numbers. Deliberately NOT decorated with @logged here; see README."""
    raise NotImplementedError


@functools.lru_cache(maxsize=None)
def fib(n):
    """Recursive Fibonacci, cached with functools.lru_cache(maxsize=None)."""
    raise NotImplementedError


add_ten = None  # TODO: functools.partial(lambda a, b: a + b, b=10)
