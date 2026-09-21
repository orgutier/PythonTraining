"""
Challenge 07 - Min Stack
Interview-style challenge (LeetCode #155). Correctness is pytest-tested
(see tests/test_challenge07.py / `python tools/cli.py test challenge07`);
see README.md in this folder for the full problem statement and the
constraints your solution must follow (O(1) get_min, no using min(), and
a docstring listing the edge cases handled).

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module, matching the convention used by
exercises/weekNN/solution.py.
"""


class MinStack:
    """
    A stack supporting push/pop/top/get_min all in O(1) time. Fill in
    this docstring as part of the challenge: explain how you track the
    running minimum without scanning, and document the edge cases you
    handle (emptying and refilling the stack, duplicate minimums, a
    single-element stack).
    """

    def __init__(self) -> None:
        raise NotImplementedError

    def push(self, val: int) -> None:
        raise NotImplementedError

    def pop(self) -> None:
        raise NotImplementedError

    def top(self) -> int:
        raise NotImplementedError

    def get_min(self) -> int:
        raise NotImplementedError
