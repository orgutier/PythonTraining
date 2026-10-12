"""
Challenge 11 - LRU Cache with a Descriptor and Class-Level Stats
Interview-style challenge. Correctness is pytest-tested (see
tests/test_challenge11.py / `python tools/cli.py test challenge11`); see
README.md in this folder for the full problem statement and the constraints
your solution must follow (a hand-built doubly linked list for O(1) operations, __slots__, a validating descriptor for `capacity`, a computed @property, @staticmethod, and a @classmethod alternate constructor).

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module, matching the convention used by
exercises/stageNN/solution.py.
"""


class _Node:
    __slots__ = ("key", "value", "prev", "next")

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class PositiveInt:
    def __set_name__(self, owner, name):
        self._name = "_" + name

    def __get__(self, obj, objtype=None):
        raise NotImplementedError

    def __set__(self, obj, value):
        """Raise ValueError unless value is an int (not bool) > 0."""
        raise NotImplementedError


class LRUCache:
    __slots__ = ("_capacity", "_map", "_head", "_tail", "_hits", "_misses")

    capacity = PositiveInt()
    total_caches_created = 0

    def __init__(self, capacity: int) -> None:
        raise NotImplementedError

    @staticmethod
    def is_valid_capacity(value) -> bool:
        """int (not bool) and > 0."""
        raise NotImplementedError

    @property
    def hit_rate(self) -> float:
        """self._hits / (self._hits + self._misses), or 0.0 if none yet."""
        raise NotImplementedError

    @classmethod
    def with_initial_items(cls, capacity: int, items: dict) -> "LRUCache":
        """A new cls(capacity) with every item in items already put() in, in order."""
        raise NotImplementedError

    def get(self, key) -> int:
        """Return the value for key (a hit, moves it to MRU), or -1 (a miss)."""
        raise NotImplementedError

    def put(self, key, value) -> None:
        """Insert/update key; evict the LRU key if over capacity."""
        raise NotImplementedError
