# Ranges and Itertools

Implement:

- `stepped_range(start: int, stop: int, step: int) -> list[int]` -- `list(range(start, stop, step))`.
- `numbered_multiples(n: int, factor: int) -> list[str]` -- build the multiples of `factor` up to `n` with `range(factor, n + 1, factor)`, then label each with its position via `enumerate(...)`, returning `[f"{i}: {v}" for i, v in enumerate(multiples)]`.
- `cycle_colors(colors: list[str], count: int) -> list[str]` -- the first `count` items of `colors` repeated forever, via `itertools.islice(itertools.cycle(colors), count)`.
- `chain_lists(list1: list, list2: list) -> list` -- `list(itertools.chain(list1, list2))`.
- `all_pairs(list1: list, list2: list) -> list[tuple]` -- every `(a, b)` combination, via `list(itertools.product(list1, list2))`.

See the Study Reference presentation, Topic 2, for the theory.
