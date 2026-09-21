"""
Challenge 15 - Matrix: A Rich Numeric Type
Interview-style challenge. Correctness is pytest-tested (see
tests/test_challenge15.py / `python tools/cli.py test challenge15`); see
README.md in this folder for the full problem statement and the constraints
your solution must follow (ten dunders on one class -- __repr__/__str__/__eq__/__hash__/__add__/__radd__/__len__/__getitem__/__iter__/__contains__/__bool__ -- with NotImplemented used correctly).

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module, matching the convention used by
exercises/weekNN/solution.py.
"""


class Matrix:
    def __init__(self, rows: list) -> None:
        raise NotImplementedError

    def __repr__(self) -> str:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError

    def __eq__(self, other) -> bool:
        raise NotImplementedError

    def __hash__(self) -> int:
        raise NotImplementedError

    def __add__(self, other):
        """Element-wise sum if other is a same-shape Matrix, else NotImplemented."""
        raise NotImplementedError

    def __radd__(self, other):
        """self if other == 0, else NotImplemented."""
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def __getitem__(self, index):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    def __contains__(self, value) -> bool:
        raise NotImplementedError

    def __bool__(self) -> bool:
        """False only if there are no rows, or every value is 0."""
        raise NotImplementedError
