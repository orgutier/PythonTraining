def sum_all(*args: int) -> int:
    return sum(args)


def build_config(**kwargs) -> dict:
    return dict(kwargs)


def describe_call(*args, **kwargs) -> str:
    return f"args={args}, kwargs={kwargs}"
