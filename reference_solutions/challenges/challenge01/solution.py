# Time: O(n * k log k), Space: O(n * k)
# n = number of words, k = length of the longest word.
# Sorting each word's letters dominates the per-word cost; every word and
# its signature are stored once, which sets the space bound.
def group_anagrams(words: list[str]) -> list[list[str]]:
    """
    Group every string in `words` with the other strings that are anagrams
    of it. Return the groups as a list of lists; neither the order of the
    groups nor the order of words within a group is guaranteed.

    Edge cases handled:
      - Empty input list -> returns [].
      - Empty string "" -> its signature is "" (sorting an empty string
        yields an empty string), so every "" in the input lands in its own
        group together.
      - Single-character words -> their signature is just that character;
        grouped correctly with other identical single-character words.
      - Duplicate words (e.g. ["eat", "eat"]) -> both land in the same
        group, since they share a signature.
      - Case sensitivity: comparison is case-SENSITIVE by design ("Eat" and
        "eat" are treated as different words, matching how the words would
        actually differ in most real-world text). Callers who want
        case-insensitive grouping should lowercase their input first.
    """
    if not words:
        return []

    signatures = ["".join(sorted(word)) for word in words]

    groups: dict[str, list[str]] = {}
    for word, signature in zip(words, signatures):
        if signature not in groups:
            groups[signature] = []
        groups[signature].append(word)

    return list(groups.values())
