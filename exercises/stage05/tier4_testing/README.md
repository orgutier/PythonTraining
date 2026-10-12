# Testing Without a Framework: Catch the Bug

Every other exercise in this stage asked you to implement something. This one asks you to **verify** something -- with your own hand-rolled tools, not `pytest`/`unittest` (don't import either in this file, and don't use `pytest.raises` -- catch exceptions with a plain `try`/`except` yourself).

Given, don't modify -- two pairs of functions, each pair *supposed* to behave the same way; at least one function in each pair has a bug. Your job is to catch it by testing, not to fix it:

```python
def safe_divide_correct(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

def safe_divide_buggy(a, b):
    return a / b

import re

def looks_like_email_correct(text):
    return re.match(r"^[\w.+-]+@[\w-]+\.[\w.-]+$", text) is not None

def looks_like_email_buggy(text):
    return re.match(r"[\w.+-]+@[\w-]+\.[\w.-]+", text) is not None
```

The spec each pair is supposed to meet:

- **safe_divide** should return `None` when dividing by zero, **never raise** `ZeroDivisionError`.
- **looks_like_email** should return `True` only if the **entire** string looks like an email address -- not just a string that happens to *contain* one.

Implement:

- `check(description: str, condition: bool) -> bool` -- append `(description, condition)` to the given `_check_log` list, then return `condition`. Unlike `assert`, this must **never raise** -- a failed check should become a recorded `False` in the log, not a crash that stops every check after it from running.
- `run_all_checks() -> dict` -- call `check()` **exactly four times**:
  - For each of `safe_divide_correct(5, 0)` and `safe_divide_buggy(5, 0)`: call it wrapped in your own `try`/`except ZeroDivisionError`, treating an unexpected raise as a **failed** check (not a crash of `run_all_checks` itself) rather than letting it propagate; the condition either way is "did this return `None` without raising?".
  - For each of `looks_like_email_correct(...)` and `looks_like_email_buggy(...)`, called on the same string `"a@b.co plus extra junk"`: the condition is "did this return `False`?" (since the whole string is not just an email).

  Then return `{"total": ..., "passed": ..., "failed": ...}` built from `_check_log`.

This is exactly what a test framework's `pytest.raises` does for you automatically -- here you're building the same safety net by hand.

See the Study Reference presentation, Topic 5, for the theory.
