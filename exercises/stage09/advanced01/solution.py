"""
OS, JSON, Datetime, XML -- Recursing with os.walk: File Discovery
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage09_advanced01.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage09/advanced01/ and import it as a submodule (e.g.
`from exercises.stage09.advanced01 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import os


def find_all_py_files(root: str) -> list[str]:
    """Every .py file under root (os.walk), full paths, sorted."""
    raise NotImplementedError


def count_files_by_extension(root: str) -> dict:
    """{extension: count} for every file under root (os.walk)."""
    raise NotImplementedError
