import re


def parse_log_line(line: str) -> dict:
    match = re.match(r"(?P<level>\w+): (?P<message>.+)", line)
    if match is None:
        raise ValueError(f"unparseable log line: {line!r}")
    return match.groupdict()


def parse_date(text: str) -> dict:
    match = re.search(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})", text)
    if match is None:
        raise ValueError(f"no date found in: {text!r}")
    return match.groupdict()


def parse_key_value(text: str) -> dict:
    match = re.match(r"(?P<key>\w+)=(?P<value>.+)", text)
    if match is None:
        raise ValueError(f"unparseable key=value: {text!r}")
    return match.groupdict()
