# Challenge 10 — Log Text Utilities with a Custom Context Manager

**Do this after:** Week 05 (Files, Exceptions, Regex)
**Correctness is pytest-tested:** `python tools/cli.py test challenge10` (or `pytest tests/test_challenge10.py`). The constraints below on *how* you write it are not something pytest can check -- grade those yourself.

## Problem

A companion to Challenge 09: text-processing helpers over raw log
content, plus the same "suppress and count matching exceptions" utility
built **two different ways** -- as a class (`__enter__`/`__exit__`) and as
a `@contextlib.contextmanager` generator -- so you see both sides of how a
context manager actually works.

Implement:

```python
class SuppressAndCount:
    """A class-based context manager: __init__(self, *exc_types) stores them; __enter__ returns self (self.count = 0); __exit__ suppresses (returns True) and increments self.count for a matching exception, else returns False."""

def suppress_and_count(*exc_types):
    """The @contextlib.contextmanager equivalent: yields a {"count": 0} dict, incrementing it (and suppressing) on a matching exception."""

def extract_error_messages(text: str) -> list:
    """Every message that follows "ERROR " on its own line, across the whole text."""

def redact_ips(text: str) -> str:
    """Every IPv4-shaped address in text replaced with "[REDACTED]"."""

def contains_stack_trace(text: str) -> bool:
    """True if text contains the literal line "Traceback (most recent call last):" anywhere."""
```

```python
with SuppressAndCount(ValueError) as counter:
    raise ValueError("bad input")
counter.count   # -> 1

with suppress_and_count(ValueError) as state:
    raise ValueError("bad input")
state["count"]  # -> 1

extract_error_messages("09:00 INFO ok\n09:05 ERROR disk full\n09:06 ERROR timeout")
# -> ["disk full", "timeout"]
redact_ips("connection from 10.0.0.5 refused")
# -> "connection from [REDACTED] refused"
```

## Constraints on HOW you write it

1. **`SuppressAndCount.__exit__` must check `issubclass(exc_type,
   self.exc_types)`** (where `self.exc_types` is the tuple passed to
   `__init__`) before suppressing -- an exception type that wasn't asked
   for must propagate normally (`__exit__` returns `False` for it).
2. **`suppress_and_count` must be a generator** decorated with
   `@contextlib.contextmanager`, catching a matching exception in a
   `try`/`except` **around its `yield`** and *not* re-raising it (that's
   what makes `contextlib.contextmanager` suppress an exception -- catch
   it and let the generator function return normally instead of letting
   the exception propagate back out of it).
3. **`extract_error_messages` must use `re.findall()`** with a capture
   group for the message, applied across the whole multi-line `text` in
   one call (pass `re.MULTILINE` if your pattern needs `^`/`$` to work
   per-line) -- not a manual `for line in text.splitlines()` loop with
   `re.match` per line.
4. **`redact_ips` must use `re.sub()`** with a pattern matching four
   dot-separated groups of 1-3 digits.
5. **`contains_stack_trace` must use `re.search()`**, not `"..." in
   text` -- the point here is specifically practicing `re.search` for a
   fixed substring, even though a plain `in` check would also work.
