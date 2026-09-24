"""
OS, JSON, Datetime, XML -- Recursing with os.walk: Size and Depth
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage09_advanced02.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage09/advanced02/ and import it as a submodule (e.g.
`from exercises.stage09.advanced02 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import os


def total_size_of_directory(root: str) -> int:
    """Sum of os.path.getsize() over every file under root (os.walk)."""
    raise NotImplementedError


def max_directory_depth(root: str) -> int:
    """Largest depth of any directory under root, via os.walk + os.path.relpath."""
    raise NotImplementedError
