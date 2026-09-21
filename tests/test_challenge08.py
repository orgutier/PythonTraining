import pandas as pd

from challenges.challenge08.solution import two_sum


def test_two_sum_basic():
    numbers = pd.Series([2, 7, 11, 15], index=["a", "b", "c", "d"])
    assert two_sum(numbers, 9) == ("a", "b")


def test_two_sum_no_pair_returns_none():
    numbers = pd.Series([2, 7, 11, 15], index=["a", "b", "c", "d"])
    assert two_sum(numbers, 100) is None


def test_two_sum_default_integer_index():
    numbers = pd.Series([3, 2, 4])
    result = two_sum(numbers, 6)
    assert result == (1, 2)  # numbers[1] + numbers[2] == 2 + 4 == 6


def test_two_sum_repeated_value_provides_the_pair():
    numbers = pd.Series([4, 1, 4], index=["x", "y", "z"])
    assert two_sum(numbers, 8) == ("x", "z")


def test_two_sum_single_element_series():
    numbers = pd.Series([5], index=["only"])
    assert two_sum(numbers, 10) is None
