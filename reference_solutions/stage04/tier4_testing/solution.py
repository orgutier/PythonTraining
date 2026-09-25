def dedupe_correct(items):
    return list(dict.fromkeys(items))


def dedupe_buggy(items):
    return list(set(items))


def evens_correct(numbers):
    return [n for n in numbers if n % 2 == 0]


def evens_buggy(numbers):
    return [n for n in numbers if n % 2 == 1]


_check_log = []


def check(description: str, condition: bool) -> bool:
    _check_log.append((description, condition))
    return condition


def run_all_checks() -> dict:
    _check_log.clear()
    sample = [3, 1, 2, 1, 3, 5, 2]

    expected_dedupe = list(dict.fromkeys(sample))
    check("dedupe_correct(sample) preserves first-seen order", dedupe_correct(sample) == expected_dedupe)
    check("dedupe_buggy(sample) preserves first-seen order", dedupe_buggy(sample) == expected_dedupe)

    expected_evens = [n for n in sample if n % 2 == 0]
    check("evens_correct(sample) keeps only even numbers", evens_correct(sample) == expected_evens)
    check("evens_buggy(sample) keeps only even numbers", evens_buggy(sample) == expected_evens)

    total = len(_check_log)
    passed = sum(1 for _, ok in _check_log if ok)
    failed = [desc for desc, ok in _check_log if not ok]
    return {"total": total, "passed": passed, "failed": failed}
