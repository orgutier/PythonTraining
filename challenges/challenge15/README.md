# Challenge 15 — Matrix: A Rich Numeric Type

**Do this after:** Stage 08 (The Python Data Model)
**Correctness is pytest-tested:** `python tools/cli.py test challenge15` (or `pytest tests/test_challenge15.py`). The constraints below on *how* you write it are not something pytest can check -- grade those yourself.

## Problem

"Implement a Matrix class" is a real interview staple precisely because it
forces you to decide what `+`, `==`, `len()`, indexing, iteration, and
`bool()` should each mean for a type that isn't a builtin -- exactly what
Stage 8's dunder methods are *for*. This challenge asks for essentially
every dunder from this stage on one cohesive class.

Implement:

```python
class Matrix:
    def __init__(self, rows: list) -> None:
        """Store rows as a tuple of tuples (immutable, hashable)."""

    def __repr__(self) -> str: ...
    def __str__(self) -> str:
        """Rows joined by "\n", values within a row joined by " "."""
    def __eq__(self, other) -> bool: ...
    def __hash__(self) -> int: ...
    def __add__(self, other):
        """Element-wise sum if other is a same-shape Matrix, else NotImplemented."""
    def __radd__(self, other):
        """self if other == 0 (for sum()), else NotImplemented."""
    def __len__(self) -> int:
        """Number of rows."""
    def __getitem__(self, index):
        """The row at index (a tuple)."""
    def __iter__(self):
        """Iterate over rows."""
    def __contains__(self, value) -> bool:
        """True if value appears anywhere in any row."""
    def __bool__(self) -> bool:
        """False only if there are no rows, or every value in every row is 0."""
```

```python
m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[10, 20], [30, 40]])
m1 + m2          # -> Matrix([[11, 22], [33, 44]])
sum([m1, m2])     # -> Matrix([[11, 22], [33, 44]])  (via __radd__)
len(m1)           # -> 2
m1[0]             # -> (1, 2)
list(m1)          # -> [(1, 2), (3, 4)]
3 in m1           # -> True
bool(Matrix([[0, 0]]))   # -> False
```

## Constraints on HOW you write it

1. **`__add__` must return `NotImplemented` (not raise) for a
   non-`Matrix` or mismatched-shape `other`** -- that's what lets Python
   fall back cleanly (and raise its own clear `TypeError` if nothing else
   can handle it either) instead of your code raising a confusing one.
2. **`__radd__` must special-case `other == 0`** (returning `self`) and
   return `NotImplemented` otherwise -- this is exactly what makes
   `sum([m1, m2, m3])` work, since `sum()` starts from `0 + m1`.
3. **`__eq__` and `__hash__` must be consistent**: equal matrices (same
   rows) must hash equal. Store `rows` as a tuple of tuples specifically
   so `hash(self.rows)` works at all (a tuple of lists wouldn't be
   hashable).
4. **`__bool__` must check every value in every row**, not just whether
   `rows` is non-empty -- a `Matrix([[0, 0], [0, 0]])` has rows, but
   should still be falsy.
5. **`__getitem__`/`__iter__`/`__contains__` must all operate on `rows`
   directly** (delegate to the underlying tuple's own behavior /
   `any(...)`, don't reimplement indexing or the "is it in here" scan
   from scratch).
6. **A docstring on `__add__`** listing edge cases: adding two matrices of
   different shapes (returns `NotImplemented`, so `m1 + "not a matrix"`
   and `m1 + Matrix([[1]])` both end up raising `TypeError` from Python
   itself), and a 1x1 matrix (still works like any other size).
