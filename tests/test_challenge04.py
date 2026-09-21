import pytest
from challenges.challenge04.solution import (
    retry_until_clean,
    group_consecutive_runs,
    status_label,
    interleave_first_n,
)


def test_retry_until_clean_finds_clean_batch():
    batches = [
        [("09:00", "ERROR", "x")],
        [("09:01", "INFO", "y")],
    ]
    assert retry_until_clean(batches, max_retries=3) == 1


def test_retry_until_clean_gives_up_after_max_retries():
    batches = [
        [("09:00", "ERROR", "x")],
        [("09:01", "INFO", "y")],
    ]
    assert retry_until_clean(batches, max_retries=1) == -1


def test_retry_until_clean_first_batch_already_clean():
    batches = [[("09:00", "INFO", "ok")]]
    assert retry_until_clean(batches, max_retries=5) == 0


def test_retry_until_clean_zero_max_retries():
    batches = [[("09:00", "INFO", "ok")]]
    assert retry_until_clean(batches, max_retries=0) == -1


def test_retry_until_clean_empty_batches_raises():
    with pytest.raises(ValueError):
        retry_until_clean([], max_retries=3)


def test_group_consecutive_runs():
    assert group_consecutive_runs(["A", "A", "B", "A"]) == [["A", "A"], ["B"], ["A"]]


def test_group_consecutive_runs_empty():
    assert group_consecutive_runs([]) == []


def test_status_label():
    assert status_label(0) == "empty"
    assert status_label(3) == "ok"
    assert status_label(9) == "busy"


def test_interleave_first_n():
    assert interleave_first_n([[1, 2], [3, 4, 5]], 3) == [1, 2, 3]


def test_interleave_first_n_limit_exceeds_total():
    assert interleave_first_n([[1], [2]], 10) == [1, 2]
