"""
Data Structures -- Collections Toolbox
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the aggregated test suite in
tests/test_week04.py imports directly from here. Need a helper function or
class of your own? Add another .py file next to this one inside
exercises/week04/exercise04/ and import it as a submodule (e.g.
`from exercises.week04.exercise04 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import collections


def group_by_first_letter(words: list[str]) -> dict:
    """Bucket words by first letter using collections.defaultdict(list)."""
    raise NotImplementedError


def count_occurrences(items: list) -> dict:
    """dict(collections.Counter(items))."""
    raise NotImplementedError


def most_common_n(items: list, n: int) -> list:
    """collections.Counter(items).most_common(n)."""
    raise NotImplementedError


def sliding_window_last_n(numbers: list[int], maxlen: int) -> list[int]:
    """Push each number onto a collections.deque(maxlen=maxlen); return list(it)."""
    raise NotImplementedError


def rotate_queue(items: list, k: int) -> list:
    """collections.deque(items), .rotate(k), then list(it)."""
    raise NotImplementedError
