# Bank Account

Implement `BankAccount`:

- `__init__(self, owner: str, balance: float = 0)` -- store `self.owner = owner` and set the *property* `self.balance = balance` (going through the setter below, so an invalid starting balance is rejected the same way a later deposit would be).
- `is_valid_amount(amount) -> bool` (`@staticmethod`) -- `True` if `amount` is an `int`/`float` and `amount >= 0`. It's a `@staticmethod` because it doesn't need `self` at all -- it's just a validation helper that happens to live on the class.
- `balance` (`@property`) -- getter returns `self._balance` (the real, "private-by-convention" storage -- this is what *encapsulation* means here: callers use `.balance`, never `._balance` directly).
- `balance` setter (`@balance.setter`) -- `raise ValueError` if `not self.is_valid_amount(value)`, else set `self._balance = value`.
- `deposit(self, amount) -> None` -- `self.balance = self.balance + amount` (going through the property, so the setter's validation applies).
- `withdraw(self, amount) -> None` -- `raise ValueError` if `amount > self.balance`, else `self.balance = self.balance - amount`.

See the Study Reference presentation, Topic 6, for the theory.
