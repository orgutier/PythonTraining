# Deck: A Collection Protocol

Implement `Deck`, a thin wrapper around a list of cards that behaves like a built-in collection -- purely by implementing the right dunders, with **no inheritance from any collection base class**:

- `__init__(self, cards: list)` -- store `self.cards = list(cards)` (a copy, so mutating the caller's original list later doesn't affect the deck).
- `__len__(self) -> int` -- `len(self.cards)`.
- `__getitem__(self, index)` -- `self.cards[index]` (this alone makes `deck[0]` and slicing like `deck[:3]` work).
- `__iter__(self)` -- `iter(self.cards)` (an explicit iterator, even though `__getitem__` alone would let old-style iteration work too).
- `__contains__(self, card) -> bool` -- `card in self.cards`.
- `__add__(self, other)` -- if `other` is a `Deck`, return a new `Deck(self.cards + other.cards)` (concatenation); else `NotImplemented`. This is **operator overloading**: `+` on `Deck` does nothing magical, it's just Python calling `__add__`.

`Deck` supports `len()`, indexing, slicing, `for x in deck`, `in`, and `+` -- all of that from five small methods, none of which required subclassing `list` or any other built-in type. That's the **protocol** idea: Python's `with`/`len()`/`for`/`in`/`+` machinery looks for matching dunder methods *at runtime*, not for a specific base class.

See the Study Reference presentation, Topic 8 (Mid tier), for the theory.
