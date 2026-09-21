# Pairing and Indexing

Implement:

- `pair_names_scores(names: list[str], scores: list[int]) -> list[tuple]` -- `list(zip(names, scores))`.
- `merge_records(keys: list[str], values: list) -> dict` -- `dict(zip(keys, values))`.
- `count_equal_pairs(list1: list, list2: list) -> int` -- count positions where `list1[i] == list2[i]`, using `zip(list1, list2)` to walk both lists together (don't index manually).
- `indexed_items(items: list[str]) -> list[str]` -- `[f"{i}: {item}" for i, item in enumerate(items)]`.
- `labeled_from(items: list[str], start: int) -> dict` -- `{i: item for i, item in enumerate(items, start)}` (note the second argument to `enumerate` sets the starting index).

See the Study Reference presentation, Topic 2, for the theory.
