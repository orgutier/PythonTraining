"""
Challenge 09 - Log File Parser with a Custom Exception Chain
Interview-style challenge. Correctness is pytest-tested (see
tests/test_challenge09.py / `python tools/cli.py test challenge09`); see
README.md in this folder for the full problem statement and the constraints
your solution must follow (a two-level custom exception hierarchy, re.compile()/named groups, with/open/as, and raise ... from ... chaining).

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module, matching the convention used by
exercises/stageNN/solution.py.
"""


import re


class LogParseError(Exception):
    pass


class MalformedLineError(LogParseError):
    pass


LOG_PATTERN = re.compile(r"(?P<time>\d{2}:\d{2}) (?P<level>\w+) (?P<message>.+)")


def parse_line(line: str, line_number: int) -> dict:
    """LOG_PATTERN.match(line); on no match, raise MalformedLineError. Else match.groupdict() + line_number."""
    raise NotImplementedError


def parse_log_file(path: str) -> list:
    """with open(path) as f: parse every non-blank line; chain MalformedLineError into LogParseError."""
    raise NotImplementedError


def scan_directory(paths: list) -> tuple:
    """Parse every path; skip (don't raise for) any that fail. Return (entries, failed_file_count)."""
    raise NotImplementedError
