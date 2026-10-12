import re


def extract_ticket_ids(text: str) -> list[str]:
    return re.findall(r"TICKET-\d+", text)


def contains_urgent_flag(text: str) -> bool:
    return re.search(r"\bURGENT\b", text) is not None


def clean_ticket_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def looks_like_ticket_id(text: str) -> bool:
    return re.match(r"TICKET-\d+$", text) is not None


def parse_priority(raw: str) -> int:
    try:
        return int(raw)
    except ValueError:
        raise Exception(f"invalid priority: {raw!r}")


_parse_attempts = 0


def parse_priority_with_default(raw: str, default: int = 0) -> int:
    global _parse_attempts
    try:
        return int(raw)
    except ValueError:
        return default
    finally:
        _parse_attempts += 1


def get_parse_attempts() -> int:
    return _parse_attempts
