import dataclasses
import math


@dataclasses.dataclass
class Point:
    x: int
    y: int

    def distance_from_origin(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5


@dataclasses.dataclass(frozen=True)
class FrozenPoint:
    x: int
    y: int

    def distance_from_origin(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5


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
