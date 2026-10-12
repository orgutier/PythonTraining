# Challenge 03 — Log Stream Parser and Scanner

**Do this after:** Stage 02 (Control Flow)
**Correctness is pytest-tested:** `python tools/cli.py test challenge03` (or `pytest tests/test_challenge03.py`). The constraints below on *how* you write it are not something pytest can check -- grade those yourself.

## Problem

Parsing and scanning a stream of log lines is the loops-and-conditionals
problem that shows up in almost every "read this input and tell me
something about it" interview prompt. This challenge is built to pull in
most of Stage 2's control-flow toolkit at once, not just a `for` loop.

Implement:

```python
def parse_log_stream(lines: list[str]) -> list[tuple[str, str, str]]:
    """Parse each "HH:MM LEVEL message" line into (time, level, message)."""

def first_critical_index(entries: list[tuple], levels: tuple = ("ERROR", "CRITICAL")) -> int:
    """Index of the first entry whose level is in `levels`, or -1 if none is."""

def label_entries(entries: list[tuple]) -> list[str]:
    """["0: LEVEL - message", "1: LEVEL - message", ...]."""

def pair_with_severity(entries: list[tuple], severities: list[int]) -> list[tuple]:
    """[(entry, severity), ...] pairing each entry with its matching severity."""

def is_healthy(entries: list[tuple], levels: tuple = ("CRITICAL",)) -> bool:
    """True only if entries is non-empty AND none of them has a level in `levels`."""
```

```python
lines = ["09:00 INFO boot", "", "09:05 ERROR disk full", "09:06 INFO retrying"]
entries = parse_log_stream(lines)
# -> [("09:00", "INFO", "boot"), ("09:05", "ERROR", "disk full"), ("09:06", "INFO", "retrying")]
first_critical_index(entries)               # -> 1
label_entries(entries)[1]                   # -> "1: ERROR - disk full"
is_healthy(entries)                          # -> True  (no CRITICAL entries)
is_healthy(entries, levels=("ERROR",))      # -> False (there's an ERROR)
```

## Constraints on HOW you write it

1. **`parse_log_stream` must skip blank lines with `continue`**, not an
   `if`/`else` that wraps the rest of the loop body -- and must split each
   line with `line.split(" ", 2)` (`message` can contain spaces; only the
   first two spaces are structural).
2. **`first_critical_index` must be a `for...else`**: `break` the instant
   a matching entry is found (tracking its index via `enumerate`); the
   loop's `else` clause is where `-1` gets returned, for the "searched
   everything, found nothing" case -- not a separate `if` after the loop.
3. **`label_entries` must use `enumerate()`**, and **`pair_with_severity`
   must use `zip()`** -- not manual index tracking (`i = 0; i += 1`) or
   `range(len(...))` for either.
4. **`is_healthy` must be one `and`/`not` expression** (as shown in the
   docstring shape above), relying on short-circuit evaluation and bare
   truthiness of `entries` -- not `if entries == []: return False` before
   a separate check.
5. **A docstring on `parse_log_stream`** listing edge cases: an all-blank
   input, a message that itself contains spaces, and a stream with no
   matching level at all for `first_critical_index`/`is_healthy` to handle
   correctly.
