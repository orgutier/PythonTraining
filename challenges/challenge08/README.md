# Challenge 08 — Longest Consecutive Run of Records

**Do this after:** Stage 04 (Data Structures)
**Correctness is pytest-tested:** `python tools/cli.py test challenge08` (or `pytest tests/test_challenge08.py`). The constraints below on *how* you write it are not something pytest can check -- grade those yourself.

## Problem

Longest Consecutive Sequence (LeetCode #128) is a classic test of whether
you reach for a `set` instead of sorting -- O(n) vs O(n log n). This
version asks for the full picture (every run, not just the longest one),
returned as proper records, plus a couple of derived reports.

Implement:

```python
Run = collections.namedtuple("Run", ["start", "length"])

def all_runs(numbers: list) -> list:
    """Every maximal run of consecutive integers in numbers, as Run records sorted by start. Duplicates count once."""

def longest_consecutive_run(numbers: list) -> Run:
    """The single longest Run. Raises ValueError if numbers is empty."""

def runs_overlap(run_a: Run, run_b: Run) -> bool:
    """True if the integer ranges [start, start+length) of the two runs overlap."""

def unique_numbers_covered(runs: list) -> set:
    """Every integer covered by any of runs, as one set (a union of ranges)."""
```

```python
all_runs([100, 4, 200, 1, 3, 2])
# -> [Run(start=1, length=4), Run(start=100, length=1), Run(start=200, length=1)]
longest_consecutive_run([100, 4, 200, 1, 3, 2])   # -> Run(start=1, length=4)
```

## Constraints on HOW you write it

1. **`all_runs` must find run starts in O(n) using a `set`**: build
   `uniq = sorted(set(numbers))` (this one `sorted()` call, on the
   deduplicated numbers, is fine -- it's the classic "sort the *unique*
   values, don't rescan for predecessors" trick, not the brute-force `O(n
   log n)` approach this problem is usually about avoiding, which is
   checking `n - 1 in numbers` for every single number with no dedup
   first). Do **not** call `.sort()`/`sorted()` on the raw `numbers` list
   itself before deduplicating.
2. **`Run` must be a `collections.namedtuple`**, not a plain tuple or a
   `dataclass` -- the point is a lightweight, allocation-free record with
   named field access (`run.start`, `run.length`).
3. **`longest_consecutive_run` must reuse `all_runs`** (call it, then pick
   the max by `.length`) -- don't re-implement the scan a second time.
4. **`unique_numbers_covered` must build its result as a union of
   `range()`-based sets** (`set(range(run.start, run.start + run.length))`
   per run, combined with `|=` or `set.union`), not by manually appending
   every integer in a loop with `.append()`.
5. **A docstring on `all_runs`** listing edge cases: an empty list (no
   runs at all), duplicate numbers (counted once, don't inflate a run's
   length), and negative numbers (runs work the same either side of zero).
