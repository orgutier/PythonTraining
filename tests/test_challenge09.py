import pytest
from challenges.challenge09.solution import (
    LogParseError,
    MalformedLineError,
    parse_line,
    parse_log_file,
    scan_directory,
)


def test_parse_line_basic():
    result = parse_line("09:05 ERROR disk full", 3)
    assert result == {"time": "09:05", "level": "ERROR", "message": "disk full", "line_number": 3}


def test_parse_line_malformed_raises():
    with pytest.raises(MalformedLineError):
        parse_line("not a log line", 1)


def test_malformed_line_error_is_a_log_parse_error():
    assert issubclass(MalformedLineError, LogParseError)


def test_parse_log_file_basic(tmp_path):
    path = tmp_path / "app.log"
    path.write_text("09:00 INFO boot\n\n09:05 ERROR disk full\n")
    entries = parse_log_file(str(path))
    assert len(entries) == 2
    assert entries[0]["line_number"] == 1
    assert entries[1]["level"] == "ERROR"


def test_parse_log_file_empty(tmp_path):
    path = tmp_path / "empty.log"
    path.write_text("")
    assert parse_log_file(str(path)) == []


def test_parse_log_file_chains_malformed_line_error(tmp_path):
    path = tmp_path / "bad.log"
    path.write_text("garbage line\n")
    with pytest.raises(LogParseError) as exc_info:
        parse_log_file(str(path))
    assert isinstance(exc_info.value.__cause__, MalformedLineError)


def test_scan_directory_skips_failed_files(tmp_path):
    good = tmp_path / "good.log"
    good.write_text("09:00 INFO boot\n")
    bad = tmp_path / "bad.log"
    bad.write_text("garbage\n")

    entries, failed = scan_directory([str(good), str(bad)])
    assert len(entries) == 1
    assert failed == 1
