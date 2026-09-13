"""
Week 5 - Files, Exceptions, Regex
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in tests/test_week05.py
imports directly from here.
"""


def extract_emails(text: str) -> list[str]:
    """Return every email address found in text, in order of appearance."""
    raise NotImplementedError


class InvalidLogLineError(Exception):
    """Raised when a log line does not match the expected format."""


def parse_log_line(line: str) -> dict:
    """
    Parse a log line of the form "YYYY-MM-DD LEVEL message" into
    {"date": ..., "level": ..., "message": ...}.
    Raise InvalidLogLineError if the line doesn't match.
    """
    raise NotImplementedError
