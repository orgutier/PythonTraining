def count_digits(n: int) -> int:
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)


def sum_of_squares_recursive(numbers: list) -> int:
    if not numbers:
        return 0
    return numbers[0] ** 2 + sum_of_squares_recursive(numbers[1:])


square = lambda x: x * x
is_even = lambda x: x % 2 == 0
