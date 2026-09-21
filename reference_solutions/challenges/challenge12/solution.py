class MinStack:
    __slots__ = ("_values", "_mins")

    total_pushes = 0

    def __init__(self) -> None:
        self._values = []
        self._mins = []

    @staticmethod
    def is_numeric(value) -> bool:
        return isinstance(value, (int, float)) and not isinstance(value, bool)

    def push(self, value) -> None:
        """
        Push value onto the stack.

        Edge cases handled:
          - A non-numeric value -> raises TypeError; total_pushes is NOT
            incremented for a rejected push.
          - A bool -> also rejected (not treated as numeric here, even
            though bool is technically an int subclass).
        """
        if not MinStack.is_numeric(value):
            raise TypeError(f"MinStack only holds numeric values, got {value!r}")
        self._values.append(value)
        if self._mins and self._mins[-1] <= value:
            self._mins.append(self._mins[-1])
        else:
            self._mins.append(value)
        MinStack.total_pushes += 1

    def pop(self) -> None:
        if not self._values:
            raise IndexError("pop from empty MinStack")
        self._values.pop()
        self._mins.pop()

    @property
    def top(self):
        if not self._values:
            raise IndexError("top from empty MinStack")
        return self._values[-1]

    @property
    def minimum(self):
        if not self._mins:
            raise IndexError("minimum from empty MinStack")
        return self._mins[-1]

    @classmethod
    def from_iterable(cls, values) -> "MinStack":
        stack = cls()
        for value in values:
            stack.push(value)
        return stack
