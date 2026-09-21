import pytest
from challenges.challenge16.solution import Ledger


def test_call_outside_with_commits_immediately():
    ledger = Ledger()
    ledger(100, "deposit")
    assert len(ledger) == 1
    assert ledger.balance == 100


def test_with_block_commits_batch_on_clean_exit():
    ledger = Ledger()
    with ledger as l:
        assert l is ledger
        ledger(-30, "withdrawal")
        ledger(-20, "fee")
    assert len(ledger) == 2
    assert ledger.balance == -50


def test_with_block_rolls_back_entire_batch_on_exception():
    ledger = Ledger()
    ledger(100, "deposit")
    with pytest.raises(RuntimeError):
        with ledger:
            ledger(-30, "withdrawal")
            ledger(9999, "should not count")
            raise RuntimeError("oops")
    assert len(ledger) == 1
    assert ledger.balance == 100


def test_exit_never_suppresses_the_exception():
    ledger = Ledger()
    with pytest.raises(ValueError):
        with ledger:
            raise ValueError("boom")


def test_empty_batch_is_a_noop():
    ledger = Ledger()
    with ledger:
        pass
    assert len(ledger) == 0


def test_repr():
    ledger = Ledger()
    ledger(50, "x")
    assert repr(ledger) == "Ledger(1 entries)"
