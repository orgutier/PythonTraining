"""
Week 14 - Capstone
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in tests/test_week14.py
imports directly from here.
"""


class Book:
    def __init__(self, title: str, author: str, isbn: str):
        raise NotImplementedError

    def __repr__(self) -> str:
        raise NotImplementedError

    def __eq__(self, other) -> bool:
        """Two books are equal if they share the same isbn."""
        raise NotImplementedError


class Library:
    def __init__(self):
        raise NotImplementedError

    def add_book(self, book: Book) -> None:
        raise NotImplementedError

    def find_by_author(self, author: str) -> list[Book]:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def __contains__(self, isbn: str) -> bool:
        raise NotImplementedError

    def save_to_json(self, path: str) -> None:
        raise NotImplementedError

    def load_from_json(self, path: str) -> None:
        raise NotImplementedError
