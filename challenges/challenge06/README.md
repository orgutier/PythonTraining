# Challenge 06 — Longest Consecutive Sequence

**Do this after:** Week 04 (Data Structures)
**Correctness is pytest-tested:** `python tools/cli.py test challenge06` (or `pytest tests/test_challenge06.py`). The constraints below on *how* you write it are not something pytest can check -- grade those yourself.

## Problem

Given an unsorted list of integers, return the length of the longest run of
consecutive integers (they don't need to appear in order or adjacent to
each other in the list -- just exist somewhere in it).

```python
longest_consecutive([100, 4, 200, 1, 3, 2])
# -> 4   (the sequence is 1, 2, 3, 4)

longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
# -> 9   (0 through 8)
```

This is LeetCode #128, and interviewers ask it specifically because the
obvious solution (sort, then scan) is O(n log n), but a *set*-based
solution can do it in O(n) -- the follow-up question is always "can you
do better than sorting?"

## Required signature

```python
def longest_consecutive(nums: list[int]) -> int:
    ...
```

## Constraints on HOW you write it

1. **No sorting.** Don't call `sorted()` or `.sort()` anywhere -- the whole
   point of this challenge is the O(n) set-based technique, not the
   O(n log n) sort-then-scan one.
2. **O(n) time overall.** Put every number in a `set` first (O(1)
   membership checks), then only *start* counting a sequence from a
   number `x` when `x - 1` is not in the set (i.e. `x` is the start of its
   run) -- that check is what keeps this from secretly becoming O(n^2).
   Write a comment above the function stating the time and space
   complexity you achieve.
3. **A docstring with a comprehensive list of the edge cases your
   implementation handles:** an empty list (what should it return?), a
   list with duplicate values (e.g. `[1, 1, 2]`), a single-element list,
   negative numbers, and a list where every number is already one
   contiguous run.

## Check your work

`python tools/cli.py test challenge06` runs `tests/test_challenge06.py`,
which checks the examples above plus the documented edge cases.
