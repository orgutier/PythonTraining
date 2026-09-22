"""
Challenge 13 - Notification System with Mixins and ABCs
Interview-style challenge. Correctness is pytest-tested (see
tests/test_challenge13.py / `python tools/cli.py test challenge13`); see
README.md in this folder for the full problem statement and the constraints
your solution must follow (an abc.ABC base with @abstractmethod, cooperative super().__init__() through a mixin chain, and isinstance()/duck typing in the dispatcher).

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module, matching the convention used by
exercises/stageNN/solution.py.
"""


from abc import ABC, abstractmethod


class Notifier(ABC):
    def __init__(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def send(self, message: str) -> str:
        raise NotImplementedError

    def _record(self) -> None:
        raise NotImplementedError


class LoggingMixin:
    def log(self, message: str) -> str:
        """f"[{self.__class__.__name__}] {message}"."""
        raise NotImplementedError


class RetryMixin:
    max_retries = 3

    def send_with_retry(self, message: str) -> str:
        """Call self.send(message); retry on ConnectionError up to max_retries times."""
        raise NotImplementedError


class EmailNotifier(LoggingMixin, Notifier):
    def __init__(self, address: str) -> None:
        raise NotImplementedError

    def send(self, message: str) -> str:
        raise NotImplementedError


class SMSNotifier(RetryMixin, LoggingMixin, Notifier):
    def __init__(self, phone: str, fail_times: int = 0) -> None:
        raise NotImplementedError

    def send(self, message: str) -> str:
        raise NotImplementedError


def broadcast(notifiers: list, message: str) -> list:
    """isinstance() to filter Notifiers; hasattr() to prefer send_with_retry when available."""
    raise NotImplementedError
