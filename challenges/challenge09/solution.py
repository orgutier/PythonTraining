"""
Challenge 09 - Bounded Blocking Queue
Interview-style challenge (LeetCode #1188). Correctness is pytest-tested
(see tests/test_challenge09.py / `python tools/cli.py test challenge09`);
see README.md in this folder for the full problem statement and the
constraints your solution must follow (threading.Condition, not
sleep-and-poll; correct under multiple producers/consumers; a docstring
listing the edge cases handled).

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module, matching the convention used by
exercises/weekNN/solution.py.
"""
import threading


class BoundedBlockingQueue:
    """
    A thread-safe, fixed-capacity queue whose enqueue/dequeue block
    instead of failing. Fill in this docstring as part of the challenge:
    explain your condition-variable design and document the edge cases
    you handle (capacity=1, dequeue-before-any-enqueue, multiple blocked
    threads waking correctly).
    """

    def __init__(self, capacity: int) -> None:
        raise NotImplementedError

    def enqueue(self, element: int) -> None:
        """Block until there's room, then add element."""
        raise NotImplementedError

    def dequeue(self) -> int:
        """Block until an element is available, then remove and return it."""
        raise NotImplementedError

    def size(self) -> int:
        """Current number of elements (never blocks)."""
        raise NotImplementedError
