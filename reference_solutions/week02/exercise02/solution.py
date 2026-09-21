def sum_until_negative(numbers: list[int]) -> int:
    total = 0
    for n in numbers:
        if n < 0:
            break
        total += n
    return total


def skip_multiples(numbers: list[int], factor: int) -> list[int]:
    result = []
    for n in numbers:
        if n % factor == 0:
            continue
        result.append(n)
    return result


def countdown(n: int) -> list[int]:
    result = []
    while n >= 1:
        result.append(n)
        n -= 1
    return result


def safe_int_list(values: list) -> list[int]:
    result = []
    for v in values:
        try:
            result.append(int(v))
        except (ValueError, TypeError):
            pass
    return result
