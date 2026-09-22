def squares(n: int) -> list[int]:
    return [x ** 2 for x in range(n)]


def evens_squared_dict(n: int) -> dict:
    return {x: x ** 2 for x in range(n) if x % 2 == 0}


def flatten(matrix: list[list[int]]) -> list[int]:
    return [x for row in matrix for x in row]
