"""
OS, JSON, Datetime, XML -- JSON Basics
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_week09_exercise03.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/week09/exercise03/ and import it as a submodule (e.g.
`from exercises.week09.exercise03 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import json


def save_json(path: str, data) -> None:
    """with open(path, "w") as f: json.dump(data, f)."""
    raise NotImplementedError


def load_json(path: str):
    """with open(path) as f: return json.load(f)."""
    raise NotImplementedError


def to_json_string(data) -> str:
    """json.dumps(data)."""
    raise NotImplementedError


def from_json_string(text: str):
    """json.loads(text)."""
    raise NotImplementedError
