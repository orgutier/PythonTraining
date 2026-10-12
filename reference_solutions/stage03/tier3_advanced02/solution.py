counter = 0


def batch_generator(items, batch_size):
    for i in range(0, len(items), batch_size):
        yield items[i:i + batch_size]


def increment_global() -> int:
    global counter
    counter += 1
    return counter


def make_local_shadow() -> int:
    counter = 100
    return counter


def append_bad(item, target=[]):
    target.append(item)
    return target


def append_safe(item, target=None):
    if target is None:
        target = []
    target.append(item)
    return target
