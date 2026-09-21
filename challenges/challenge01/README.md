# Challenge 01 — Typed Config Loader

**Do this after:** Week 01 (Python Fundamentals)
**Correctness is pytest-tested:** `python tools/cli.py test challenge01` (or `pytest tests/test_challenge01.py`). The constraints below on *how* you write it are not something pytest can check -- grade those yourself.

## Problem

Config files are almost always just text -- `KEY=value` lines -- but every
value on the right of the `=` needs to become an actual Python `int`,
`float`, `bool`, `None`, or `str` before your program can use it. This is
the "parse untyped input into typed data" problem every backend engineer
hits in their first week on any real codebase, and it's a natural fit for
everything Week 1 covers: `int`/`float`/`str`/`bool`/`None`/`True`/`False`,
`type()`, `isinstance()`, `and`/`or`/`not`/`is`/`in`, and mutability.

Implement four functions:

```python
def parse_config_line(line: str) -> tuple[str, object]:
    """Parse one "KEY=value" line into (key, typed_value)."""

def load_config(lines: list[str]) -> dict[str, object]:
    """Parse every non-blank line in lines via parse_config_line into a dict."""

def describe_types(config: dict) -> dict[str, str]:
    """{key: type(value).__name__ for key, value in config.items()}."""

def merge_configs(base: dict, override: dict) -> dict:
    """A NEW dict: base's entries, with override's entries taking priority."""
```

### Type inference rules for `parse_config_line`

Split the line on the **first** `=` only (a value may itself contain `=`,
e.g. `URL=http://example.com?x=1`), then strip whitespace from both the key
and the value, then classify the value **in this order**:

1. Value is `""` (empty after stripping) -> `None`.
2. Value is `"true"`/`"false"`, any letter case (`"True"`, `"FALSE"`, ...) -> `bool`.
3. Value is an integer literal (optional leading `-`, otherwise all digits,
   at least one digit) -> `int`.
4. Value is a float literal (optional leading `-`, exactly one `.`, digits
   on both sides, at least one digit on each side) -> `float`.
5. Otherwise -> `str`, unchanged (already stripped).

```python
parse_config_line("PORT=8080")        # -> ("PORT", 8080)
parse_config_line("DEBUG=true")       # -> ("DEBUG", True)
parse_config_line("RATE = 3.14 ")     # -> ("RATE", 3.14)
parse_config_line("TIMEOUT=")         # -> ("TIMEOUT", None)
parse_config_line("NAME=myapp")       # -> ("NAME", "myapp")
parse_config_line("URL=http://x?y=1") # -> ("URL", "http://x?y=1")
```

A line with no `=` at all (e.g. `"# a comment"`) should raise `ValueError`.

## Constraints on HOW you write it

1. **No `try`/`except` anywhere in this challenge.** Numeric detection
   must be done by hand with string methods (`str.isdigit()`, `str.split()`,
   `str.startswith()`) combined with `and`/`or`/`not`/`in` -- not by
   attempting `int(value)`/`float(value)` and catching `ValueError`. The
   point is to practice explicit validation logic, not the EAFP shortcut
   (which is a fine idiom, just not the one this challenge is about).
2. **`describe_types` must use `type()`, not `isinstance()`** -- you want
   the *exact* runtime type name (`"bool"`, not `"int"`, for a boolean
   value -- remember `bool` is a subclass of `int`, so `isinstance(True,
   int)` is `True` even though you want `"bool"` reported here).
3. **`load_config` and `merge_configs` must never mutate their inputs.**
   `merge_configs(base, override)` returns a *new* dict; the caller's
   `base` and `override` must be unchanged afterward (a test checks this
   with `is not`, not just equality). Skip blank (post-`.strip()`-empty)
   lines entirely in `load_config` -- they produce no entry, not a
   `("", None)` one.
4. **Full type hints** on every function signature, matching the ones
   shown above exactly.
5. **A docstring on `parse_config_line`** listing every edge case your
   type-inference logic handles: an empty value, a boolean value in mixed
   case, a value containing `=`, surrounding whitespace on the key and/or
   value, and a line with no `=` at all.
