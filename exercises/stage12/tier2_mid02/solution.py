"""
Requests + Threading -- Locks Guarding Shared State
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage12_tier2_mid02.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage12/tier2_mid02/ and import it as a submodule (e.g.
`from exercises.stage12.tier2_mid02 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import threading


class SafeCounter:
    def __init__(self):
        self._lock = threading.Lock()
        self._value = 0

    def increment(self) -> None:
        """with self._lock: self._value += 1."""
        raise NotImplementedError

    @property
    def value(self) -> int:
        return self._value


class SafeList:
    def __init__(self):
        self._lock = threading.Lock()
        self._items = []

    def append_safe(self, item) -> None:
        """with self._lock: self._items.append(item)."""
        raise NotImplementedError

    @property
    def items(self) -> list:
        return self._items


def transfer_funds(accounts: dict, lock: threading.Lock, from_key, to_key, amount) -> None:
    """with lock: accounts[from_key] -= amount; accounts[to_key] += amount."""
    raise NotImplementedError


def parallel_increment(counter, times: int, num_threads: int) -> None:
    """Split `times` counter.increment() calls across num_threads threads; start then join all."""
    raise NotImplementedError
