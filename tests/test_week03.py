import pytest
from exercises.week03.solution import factorial, fibonacci


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120


def test_factorial_negative_raises():
    with pytest.raises(ValueError):
        factorial(-1)


def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(10) == 55

# NOTE: this test suite checks OUTPUT correctness only. Whether the
# implementation is actually recursive (as the exercise asks) is a soft,
# human-reviewed requirement -- an iterative solution will still pass here.
