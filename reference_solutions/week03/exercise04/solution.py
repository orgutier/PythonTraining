_counter = 0


def increment_counter() -> int:
    global _counter
    _counter += 1
    return _counter


def reset_counter() -> None:
    global _counter
    _counter = 0


def set_counter(value: int) -> None:
    global _counter
    _counter = value


def get_counter() -> int:
    return _counter


def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


def make_accumulator(start: int = 0):
    total = start

    def add(x):
        nonlocal total
        total += x
        return total

    return add


def make_toggle(initial: bool = False):
    state = initial

    def toggle():
        nonlocal state
        state = not state
        return state

    return toggle
