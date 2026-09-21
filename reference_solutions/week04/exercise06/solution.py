import collections
import math

Coordinate = collections.namedtuple("Coordinate", ["x", "y"])


def make_coordinate(x: int, y: int):
    return Coordinate(x, y)


class SimpleFraction:
    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ZeroDivisionError("denominator cannot be 0")
        if denominator < 0:
            numerator, denominator = -numerator, -denominator
        g = math.gcd(numerator, denominator)
        self.numerator = numerator // g
        self.denominator = denominator // g

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, SimpleFraction)
            and self.numerator == other.numerator
            and self.denominator == other.denominator
        )

    def __hash__(self) -> int:
        return hash((self.numerator, self.denominator))


def dedupe_preserving_order(items: list) -> list:
    return list(dict.fromkeys(items))
