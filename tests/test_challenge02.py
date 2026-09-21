from challenges.challenge02.solution import (
    classify_pairs,
    dedupe_by_identity,
    dedupe_by_equality,
    prompt_login,
)


def test_classify_pairs_basic():
    a = [1, 2]
    b = [1, 2]
    c = a
    result = classify_pairs([a, b, c])
    assert result == {"same_object": 1, "equal_but_different": 2, "different": 0}


def test_classify_pairs_empty_and_single():
    assert classify_pairs([]) == {"same_object": 0, "equal_but_different": 0, "different": 0}
    assert classify_pairs([1]) == {"same_object": 0, "equal_but_different": 0, "different": 0}


def test_classify_pairs_all_different():
    result = classify_pairs([1, 2, 3])
    assert result == {"same_object": 0, "equal_but_different": 0, "different": 3}


def test_dedupe_by_identity_keeps_equal_but_distinct_objects():
    a = [1, 2]
    b = [1, 2]
    c = a
    result = dedupe_by_identity([a, b, c])
    assert len(result) == 2
    assert result[0] is a
    assert result[1] is b


def test_dedupe_by_equality_keeps_only_first_equal_value():
    a = [1, 2]
    b = [1, 2]
    c = a
    result = dedupe_by_equality([a, b, c])
    assert result == [[1, 2]]
    assert len(result) == 1


def test_prompt_login_uses_input_when_username_is_none(monkeypatch, capsys):
    answers = iter(["ada", "secret"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(answers))
    result = prompt_login()
    assert result == "ada"
    assert "Welcome, ada!" in capsys.readouterr().out


def test_prompt_login_empty_string_is_not_treated_as_missing(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda prompt="": "unused-password")
    result = prompt_login("")
    assert result == ""
    assert "Welcome, !" in capsys.readouterr().out
