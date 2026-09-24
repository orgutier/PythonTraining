"""
Files, Exceptions, Regex -- Generator-Based Context Managers
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage05_advanced02.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage05/advanced02/ and import it as a submodule (e.g.
`from exercises.stage05.advanced02 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import contextlib
import time


@contextlib.contextmanager
def temporary_value(obj, attr, value):
    """Temporarily set obj.attr to value, restoring the original in a finally."""
    raise NotImplementedError


@contextlib.contextmanager
def suppress_and_log(log: list, *exc_types):
    """Swallow a matching exception, appending str(e) to log instead of propagating."""
    raise NotImplementedError


@contextlib.contextmanager
def timing_block(results: list):
    """Append the elapsed seconds of the with-block to results, via finally."""
    raise NotImplementedError
