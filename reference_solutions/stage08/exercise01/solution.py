class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __eq__(self, other) -> bool:
        return isinstance(other, Vector) and self.x == other.x and self.y == other.y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __radd__(self, other):
        if other == 0:
            return self
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __bool__(self) -> bool:
        return not (self.x == 0 and self.y == 0)

    def __getitem__(self, index):
        return (self.x, self.y)[index]
