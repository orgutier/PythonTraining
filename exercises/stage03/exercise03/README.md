# Lambdas and Higher-Order Functions

Implement:

- `make_multiplier(factor: int)` -- return a one-argument callable equivalent to `lambda x: x * factor`, built with an actual `lambda`.
- `sort_by_length(words: list[str]) -> list[str]` -- `sorted(words, key=lambda w: len(w))`.
- `top_scorer(records: list[dict]) -> dict` -- `max(records, key=lambda r: r["score"])`.

All three use a `lambda` -- short, throwaway functions passed directly where a callable is expected, instead of a separate `def`.

See the Study Reference presentation, Topic 3, for the theory.
