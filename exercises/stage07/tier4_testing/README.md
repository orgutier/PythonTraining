# Testing Without a Framework: Catch the Bug

Every other exercise in this stage asked you to implement something. This one asks you to **verify** something -- with your own hand-rolled tools, not `pytest`/`unittest` (don't import either in this file).

Given, don't modify -- two pairs of implementations, each pair *supposed* to behave the same way; at least one in each pair has a bug. Your job is to catch it by testing, not to fix it:

```python
class Shape:
    def area(self):
        raise NotImplementedError

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class SquareBuggy(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * 2

class Duck:
    def quack(self):
        return "Quack!"

def make_it_quack_correct(obj):
    return obj.quack()

def make_it_quack_buggy(obj):
    return obj.quack
```

The spec each pair is supposed to meet:

- **area** (on a `Shape` subclass) should equal `side ** 2` for a square.
- **make_it_quack** should **call** the object's `.quack()` method and return its result (a `str`), not the method object itself.

Implement:

- `check(description: str, condition: bool) -> bool` -- append `(description, condition)` to the given `_check_log` list, then return `condition`. Unlike `assert`, this must **never raise** -- a failed check should become a recorded `False` in the log, not a crash that stops every check after it from running.
- `run_all_checks() -> dict` -- call `check()` **exactly four times**:
  - `Square(4).area()` and `SquareBuggy(4).area()`, each compared against the spec-computed expected value, `16`.
  - `make_it_quack_correct(Duck())` and `make_it_quack_buggy(Duck())`, each compared against the spec-computed expected value, `"Quack!"`.

  Then return `{"total": ..., "passed": ..., "failed": ...}` built from `_check_log`.

See the Study Reference presentation, Topic 7, for the theory.
