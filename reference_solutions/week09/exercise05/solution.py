import datetime


def current_timestamp_iso() -> str:
    return datetime.datetime.now().isoformat()


def format_date(dt) -> str:
    return dt.strftime("%Y-%m-%d")


def parse_iso(text: str):
    return datetime.datetime.fromisoformat(text)


def days_between(d1, d2) -> int:
    return (d2 - d1).days
