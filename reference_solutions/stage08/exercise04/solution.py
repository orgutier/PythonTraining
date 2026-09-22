class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor


class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return x + self.n


class Toggler:
    def __init__(self):
        self.state = False

    def __call__(self) -> bool:
        self.state = not self.state
        return self.state
