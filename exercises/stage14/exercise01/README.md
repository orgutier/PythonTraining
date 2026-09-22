# Library and Book

Implement a small library system:

- `Book.__init__(self, title, author, isbn)` -- store all three.
- `Book.__repr__(self) -> str` -- `f"Book({self.title!r}, {self.author!r}, {self.isbn!r})"`.
- `Book.__eq__(self, other) -> bool` -- two books are equal if they share the same `isbn`.
- `Library.__init__(self)` -- `self._books = []`.
- `Library.add_book(self, book: Book) -> None` -- append it.
- `Library.find_by_author(self, author: str) -> list[Book]` -- every book by that author.
- `Library.__len__(self) -> int` -- how many books.
- `Library.__contains__(self, isbn: str) -> bool` -- whether any book has that isbn.
- `Library.save_to_json(self, path: str) -> None` -- write the books out as a JSON list of `{"title":..., "author":..., "isbn":...}` objects.
- `Library.load_from_json(self, path: str) -> None` -- read that JSON back and rebuild `self._books`.

This is deliberately a synthesis exercise, not a place to learn something new -- every piece here (classes, dunders, `json.dump`/`json.load`, list comprehensions) is something you've already built from scratch earlier in the course.

For the actual capstone project, pick your own idea that combines two or more earlier topics (see this stage's schedule) -- this exercise is the graded fallback/warm-up, not a replacement for it.
