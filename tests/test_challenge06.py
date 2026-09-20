from challenges.challenge06.solution import longest_consecutive


def test_longest_consecutive_basic():
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4


def test_longest_consecutive_full_run():
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9


def test_longest_consecutive_empty_list():
    assert longest_consecutive([]) == 0


def test_longest_consecutive_duplicates_do_not_inflate_length():
    assert longest_consecutive([1, 1, 2]) == 2


def test_longest_consecutive_single_element():
    assert longest_consecutive([5]) == 1


def test_longest_consecutive_negative_numbers():
    assert longest_consecutive([-3, -2, -1, 0, 5]) == 4


def test_longest_consecutive_already_contiguous():
    assert longest_consecutive([5, 4, 3, 2, 1]) == 5
