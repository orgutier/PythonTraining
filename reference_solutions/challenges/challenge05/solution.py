import functools


def make_pipeline():
    handlers = {}

    def register(name):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            handlers[name] = wrapper
            return wrapper
        return decorator

    def run(name, *args, **kwargs):
        if name not in handlers:
            raise KeyError(f"no handler registered for {name!r}")
        return handlers[name](*args, **kwargs)

    return register, run


def count_calls(func):
    count = 0

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        wrapper.call_count = count
        return func(*args, **kwargs)

    wrapper.call_count = 0
    return wrapper


def memoize(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return wrapper


@functools.lru_cache(maxsize=None)
def cached_expensive(n: int, *, precision: int = 2) -> float:
    return round(n ** 0.5, precision)
