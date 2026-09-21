import pytest
from challenges.challenge13.solution import (
    Notifier,
    LoggingMixin,
    RetryMixin,
    EmailNotifier,
    SMSNotifier,
    broadcast,
)


def test_notifier_cannot_be_instantiated():
    with pytest.raises(TypeError):
        Notifier()


def test_email_notifier_send_and_record():
    email = EmailNotifier("a@example.com")
    assert email.send("hi") == "Emailed a@example.com: hi"
    assert email.sent_count == 1


def test_super_init_runs_through_mixin_chain():
    email = EmailNotifier("a@example.com")
    assert email.sent_count == 0  # set by Notifier.__init__ via super()


def test_sms_notifier_send_with_retry_succeeds_eventually():
    sms = SMSNotifier("555-0100", fail_times=2)
    result = sms.send_with_retry("hi")
    assert result == "Texted 555-0100: hi"
    assert sms.sent_count == 1


def test_sms_notifier_send_with_retry_gives_up_after_max_retries():
    sms = SMSNotifier("555-0100", fail_times=5)
    with pytest.raises(ConnectionError):
        sms.send_with_retry("hi")


def test_logging_mixin():
    email = EmailNotifier("a@example.com")
    assert email.log("test") == "[EmailNotifier] test"


def test_broadcast_uses_retry_when_available_and_skips_non_notifiers():
    email = EmailNotifier("a@example.com")
    sms = SMSNotifier("555-0100", fail_times=1)
    results = broadcast([email, sms, "not a notifier", 42], "hello")
    assert results == ["Emailed a@example.com: hello", "Texted 555-0100: hello"]


def test_broadcast_empty_list():
    assert broadcast([], "hello") == []
