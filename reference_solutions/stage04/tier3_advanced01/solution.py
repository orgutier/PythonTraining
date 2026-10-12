import collections


def entries_by_level(entries: list[str]) -> dict:
    groups = collections.defaultdict(list)
    for entry in entries:
        level = entry.split(":")[0]
        groups[level].append(entry)
    return dict(sorted(groups.items()))


def level_counts(entries: list[str]) -> dict:
    levels = [entry.split(":")[0] for entry in entries]
    return dict(collections.Counter(levels))


def most_common_level(entries: list[str]) -> tuple:
    levels = [entry.split(":")[0] for entry in entries]
    return collections.Counter(levels).most_common(1)[0]


def last_n_entries(entries: list[str], n: int) -> list[str]:
    window = collections.deque(maxlen=n)
    for entry in entries:
        window.append(entry)
    return list(window)


def rotate_entries(entries: list[str], k: int) -> list[str]:
    d = collections.deque(entries)
    d.rotate(k)
    return list(d)
