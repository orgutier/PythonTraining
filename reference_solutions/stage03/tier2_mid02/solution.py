def count_calls(fn):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return fn(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


def greet(name):
    return "Hello, " + name


def make_validator(*, min_value, max_value=100):
    def validate(n):
        return min_value <= n <= max_value

    return validate
