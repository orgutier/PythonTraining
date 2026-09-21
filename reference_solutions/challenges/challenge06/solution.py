import functools


def stream_batches(data: list, size: int, /):
    """
    Yield successive chunks of data, each up to size items long.

    Edge cases handled:
      - len(data) not a multiple of size -> the final chunk is shorter
        than size (whatever remains).
      - Empty data -> the generator yields nothing at all.
    """
    for i in range(0, len(data), size):
        yield data[i:i + size]


_total_processed = 0


def process_batch(batch: list, /, *, transform=lambda x: x) -> list:
    global _total_processed
    result = [transform(item) for item in batch]
    _total_processed += len(batch)
    return result


def get_total_processed() -> int:
    return _total_processed


def reset_total_processed() -> None:
    global _total_processed
    _total_processed = 0


def _scale(factor, value):
    return value * factor


def make_scaled_transform(factor: int):
    return functools.partial(_scale, factor)
