import pytest
from challenges.challenge15.solution import Matrix


def test_repr_and_str():
    m = Matrix([[1, 2], [3, 4]])
    assert repr(m) == "Matrix([[1, 2], [3, 4]])"
    assert str(m) == "1 2\n3 4"


def test_eq():
    assert Matrix([[1, 2]]) == Matrix([[1, 2]])
    assert Matrix([[1, 2]]) != Matrix([[1, 3]])


def test_hash_consistent_with_eq():
    matrices = {Matrix([[1, 2]]), Matrix([[1, 2]]), Matrix([[3, 4]])}
    assert len(matrices) == 2


def test_add_same_shape():
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[10, 20], [30, 40]])
    assert m1 + m2 == Matrix([[11, 22], [33, 44]])


def test_add_mismatched_shape_raises_typeerror():
    m1 = Matrix([[1, 2]])
    m2 = Matrix([[1]])
    with pytest.raises(TypeError):
        m1 + m2
    with pytest.raises(TypeError):
        m1 + "not a matrix"


def test_radd_via_sum():
    m1 = Matrix([[1, 2]])
    m2 = Matrix([[10, 20]])
    assert sum([m1, m2]) == Matrix([[11, 22]])


def test_len_getitem_iter():
    m = Matrix([[1, 2], [3, 4]])
    assert len(m) == 2
    assert m[0] == (1, 2)
    assert list(m) == [(1, 2), (3, 4)]


def test_contains():
    m = Matrix([[1, 2], [3, 4]])
    assert 3 in m
    assert 99 not in m


def test_bool_false_for_all_zero():
    assert bool(Matrix([[0, 0], [0, 0]])) is False


def test_bool_true_with_any_nonzero():
    assert bool(Matrix([[0, 0], [0, 1]])) is True
