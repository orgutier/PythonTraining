# Challenge 09 — Log File Parser with a Custom Exception Chain

**Do this after:** Week 05 (Files, Exceptions, Regex)
**Correctness is pytest-tested:** `python tools/cli.py test challenge09` (or `pytest tests/test_challenge09.py`). The constraints below on *how* you write it are not something pytest can check -- grade those yourself.

## Problem

Reading a real log file means three things happening together: file I/O,
a regex pulling structured fields out of free text, and deciding what to
do when a line doesn't match -- raise, skip, or something in between. This
challenge asks for all three, wired together with a proper custom
exception hierarchy instead of bare `Exception`/`ValueError`.

Implement:

```python
class LogParseError(Exception):
    pass

class MalformedLineError(LogParseError):
    pass

LOG_PATTERN = re.compile(r"(?P<time>\d{2}:\d{2}) (?P<level>\w+) (?P<message>.+)")

def parse_line(line: str, line_number: int) -> dict:
    """Match LOG_PATTERN against line; on no match, raise MalformedLineError. On a match, return match.groupdict() plus "line_number"."""

def parse_log_file(path: str) -> list:
    """Read path, parse every non-blank line via parse_line. If any line raises MalformedLineError, catch it and raise LogParseError(...) from that error instead."""

def scan_directory(paths: list) -> tuple:
    """Parse every path via parse_log_file, skipping (not raising for) any whose LogParseError propagates. Return (all_parsed_entries, how_many_files_failed)."""
```

```python
parse_line("09:05 ERROR disk full", 3)
# -> {"time": "09:05", "level": "ERROR", "message": "disk full", "line_number": 3}
parse_line("not a log line", 1)   # -> raises MalformedLineError
```

## Constraints on HOW you write it

1. **`MalformedLineError` must subclass `LogParseError`**, not `Exception`
   directly -- a two-level hierarchy, so catching `LogParseError` also
   catches `MalformedLineError`.
2. **`LOG_PATTERN` must be a module-level `re.compile(...)`**, reused by
   `parse_line` via `LOG_PATTERN.match(line)` -- not a fresh `re.match(...,
   line)` call with the raw pattern string every time.
3. **`parse_log_file` must open the file with `with open(path) as f:`**
   and iterate it with `for i, line in enumerate(f, start=1)`, skipping
   blank lines (after `.strip()`) with `continue`.
4. **`parse_log_file` must catch `MalformedLineError` and re-raise
   `LogParseError(f"failed to parse {path!r}") from e`** -- chaining, so
   the original `MalformedLineError` is still available as `.__cause__`
   on the new exception, not swallowed.
5. **`scan_directory` must catch `LogParseError` per-file** (`try` inside
   the `for` loop, not one `try` wrapping the whole loop, which would stop
   at the first bad file instead of skipping it and continuing).
6. **A docstring on `parse_log_file`** listing edge cases: a completely
   empty file (returns `[]`), a file where every line is malformed (the
   `LogParseError` is raised on the *first* bad line, not after scanning
   the rest), and blank lines mixed in with good ones (skipped, not
   counted as entries or errors).
