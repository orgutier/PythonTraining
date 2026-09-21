class NumberRange:
    def __init__(self, start: int, stop: int):
        self.start = start
        self.stop = stop

    def __repr__(self) -> str:
        return f"NumberRange({self.start}, {self.stop})"

    def __eq__(self, other) -> bool:
        return isinstance(other, NumberRange) and self.start == other.start and self.stop == other.stop

    def __hash__(self) -> int:
        return hash((self.start, self.stop))

    def __len__(self) -> int:
        return max(0, self.stop - self.start)

    def __getitem__(self, index):
        if index < 0 or index >= len(self):
            raise IndexError("NumberRange index out of range")
        return self.start + index

    def __iter__(self):
        return iter(range(self.start, self.stop))

    def __contains__(self, value) -> bool:
        return self.start <= value < self.stop

    def __bool__(self) -> bool:
        return len(self) > 0
