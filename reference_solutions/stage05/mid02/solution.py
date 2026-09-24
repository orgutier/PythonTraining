import re

LINE_PATTERN = re.compile(r"(?P<key>\w+)=(?P<value>.+)")
DATE_PATTERN = re.compile(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})")
LOG_PATTERN = re.compile(r"(?P<level>\w+): (?P<message>.+)")


def parse_config_line(line: str) -> dict:
    match = LINE_PATTERN.match(line)
    if match is None:
        raise ValueError(f"unparseable config line: {line!r}")
    return match.groupdict()


def find_date(text: str) -> dict:
    match = DATE_PATTERN.search(text)
    if match is None:
        raise ValueError(f"no date found in: {text!r}")
    return match.groupdict()


def parse_log_entry(line: str) -> dict:
    match = LOG_PATTERN.match(line)
    if match is None:
        raise ValueError(f"unparseable log entry: {line!r}")
    return match.groupdict()
