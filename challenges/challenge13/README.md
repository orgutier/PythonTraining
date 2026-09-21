# Challenge 13 — Notification System with Mixins and ABCs

**Do this after:** Week 07 (OOP II)
**Correctness is pytest-tested:** `python tools/cli.py test challenge13` (or `pytest tests/test_challenge13.py`). The constraints below on *how* you write it are not something pytest can check -- grade those yourself.

## Problem

"Design a notification system that can email or text people, and retry
flaky ones" is a realistic system-design-flavored coding interview
prompt. It's also a natural fit for almost everything Week 7 covers:
an abstract base class, mixins layered in via multiple inheritance,
`super()` cooperating through that chain, and a dispatcher that uses both
`isinstance()` and duck typing.

Implement:

```python
class Notifier(ABC):
    def __init__(self) -> None:
        """self.sent_count = 0."""

    @abstractmethod
    def send(self, message: str) -> str:
        """Send message; return a delivery confirmation string."""

    def _record(self) -> None:
        """self.sent_count += 1."""

class LoggingMixin:
    def log(self, message: str) -> str:
        """f"[{self.__class__.__name__}] {message}"."""

class RetryMixin:
    max_retries = 3

    def send_with_retry(self, message: str) -> str:
        """Call self.send(message); on ConnectionError, retry up to max_retries times total; re-raise the last error if every attempt fails."""

class EmailNotifier(LoggingMixin, Notifier):
    def __init__(self, address: str) -> None: ...
    def send(self, message: str) -> str:
        """f"Emailed {self.address}: {message}"; call self._record()."""

class SMSNotifier(RetryMixin, LoggingMixin, Notifier):
    def __init__(self, phone: str, fail_times: int = 0) -> None:
        """fail_times: how many of the next send() calls should simulate a ConnectionError, for testing retry."""
    def send(self, message: str) -> str:
        """Raise ConnectionError if fail_times > 0 (decrementing it); else f"Texted {self.phone}: {message}" and self._record()."""

def broadcast(notifiers: list, message: str) -> list:
    """For each item that IS a Notifier: call .send_with_retry(message) if it has that method, else .send(message). Skip (silently) anything that isn't a Notifier at all."""
```

```python
email = EmailNotifier("a@example.com")
sms = SMSNotifier("555-0100", fail_times=2)
broadcast([email, sms, "not a notifier"], "hello")
# -> ["Emailed a@example.com: hello", "Texted 555-0100: hello"]
# (sms succeeded on its 3rd attempt via send_with_retry; the plain string was skipped)
```

## Constraints on HOW you write it

1. **`Notifier` must subclass `abc.ABC`** and **`send` must be
   `@abstractmethod`** -- `Notifier()` on its own must raise `TypeError`.
2. **`EmailNotifier.__init__` and `SMSNotifier.__init__` must call
   `super().__init__()`** before setting their own attributes -- this is
   what actually runs `Notifier.__init__` (setting `sent_count = 0`)
   through the multiple-inheritance chain; skipping it would leave
   `sent_count` never initialized.
3. **`RetryMixin.send_with_retry` must call `self.send(...)`**, not
   reimplement sending itself -- it's a mixin specifically meant to be
   combined with a class that already has its own `send`.
4. **`broadcast` must use `isinstance(notifier, Notifier)`** to filter out
   non-notifiers, and **`hasattr(notifier, "send_with_retry")`** (duck
   typing -- not `isinstance(notifier, RetryMixin)`) to decide whether to
   retry. The dispatcher shouldn't need to know about every mixin by
   name.
5. **A docstring on `broadcast`** listing edge cases: an empty
   `notifiers` list, a notifier that isn't a `Notifier` at all (skipped,
   not an error), and an `SMSNotifier` whose `fail_times` exceeds
   `max_retries` (its `ConnectionError` propagates out of `broadcast`
   uncaught -- document that this is expected, not something `broadcast`
   itself should swallow).
