import itertools


def stepped_range(start: int, stop: int, step: int) -> list[int]:
    return list(range(start, stop, step))


def numbered_multiples(n: int, factor: int) -> list[str]:
    multiples = list(range(factor, n + 1, factor))
    return [f"{i}: {v}" for i, v in enumerate(multiples)]


def cycle_colors(colors: list[str], count: int) -> list[str]:
    return list(itertools.islice(itertools.cycle(colors), count))


def chain_lists(list1: list, list2: list) -> list:
    return list(itertools.chain(list1, list2))


def all_pairs(list1: list, list2: list) -> list[tuple]:
    return list(itertools.product(list1, list2))
