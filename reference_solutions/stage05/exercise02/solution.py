class ValidationError(Exception):
    pass


class NegativeValueError(ValidationError):
    pass


def validate_positive(n: int) -> int:
    if n < 0:
        raise NegativeValueError(f"negative value: {n}")
    return n


def safe_parse_int(s: str):
    try:
        return int(s)
    except ValueError:
        return None


_attempts = 0


def divide_with_cleanup(a: float, b: float) -> float:
    global _attempts
    try:
        return a / b
    except ZeroDivisionError:
        raise
    finally:
        _attempts += 1


def get_attempts() -> int:
    return _attempts


def reset_attempts() -> None:
    global _attempts
    _attempts = 0
