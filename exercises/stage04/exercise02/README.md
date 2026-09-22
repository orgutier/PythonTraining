# Dict and Set Operations

Implement:

- `word_lengths(words: list[str]) -> dict` -- `{w: len(w) for w in words}`.
- `index_lookup(items: list[str]) -> dict` -- `{item: i for i, item in enumerate(items)}`.
- `numbered_pairs(items: list[str]) -> list[tuple]` -- `list(enumerate(items))`.
- `pair_and_dict(keys: list[str], values: list) -> dict` -- `dict(zip(keys, values))`.
- `common_elements(a: set, b: set) -> set` -- `a & b` (intersection).
- `unique_to_first(a: set, b: set) -> set` -- `a - b` (difference).
- `all_elements(a: set, b: set) -> set` -- `a | b` (union).

See the Study Reference presentation, Topic 4, for the theory.
