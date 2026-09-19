from challenges.challenge01.solution import group_anagrams


def _normalize(groups):
    return sorted(sorted(group) for group in groups)


def test_group_anagrams_basic():
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    expected = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    assert _normalize(result) == _normalize(expected)


def test_group_anagrams_empty_list():
    assert group_anagrams([]) == []


def test_group_anagrams_empty_string():
    assert _normalize(group_anagrams([""])) == _normalize([[""]])


def test_group_anagrams_single_character_words():
    assert _normalize(group_anagrams(["a", "b", "a"])) == _normalize([["a", "a"], ["b"]])


def test_group_anagrams_duplicate_words():
    assert _normalize(group_anagrams(["eat", "eat"])) == _normalize([["eat", "eat"]])


def test_group_anagrams_is_case_sensitive():
    result = group_anagrams(["Eat", "eat"])
    assert _normalize(result) == _normalize([["Eat"], ["eat"]])
