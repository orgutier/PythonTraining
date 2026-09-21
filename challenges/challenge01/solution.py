"""
Challenge 01 - Group Anagrams
Interview-style challenge. Correctness is pytest-tested (see
tests/test_challenge01.py / `python tools/cli.py test challenge01`); see README.md in this folder
for the full problem statement and the constraints your solution must follow
(no collections.Counter/defaultdict, a comprehension for the per-word
signature, full type hints, and a docstring listing the edge cases handled).

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module, matching the convention used by
exercises/weekNN/solution.py.
"""


# Time: O(?), Space: O(?)  -- fill in your actual complexity once implemented.
def group_anagrams(words: list[str]) -> list[list[str]]:
    """
    Group every string in `words` with the other strings that are anagrams
    of it. Return the groups as a list of lists; neither the order of the
    groups nor the order of words within a group is checked.

    Edge cases to handle (see README.md): fill this in as part of the
    challenge -- document exactly what your implementation does for an
    empty list, an empty string, single-character words, duplicate words,
    and case sensitivity.
    """
    raise NotImplementedError
