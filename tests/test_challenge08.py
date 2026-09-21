import pytest
from challenges.challenge08.solution import (
    Run,
    all_runs,
    longest_consecutive_run,
    runs_overlap,
    unique_numbers_covered,
)


def test_all_runs_basic():
    result = all_runs([100, 4, 200, 1, 3, 2])
    assert result == [Run(1, 4), Run(100, 1), Run(200, 1)]


def test_all_runs_empty():
    assert all_runs([]) == []


def test_all_runs_ignores_duplicates():
    assert all_runs([1, 2, 2, 3]) == [Run(1, 3)]


def test_all_runs_negative_numbers():
    assert all_runs([-2, -1, 0, 1]) == [Run(-2, 4)]


def test_longest_consecutive_run():
    assert longest_consecutive_run([100, 4, 200, 1, 3, 2]) == Run(1, 4)


def test_longest_consecutive_run_empty_raises():
    with pytest.raises(ValueError):
        longest_consecutive_run([])


def test_runs_overlap_true():
    assert runs_overlap(Run(1, 4), Run(3, 5)) is True


def test_runs_overlap_false():
    assert runs_overlap(Run(1, 4), Run(10, 2)) is False


def test_unique_numbers_covered():
    runs = [Run(1, 3), Run(10, 2)]
    assert unique_numbers_covered(runs) == {1, 2, 3, 10, 11}
