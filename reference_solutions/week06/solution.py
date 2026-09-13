class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self._balance = 0.0
        self.balance = balance  # goes through the setter for validation

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, value: float) -> None:
        if not BankAccount.is_valid_amount(value):
            raise ValueError("balance cannot be negative")
        self._balance = value

    @staticmethod
    def is_valid_amount(amount: float) -> bool:
        return amount >= 0
