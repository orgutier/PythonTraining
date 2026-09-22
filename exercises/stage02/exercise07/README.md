# The else Clause on Loops

`for` and `while` loops can both carry an `else` clause that runs only if the loop finished *without* hitting a `break`. Implement:

- `contains_value(items: list, target) -> bool` -- `for...else`: `break` when `item == target` is found; the `else` clause returns `False`.
- `all_positive(numbers: list[int]) -> bool` -- `for...else`: `break` the moment a non-positive number is found; the `else` clause returns `True` (every number was positive).
- `find_first_negative_index(numbers: list[int]) -> int` -- `while...else`: walk an index `i` with a `while` loop, `break` when `numbers[i] < 0`; the `else` clause (loop ran out without breaking) returns `-1`.
- `retry_until_success(attempts: list[bool]) -> bool` -- `while...else`: walk `attempts` with a `while` loop, `break` on the first `True`; the `else` clause returns `False` (never succeeded).
- `first_positive_index(numbers: list[int]) -> int` -- `while...else`: same shape as `find_first_negative_index`, but for the first positive number; `else` returns `-1`.

See the Study Reference presentation, Topic 2, for the theory.
