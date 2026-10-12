import re


def safe_divide_correct(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


def safe_divide_buggy(a, b):
    return a / b


def looks_like_email_correct(text):
    return re.match(r"^[\w.+-]+@[\w-]+\.[\w.-]+$", text) is not None


def looks_like_email_buggy(text):
    return re.match(r"[\w.+-]+@[\w-]+\.[\w.-]+", text) is not None


_check_log = []


def check(description: str, condition: bool) -> bool:
    _check_log.append((description, condition))
    return condition


def run_all_checks() -> dict:
    _check_log.clear()

    try:
        ok = safe_divide_correct(5, 0) is None
    except ZeroDivisionError:
        ok = False
    check("safe_divide_correct(5, 0) returns None without raising", ok)

    try:
        ok = safe_divide_buggy(5, 0) is None
    except ZeroDivisionError:
        ok = False
    check("safe_divide_buggy(5, 0) returns None without raising", ok)

    sample_text = "a@b.co plus extra junk"
    check(
        "looks_like_email_correct rejects a string that only contains an email",
        looks_like_email_correct(sample_text) is False,
    )
    check(
        "looks_like_email_buggy rejects a string that only contains an email",
        looks_like_email_buggy(sample_text) is False,
    )

    total = len(_check_log)
    passed = sum(1 for _, ok in _check_log if ok)
    failed = [desc for desc, ok in _check_log if not ok]
    return {"total": total, "passed": passed, "failed": failed}
