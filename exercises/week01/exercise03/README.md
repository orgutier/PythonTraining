# Type Inspector

Implement:

- `describe_value(value) -> str` -- if `value is None`, return the exact string `"None (the absence of a value)"`. Otherwise return `f"{value!r} is a {type(value).__name__}"` (use `type()`, not `isinstance()`, here).
- `print_type_report(value) -> None` -- `print()` the result of `describe_value(value)`. Nothing to return.
- `classify_values(values: list) -> dict` -- return a dict with keys `"ints"`, `"floats"`, `"strs"`, `"bools"`, `"nones"`, each mapped to a list of the matching items from `values`, preserving order. **`bool` must be checked before `int`**: since `True`/`False` are technically ints, checking `isinstance(v, int)` first would put them in the wrong bucket. Use `type(v) is bool` (not `isinstance`) to catch booleans precisely, then `isinstance(v, int)` / `isinstance(v, float)` / `isinstance(v, str)` for the rest, and `v is None` for the last bucket.

See the Study Reference presentation, Topic 1, for the theory.
