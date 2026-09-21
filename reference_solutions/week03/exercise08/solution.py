import itertools


def count_up_to(n: int):
    for i in range(1, n + 1):
        yield i


def evens_only(numbers: list[int]):
    for n in numbers:
        if n % 2 == 0:
            yield n


def infinite_counter():
    i = 0
    while True:
        yield i
        i += 1


def take(iterable, n: int) -> list:
    return list(itertools.islice(iterable, n))
