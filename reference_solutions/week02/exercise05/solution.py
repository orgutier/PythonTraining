def is_valid_username(name) -> bool:
    return isinstance(name, str) and len(name) > 0 and len(name) <= 20


def has_valid_first_item(items: list) -> bool:
    return bool(items) and bool(items[0])


def is_within_bounds(numbers: list[int], index: int) -> bool:
    return 0 <= index < len(numbers) and numbers[index] >= 0


def describe_truthiness(value) -> str:
    return "truthy" if value else "falsy"


def filter_truthy(values: list) -> list:
    return [v for v in values if v]


def count_falsy(values: list) -> int:
    return sum(1 for v in values if not v)
