# List and Tuple Basics

Implement:

- `build_shopping_list(items: list[str]) -> list[str]` -- start with `[]` and `.append()` each item from `items` onto it in a `for` loop (don't just return `items`/`list(items)`).
- `unique_sorted(numbers: list[int]) -> list[int]` -- `sorted(set(numbers))`.
- `sort_in_place(items: list) -> None` -- `items.sort()` (the **method**, which mutates in place and returns `None` -- different from the `sorted()` builtin used above, which returns a new list).
- `as_tuple_pairs(names: list[str], ages: list[int]) -> list[tuple]` -- `list(zip(names, ages))`.
- `zip_and_sum(list1: list[int], list2: list[int]) -> list[int]` -- `[a + b for a, b in zip(list1, list2)]`.
- `label_each(items: list[str]) -> list[str]` -- `[f"{i}:{v}" for i, v in enumerate(items)]`.
- `count_items(items: list) -> int` -- `len(items)`.

See the Study Reference presentation, Topic 4, for the theory.
