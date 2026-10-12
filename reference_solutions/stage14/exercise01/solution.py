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
