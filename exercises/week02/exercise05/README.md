# Short-Circuit Guards and Truthiness

Implement:

- `is_valid_username(name) -> bool` -- `True` only if `name` is a non-empty `str` of length <= 20. Use one chained `and` expression: `isinstance(name, str) and len(name) > 0 and len(name) <= 20`. Because `and` short-circuits, `len(name)` never runs if `name` isn't a `str` in the first place -- that's the point, not just a style choice.
- `has_valid_first_item(items: list) -> bool` -- `True` only if `items` is non-empty **and** its first item is truthy: `bool(items) and bool(items[0])`. The short-circuit here protects `items[0]` from ever running on an empty list.
- `is_within_bounds(numbers: list[int], index: int) -> bool` -- `True` only if `0 <= index < len(numbers)` **and** `numbers[index] >= 0`. Same guard pattern: the bounds check must pass before `numbers[index]` is safe to evaluate.
- `describe_truthiness(value) -> str` -- `"truthy"` if `value` (bare truthiness check, no `==`), else `"falsy"`.
- `filter_truthy(values: list) -> list` -- `[v for v in values if v]`.
- `count_falsy(values: list) -> int` -- `sum(1 for v in values if not v)`.

See the Study Reference presentation, Topic 2, for the theory.
