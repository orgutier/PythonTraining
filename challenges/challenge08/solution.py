"""
Challenge 08 - Two Sum, Pandas-Style
Interview-style challenge (LeetCode #1, adapted to pandas). Correctness is
pytest-tested (see tests/test_challenge08.py / `python tools/cli.py test
challenge08`); see README.md in this folder for the full problem
statement and the constraints your solution must follow (no nested loop,
return index labels not positions, and a docstring listing the edge
cases handled).

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module, matching the convention used by
exercises/weekNN/solution.py.
"""
import pandas as pd


def two_sum(numbers: pd.Series, target: int):
    """
    Return the (index_a, index_b) pair of index LABELS such that
    numbers[index_a] + numbers[index_b] == target, or None if no such
    pair exists.

    Edge cases to handle (see README.md): fill this in as part of the
    challenge -- document what your implementation returns when no pair
    exists, when a repeated value provides the pair, and for a
    single-element Series.
    """
    raise NotImplementedError
