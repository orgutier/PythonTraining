"""
Files, Exceptions, Regex -- Context Managers
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the aggregated test suite in
tests/test_week05.py imports directly from here. Need a helper function or
class of your own? Add another .py file next to this one inside
exercises/week05/exercise06/ and import it as a submodule (e.g.
`from exercises.week05.exercise06 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import contextlib
import time


class Timer:
    def __enter__(self):
        """Record self._start = time.time(); return self."""
        raise NotImplementedError

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Set self.elapsed = time.time() - self._start; return False."""
        raise NotImplementedError


class SuppressErrors:
    def __init__(self, exc_type):
        self.exc_type = exc_type

    def __enter__(self):
        raise NotImplementedError

    def __exit__(self, exc_type, exc_val, exc_tb):
        """True (suppress) if exc_type matches self.exc_type, else False."""
        raise NotImplementedError


class FileLineCounter:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        """Open self.path and return the file object."""
        raise NotImplementedError

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close the file; return False."""
        raise NotImplementedError


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
