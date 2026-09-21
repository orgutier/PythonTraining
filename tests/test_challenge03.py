from challenges.challenge03.solution import (
    parse_log_stream,
    first_critical_index,
    label_entries,
    pair_with_severity,
    is_healthy,
)


def _sample_entries():
    return parse_log_stream([
        "09:00 INFO boot sequence started",
        "",
        "09:05 ERROR disk full",
        "09:06 INFO retrying",
    ])


def test_parse_log_stream_skips_blanks_and_keeps_message_spaces():
    entries = _sample_entries()
    assert entries == [
        ("09:00", "INFO", "boot sequence started"),
        ("09:05", "ERROR", "disk full"),
        ("09:06", "INFO", "retrying"),
    ]


def test_first_critical_index_found():
    assert first_critical_index(_sample_entries()) == 1


def test_first_critical_index_not_found():
    entries = parse_log_stream(["09:00 INFO ok", "09:01 INFO still ok"])
    assert first_critical_index(entries) == -1


def test_label_entries():
    entries = _sample_entries()
    assert label_entries(entries)[1] == "1: ERROR - disk full"


def test_pair_with_severity():
    entries = _sample_entries()
    result = pair_with_severity(entries, [1, 5, 1])
    assert result[1] == (("09:05", "ERROR", "disk full"), 5)


def test_is_healthy_true_without_critical():
    assert is_healthy(_sample_entries()) is True


def test_is_healthy_false_with_matching_level():
    assert is_healthy(_sample_entries(), levels=("ERROR",)) is False


def test_is_healthy_false_when_empty():
    assert is_healthy([]) is False
