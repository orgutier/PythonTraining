# Challenge 06 — Streaming Metrics Aggregator

**Do this after:** Week 03 (Functions)
**Correctness is pytest-tested:** `python tools/cli.py test challenge06` (or `pytest tests/test_challenge06.py`). The constraints below on *how* you write it are not something pytest can check -- grade those yourself.

## Problem

A companion to Challenge 05: simulate a streaming batch processor --
chunking a large dataset with a generator, transforming each chunk, and
tracking a running total -- the shape behind real log/metrics pipelines,
and a good excuse to combine positional-only and keyword-only parameters
in the *same* signature, plus `yield`, `global`, and `functools.partial`.

Implement:

```python
def stream_batches(data: list, size: int, /):
    """Generator: yield successive chunks of data, each up to size items long. Both parameters are positional-only."""

def process_batch(batch: list, /, *, transform=lambda x: x) -> list:
    """[transform(item) for item in batch]; batch is positional-only, transform is keyword-only. Adds len(batch) to the module-level _total_processed counter."""

def get_total_processed() -> int:
    """Return _total_processed."""

def reset_total_processed() -> None:
    """Reset _total_processed to 0."""

def make_scaled_transform(factor: int):
    """A one-arg callable multiplying its input by factor, built with functools.partial (not a lambda/closure)."""
```

```python
list(stream_batches([1, 2, 3, 4, 5], 2))     # -> [[1, 2], [3, 4], [5]]

reset_total_processed()
process_batch([1, 2, 3])                       # -> [1, 2, 3]  (default transform: identity)
process_batch([4, 5], transform=make_scaled_transform(10))   # -> [40, 50]
get_total_processed()                           # -> 5
```

## Constraints on HOW you write it

1. **`stream_batches` must be a real generator function** (a `yield`
   inside a loop, not a function that builds and returns a full list of
   chunks) -- both `data` and `size` are **positional-only**
   (`stream_batches(data=[1, 2], size=1)` must raise `TypeError`).
2. **`process_batch`'s `batch` is positional-only and `transform` is
   keyword-only, in the same signature** (`batch, /, *, transform=...`) --
   calling `process_batch(batch=[1])` or `process_batch([1], lambda x: x)`
   must both raise `TypeError`.
3. **`process_batch` must update the running total through the `global`
   keyword**, not by returning a delta the caller has to add up itself.
4. **`make_scaled_transform` must return `functools.partial(_scale,
   factor)`**, not a `lambda`/inner function that closes over `factor` --
   the module already provides a two-argument `_scale(factor, value)`
   helper for `functools.partial` to bind against.
5. **A docstring on `stream_batches`** listing edge cases: `data` whose
   length isn't a multiple of `size` (the last chunk is shorter, as in the
   example above), and an empty `data` list (yields nothing at all).
