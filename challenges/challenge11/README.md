# Challenge 11 — LRU Cache with a Descriptor and Class-Level Stats

**Do this after:** Stage 06 (OOP I)
**Correctness is pytest-tested:** `python tools/cli.py test challenge11` (or `pytest tests/test_challenge11.py`). The constraints below on *how* you write it are not something pytest can check -- grade those yourself.

## Problem

LRU Cache (LeetCode #146) is one of the most commonly asked interview
problems at every level: build a fixed-capacity least-recently-used cache
with O(1) `get`/`put`. This version asks you to build it the way a real
class would look in a codebase that takes OOP seriously -- validated
attributes, computed properties, and an alternate constructor -- not just
the bare data structure.

Implement:

```python
class PositiveInt:
    """A descriptor: only accepts an int (not bool) > 0."""
    def __set_name__(self, owner, name): ...
    def __get__(self, obj, objtype=None): ...
    def __set__(self, obj, value): ...

class LRUCache:
    capacity = PositiveInt()
    total_caches_created = 0   # shared across every instance

    def __init__(self, capacity: int) -> None: ...

    @staticmethod
    def is_valid_capacity(value) -> bool: ...

    @property
    def hit_rate(self) -> float:
        """self._hits / (self._hits + self._misses), or 0.0 if there have been no get() calls yet."""

    @classmethod
    def with_initial_items(cls, capacity: int, items: dict) -> "LRUCache":
        """A new LRUCache(capacity) with every (key, value) in items already put() into it, in insertion order."""

    def get(self, key) -> int:
        """Return the value for key (counts as a use, moving it to most-recently-used), or -1 if absent (counts as a miss)."""

    def put(self, key, value) -> None:
        """Insert or update key (counts as a use). Evict the least-recently-used key if this would exceed capacity."""
```

```python
cache = LRUCache(2)
cache.put("a", 1)
cache.put("b", 2)
cache.get("a")          # -> 1   (a is now most-recently-used)
cache.put("c", 3)        # over capacity -> evicts "b"
cache.get("b")           # -> -1  (evicted)
cache.hit_rate           # -> 0.5  (1 hit, 1 miss so far)
cache.capacity = 5       # -- goes through the PositiveInt descriptor
LRUCache.total_caches_created   # -> however many LRUCache()s have been built, across ALL of them
```

## Constraints on HOW you write it

1. **`get()` and `put()` must both run in O(1) time.** Track
   most-recently-used order with a hand-built doubly linked list (a small
   `_Node` class with `prev`/`next`), not by scanning a list to find the
   LRU key, and not `collections.OrderedDict` (the point is building the
   O(1) structure yourself).
2. **`LRUCache` must declare `__slots__`** for its actual instance data
   (the map, the two sentinel nodes, hit/miss counters, and whatever the
   `PositiveInt` descriptor needs to store `capacity` under) -- no
   per-instance `__dict__`. This is compatible with `capacity =
   PositiveInt()` being a *class* attribute; `__slots__` only restricts
   *instance* attributes.
3. **`capacity` must be implemented as the `PositiveInt` descriptor**,
   not a `@property`/`@x.setter` pair.
   Setting `cache.capacity = -1` (or any non-positive-int) must raise
   `ValueError`, both at construction and later.
4. **`hit_rate` must be a read-only `@property`** (no setter) -- it's
   *derived* from `_hits`/`_misses`, never set directly.
5. **`is_valid_capacity` must be a `@staticmethod`** (it doesn't touch
   `self` at all) and **`with_initial_items` must be a `@classmethod`**
   using `cls(...)` to construct, not `LRUCache(...)` by name (so a
   subclass calling `with_initial_items` would construct *itself*, not
   hard-code the base class).
6. **A docstring on `get`** listing edge cases: `capacity=1` (every `put`
   evicts the previous key), getting/putting a key already present
   (updates its position without changing the cache's size), and calling
   `get` before any `put` (a miss, `hit_rate` reflects it).
