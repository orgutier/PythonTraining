# Race Results Ledger

A local 5K's raw results arrive as two parallel lists. Given, don't modify:

```python
raw_names = ["Ava", "Ben", "Cy", "Dee", "Emi"]
raw_times = [54.2, 49.8, 61.0, 49.8, 57.3]  # seconds
```

Implement:

- `build_results(names: list[str], times: list[float]) -> list[tuple]` -- start with `results = []`, then use a `for` loop over `zip(names, times)` that `.append()`s each `(name, time)` **tuple** onto `results` one at a time (don't just return `list(zip(...))` directly -- the point here is the explicit loop + `.append()`, not the shortcut).
- `rank_by_time(results: list[tuple]) -> list[tuple]` -- `sorted(results, key=lambda r: r[1])` (fastest time first; `sorted()` returns a **new** list, it never touches `results`).
- `fastest_n(ranked_results: list[tuple], n: int) -> list[tuple]` -- `ranked_results[:n]`.
- `podium_labels(fastest: list[tuple]) -> list[str]` -- `[f"{i+1}. {name} ({time}s)" for i, (name, time) in enumerate(fastest)]` (a list comprehension over `enumerate()`, unpacking each tuple as it goes).
- `racer_count(names: list[str]) -> int` -- `len(names)`.

See the Study Reference presentation, Topic 4 (Basic tier), for the theory.
