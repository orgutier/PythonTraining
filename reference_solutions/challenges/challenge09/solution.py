import re


class LogParseError(Exception):
    pass


class MalformedLineError(LogParseError):
    pass


LOG_PATTERN = re.compile(r"(?P<time>\d{2}:\d{2}) (?P<level>\w+) (?P<message>.+)")


def parse_line(line: str, line_number: int) -> dict:
    match = LOG_PATTERN.match(line)
    if match is None:
        raise MalformedLineError(f"line {line_number}: {line!r}")
    result = match.groupdict()
    result["line_number"] = line_number
    return result


def parse_log_file(path: str) -> list:
    """
    Parse every non-blank line of path.

    Edge cases handled:
      - Empty file -> returns [].
      - A malformed line -> LogParseError is raised immediately at that
        line (chained to the underlying MalformedLineError), not after
        scanning the rest of the file.
      - Blank lines -> skipped entirely, not counted as entries or errors.
    """
    entries = []
    with open(path) as f:
        for i, line in enumerate(f, start=1):
            stripped = line.strip()
            if not stripped:
                continue
            try:
                entries.append(parse_line(stripped, i))
            except MalformedLineError as e:
                raise LogParseError(f"failed to parse {path!r}") from e
    return entries


def scan_directory(paths: list) -> tuple:
    all_entries = []
    failed = 0
    for path in paths:
        try:
            all_entries.extend(parse_log_file(path))
        except LogParseError:
            failed += 1
            continue
    return all_entries, failed
