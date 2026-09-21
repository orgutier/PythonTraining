import threading
from collections import deque


class BoundedBlockingQueue:
    """
    A thread-safe, fixed-capacity queue whose enqueue/dequeue block
    instead of failing, backed by a single threading.Condition shared by
    both operations (one lock, one condition, two different wait
    predicates -- "not full" for enqueue, "not empty" for dequeue).
    notify_all() is used on every change so any number of waiting
    producers or consumers can be woken to re-check their own condition,
    not just one.

    Edge cases handled:
      - capacity=1: enqueue blocks the moment one element is in the
        queue, and only unblocks once dequeue() removes it -- the same
        Condition mechanism as any other capacity, just a tighter window.
      - dequeue() called before any enqueue(): size() is 0, so the while
        loop's wait() blocks immediately instead of raising or returning
        a sentinel, until an enqueue() arrives.
      - Multiple threads blocked at once: notify_all() (not notify(),
        which would only wake one) is called on every successful
        enqueue/dequeue, so every waiter gets a chance to re-check its
        own condition in its while loop rather than only the single
        thread that happened to be notified.
    """

    def __init__(self, capacity: int) -> None:
        self._capacity = capacity
        self._items: deque[int] = deque()
        self._condition = threading.Condition()

    def enqueue(self, element: int) -> None:
        """Block until there's room, then add element."""
        with self._condition:
            while len(self._items) >= self._capacity:
                self._condition.wait()
            self._items.append(element)
            self._condition.notify_all()

    def dequeue(self) -> int:
        """Block until an element is available, then remove and return it."""
        with self._condition:
            while len(self._items) == 0:
                self._condition.wait()
            element = self._items.popleft()
            self._condition.notify_all()
            return element

    def size(self) -> int:
        """Current number of elements (never blocks)."""
        with self._condition:
            return len(self._items)
