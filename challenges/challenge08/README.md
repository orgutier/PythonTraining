# Challenge 08 — Two Sum, Pandas-Style

**Do this after:** Week 10 (Pandas)
**Correctness is pytest-tested:** `python tools/cli.py test challenge08` (or `pytest tests/test_challenge08.py`). The constraints below on *how* you write it are not something pytest can check -- grade those yourself.

## Problem

LeetCode #1 ("Two Sum") is the most famous interview question there is:
given a list of numbers and a target, find the indices of the two
numbers that add up to the target. This challenge asks for the same
thing, but solved the way a data engineer would -- as a `pandas.Series`
operation, not a plain Python loop.

```python
import pandas as pd

numbers = pd.Series([2, 7, 11, 15], index=["a", "b", "c", "d"])
two_sum(numbers, 9)
# -> ("a", "b")   because numbers["a"] + numbers["b"] == 9

two_sum(numbers, 100)
# -> None          no pair sums to 100
```

Note the function returns **index labels**, not positions -- the whole
point is to operate on the Series by its own index, the pandas way.

## Required signature

```python
def two_sum(numbers: "pd.Series", target: int) -> tuple | None:
    ...
```

## Constraints on HOW you write it

1. **No explicit nested loop over the values** (no `for i in ...: for j
   in ...:` comparing every pair -- that's the brute-force O(n^2)
   approach this challenge is specifically about avoiding). Solve it by
   building a second Series of complements (`target - numbers`) and
   using a vectorized/set-based lookup against the original Series'
   index or values -- e.g. `pandas.Series.isin()`, or converting to a
   dict of value -> index for an O(1) lookup pass.
2. **Return index *labels*, not positional integers** -- if the Series
   has a custom index (like the string labels in the example above),
   your answer must use that index, not `.iloc` positions.
3. **A docstring with a comprehensive list of the edge cases your
   implementation handles:** no pair exists (return `None`), the same
   value appears at two different indices and together they sum to the
   target (e.g. `target=8` with two `4`s), and a Series with only one
   element (no valid pair is possible).

## Check your work

`python tools/cli.py test challenge08` runs `tests/test_challenge08.py`,
which checks the examples above plus the documented edge cases.
