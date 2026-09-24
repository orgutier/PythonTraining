"""
OOP I -- Bank Account
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage06_basic01.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage06/basic01/ and import it as a submodule (e.g.
`from exercises.stage06.basic01 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


class BankAccount:
    def __init__(self, owner: str, balance: float = 0):
        raise NotImplementedError

    @staticmethod
    def is_valid_amount(amount) -> bool:
        """True if amount is an int/float (not bool) and >= 0."""
        raise NotImplementedError

    @property
    def balance(self) -> float:
        """Return self._balance."""
        raise NotImplementedError

    @balance.setter
    def balance(self, value) -> None:
        """Validate with is_valid_amount, then set self._balance."""
        raise NotImplementedError

    def deposit(self, amount) -> None:
        """self.balance += amount, through the property."""
        raise NotImplementedError

    def withdraw(self, amount) -> None:
        """Raise ValueError if amount > self.balance, else self.balance -= amount."""
        raise NotImplementedError
