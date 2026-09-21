def describe_value(value) -> str:
    if value is None:
        return "None (the absence of a value)"
    return f"{value!r} is a {type(value).__name__}"


def print_type_report(value) -> None:
    print(describe_value(value))


def classify_values(values: list) -> dict:
    buckets = {"ints": [], "floats": [], "strs": [], "bools": [], "nones": []}
    for v in values:
        if v is None:
            buckets["nones"].append(v)
        elif type(v) is bool:
            buckets["bools"].append(v)
        elif isinstance(v, int):
            buckets["ints"].append(v)
        elif isinstance(v, float):
            buckets["floats"].append(v)
        elif isinstance(v, str):
            buckets["strs"].append(v)
    return buckets
