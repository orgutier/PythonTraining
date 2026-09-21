import collections
import dataclasses


@dataclasses.dataclass(frozen=True)
class AnagramGroup:
    signature: str
    words: tuple

    def __len__(self) -> int:
        return len(self.words)


def build_signature(word: str) -> str:
    return "".join(sorted(word))


def group_anagrams(words: list) -> list:
    """
    Group words sharing an anagram signature into AnagramGroup records.

    Edge cases handled:
      - Empty input list -> returns [].
      - The empty string "" -> its signature is "" too; every "" in the
        input lands in the same group together.
      - Single-character words -> their signature is just that character.
    """
    buckets = collections.defaultdict(list)
    for word in words:
        buckets[build_signature(word)].append(word)

    groups = [
        AnagramGroup(signature=signature, words=tuple(bucket))
        for signature, bucket in buckets.items()
    ]
    return sorted(groups, key=lambda g: g.signature)


def common_words(group_a: AnagramGroup, group_b: AnagramGroup) -> set:
    return set(group_a.words) & set(group_b.words)


def largest_groups(groups: list, n: int) -> list:
    return sorted(groups, key=lambda g: (len(g), g.signature), reverse=True)[:n]


def label_groups(groups: list) -> list:
    return [f"{i}: {group.signature} ({len(group)} words)" for i, group in enumerate(groups)]
