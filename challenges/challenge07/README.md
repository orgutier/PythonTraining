# Challenge 07 — Anagram Groups with Records

**Do this after:** Stage 04 (Data Structures)
**Correctness is pytest-tested:** `python tools/cli.py test challenge07` (or `pytest tests/test_challenge07.py`). The constraints below on *how* you write it are not something pytest can check -- grade those yourself.

## Problem

Group Anagrams (LeetCode #49) is a real, frequently-asked interview
question: group every string in a list with its anagrams. This version
asks for it the way you'd actually build it in a real codebase -- returning
proper records instead of bare lists, and built with the container tools
Stage 4 is about, not around them.

Implement:

```python
@dataclasses.dataclass(frozen=True)
class AnagramGroup:
    signature: str
    words: tuple

    def __len__(self) -> int:
        return len(self.words)

def build_signature(word: str) -> str:
    """The word's letters sorted and joined -- "".join(sorted(word))."""

def group_anagrams(words: list) -> list:
    """Group words sharing a signature into AnagramGroup records, sorted by signature."""

def common_words(group_a: AnagramGroup, group_b: AnagramGroup) -> set:
    """Words appearing in both groups' .words."""

def largest_groups(groups: list, n: int) -> list:
    """The n largest groups by len(), ties broken by signature, largest first."""

def label_groups(groups: list) -> list:
    """["0: SIGNATURE (K words)", "1: SIGNATURE (K words)", ...]."""
```

```python
groups = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
# -> [AnagramGroup(signature="abt", words=("bat",)),
#     AnagramGroup(signature="aet", words=("eat", "tea", "ate")),
#     AnagramGroup(signature="ant", words=("tan", "nat"))]
label_groups(groups)[0]   # -> "0: abt (1 words)"
```

## Constraints on HOW you write it

1. **`build_signature` must be `"".join(sorted(word))`** -- one line, no
   manual sorting loop.
2. **`group_anagrams` must use `collections.defaultdict(list)`** to
   accumulate words per signature (this is exactly the tool Stage 4
   introduces for this), then convert each bucket into a **frozen**
   `AnagramGroup` (`words` as a `tuple`, not a `list` -- frozen dataclasses
   need hashable fields to actually be hashable themselves), and return
   the groups **sorted by `signature`** via `sorted()`.
3. **`AnagramGroup` must be `@dataclasses.dataclass(frozen=True)`** --
   this gets you `__eq__` and `__hash__` for free (two groups with the
   same signature and words compare and hash equal, and are usable in a
   `set`), which a plain class wouldn't without writing both by hand.
4. **`common_words` must use the `&` set operator** on `set(group_a.words)
   & set(group_b.words)` -- not a list comprehension with an `in` check.
5. **`largest_groups` must use `sorted(..., key=..., reverse=True)`**,
   slicing the top `n` -- not a manual max-finding loop.
6. **`label_groups` must use `enumerate()`.**
7. **A docstring on `group_anagrams`** listing edge cases: an empty input
   list, a word that's the empty string, and single-character words.
