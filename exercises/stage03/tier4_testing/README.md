# Testing Without a Framework: Catch the Bug

Every other exercise in this stage asked you to implement something. This one asks you to **verify** something -- with your own hand-rolled tools, not `pytest`/`unittest` (don't import either in this file).

Given, don't modify -- two pairs of functions, each pair *supposed* to compute the same thing; at least one function in each pair has a bug. Your job is to catch it by testing, not to fix it:

```python
def factorial_correct(n):
    if n <= 1:
        return 1
    return n * factorial_correct(n - 1)

def factorial_buggy(n):
    if n <= 1:
        return 1
    return n + factorial_buggy(n - 1)

def apply_discount_correct(price, pct=0.1):
    return round(price * (1 - pct), 2)

def apply_discount_buggy(price, pct=0.1):
    return round(price * (1 + pct), 2)
```

Implement:

- `check(description: str, condition: bool) -> bool` -- append `(description, condition)` to the given `_check_log` list, then return `condition`. Unlike `assert`, this must **never raise** -- a failed check should become a recorded `False` in the log, not a crash that stops every check after it from running.
- `run_all_checks() -> dict` -- call `check()` **exactly four times**, once per function above:
  - `check("factorial_correct(5) == 120", factorial_correct(5) == 120)`
  - the same shape for `factorial_buggy(5)` against the same expected value, `120`
  - `apply_discount_correct(100)` against the expected value, `90.0`
  - the same shape for `apply_discount_buggy(100)` against that same expected value, `90.0`

  Then return `{"total": ..., "passed": ..., "failed": ...}` built from `_check_log`: `total` is how many entries it has, `passed` is how many passed, `failed` is the list of descriptions of the ones that didn't.

If you check both functions in a pair against the **same** expected value (the spec, not "whatever that function already returns"), the buggy one will fail -- that's the whole exercise: a check written against the spec catches a real bug instead of rubber-stamping it.

See the Study Reference presentation, Topic 3, for the theory.
