import collections


def group_by_first_letter(words: list[str]) -> dict:
    groups = collections.defaultdict(list)
    for word in words:
        groups[word[0]].append(word)
    return dict(sorted(groups.items()))


def count_occurrences(items: list) -> dict:
    return dict(collections.Counter(items))


def most_common_n(items: list, n: int) -> list:
    return collections.Counter(items).most_common(n)


def sliding_window_last_n(numbers: list[int], maxlen: int) -> list[int]:
    window = collections.deque(maxlen=maxlen)
    for n in numbers:
        window.append(n)
    return list(window)


def rotate_queue(items: list, k: int) -> list:
    d = collections.deque(items)
    d.rotate(k)
    return list(d)
