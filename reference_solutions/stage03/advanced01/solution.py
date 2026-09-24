import functools


def logged(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)

    return wrapper


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


@functools.lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


add_ten = functools.partial(lambda a, b: a + b, b=10)
