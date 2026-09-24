"""
OS, JSON, Datetime, XML -- Timezone-Aware Timestamps in JSON
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage09_mid02.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage09/mid02/ and import it as a submodule (e.g.
`from exercises.stage09.mid02 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import datetime
import json


def aware_now_utc():
    """datetime.datetime.now(datetime.timezone.utc)."""
    raise NotImplementedError


def is_timezone_aware(dt) -> bool:
    """dt.tzinfo is not None and dt.tzinfo.utcoffset(dt) is not None."""
    raise NotImplementedError


def make_aware(dt, tz):
    """dt.replace(tzinfo=tz)."""
    raise NotImplementedError


def datetime_default(obj):
    """obj.isoformat() for a datetime.datetime, else raise TypeError."""
    raise NotImplementedError


def serialize_event(name: str, timestamp) -> str:
    """json.dumps({"name": name, "timestamp": timestamp}, default=datetime_default)."""
    raise NotImplementedError
