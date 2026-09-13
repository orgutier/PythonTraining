import pytest
from exercises.week05.solution import (
    extract_emails,
    parse_log_line,
    InvalidLogLineError,
)


def test_extract_emails():
    text = "Contact a@x.com or b@y.org, cc c@z.net"
    assert extract_emails(text) == ["a@x.com", "b@y.org", "c@z.net"]


def test_parse_log_line_valid():
    result = parse_log_line("2024-01-01 ERROR disk full")
    assert result == {"date": "2024-01-01", "level": "ERROR", "message": "disk full"}


def test_parse_log_line_invalid():
    with pytest.raises(InvalidLogLineError):
        parse_log_line("garbage")
