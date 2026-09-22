# Regex Named Groups

Implement three parsers, each using `re` **named groups** (`(?P<name>...)`) and returning `match.groupdict()`:

- `parse_log_line(line: str) -> dict` -- parse `"LEVEL: message"` (e.g. `"ERROR: disk full"`) with `re.match(r"(?P<level>\w+): (?P<message>.+)", line)`. Raise `ValueError` if it doesn't match.
- `parse_date(text: str) -> dict` -- find the first `YYYY-MM-DD` date anywhere in `text` with `re.search(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})", text)`. Raise `ValueError` if none is found.
- `parse_key_value(text: str) -> dict` -- parse `"key=value"` with `re.match(r"(?P<key>\w+)=(?P<value>.+)", text)`. Raise `ValueError` if it doesn't match.

Named groups turn `match.group(1)`, `match.group(2)`, ... into self-documenting keys in `match.groupdict()` -- much easier to read (and to keep correct after editing the pattern) than counting parentheses.

See the Study Reference presentation, Topic 5, for the theory.
