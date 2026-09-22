# Challenge 16 — Transaction Ledger: Callable and Context Manager

**Do this after:** Stage 08 (The Python Data Model)
**Correctness is pytest-tested:** `python tools/cli.py test challenge16` (or `pytest tests/test_challenge16.py`). The constraints below on *how* you write it are not something pytest can check -- grade those yourself.

## Problem

A companion to Challenge 15: a small transaction ledger that's directly
**callable** to record an entry, and usable as a **context manager** to
batch several entries together with commit-or-rollback semantics -- two
dunders Challenge 15 didn't need. `Ledger` never inherits from any special
base class for either behavior to work; Python finds `__call__`/
`__enter__`/`__exit__` by looking at the object itself. That's the
**protocol vs. explicit inheritance** idea from this stage made concrete.

Implement:

```python
class Ledger:
    def __init__(self) -> None: ...

    def __call__(self, amount: float, description: str = "") -> None:
        """Record (amount, description). If currently inside a `with` block, buffer it instead of committing immediately."""

    def __enter__(self) -> "Ledger":
        """Start a batch: begin buffering calls instead of recording them directly."""

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        """On a clean exit, commit the whole buffered batch. On an exception, discard it (rollback) -- and never suppress the exception."""

    def __len__(self) -> int:
        """Number of COMMITTED entries (never includes an in-progress or rolled-back batch)."""

    def __repr__(self) -> str:
        """f"Ledger({len(self)} entries)"."""

    @property
    def balance(self) -> float:
        """Sum of every committed entry's amount."""
```

```python
ledger = Ledger()
ledger(100, "deposit")          # committed immediately -- not inside a `with`
len(ledger)                      # -> 1

with ledger:
    ledger(-30, "withdrawal")
    ledger(-20, "fee")
len(ledger)                      # -> 3 (both batched entries committed on clean exit)

try:
    with ledger:
        ledger(9999, "should not count")
        raise RuntimeError("oops")
except RuntimeError:
    pass
len(ledger)                      # -> still 3 (the whole batch was rolled back)
```

## Constraints on HOW you write it

1. **`__call__` must check whether a batch is currently open** (an
   instance attribute that's `None` outside a `with` block, and a list
   while inside one) and append to the batch instead of committing
   directly when one is open -- not a separate `record_batched()` method
   the caller has to call themselves.
2. **`__enter__` must start a fresh empty batch and return `self`**, so
   `with ledger as l:` gives you the same ledger back (there's only ever
   one `Ledger` involved, not a separate "transaction" object).
3. **`__exit__` must commit the batch (extend the committed entries) only
   when `exc_type is None`**, discard it otherwise, and **always return
   `False`** -- a `Ledger` batch never swallows an exception raised
   inside its `with` block.
4. **Nesting**: this challenge does not require supporting a `with
   ledger:` inside another `with ledger:` on the *same* ledger -- assume
   batches are never nested.
5. **A docstring on `__exit__`** listing edge cases: a batch with zero
   calls in it (commits an empty batch -- a no-op, `len()` doesn't
   change), and an exception raised partway through a batch (everything
   in that batch is discarded, not just the entries added after the
   exception).
