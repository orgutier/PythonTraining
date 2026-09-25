# Testing Without a Framework: Catch the Bug

Every other exercise in this stage asked you to implement something. This one asks you to **verify** something -- with your own hand-rolled tools, not `pytest`/`unittest` (don't import either in this file).

Given, don't modify -- two pairs of functions, each pair *supposed* to compute the same thing; at least one function in each pair has a bug. Your job is to catch it by testing, not to fix it:

```python
def dedupe_correct(items):
    return list(dict.fromkeys(items))

def dedupe_buggy(items):
    return list(set(items))

def evens_correct(numbers):
    return [n for n in numbers if n % 2 == 0]

def evens_buggy(numbers):
    return [n for n in numbers if n % 2 == 1]
```

The spec each pair is supposed to meet:

- **dedupe** should remove duplicates while preserving **first-seen order**.
- **evens** should keep only the **even** numbers from the input, in order.

Implement:

- `check(description: str, condition: bool) -> bool` -- append `(description, condition)` to the given `_check_log` list, then return `condition`. Unlike `assert`, this must **never raise** -- a failed check should become a recorded `False` in the log, not a crash that stops every check after it from running.
- `run_all_checks() -> dict` -- using the shared input `[3, 1, 2, 1, 3, 5, 2]`, call `check()` **exactly four times**, once per function above, each time comparing that function's result on this input against what the *spec* says it should be (compute the expected value yourself, e.g. with a comprehension or `dict.fromkeys` -- not by copying whatever `dedupe_correct`/`evens_correct` happen to return). Then return `{"total": ..., "passed": ..., "failed": ...}` built from `_check_log`: `total` is how many entries it has, `passed` is how many passed, `failed` is the list of descriptions of the ones that didn't.

If you check both functions in a pair against the **same** spec-derived expected value, the buggy one will fail -- that's the whole exercise.

See the Study Reference presentation, Topic 4, for the theory.
