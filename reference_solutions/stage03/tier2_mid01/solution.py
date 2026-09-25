def make_logger(*, prefix, max_entries=5):
    entries = []

    def log(message):
        entries.append(prefix + ": " + message)
        if len(entries) > max_entries:
            entries.pop(0)
        return list(entries)

    return log


def clamp(value, lo, hi, /):
    if value < lo:
        return lo
    if value > hi:
        return hi
    return value


def function_signature_info(fn) -> dict:
    return {"name": fn.__name__, "doc": fn.__doc__}
