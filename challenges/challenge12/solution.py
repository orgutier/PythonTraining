"""
Challenge 12 - Min Stack with Class-Level Push Stats
Interview-style challenge. Correctness is pytest-tested (see
tests/test_challenge12.py / `python tools/cli.py test challenge12`); see
README.md in this folder for the full problem statement and the constraints
your solution must follow (O(1) push/pop/top/minimum without min(), __slots__, a class attribute shared across all instances, @property, @staticmethod, and a @classmethod alternate constructor).

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module, matching the convention used by
exercises/weekNN/solution.py.
"""


class MinStack:
    __slots__ = ("_values", "_mins")

    total_pushes = 0

    def __init__(self) -> None:
        raise NotImplementedError

    @staticmethod
    def is_numeric(value) -> bool:
        """int or float, but not bool."""
        raise NotImplementedError

    def push(self, value) -> None:
        """Push value; raise TypeError if not is_numeric(value). Update MinStack.total_pushes."""
        raise NotImplementedError

    def pop(self) -> None:
        """Remove the top value; raise IndexError if empty."""
        raise NotImplementedError

    @property
    def top(self):
        """The current top value; raise IndexError if empty."""
        raise NotImplementedError

    @property
    def minimum(self):
        """The current minimum value (no min()); raise IndexError if empty."""
        raise NotImplementedError

    @classmethod
    def from_iterable(cls, values) -> "MinStack":
        """A new MinStack with every value in values push()ed, in order."""
        raise NotImplementedError
