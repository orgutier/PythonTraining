# Challenge 09 — Bounded Blocking Queue

**Do this after:** Week 12 (Requests + Threading)
**Correctness is pytest-tested:** `python tools/cli.py test challenge09` (or `pytest tests/test_challenge09.py`). The constraints below on *how* you write it are not something pytest can check -- grade those yourself.

## Problem

Implement a thread-safe, fixed-capacity queue: `enqueue(element)` blocks
(waits) if the queue is already full instead of raising or dropping the
element, and `dequeue()` blocks if the queue is empty instead of
returning a sentinel. Once space/an element becomes available, a
blocked caller wakes up and completes.

This is LeetCode #1188 ("Design Bounded Blocking Queue"), a real
producer/consumer concurrency problem -- the kind of thing that comes up
whenever a system needs backpressure between a fast producer and a
slower consumer (or vice versa).

## Required interface

```python
class BoundedBlockingQueue:
    def __init__(self, capacity: int) -> None: ...
    def enqueue(self, element: int) -> None:
        """Block until there's room, then add element."""
    def dequeue(self) -> int:
        """Block until an element is available, then remove and return it."""
    def size(self) -> int:
        """Current number of elements (never blocks)."""
```

## Constraints on HOW you write it

1. **Use `threading.Condition` to block, not a sleep-and-poll loop.**
   A `while queue_is_full: time.sleep(0.01)` "works" but wastes CPU and
   adds latency; a proper solution calls `condition.wait()` and lets
   another thread's `enqueue`/`dequeue` call `condition.notify()` (or
   `notify_all()`) to wake it. Write a comment explaining which
   condition(s) you used and why.
2. **Must be correct with multiple producer and multiple consumer
   threads running at once** -- not just one producer and one consumer.
   That means every check-then-act sequence (checking if there's room,
   then adding) has to happen while holding the lock, and has to
   re-check its condition in a `while` loop (not `if`) after waking up,
   since another thread might have grabbed the last slot first.
3. **A docstring with a comprehensive list of the edge cases your
   implementation handles:** `capacity=1` (only one element in flight at
   a time), a `dequeue()` call that arrives before any `enqueue()` (it
   must block, not error), and what happens when multiple threads are
   all blocked waiting at once (all of them must eventually be woken,
   not just one, as capacity/elements keep freeing up).

## Check your work

`python tools/cli.py test challenge09` runs `tests/test_challenge09.py`,
which includes a real multi-producer/multi-consumer test with a small
capacity and a timeout, so a solution that deadlocks or loses a wakeup
will actually fail instead of just running slow.
