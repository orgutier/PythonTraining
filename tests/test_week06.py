import pytest
from exercises.week06.solution import BankAccount


def test_bank_account_balance():
    acct = BankAccount("Ana", 100)
    assert acct.balance == 100


def test_bank_account_negative_raises():
    acct = BankAccount("Ana", 100)
    with pytest.raises(ValueError):
        acct.balance = -50


def test_is_valid_amount():
    assert BankAccount.is_valid_amount(-5) is False
    assert BankAccount.is_valid_amount(10) is True
