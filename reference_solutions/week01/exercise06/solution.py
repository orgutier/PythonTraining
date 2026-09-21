def append_and_return(lst: list, item) -> list:
    lst.append(item)
    return lst


def concat_strings(a: str, b: str) -> str:
    return a + b


def same_object(a, b) -> bool:
    return a is b


def equal_but_not_identical() -> tuple:
    return ([1, 2, 3], [1, 2, 3])


def default_if_none(value, default):
    return default if value is None else value
