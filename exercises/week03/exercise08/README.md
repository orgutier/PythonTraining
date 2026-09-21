# Generators

Implement three generator functions and a consumer:

- `count_up_to(n: int)` -- `yield 1, 2, ..., n` one at a time (a `for` loop with a `yield` inside, not a `return`ed list).
- `evens_only(numbers: list[int])` -- `yield` only the even numbers from `numbers`, in order.
- `infinite_counter()` -- `yield 0, 1, 2, 3, ...` **forever**, no stopping condition (`while True: yield i; i += 1`). Never call `list()` on this one -- it doesn't stop.
- `take(iterable, n: int) -> list` -- return the first `n` items from any iterable (including an infinite one), via `list(itertools.islice(iterable, n))`. This is how you safely consume `infinite_counter()`.

A generator function is any function whose body contains `yield` -- calling it doesn't run any code immediately, it just returns a generator object; the body only executes as you pull values out with `next()` (or a `for` loop, or `itertools.islice`).

See the Study Reference presentation, Topic 3, for the theory.
