"""
Week 6 - OOP I
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in tests/test_week06.py
imports directly from here.
"""


class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        raise NotImplementedError

    @property
    def balance(self) -> float:
        raise NotImplementedError

    @balance.setter
    def balance(self, value: float) -> None:
        """Must raise ValueError if value is negative."""
        raise NotImplementedError

    @staticmethod
    def is_valid_amount(amount: float) -> bool:
        raise NotImplementedError
