"""
OS, JSON, Datetime, XML -- os.path and pathlib Basics
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_week09_exercise01.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/week09/exercise01/ and import it as a submodule (e.g.
`from exercises.week09.exercise01 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import os
import pathlib


def list_files(directory: str) -> list[str]:
    """sorted(os.listdir(directory))."""
    raise NotImplementedError


def join_path(directory: str, filename: str) -> str:
    """os.path.join(directory, filename)."""
    raise NotImplementedError


def file_exists(path: str) -> bool:
    """os.path.exists(path)."""
    raise NotImplementedError


def list_files_pathlib(directory: str) -> list[str]:
    """sorted(p.name for p in pathlib.Path(directory).iterdir())."""
    raise NotImplementedError


def read_text_pathlib(path: str) -> str:
    """pathlib.Path(path).read_text()."""
    raise NotImplementedError
