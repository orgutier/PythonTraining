def factorial_correct(n):
    if n <= 1:
        return 1
    return n * factorial_correct(n - 1)


def factorial_buggy(n):
    if n <= 1:
        return 1
    return n + factorial_buggy(n - 1)


def apply_discount_correct(price, pct=0.1):
    return round(price * (1 - pct), 2)


def apply_discount_buggy(price, pct=0.1):
    return round(price * (1 + pct), 2)


_check_log = []


def check(description: str, condition: bool) -> bool:
    _check_log.append((description, condition))
    return condition


def run_all_checks() -> dict:
    _check_log.clear()
    check("factorial_correct(5) == 120", factorial_correct(5) == 120)
    check("factorial_buggy(5) == 120", factorial_buggy(5) == 120)
    check("apply_discount_correct(100) == 90.0", apply_discount_correct(100) == 90.0)
    check("apply_discount_buggy(100) == 90.0", apply_discount_buggy(100) == 90.0)
    total = len(_check_log)
    passed = sum(1 for _, ok in _check_log if ok)
    failed = [desc for desc, ok in _check_log if not ok]
    return {"total": total, "passed": passed, "failed": failed}
