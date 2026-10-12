# Log Aggregator

Raw log lines from a service, each shaped `"LEVEL:tag"`. Given, don't modify:

```python
log_entries = [
    "ERROR:disk", "INFO:boot", "ERROR:disk", "WARN:mem",
    "ERROR:net", "INFO:boot", "ERROR:disk",
]
```

Implement:

- `entries_by_level(entries: list[str]) -> dict` -- bucket whole entries by their `LEVEL` prefix (`entry.split(":")[0]`) using a `collections.defaultdict(list)` (`.append()` each entry onto `groups[level]`); return `dict(sorted(groups.items()))` so the result is a plain dict with sorted keys.
- `level_counts(entries: list[str]) -> dict` -- extract each entry's level, then `dict(collections.Counter(levels))`.
- `most_common_level(entries: list[str]) -> tuple` -- `collections.Counter(levels).most_common(1)[0]` (a `(level, count)` tuple for the single most frequent level).
- `last_n_entries(entries: list[str], n: int) -> list[str]` -- push every entry, one at a time, onto a `collections.deque(maxlen=n)` (via `.append()`); once it's full, older items automatically fall off the left. Return `list(the_deque)`.
- `rotate_entries(entries: list[str], k: int) -> list[str]` -- build a `collections.deque(entries)`, call `.rotate(k)`, return `list(the_deque)`.

See the Study Reference presentation, Topic 4 (Advanced tier), for the theory.
