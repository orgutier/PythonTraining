class BankAccount:
    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        self.balance = balance

    @staticmethod
    def is_valid_amount(amount) -> bool:
        return isinstance(amount, (int, float)) and not isinstance(amount, bool) and amount >= 0

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, value) -> None:
        if not self.is_valid_amount(value):
            raise ValueError(f"invalid balance: {value!r}")
        self._balance = value

    def deposit(self, amount) -> None:
        self.balance = self.balance + amount

    def withdraw(self, amount) -> None:
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance = self.balance - amount
