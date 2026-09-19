# Challenge 02 — LRU Cache

**Do this after:** Week 06 (OOP I)
**Correctness is pytest-tested:** `python tools/cli.py test challenge02` (or `pytest tests/test_challenge02.py`). The constraints below on *how* you write it are not something pytest can check -- grade those yourself.

## Problem

Implement a fixed-capacity Least-Recently-Used (LRU) cache: a key-value
store that holds at most `capacity` items, and when a `put()` would exceed
that capacity, evicts whichever key was used least recently (by `get()` or
`put()`) before inserting the new one. This is one of the most commonly
asked interview problems at every level (it's LeetCode #146) because it
tests data-structure design under real constraints, not just syntax.

```python
cache = LRUCache(capacity=2)
cache.put("a", 1)
cache.put("b", 2)
cache.get("a")        # -> 1   (a is now the most recently used)
cache.put("c", 3)      # capacity exceeded -> evicts "b" (least recently used)
cache.get("b")         # -> -1  (evicted, not found)
```

## Required interface

```python
class LRUCache:
    def __init__(self, capacity: int) -> None: ...
    def get(self, key: str) -> int:
        """Return the value for key, or -1 if not present. Counts as a use."""
    def put(self, key: str, value: int) -> None:
        """Insert or update key. Counts as a use. Evict the LRU key if over capacity."""
```

## Constraints on HOW you write it

1. **`get()` and `put()` must both run in O(1) time.** That rules out
   scanning a list to find the least-recently-used key. Write a comment
   above the class explaining *why* your chosen data structure achieves
   O(1) for both operations.
2. **You may not use `collections.OrderedDict`** (or any other library
   that solves this for you). Build the ordering mechanism yourself: a
   dict for O(1) key lookup, combined with a manually-implemented doubly
   linked list (write your own `Node` class) to track usage order in O(1).
   This is the actual point of the exercise -- an interviewer asking this
   question wants to see you build the linked list, not import one.
3. **Full docstrings** on the class and on both public methods, each
   covering: what it does, its time complexity, and its behavior on edge
   cases.
4. **A comprehensive list of edge cases**, documented in the class
   docstring, that your implementation is expected to handle: `capacity`
   of 0 (nothing should ever be stored), calling `get()` on a key that was
   never inserted, calling `put()` again on a key that already exists
   (update the value *and* mark it most-recently-used, without changing
   capacity usage), and eviction order when several keys are tied for
   "used longest ago" (evict whichever became LRU first).
5. **Implement `__repr__`** so printing the cache shows its contents
   ordered from most-recently-used to least-recently-used -- this is your
   Topic 8 (Python Data Model) callback, and it's also how you'll debug it.

## Complexity target

`get()` and `put()`: O(1) time each. Space: O(capacity).
