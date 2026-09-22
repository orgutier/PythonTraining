# Mutability and Identity

Implement five functions that make mutability and identity concrete instead of abstract:

- `append_and_return(lst: list, item) -> list` -- `lst.append(item)` then `return lst`. Because lists are mutable, the object you return is the *same* object the caller passed in.
- `concat_strings(a: str, b: str) -> str` -- `return a + b`. Because strings are immutable, the result is always a *new* object, never `a` or `b` themselves.
- `same_object(a, b) -> bool` -- `return a is b` (identity, not equality).
- `equal_but_not_identical() -> tuple` -- return a tuple of two separately built but `==`-equal lists, e.g. `([1, 2, 3], [1, 2, 3])`, to demonstrate equality without identity.
- `default_if_none(value, default)` -- `return default if value is None else value`.

See the Study Reference presentation, Topic 1 (mutability vs immutability, identity vs equality), for the theory.
