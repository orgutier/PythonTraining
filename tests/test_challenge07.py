from challenges.challenge07.solution import (
    AnagramGroup,
    build_signature,
    group_anagrams,
    common_words,
    largest_groups,
    label_groups,
)


def test_build_signature():
    assert build_signature("eat") == "aet"


def test_group_anagrams_basic_and_sorted_by_signature():
    groups = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert [g.signature for g in groups] == sorted(g.signature for g in groups)
    by_sig = {g.signature: set(g.words) for g in groups}
    assert by_sig == {
        "aet": {"eat", "tea", "ate"},
        "ant": {"tan", "nat"},
        "abt": {"bat"},
    }


def test_group_anagrams_empty_list():
    assert group_anagrams([]) == []


def test_anagram_group_is_hashable_and_eq():
    a = AnagramGroup(signature="aet", words=("eat", "tea"))
    b = AnagramGroup(signature="aet", words=("eat", "tea"))
    assert a == b
    assert hash(a) == hash(b)
    assert len({a, b}) == 1


def test_common_words():
    a = AnagramGroup(signature="aet", words=("eat", "tea", "ate"))
    b = AnagramGroup(signature="x", words=("tea", "zzz"))
    assert common_words(a, b) == {"tea"}


def test_largest_groups():
    groups = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    top = largest_groups(groups, 1)
    assert len(top) == 1
    assert top[0].signature == "aet"


def test_label_groups():
    groups = [AnagramGroup(signature="abt", words=("bat",))]
    assert label_groups(groups) == ["0: abt (1 words)"]
