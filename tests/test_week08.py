from exercises.week08.solution import Vector, Deck


def test_vector_add():
    assert Vector(1, 2) + Vector(3, 4) == Vector(4, 6)


def test_vector_repr():
    assert repr(Vector(1, 2)) == "Vector(1, 2)"


def test_deck_len_getitem_iter():
    deck = Deck([1, 2, 3])
    assert len(deck) == 3
    assert deck[0] == 1
    assert list(deck) == [1, 2, 3]
