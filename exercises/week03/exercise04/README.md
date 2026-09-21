# Scope: global and nonlocal

Implement a module-level counter using `global`, and three closures using `nonlocal`:

- `_counter = 0` (module-level variable, already in the stub).
- `increment_counter() -> int` -- `global _counter`, `_counter += 1`, return the new value.
- `reset_counter() -> None` -- `global _counter`, set it back to `0`.
- `set_counter(value: int) -> None` -- `global _counter`, set it directly to `value`.
- `get_counter() -> int` -- return `_counter`. No `global` needed here: `global` is only required when *assigning* to a module-level name from inside a function, not when reading it.
- `make_counter()` -- return a zero-arg function that returns `1, 2, 3, ...` on successive calls: a local `count = 0` inside `make_counter`, an inner `counter()` that does `nonlocal count; count += 1; return count`. This is a **closure**: each call to `make_counter()` creates a fresh, independent `count`.
- `make_accumulator(start: int = 0)` -- return a one-arg `add(x)` closure that adds `x` to a running total (starting at `start`) and returns the new total, using `nonlocal`.
- `make_toggle(initial: bool = False)` -- return a zero-arg closure that flips and returns a running bool each call, using `nonlocal`.

See the Study Reference presentation, Topic 3, for the theory.
