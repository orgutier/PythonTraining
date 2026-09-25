# Custom Iterator: CountdownTimer

Implement a class `CountdownTimer` that is its own iterator, counting down from `start` to `0` **inclusive**:

- `__init__(self, start)` -- store `start` and a `current` counter beginning at `start`.
- `__iter__(self)` -- an iterator is required to return itself from `__iter__`: `return self`.
- `__next__(self)` -- if `current < 0`, `raise StopIteration` (the iterator is exhausted -- this must keep happening on every subsequent call, not just the first time past the end). Otherwise, save `current`'s value, decrement `current` by 1, and return the saved value.

This is the exact protocol `for x in some_iterator:` relies on under the hood: it calls `__iter__` once, then `__next__` repeatedly until `StopIteration` is raised. `list(CountdownTimer(3))` should give `[3, 2, 1, 0]`.
