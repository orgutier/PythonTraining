"""
Data Structures -- Log Aggregator
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage04_advanced01.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage04/advanced01/ and import it as a submodule (e.g.
`from exercises.stage04.advanced01 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import collections


def entries_by_level(entries: list[str]) -> dict:
    """Bucket entries by their LEVEL prefix using collections.defaultdict(list); return dict(sorted(...))."""
    raise NotImplementedError


def level_counts(entries: list[str]) -> dict:
    """dict(collections.Counter(levels)) -- levels extracted from each entry's prefix."""
    raise NotImplementedError


def most_common_level(entries: list[str]) -> tuple:
    """collections.Counter(levels).most_common(1)[0]."""
    raise NotImplementedError


def last_n_entries(entries: list[str], n: int) -> list[str]:
    """Push each entry onto a collections.deque(maxlen=n); return list(it)."""
    raise NotImplementedError


def rotate_entries(entries: list[str], k: int) -> list[str]:
    """collections.deque(entries), .rotate(k), then list(it)."""
    raise NotImplementedError
