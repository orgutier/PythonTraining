from challenges.challenge10.solution import (
    SuppressAndCount,
    suppress_and_count,
    extract_error_messages,
    redact_ips,
    contains_stack_trace,
)


def test_suppress_and_count_class_suppresses_matching():
    with SuppressAndCount(ValueError) as counter:
        raise ValueError("bad input")
    assert counter.count == 1


def test_suppress_and_count_class_propagates_non_matching():
    import pytest
    with pytest.raises(TypeError):
        with SuppressAndCount(ValueError):
            raise TypeError("nope")


def test_suppress_and_count_generator_suppresses_matching():
    with suppress_and_count(ValueError) as state:
        raise ValueError("bad input")
    assert state["count"] == 1


def test_suppress_and_count_generator_propagates_non_matching():
    import pytest
    with pytest.raises(TypeError):
        with suppress_and_count(ValueError):
            raise TypeError("nope")


def test_extract_error_messages():
    text = "09:00 INFO ok\n09:05 ERROR disk full\n09:06 ERROR timeout"
    assert extract_error_messages(text) == ["disk full", "timeout"]


def test_extract_error_messages_none_found():
    assert extract_error_messages("09:00 INFO all good") == []


def test_redact_ips():
    assert redact_ips("connection from 10.0.0.5 refused") == "connection from [REDACTED] refused"


def test_redact_ips_multiple():
    text = "10.0.0.1 talked to 192.168.1.20"
    assert redact_ips(text) == "[REDACTED] talked to [REDACTED]"


def test_contains_stack_trace_true():
    text = "something broke\nTraceback (most recent call last):\n  File ..."
    assert contains_stack_trace(text) is True


def test_contains_stack_trace_false():
    assert contains_stack_trace("all good here") is False
