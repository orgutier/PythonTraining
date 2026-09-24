"""
OS, JSON, Datetime, XML -- pathlib: The Modern os.path Alternative
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage09_mid01.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage09/mid01/ and import it as a submodule (e.g.
`from exercises.stage09.mid01 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import pathlib


def list_entries(directory: str) -> list[str]:
    """sorted(p.name for p in pathlib.Path(directory).iterdir())."""
    raise NotImplementedError


def build_path(directory: str, filename: str) -> pathlib.Path:
    """pathlib.Path(directory) / filename."""
    raise NotImplementedError


def read_and_write_pathlib(path: str, content: str) -> str:
    """Write content via Path.write_text, then return Path.read_text()."""
    raise NotImplementedError


def find_txt_files(root: str) -> list[str]:
    """sorted(p.name for p in pathlib.Path(root).rglob("*.txt"))."""
    raise NotImplementedError
