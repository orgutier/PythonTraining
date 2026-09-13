"""
Week 9 - OS, JSON, Datetime, XML
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in tests/test_week09.py
imports directly from here.
"""


def read_config(path: str) -> dict:
    raise NotImplementedError


def write_config(path: str, data: dict) -> None:
    raise NotImplementedError


def timestamp_now() -> str:
    """Return the current UTC time as an ISO-8601 string."""
    raise NotImplementedError


def parse_xml_titles(xml_string: str) -> list[str]:
    """Return the text of every <title> element in xml_string, in order."""
    raise NotImplementedError
