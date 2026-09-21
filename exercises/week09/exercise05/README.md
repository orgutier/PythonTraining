# Datetime Basics

Implement:

- `current_timestamp_iso() -> str` -- `datetime.datetime.now().isoformat()`.
- `format_date(dt) -> str` -- `dt.strftime("%Y-%m-%d")`.
- `parse_iso(text: str)` -- `datetime.datetime.fromisoformat(text)` (the inverse of `.isoformat()`).
- `days_between(d1, d2) -> int` -- `(d2 - d1).days` (subtracting two `datetime`/`date` objects gives a `timedelta`, which has a `.days` attribute).

See the Study Reference presentation, Topic 9, for the theory.
