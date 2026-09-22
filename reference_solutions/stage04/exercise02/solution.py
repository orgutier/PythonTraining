def word_lengths(words: list[str]) -> dict:
    return {w: len(w) for w in words}


def index_lookup(items: list[str]) -> dict:
    return {item: i for i, item in enumerate(items)}


def numbered_pairs(items: list[str]) -> list[tuple]:
    return list(enumerate(items))


def pair_and_dict(keys: list[str], values: list) -> dict:
    return dict(zip(keys, values))


def common_elements(a: set, b: set) -> set:
    return a & b


def unique_to_first(a: set, b: set) -> set:
    return a - b


def all_elements(a: set, b: set) -> set:
    return a | b
