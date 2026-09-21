import itertools


def retry_until_clean(batches: list, max_retries: int, bad_levels: tuple = ("ERROR", "CRITICAL")) -> int:
    """
    Cyclically retry batches[0], batches[1], ... up to max_retries attempts.

    Edge cases handled:
      - Empty batches -> raises ValueError (nothing meaningful to retry).
      - max_retries == 0 -> no attempt is made, returns -1 immediately.
      - batches[0] already clean -> returns 0 on the very first attempt.
    """
    if not batches:
        raise ValueError("batches must not be empty")

    attempt = 0
    while attempt < max_retries:
        index = attempt % len(batches)
        batch = batches[index]
        if any(entry[1] in bad_levels for entry in batch):
            attempt += 1
            continue
        break
    else:
        return -1
    return index


def group_consecutive_runs(levels: list) -> list:
    if not levels:
        return []
    runs = [[levels[0]]]
    for i in range(1, len(levels)):
        if levels[i] == levels[i - 1]:
            runs[-1].append(levels[i])
        else:
            runs.append([levels[i]])
    return runs


def status_label(count: int) -> str:
    return "empty" if count == 0 else "ok" if count < 5 else "busy"


def interleave_first_n(batches: list, limit: int) -> list:
    return list(itertools.islice(itertools.chain.from_iterable(batches), limit))
