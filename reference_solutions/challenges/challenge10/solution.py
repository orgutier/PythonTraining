import re
import contextlib


class SuppressAndCount:
    def __init__(self, *exc_types):
        self.exc_types = exc_types

    def __enter__(self):
        self.count = 0
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None and issubclass(exc_type, self.exc_types):
            self.count += 1
            return True
        return False


@contextlib.contextmanager
def suppress_and_count(*exc_types):
    state = {"count": 0}
    try:
        yield state
    except exc_types:
        state["count"] += 1


def extract_error_messages(text: str) -> list:
    return re.findall(r"ERROR (.+)$", text, re.MULTILINE)


def redact_ips(text: str) -> str:
    return re.sub(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", "[REDACTED]", text)


def contains_stack_trace(text: str) -> bool:
    return re.search(r"Traceback \(most recent call last\):", text) is not None
