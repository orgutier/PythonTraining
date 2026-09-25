# Testing Without a Framework: Catch the Bug

Every other exercise in this stage asked you to implement something. This one asks you to **verify** something -- with your own hand-rolled tools, not `pytest`/`unittest` (don't import either in this file).

Given, don't modify -- two pairs of classes, each pair *supposed* to behave the same way; at least one class in each pair has a bug. Your job is to catch it by testing, not to fix it:

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32

class TemperatureBuggy:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5

class Counter:
    def __init__(self, start=0):
        self.value = start

    @classmethod
    def from_string(cls, text):
        return cls(int(text))

class CounterBuggy:
    def __init__(self, start=0):
        self.value = start

    @classmethod
    def from_string(cls, text):
        return cls(text)
```

The spec each pair is supposed to meet:

- **fahrenheit** should equal `celsius * 9 / 5 + 32`.
- **from_string** should build an instance whose `.value` is the **integer** the string represents, not the string itself.

Implement:

- `check(description: str, condition: bool) -> bool` -- append `(description, condition)` to the given `_check_log` list, then return `condition`. Unlike `assert`, this must **never raise** -- a failed check should become a recorded `False` in the log, not a crash that stops every check after it from running.
- `run_all_checks() -> dict` -- call `check()` **exactly four times**:
  - `Temperature(100).fahrenheit` and `TemperatureBuggy(100).fahrenheit`, each compared against the spec-computed expected value, `212.0`.
  - `Counter.from_string("5").value` and `CounterBuggy.from_string("5").value`, each compared against the spec-computed expected value, `5` (the `int`, not the string `"5"`).

  Then return `{"total": ..., "passed": ..., "failed": ...}` built from `_check_log`.

See the Study Reference presentation, Topic 6, for the theory.
