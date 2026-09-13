from exercises.week04.solution import word_frequency


def test_word_frequency():
    result = word_frequency("The cat sat. The cat ran.")
    assert result == {"the": 2, "cat": 2, "sat": 1, "ran": 1}

# NOTE: "uses a comprehension" is a soft/manual review item, not enforced here.
