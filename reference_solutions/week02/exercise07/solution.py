def contains_value(items: list, target) -> bool:
    for item in items:
        if item == target:
            break
    else:
        return False
    return True


def all_positive(numbers: list[int]) -> bool:
    for n in numbers:
        if n <= 0:
            break
    else:
        return True
    return False


def find_first_negative_index(numbers: list[int]) -> int:
    i = 0
    while i < len(numbers):
        if numbers[i] < 0:
            break
        i += 1
    else:
        return -1
    return i


def retry_until_success(attempts: list[bool]) -> bool:
    i = 0
    while i < len(attempts):
        if attempts[i]:
            break
        i += 1
    else:
        return False
    return True


def first_positive_index(numbers: list[int]) -> int:
    i = 0
    while i < len(numbers):
        if numbers[i] > 0:
            break
        i += 1
    else:
        return -1
    return i
