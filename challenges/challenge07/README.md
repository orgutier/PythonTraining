# Challenge 07 — Min Stack

**Do this after:** Week 06 (OOP I)
**Correctness is pytest-tested:** `python tools/cli.py test challenge07` (or `pytest tests/test_challenge07.py`). The constraints below on *how* you write it are not something pytest can check -- grade those yourself.

## Problem

Design a stack that supports `push`, `pop`, `top`, and retrieving the
minimum element, **all in O(1) time**.

```python
s = MinStack()
s.push(-2)
s.push(0)
s.push(-3)
s.get_min()   # -> -3
s.pop()
s.top()       # -> 0
s.get_min()   # -> -2
```

This is LeetCode #155, and it's a favorite OOP/data-structure-design
question because the naive approach (`min(self._items)` every time)
"works" but is O(n) per call -- the whole challenge is making `get_min()`
just as fast as `push`/`pop`.

## Required interface

```python
class MinStack:
    def __init__(self) -> None: ...
    def push(self, val: int) -> None: ...
    def pop(self) -> None: ...
    def top(self) -> int: ...
    def get_min(self) -> int: ...
```

## Constraints on HOW you write it

1. **`get_min()` must be O(1)**, not O(n). That rules out scanning the
   stack (or calling `min()` on it) inside `get_min()`. Maintain the
   running minimum incrementally as part of `push`/`pop` instead --
   write a comment above the class explaining your approach (e.g. a
   second stack tracking the min-so-far at each level, or storing
   `(value, min_at_this_point)` pairs).
2. **Do not use `min()` anywhere in your implementation.** Track the
   minimum yourself with comparisons -- using the builtin defeats the
   point of the exercise.
3. **A docstring with a comprehensive list of the edge cases your
   implementation handles:** popping down to an empty stack and then
   pushing again (the min tracking must reset correctly, not get stuck
   on a stale value), pushing the same minimum value more than once and
   then popping one of them (the min must still be correct afterward),
   and a stack containing only one element.
4. **Full type hints**, matching the interface above exactly.

## Check your work

`python tools/cli.py test challenge07` runs `tests/test_challenge07.py`,
which walks through the example above plus the documented edge cases
(including the "push the same min twice, pop once" scenario, which is
the one naive implementations usually get wrong).
