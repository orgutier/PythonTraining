# Exceptions and Hierarchies

Implement:

- `ValidationError(Exception)` -- an empty custom exception class (`class ValidationError(Exception): pass`).
- `NegativeValueError(ValidationError)` -- another empty class, this time subclassing `ValidationError` (not `Exception` directly) -- a two-level hierarchy: `NegativeValueError` **is a** `ValidationError` **is a** `Exception`.
- `validate_positive(n: int) -> int` -- return `n` if `n >= 0`, else `raise NegativeValueError(f"negative value: {n}")`.
- `safe_parse_int(s: str)` -- `try: return int(s)` `except ValueError: return None`.
- `divide_with_cleanup(a: float, b: float) -> float` -- `try: return a / b` `except ZeroDivisionError: raise` (re-raise unchanged) `finally:` increment the module-level `_attempts` counter -- `finally` runs whether or not an exception occurred, which is exactly why it's the right place to count *every* attempt, successful or not.
- `get_attempts() -> int` / `reset_attempts() -> None` -- read/reset `_attempts`.

See the Study Reference presentation, Topic 5, for the theory.
