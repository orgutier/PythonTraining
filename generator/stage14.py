"""
Stage 14 -- Capstone.

Stage 14 has no new keywords/dunders/concepts of its own in
presentation/data.js -- its "modules" entry is literally "json + your
choice of pandas/requests/opencv/FastAPI", and its schedule is
project-shaped (kickoff, build, build, polish, demo), not tier-shaped like
every other stage. The 3x-per-concept coverage bar this generator applies
everywhere else doesn't map onto a stage whose entire point is picking your
own second module and synthesizing it with the rest of the course -- that
choice belongs to the trainee, not a fixed exercise spec. So this stage
stays a single, cohesive graded exercise (still moved into the same
exercises/stage14/exerciseXX/ + solution.py convention as every other stage,
for git-hook and generate.py consistency) instead of being fragmented into
drills.
"""

STAGE = "stage14"
TOPIC = "Capstone"
OVERVIEW = (
    "One graded exercise -- a small Library/Book system with JSON "
    "persistence, synthesizing dict/list/dataclass-style records, dunders "
    "(__len__, __contains__), and the json module from earlier stages. "
    "pandas/requests/opencv/FastAPI usage is bonus scope for your own "
    "capstone idea on top of this, not required here -- see the stage's "
    "project-shaped schedule (kickoff, build, build, polish, demo)."
)

EXERCISES = [
    {
        "name": "exercise01",
        "title": "Library and Book",
        "summary": "records, dunders, and JSON persistence tying the course together",
        "readme": (
            "Implement a small library system:\n\n"
            "- `Book.__init__(self, title, author, isbn)` -- store all "
            "three.\n"
            "- `Book.__repr__(self) -> str` -- "
            "`f\"Book({self.title!r}, {self.author!r}, {self.isbn!r})\"`.\n"
            "- `Book.__eq__(self, other) -> bool` -- two books are equal if "
            "they share the same `isbn`.\n"
            "- `Library.__init__(self)` -- `self._books = []`.\n"
            "- `Library.add_book(self, book: Book) -> None` -- append it.\n"
            "- `Library.find_by_author(self, author: str) -> list[Book]` -- "
            "every book by that author.\n"
            "- `Library.__len__(self) -> int` -- how many books.\n"
            "- `Library.__contains__(self, isbn: str) -> bool` -- whether "
            "any book has that isbn.\n"
            "- `Library.save_to_json(self, path: str) -> None` -- write the "
            "books out as a JSON list of `{\"title\":..., \"author\":..., "
            "\"isbn\":...}` objects.\n"
            "- `Library.load_from_json(self, path: str) -> None` -- read "
            "that JSON back and rebuild `self._books`.\n\n"
            "This is deliberately a synthesis exercise, not a place to "
            "learn something new -- every piece here (classes, dunders, "
            "`json.dump`/`json.load`, list comprehensions) is something "
            "you've already built from scratch earlier in the course.\n\n"
            "For the actual capstone project, pick your own idea that "
            "combines two or more earlier topics (see this stage's schedule) "
            "-- this exercise is the graded fallback/warm-up, not a "
            "replacement for it."
        ),
        "stub": '''\
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

    def find_by_author(self, author: str) -> list:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def __contains__(self, isbn: str) -> bool:
        raise NotImplementedError

    def save_to_json(self, path: str) -> None:
        raise NotImplementedError

    def load_from_json(self, path: str) -> None:
        raise NotImplementedError
''',
        "reference": '''\
import json


class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __repr__(self) -> str:
        return f"Book({self.title!r}, {self.author!r}, {self.isbn!r})"

    def __eq__(self, other) -> bool:
        return isinstance(other, Book) and self.isbn == other.isbn


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book: Book) -> None:
        self._books.append(book)

    def find_by_author(self, author: str) -> list:
        return [b for b in self._books if b.author == author]

    def __len__(self) -> int:
        return len(self._books)

    def __contains__(self, isbn: str) -> bool:
        return any(b.isbn == isbn for b in self._books)

    def save_to_json(self, path: str) -> None:
        data = [{"title": b.title, "author": b.author, "isbn": b.isbn} for b in self._books]
        with open(path, "w") as f:
            json.dump(data, f)

    def load_from_json(self, path: str) -> None:
        with open(path) as f:
            data = json.load(f)
        self._books = [Book(**d) for d in data]
''',
        "test": '''\
from exercises.stage14.exercise01.solution import Book, Library


def test_add_and_len():
    lib = Library()
    lib.add_book(Book("Dune", "Herbert", "111"))
    assert len(lib) == 1


def test_find_by_author():
    lib = Library()
    lib.add_book(Book("Dune", "Herbert", "111"))
    lib.add_book(Book("Foundation", "Asimov", "222"))
    result = lib.find_by_author("Herbert")
    assert len(result) == 1
    assert result[0].isbn == "111"


def test_contains():
    lib = Library()
    lib.add_book(Book("Dune", "Herbert", "111"))
    assert "111" in lib


def test_book_eq_by_isbn():
    assert Book("Dune", "Herbert", "111") == Book("Dune (reprint)", "F. Herbert", "111")


def test_save_and_load_roundtrip(tmp_path):
    lib = Library()
    lib.add_book(Book("Dune", "Herbert", "111"))
    path = str(tmp_path / "lib.json")
    lib.save_to_json(path)

    new_lib = Library()
    new_lib.load_from_json(path)
    assert len(new_lib) == 1
    assert new_lib._books[0].title == "Dune"
''',
    },
]
