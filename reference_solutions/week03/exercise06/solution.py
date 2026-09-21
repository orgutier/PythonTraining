import functools


@functools.lru_cache(maxsize=None)
def cached_fibonacci(n: int) -> int:
    if n in (0, 1):
        return n
    return cached_fibonacci(n - 1) + cached_fibonacci(n - 2)


@functools.lru_cache(maxsize=None)
def cached_is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


@functools.lru_cache(maxsize=None)
def cached_factorial(n: int) -> int:
    if n in (0, 1):
        return 1
    return n * cached_factorial(n - 1)


def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b


def format_currency(amount: float, symbol: str) -> str:
    return f"{symbol}{amount:.2f}"


def make_adder(n: int):
    return functools.partial(add, n)


def make_multiplier_via_partial(n: int):
    return functools.partial(multiply, n)


def make_usd_formatter():
    return functools.partial(format_currency, symbol="$")
