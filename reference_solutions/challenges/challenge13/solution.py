from abc import ABC, abstractmethod


class Notifier(ABC):
    def __init__(self) -> None:
        self.sent_count = 0

    @abstractmethod
    def send(self, message: str) -> str:
        raise NotImplementedError

    def _record(self) -> None:
        self.sent_count += 1


class LoggingMixin:
    def log(self, message: str) -> str:
        return f"[{self.__class__.__name__}] {message}"


class RetryMixin:
    max_retries = 3

    def send_with_retry(self, message: str) -> str:
        last_error = None
        for _ in range(self.max_retries):
            try:
                return self.send(message)
            except ConnectionError as e:
                last_error = e
        raise last_error


class EmailNotifier(LoggingMixin, Notifier):
    def __init__(self, address: str) -> None:
        super().__init__()
        self.address = address

    def send(self, message: str) -> str:
        self._record()
        return f"Emailed {self.address}: {message}"


class SMSNotifier(RetryMixin, LoggingMixin, Notifier):
    def __init__(self, phone: str, fail_times: int = 0) -> None:
        super().__init__()
        self.phone = phone
        self._fail_times = fail_times

    def send(self, message: str) -> str:
        if self._fail_times > 0:
            self._fail_times -= 1
            raise ConnectionError("simulated failure")
        self._record()
        return f"Texted {self.phone}: {message}"


def broadcast(notifiers: list, message: str) -> list:
    """
    Send message via every Notifier in notifiers.

    Edge cases handled:
      - Empty notifiers -> returns [].
      - A non-Notifier item -> skipped silently (isinstance check).
      - An SMSNotifier whose fail_times exceeds max_retries -> its
        ConnectionError propagates out of broadcast uncaught; broadcast
        does not swallow a failure that outlasted its own retries.
    """
    results = []
    for notifier in notifiers:
        if not isinstance(notifier, Notifier):
            continue
        if hasattr(notifier, "send_with_retry"):
            results.append(notifier.send_with_retry(message))
        else:
            results.append(notifier.send(message))
    return results
