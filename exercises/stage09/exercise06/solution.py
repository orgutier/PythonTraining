"""
OS, JSON, Datetime, XML -- Timezone-Aware vs. Naive Datetimes
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage09_exercise06.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage09/exercise06/ and import it as a submodule (e.g.
`from exercises.stage09.exercise06 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import datetime


def naive_now():
    """datetime.datetime.now() -- no timezone info."""
    raise NotImplementedError


def aware_now_utc():
    """datetime.datetime.now(datetime.timezone.utc)."""
    raise NotImplementedError


def is_timezone_aware(dt) -> bool:
    """dt.tzinfo is not None and dt.tzinfo.utcoffset(dt) is not None."""
    raise NotImplementedError


def to_utc_isoformat(dt) -> str:
    """dt.astimezone(datetime.timezone.utc).isoformat()."""
    raise NotImplementedError


def make_aware(dt, tz):
    """dt.replace(tzinfo=tz)."""
    raise NotImplementedError
