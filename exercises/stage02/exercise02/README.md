# Loop Controls

Implement:

- `sum_until_negative(numbers: list[int]) -> int` -- sum numbers with a `for` loop, `break`-ing the instant you hit a negative one (don't include it in the sum).
- `skip_multiples(numbers: list[int], factor: int) -> list[int]` -- `for` over numbers, `continue`-ing past (skipping) any multiple of `factor`, collecting the rest.
- `countdown(n: int) -> list[int]` -- `[n, n-1, ..., 1]` built with a `while` loop (not `range`).
- `safe_int_list(values: list) -> list[int]` -- try `int(v)` for each `v`; on `ValueError`/`TypeError`, silently skip it with `except (...): pass` and move on. This is the standard, idiomatic use of `pass`: an intentionally empty except block.

See the Study Reference presentation, Topic 2, for the theory.
