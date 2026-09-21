from challenges.challenge07.solution import MinStack


def test_basic_push_pop_top_min():
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    assert s.get_min() == -3
    s.pop()
    assert s.top() == 0
    assert s.get_min() == -2


def test_single_element_stack():
    s = MinStack()
    s.push(7)
    assert s.top() == 7
    assert s.get_min() == 7


def test_empty_then_refill_resets_minimum():
    s = MinStack()
    s.push(5)
    s.push(1)
    s.pop()
    s.pop()
    s.push(10)
    assert s.get_min() == 10
    assert s.top() == 10


def test_duplicate_minimum_values():
    s = MinStack()
    s.push(2)
    s.push(-1)
    s.push(-1)
    assert s.get_min() == -1
    s.pop()
    assert s.get_min() == -1  # the other -1 is still there
    assert s.top() == -1


def test_min_updates_as_values_are_popped():
    s = MinStack()
    for v in [5, 3, 7, 1, 9]:
        s.push(v)
    assert s.get_min() == 1
    s.pop()  # remove 9
    assert s.get_min() == 1
    s.pop()  # remove 1
    assert s.get_min() == 3
