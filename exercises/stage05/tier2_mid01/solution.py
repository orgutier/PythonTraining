"""
Files, Exceptions, Regex -- Order Validation Pipeline
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage05_tier2_mid01.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage05/tier2_mid01/ and import it as a submodule (e.g.
`from exercises.stage05.tier2_mid01 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


class OrderError(Exception):
    pass


class OrderValidationError(OrderError):
    pass


class OrderProcessingError(OrderError):
    pass


def parse_order_quantity(raw: str) -> int:
    """int(raw) (chain ValueError via `from e`); then validate qty > 0 (raise directly, no chain)."""
    raise NotImplementedError


def apply_bulk_discount(quantity: int, discount_pct_raw: str) -> float:
    """float(discount_pct_raw) (chain ValueError via `from e`); validate 0..100 (raise ... from None if not)."""
    raise NotImplementedError


def fulfill_order(quantity: int, stock: int) -> int:
    """stock - quantity, or raise OrderProcessingError if quantity > stock."""
    raise NotImplementedError
