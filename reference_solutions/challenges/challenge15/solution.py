class Matrix:
    def __init__(self, rows: list) -> None:
        self.rows = tuple(tuple(row) for row in rows)

    def __repr__(self) -> str:
        return f"Matrix({[list(row) for row in self.rows]!r})"

    def __str__(self) -> str:
        return "\n".join(" ".join(str(v) for v in row) for row in self.rows)

    def __eq__(self, other) -> bool:
        return isinstance(other, Matrix) and self.rows == other.rows

    def __hash__(self) -> int:
        return hash(self.rows)

    def _same_shape(self, other) -> bool:
        return len(self.rows) == len(other.rows) and all(
            len(a) == len(b) for a, b in zip(self.rows, other.rows)
        )

    def __add__(self, other):
        """
        Element-wise sum of two same-shape matrices.

        Edge cases handled:
          - A different-shape Matrix, or a non-Matrix -> returns
            NotImplemented (Python then raises its own TypeError, since
            there's no other way to add it).
          - A 1x1 matrix -> works the same as any other size.
        """
        if not (isinstance(other, Matrix) and self._same_shape(other)):
            return NotImplemented
        return Matrix([
            [a + b for a, b in zip(row_a, row_b)]
            for row_a, row_b in zip(self.rows, other.rows)
        ])

    def __radd__(self, other):
        if other == 0:
            return self
        return NotImplemented

    def __len__(self) -> int:
        return len(self.rows)

    def __getitem__(self, index):
        return self.rows[index]

    def __iter__(self):
        return iter(self.rows)

    def __contains__(self, value) -> bool:
        return any(value in row for row in self.rows)

    def __bool__(self) -> bool:
        return any(any(v != 0 for v in row) for row in self.rows)
