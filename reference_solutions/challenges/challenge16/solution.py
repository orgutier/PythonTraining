class Ledger:
    def __init__(self) -> None:
        self._entries = []
        self._pending = None

    def __call__(self, amount: float, description: str = "") -> None:
        target = self._pending if self._pending is not None else self._entries
        target.append((amount, description))

    def __enter__(self) -> "Ledger":
        self._pending = []
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        """
        End the current batch.

        Edge cases handled:
          - A batch with zero calls -> commits an empty batch, a no-op;
            len() is unaffected either way.
          - An exception partway through a batch -> the ENTIRE batch is
            discarded, including entries recorded before the exception,
            not just the ones after it.
        """
        if exc_type is None:
            self._entries.extend(self._pending)
        self._pending = None
        return False

    def __len__(self) -> int:
        return len(self._entries)

    def __repr__(self) -> str:
        return f"Ledger({len(self)} entries)"

    @property
    def balance(self) -> float:
        return sum(amount for amount, _ in self._entries)
