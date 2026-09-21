"""
Challenge 02 - LRU Cache
Interview-style challenge. Correctness is pytest-tested (see
tests/test_challenge02.py / `python tools/cli.py test challenge02`); see README.md in this folder
for the full problem statement and the constraints your solution must follow
(O(1) get/put, no collections.OrderedDict, a hand-built doubly linked list,
full docstrings, and a documented list of edge cases).

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module, matching the convention used by
exercises/weekNN/solution.py.
"""


class LRUCache:
    """
    Fixed-capacity least-recently-used cache. Fill in this docstring as
    part of the challenge: explain your data structure choice, why get()
    and put() are both O(1), and the edge cases you handle (capacity of 0,
    get() on a missing key, put() on an existing key, eviction ties).
    """

    def __init__(self, capacity: int) -> None:
        raise NotImplementedError

    def get(self, key: str) -> int:
        """Return the value for key, or -1 if not present. Counts as a use."""
        raise NotImplementedError

    def put(self, key: str, value: int) -> None:
        """Insert or update key. Counts as a use. Evict the LRU key if over capacity."""
        raise NotImplementedError

    def __repr__(self) -> str:
        raise NotImplementedError
