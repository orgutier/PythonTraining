def make_multiplier(factor: int):
    return lambda x: x * factor


def sort_by_length(words: list[str]) -> list[str]:
    return sorted(words, key=lambda w: len(w))


def top_scorer(records: list[dict]) -> dict:
    return max(records, key=lambda r: r["score"])
