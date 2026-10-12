# Challenge 04 — Batch Retry Simulator

**Do this after:** Stage 02 (Control Flow)
**Correctness is pytest-tested:** `python tools/cli.py test challenge04` (or `pytest tests/test_challenge04.py`). The constraints below on *how* you write it are not something pytest can check -- grade those yourself.

## Problem

A companion to Challenge 03: given the log entries it parses, batched into
groups, simulate retrying batches until a "clean" one is found -- the same
retry-with-a-give-up-point shape behind real job queues and API retry
logic, and a good excuse to use `while`, `itertools`, and both of Stage 2's
`else`-on-a-loop forms.

Implement:

```python
def retry_until_clean(batches: list[list[tuple]], max_retries: int, bad_levels: tuple = ("ERROR", "CRITICAL")) -> int:
    """Try batches[0], batches[1], ... cyclically, up to max_retries attempts. Return the index (into batches) of the first one with no bad_levels entries, or -1 if none was found within max_retries attempts."""

def group_consecutive_runs(levels: list[str]) -> list[list[str]]:
    """Group consecutive equal values in levels into sublists."""

def status_label(count: int) -> str:
    """"empty" if count == 0, "ok" if 1 <= count < 5, else "busy"."""

def interleave_first_n(batches: list[list], limit: int) -> list:
    """The first `limit` items across all batches, flattened in order."""
```

```python
batches = [
    [("09:00", "ERROR", "x")],
    [("09:01", "INFO", "y")],
]
retry_until_clean(batches, max_retries=3)   # -> 1 (batches[1] has no ERROR/CRITICAL)
retry_until_clean(batches, max_retries=1)   # -> -1 (only tries batches[0] once, never gets to batches[1])

group_consecutive_runs(["A", "A", "B", "A"])   # -> [["A", "A"], ["B"], ["A"]]
status_label(0), status_label(3), status_label(9)   # -> "empty", "ok", "busy"
interleave_first_n([[1, 2], [3, 4, 5]], 3)     # -> [1, 2, 3]
```

## Constraints on HOW you write it

1. **`retry_until_clean` must be a `while` loop with a `while...else`**:
   `break` the moment `batches[attempt % len(batches)]` has no matching
   `bad_levels` entry (return that batch's index); `continue` past a bad
   batch; the loop condition is `attempt < max_retries`; its `else` clause
   (loop ran out of attempts without breaking) is where `-1` comes from.
2. **`group_consecutive_runs` must use `range()`**, comparing
   `levels[i]` to `levels[i - 1]` by index -- not `itertools.groupby`
   (save that for the next function) and not a manual "previous value"
   variable tracked outside the loop.
3. **`status_label` must be one chained ternary expression**
   (`X if cond1 else Y if cond2 else Z`), not `if`/`elif`/`else`
   statements.
4. **`interleave_first_n` must use `itertools.chain.from_iterable` and
   `itertools.islice`** to flatten and truncate in one pass -- not
   `sum(batches, [])` or building a flat list by hand with nested loops.
5. **A docstring on `retry_until_clean`** listing edge cases: an empty
   `batches` list is meaningless (document what your function does --
   raising `ValueError` is reasonable), `max_retries=0` (returns `-1`
   immediately, no attempt made), and `batches[0]` itself already being
   clean (returns `0` on the very first attempt).
