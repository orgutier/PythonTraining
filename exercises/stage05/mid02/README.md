# Config and Log Parsers

Three module-level **compiled** patterns (`re.compile(...)`), each with **named groups** (`(?P<name>...)`), each paired with a parser that returns `match.groupdict()`:

```python
LINE_PATTERN = re.compile(r"(?P<key>\w+)=(?P<value>.+)")
DATE_PATTERN = re.compile(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})")
LOG_PATTERN = re.compile(r"(?P<level>\w+): (?P<message>.+)")
```

Compiling once at module level (instead of calling `re.match`/`re.search` with a raw pattern string every time) is the idiomatic move for a pattern you'll reuse across many calls.

Implement:

- `parse_config_line(line: str) -> dict` -- `LINE_PATTERN.match(line)`; if it's `None`, `raise ValueError(...)`; otherwise return `match.groupdict()` (`{"key": ..., "value": ...}`).
- `find_date(text: str) -> dict` -- `DATE_PATTERN.search(text)` (search anywhere in `text`, not just at the start); `raise ValueError(...)` if none found; otherwise `match.groupdict()` (`{"year": ..., "month": ..., "day": ...}`).
- `parse_log_entry(line: str) -> dict` -- `LOG_PATTERN.match(line)`; `raise ValueError(...)` if it doesn't match; otherwise `match.groupdict()` (`{"level": ..., "message": ...}`).

Named groups turn `match.group(1)`, `match.group(2)`, ... into self-documenting keys in `match.groupdict()` -- much easier to read (and to keep correct after editing the pattern) than counting parentheses.

See the Study Reference presentation, Topic 5 (Mid tier), for the theory.
