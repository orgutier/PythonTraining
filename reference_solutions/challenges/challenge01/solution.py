def _is_int_literal(s: str) -> bool:
    if s.startswith("-"):
        s = s[1:]
    return len(s) > 0 and s.isdigit()


def _is_float_literal(s: str) -> bool:
    if s.startswith("-"):
        s = s[1:]
    parts = s.split(".")
    if len(parts) != 2:
        return False
    left, right = parts
    return left != "" and right != "" and left.isdigit() and right.isdigit()


def parse_config_line(line: str) -> tuple[str, object]:
    """
    Parse "KEY=value" into (key, typed_value).

    Edge cases handled:
      - No "=" at all -> raises ValueError.
      - Empty value (after stripping) -> None.
      - "true"/"false" in any letter case -> bool (checked before int/float,
        since "true" would otherwise fall through to the str case).
      - A value containing "=" (e.g. a URL with a query string) -> kept
        intact, since we split on the FIRST "=" only.
      - Surrounding whitespace on the key and/or value -> stripped from both.
    """
    if "=" not in line:
        raise ValueError(f"not a KEY=value line: {line!r}")

    raw_key, raw_value = line.split("=", 1)
    key = raw_key.strip()
    value_str = raw_value.strip()

    if value_str == "":
        return key, None
    if value_str.lower() in ("true", "false"):
        return key, value_str.lower() == "true"
    if _is_int_literal(value_str):
        return key, int(value_str)
    if _is_float_literal(value_str):
        return key, float(value_str)
    return key, value_str


def load_config(lines: list[str]) -> dict[str, object]:
    config: dict[str, object] = {}
    for line in lines:
        if line.strip() == "":
            continue
        key, value = parse_config_line(line)
        config[key] = value
    return config


def describe_types(config: dict) -> dict[str, str]:
    return {key: type(value).__name__ for key, value in config.items()}


def merge_configs(base: dict, override: dict) -> dict:
    merged = dict(base)
    merged.update(override)
    return merged
