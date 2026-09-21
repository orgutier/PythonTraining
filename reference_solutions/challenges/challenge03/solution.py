def parse_log_stream(lines: list[str]) -> list[tuple[str, str, str]]:
    """
    Parse "HH:MM LEVEL message" lines into (time, level, message) tuples.

    Edge cases handled:
      - Blank lines (after stripping) are skipped with `continue`, not
        included as empty-tuple entries.
      - A message containing spaces is kept intact, since we split with
        maxsplit=2 (only the first two spaces are structural).
      - An all-blank input list returns an empty list.
    """
    entries = []
    for line in lines:
        if not line.strip():
            continue
        time, level, message = line.split(" ", 2)
        entries.append((time, level, message))
    return entries


def first_critical_index(entries: list[tuple], levels: tuple = ("ERROR", "CRITICAL")) -> int:
    for i, entry in enumerate(entries):
        if entry[1] in levels:
            break
    else:
        return -1
    return i


def label_entries(entries: list[tuple]) -> list[str]:
    return [f"{i}: {level} - {message}" for i, (time, level, message) in enumerate(entries)]


def pair_with_severity(entries: list[tuple], severities: list[int]) -> list[tuple]:
    return list(zip(entries, severities))


def is_healthy(entries: list[tuple], levels: tuple = ("CRITICAL",)) -> bool:
    return bool(entries) and not any(entry[1] in levels for entry in entries)
