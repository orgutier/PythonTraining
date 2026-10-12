"""
Challenge 07 - Anagram Groups with Records
Interview-style challenge. Correctness is pytest-tested (see
tests/test_challenge07.py / `python tools/cli.py test challenge07`); see
README.md in this folder for the full problem statement and the constraints
your solution must follow (collections.defaultdict for grouping, a frozen dataclass for each group (auto __eq__/__hash__), set operations, and enumerate() for labeling).

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module, matching the convention used by
exercises/stageNN/solution.py.
"""


import dataclasses


@dataclasses.dataclass(frozen=True)
class AnagramGroup:
    signature: str
    words: tuple

    def __len__(self) -> int:
        return len(self.words)


def build_signature(word: str) -> str:
    """"".join(sorted(word))."""
    raise NotImplementedError


def group_anagrams(words: list) -> list:
    """Group words into AnagramGroup records via collections.defaultdict(list), sorted by signature."""
    raise NotImplementedError


def common_words(group_a: AnagramGroup, group_b: AnagramGroup) -> set:
    """Words in both groups, via the & set operator."""
    raise NotImplementedError


def largest_groups(groups: list, n: int) -> list:
    """The n largest groups by len(), ties broken by signature, largest first."""
    raise NotImplementedError


def label_groups(groups: list) -> list:
    """["0: SIGNATURE (K words)", ...] via enumerate()."""
    raise NotImplementedError
