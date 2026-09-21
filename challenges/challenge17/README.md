# Challenge 17 — Directory Report Builder

**Do this after:** Week 09 (OS, JSON, Datetime, XML)
**Correctness is pytest-tested:** `python tools/cli.py test challenge17` (or `pytest tests/test_challenge17.py`). The constraints below on *how* you write it are not something pytest can check -- grade those yourself.

## Problem

"Write a script that reports on a directory tree" is a real everyday
utility -- and a natural way to combine `os.walk`, `datetime`, and JSON's
`default=` hook (since a directory report naturally wants to carry real
`datetime` objects, which `json.dump` can't serialize on its own).

Implement:

```python
def scan_directory_report(root: str) -> dict:
    """Walk root; for every file, its size (os.path.getsize) and modified time (a real datetime.datetime, from os.path.getmtime via datetime.datetime.fromtimestamp). Return {"total_files": N, "total_size": N, "files": [{"path": ..., "size": ..., "modified": <datetime>}, ...]}, files sorted by path."""

def save_report(report: dict, path: str) -> None:
    """json.dump report to path, with a default= handler for the datetime "modified" values."""

def load_report(path: str) -> dict:
    """json.load path, converting each file's "modified" ISO string back into a real datetime.datetime."""

def list_py_files_pathlib(root: str) -> list:
    """Every .py file under root, found via pathlib.Path(root).rglob("*.py"), returned as a sorted list of str paths."""
```

```python
report = scan_directory_report("some/dir")
report["files"][0]["modified"]   # -> a real datetime.datetime object
save_report(report, "report.json")   # works even though "modified" isn't JSON-native
load_report("report.json")           # "modified" comes back as datetime.datetime again, not a string
```

## Constraints on HOW you write it

1. **`scan_directory_report` must use `os.walk(root)`** to traverse, and
   `os.path.getsize`/`os.path.getmtime` per file -- not `pathlib` (that's
   what `list_py_files_pathlib` is for, as the contrasting modern
   alternative).
2. **`scan_directory_report`'s `"modified"` value must be a real
   `datetime.datetime`**, not a pre-formatted string -- the whole reason
   `save_report` needs a `default=` handler.
3. **`save_report` must pass a `default=` function to `json.dump`** that
   converts a `datetime.datetime` to `obj.isoformat()` and raises
   `TypeError` for anything else -- not pre-converting every datetime to
   a string before calling `json.dump` (that would make `default=`
   pointless).
4. **`load_report` must convert every `"modified"` string back into a
   `datetime.datetime`** via `datetime.datetime.fromisoformat(...)` --
   the round trip through `save_report`/`load_report` should leave you
   with the same *type* of value you started with, not a string.
5. **`list_py_files_pathlib` must use `pathlib.Path(root).rglob("*.py")`**
   -- not `os.walk` with a `.endswith(".py")` filter.
6. **A docstring on `scan_directory_report`** listing edge cases: an
   empty directory (`total_files: 0`, `files: []`), and files nested
   several subdirectories deep (still found, `os.walk` is recursive by
   default).
