# Collections Toolbox

Implement:

- `group_by_first_letter(words: list[str]) -> dict` -- use `collections.defaultdict(list)` to bucket each word under its first letter (`.append()` each word to its bucket); return `dict(sorted(groups.items()))` so the result is a plain dict with sorted keys.
- `count_occurrences(items: list) -> dict` -- `dict(collections.Counter(items))`.
- `most_common_n(items: list, n: int) -> list[tuple]` -- `collections.Counter(items).most_common(n)`.
- `sliding_window_last_n(numbers: list[int], maxlen: int) -> list[int]` -- push every number, one at a time, onto a `collections.deque(maxlen=maxlen)` (via `.append()`); once it's full, older items fall off the left automatically. Return `list(the_deque)` at the end.
- `rotate_queue(items: list, k: int) -> list` -- build a `collections.deque(items)`, call `.rotate(k)`, return `list(the_deque)`.

See the Study Reference presentation, Topic 4, for the theory.
