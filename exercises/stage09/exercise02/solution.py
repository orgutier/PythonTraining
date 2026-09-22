"""
OS, JSON, Datetime, XML -- Recursive Traversal
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage09_exercise02.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage09/exercise02/ and import it as a submodule (e.g.
`from exercises.stage09.exercise02 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import os
import pathlib


def find_all_py_files(root: str) -> list[str]:
    """Every .py file under root (os.walk), full paths, sorted."""
    raise NotImplementedError


def count_files_by_extension(root: str) -> dict:
    """{extension: count} for every file under root (os.walk)."""
    raise NotImplementedError


def total_size_of_directory(root: str) -> int:
    """Sum of os.path.getsize() over every file under root (os.walk)."""
    raise NotImplementedError


def find_txt_files_pathlib(root: str) -> list[str]:
    """sorted(p.name for p in pathlib.Path(root).rglob("*.txt"))."""
    raise NotImplementedError
