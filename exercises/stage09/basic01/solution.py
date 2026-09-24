"""
OS, JSON, Datetime, XML -- Config File Manager
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage09_basic01.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage09/basic01/ and import it as a submodule (e.g.
`from exercises.stage09.basic01 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import json
import os


def config_path(directory: str, name: str) -> str:
    """os.path.join(directory, name + ".json")."""
    raise NotImplementedError


def config_exists(directory: str, name: str) -> bool:
    """os.path.exists(config_path(directory, name))."""
    raise NotImplementedError


def save_config(directory: str, name: str, data: dict) -> None:
    """Write data as JSON to config_path(directory, name)."""
    raise NotImplementedError


def load_config(directory: str, name: str) -> dict:
    """Read and json.load the file at config_path(directory, name)."""
    raise NotImplementedError


def list_config_names(directory: str) -> list[str]:
    """sorted names (without ".json") of every *.json file in directory."""
    raise NotImplementedError
