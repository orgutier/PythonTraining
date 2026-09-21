"""
Challenge 16 - Transaction Ledger: Callable and Context Manager
Interview-style challenge. Correctness is pytest-tested (see
tests/test_challenge16.py / `python tools/cli.py test challenge16`); see
README.md in this folder for the full problem statement and the constraints
your solution must follow (__call__ for recording, __enter__/__exit__ for batched commit-or-rollback semantics, and __len__/__repr__ reinforced in a different class).

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module, matching the convention used by
exercises/weekNN/solution.py.
"""


class Ledger:
    def __init__(self) -> None:
        raise NotImplementedError

    def __call__(self, amount: float, description: str = "") -> None:
        """Record directly, or buffer if a batch (via __enter__) is currently open."""
        raise NotImplementedError

    def __enter__(self) -> "Ledger":
        """Start an empty batch; return self."""
        raise NotImplementedError

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        """Commit the batch if exc_type is None, else discard it. Always return False."""
        raise NotImplementedError

    def __len__(self) -> int:
        """Number of committed entries."""
        raise NotImplementedError

    def __repr__(self) -> str:
        raise NotImplementedError

    @property
    def balance(self) -> float:
        """Sum of every committed entry's amount."""
        raise NotImplementedError
