"""
Week 8 - The Python Data Model
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in tests/test_week08.py
imports directly from here.
"""


class Vector:
    def __init__(self, x: float, y: float):
        raise NotImplementedError

    def __add__(self, other: "Vector") -> "Vector":
        raise NotImplementedError

    def __eq__(self, other) -> bool:
        raise NotImplementedError

    def __repr__(self) -> str:
        raise NotImplementedError


class Deck:
    def __init__(self, cards: list):
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def __getitem__(self, index: int):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError
