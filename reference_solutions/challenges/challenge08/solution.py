# Time: O(n), Space: O(n). A single pass over the Series (via .items(),
# which is pandas' label-aware iterator) with a value -> index-label
# lookup dict -- the same one-pass hash technique as the classic Two Sum,
# just index-label-aware instead of position-based, and with no nested
# comparison loop.
import pandas as pd


def two_sum(numbers: pd.Series, target: int):
    """
    Return the (index_a, index_b) pair of index LABELS such that
    numbers[index_a] + numbers[index_b] == target, or None if no such
    pair exists.

    Edge cases handled:
      - No pair sums to target -> returns None.
      - A repeated value provides the pair (e.g. two entries equal to 4
        with target=8): the first occurrence is recorded in `seen`
        before the second is checked, so the second correctly finds the
        first as its complement -- an index is never paired with itself.
      - A single-element Series -> the loop body runs once with an empty
        `seen`, so no complement can be found and None is returned.
    """
    seen: dict[int, object] = {}
    for idx, value in numbers.items():
        complement = target - value
        if complement in seen:
            return (seen[complement], idx)
        seen[value] = idx
    return None
