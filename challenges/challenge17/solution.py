"""
Challenge 17 - Directory Report Builder
Interview-style challenge. Correctness is pytest-tested (see
tests/test_challenge17.py / `python tools/cli.py test challenge17`); see
README.md in this folder for the full problem statement and the constraints
your solution must follow (os.walk() for the scan, pathlib.Path for the alternative listing, and json.dumps(default=...) to serialize the datetime fields it collects).

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module, matching the convention used by
exercises/stageNN/solution.py.
"""


import os
import json
import datetime
import pathlib


def scan_directory_report(root: str) -> dict:
    """Walk root; report size + a real datetime "modified" per file. See README."""
    raise NotImplementedError


def _json_default(obj):
    """datetime -> obj.isoformat(); else raise TypeError."""
    raise NotImplementedError


def save_report(report: dict, path: str) -> None:
    """json.dump(report, f, default=_json_default)."""
    raise NotImplementedError


def load_report(path: str) -> dict:
    """json.load, converting each "modified" string back into a datetime.datetime."""
    raise NotImplementedError


def list_py_files_pathlib(root: str) -> list:
    """Sorted list of str paths for every .py file under root, via pathlib.Path(root).rglob("*.py")."""
    raise NotImplementedError
