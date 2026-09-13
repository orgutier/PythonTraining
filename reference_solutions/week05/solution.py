import re


def extract_emails(text: str) -> list[str]:
    return re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+", text)


class InvalidLogLineError(Exception):
    """Raised when a log line does not match the expected format."""


def parse_log_line(line: str) -> dict:
    match = re.match(r"^(\d{4}-\d{2}-\d{2})\s+(\w+)\s+(.+)$", line)
    if not match:
        raise InvalidLogLineError(f"Malformed log line: {line!r}")
    date, level, message = match.groups()
    return {"date": date, "level": level, "message": message}
