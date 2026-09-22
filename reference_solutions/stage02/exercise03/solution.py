def pair_names_scores(names: list[str], scores: list[int]) -> list[tuple]:
    return list(zip(names, scores))


def merge_records(keys: list[str], values: list) -> dict:
    return dict(zip(keys, values))


def count_equal_pairs(list1: list, list2: list) -> int:
    return sum(1 for a, b in zip(list1, list2) if a == b)


def indexed_items(items: list[str]) -> list[str]:
    return [f"{i}: {item}" for i, item in enumerate(items)]


def labeled_from(items: list[str], start: int) -> dict:
    return {i: item for i, item in enumerate(items, start)}
