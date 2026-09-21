def grade_label(score: int) -> str:
    return "pass" if score >= 60 else "fail"


def abs_value(n: int) -> int:
    return n if n >= 0 else -n


def clamp_to_range(n: int, lo: int, hi: int) -> int:
    return lo if n < lo else hi if n > hi else n
