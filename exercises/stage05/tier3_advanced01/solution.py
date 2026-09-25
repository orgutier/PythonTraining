"""
Files, Exceptions, Regex -- Class-Based Context Managers
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage05_tier3_advanced01.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage05/tier3_advanced01/ and import it as a submodule (e.g.
`from exercises.stage05.tier3_advanced01 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


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
        """True (suppress) if exc_type is a subclass of self.exc_type, else False."""
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
