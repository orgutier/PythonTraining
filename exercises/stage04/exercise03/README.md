# Comprehensions

Implement:

- `squares(n: int) -> list[int]` -- `[x ** 2 for x in range(n)]`.
- `evens_squared_dict(n: int) -> dict` -- `{x: x ** 2 for x in range(n) if x % 2 == 0}` (a dict comprehension with an `if` filter).
- `flatten(matrix: list[list[int]]) -> list[int]` -- a **nested** list comprehension: `[x for row in matrix for x in row]` (flattens a list of lists into one list, left-to-right, top-to-bottom).

See the Study Reference presentation, Topic 4, for the theory.
