# Challenge 12 — Min Stack with Class-Level Push Stats

**Do this after:** Week 06 (OOP I)
**Correctness is pytest-tested:** `python tools/cli.py test challenge12` (or `pytest tests/test_challenge12.py`). The constraints below on *how* you write it are not something pytest can check -- grade those yourself.

## Problem

Min Stack (LeetCode #155) asks for a stack that also supports O(1)
`minimum()`. This version wraps the classic two-stacks trick in a class
that also tracks how many pushes have happened **across every `MinStack`
that's ever been created**, using a class attribute -- a very concrete way
to feel the instance-vs-class-attribute distinction.

Implement:

```python
class MinStack:
    __slots__ = ("_values", "_mins")
    total_pushes = 0   # shared across ALL MinStack instances

    def __init__(self) -> None: ...

    @staticmethod
    def is_numeric(value) -> bool:
        """int or float, but not bool."""

    def push(self, value) -> None:
        """Push value. Raises TypeError if not is_numeric(value)."""

    def pop(self) -> None:
        """Remove the top value. Raises IndexError if empty."""

    @property
    def top(self):
        """The current top value. Raises IndexError if empty."""

    @property
    def minimum(self):
        """The current minimum value. Raises IndexError if empty."""

    @classmethod
    def from_iterable(cls, values) -> "MinStack":
        """A new MinStack with every value in values push()ed, in order."""
```

```python
stack = MinStack()
stack.push(3)
stack.push(1)
stack.push(2)
stack.minimum   # -> 1
stack.pop()
stack.top        # -> 1
stack.minimum   # -> 1   (still, since 1 hasn't been popped)

MinStack.total_pushes   # -> 3, and shared with every OTHER MinStack too
```

## Constraints on HOW you write it

1. **`push`, `pop`, `top`, and `minimum` must all run in O(1) time**, and
   **`minimum` must never call the builtin `min()`.** Track it with a
   second, parallel stack (`_mins`): push the smaller of `(value,
   _mins[-1])` (or just `value` if `_mins` is empty) every time you push
   onto `_values`; pop both stacks together.
2. **`MinStack` must declare `__slots__ = ("_values", "_mins")`** -- no
   per-instance `__dict__`.
3. **`total_pushes` must be incremented on the *class*, not the
   instance** (`MinStack.total_pushes += 1`, not `self.total_pushes +=
   1` -- the latter would create a brand-new *instance* attribute
   shadowing the shared class one, instead of updating the count every
   `MinStack` shares).
4. **`top` and `minimum` must be read-only `@property`s** (no setters --
   there's nothing sensible to assign to either).
5. **`is_numeric` must be a `@staticmethod`**, and **`from_iterable` must
   be a `@classmethod`** using `cls()` to construct.
6. **A docstring on `push`** listing edge cases: pushing a non-numeric
   value (rejected with `TypeError`, and `total_pushes` must **not**
   increment for a rejected push), pushing a `bool` (also rejected --
   `bool` is technically an `int` subclass but isn't a "numeric value"
   for this stack), and popping/reading `top`/`minimum` on an empty
   stack.
