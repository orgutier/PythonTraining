"""
Challenge 10 - Log Text Utilities with a Custom Context Manager
Interview-style challenge. Correctness is pytest-tested (see
tests/test_challenge10.py / `python tools/cli.py test challenge10`); see
README.md in this folder for the full problem statement and the constraints
your solution must follow (both forms of a custom context manager (a class and @contextlib.contextmanager), plus re.findall()/re.sub()/re.search()).

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module, matching the convention used by
exercises/stageNN/solution.py.
"""


import re
import contextlib


class SuppressAndCount:
    def __init__(self, *exc_types):
        self.exc_types = exc_types

    def __enter__(self):
        raise NotImplementedError

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Suppress + count a matching exception (issubclass check); else return False."""
        raise NotImplementedError


@contextlib.contextmanager
def suppress_and_count(*exc_types):
    """yield a {"count": 0} dict; catch a matching exception around the yield, incrementing it, without re-raising."""
    raise NotImplementedError


def extract_error_messages(text: str) -> list:
    """Every message following "ERROR " on its own line, via re.findall()."""
    raise NotImplementedError


def redact_ips(text: str) -> str:
    """Every IPv4-shaped address replaced with "[REDACTED]", via re.sub()."""
    raise NotImplementedError


def contains_stack_trace(text: str) -> bool:
    """True if "Traceback (most recent call last):" appears anywhere, via re.search()."""
    raise NotImplementedError
