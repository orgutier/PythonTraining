def build_shopping_list(items: list[str]) -> list[str]:
    result = []
    for item in items:
        result.append(item)
    return result


def unique_sorted(numbers: list[int]) -> list[int]:
    return sorted(set(numbers))


def sort_in_place(items: list) -> None:
    items.sort()


def as_tuple_pairs(names: list[str], ages: list[int]) -> list[tuple]:
    return list(zip(names, ages))


def zip_and_sum(list1: list[int], list2: list[int]) -> list[int]:
    return [a + b for a, b in zip(list1, list2)]


def label_each(items: list[str]) -> list[str]:
    return [f"{i}:{v}" for i, v in enumerate(items)]


def count_items(items: list) -> int:
    return len(items)
