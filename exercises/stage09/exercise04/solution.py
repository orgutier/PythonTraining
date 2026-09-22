"""
OS, JSON, Datetime, XML -- Custom JSON Encoding
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage09_exercise04.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage09/exercise04/ and import it as a submodule (e.g.
`from exercises.stage09.exercise04 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import json
import datetime


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def point_default(obj):
    """{"x": obj.x, "y": obj.y} for a Point, else raise TypeError."""
    raise NotImplementedError


def serialize_with_points(data) -> str:
    """json.dumps(data, default=point_default)."""
    raise NotImplementedError


def datetime_default(obj):
    """obj.isoformat() for a datetime.datetime, else raise TypeError."""
    raise NotImplementedError


def serialize_with_datetimes(data) -> str:
    """json.dumps(data, default=datetime_default)."""
    raise NotImplementedError


def set_default(obj):
    """sorted(obj) for a set, else raise TypeError."""
    raise NotImplementedError


def serialize_with_sets(data) -> str:
    """json.dumps(data, default=set_default)."""
    raise NotImplementedError
