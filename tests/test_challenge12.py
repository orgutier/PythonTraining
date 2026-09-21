import pytest
from challenges.challenge12.solution import MinStack


def test_push_top_minimum():
    stack = MinStack()
    stack.push(3)
    stack.push(1)
    stack.push(2)
    assert stack.top == 2
    assert stack.minimum == 1


def test_minimum_survives_pop_of_non_minimum():
    stack = MinStack()
    stack.push(3)
    stack.push(1)
    stack.push(2)
    stack.pop()
    assert stack.top == 1
    assert stack.minimum == 1


def test_minimum_updates_after_popping_the_minimum():
    stack = MinStack()
    stack.push(3)
    stack.push(1)
    stack.pop()
    assert stack.minimum == 3


def test_duplicate_minimum_values():
    stack = MinStack()
    stack.push(1)
    stack.push(1)
    stack.pop()
    assert stack.minimum == 1


def test_push_rejects_non_numeric():
    stack = MinStack()
    with pytest.raises(TypeError):
        stack.push("nope")


def test_push_rejects_bool():
    stack = MinStack()
    with pytest.raises(TypeError):
        stack.push(True)


def test_pop_top_minimum_on_empty_raise():
    stack = MinStack()
    with pytest.raises(IndexError):
        stack.pop()
    with pytest.raises(IndexError):
        _ = stack.top
    with pytest.raises(IndexError):
        _ = stack.minimum


def test_from_iterable_classmethod():
    stack = MinStack.from_iterable([5, 2, 8, 1])
    assert stack.top == 1
    assert stack.minimum == 1


def test_total_pushes_is_shared_across_instances():
    before = MinStack.total_pushes
    a = MinStack()
    b = MinStack()
    a.push(1)
    b.push(2)
    assert MinStack.total_pushes == before + 2


def test_rejected_push_does_not_increment_total_pushes():
    stack = MinStack()
    before = MinStack.total_pushes
    with pytest.raises(TypeError):
        stack.push("nope")
    assert MinStack.total_pushes == before


def test_slots_rejects_new_attribute():
    stack = MinStack()
    with pytest.raises(AttributeError):
        stack.extra = 1
