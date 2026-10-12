"""
Functions -- Order Total Calculator
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage03_tier1_basic01.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage03/tier1_basic01/ and import it as a submodule (e.g.
`from exercises.stage03.tier1_basic01 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


def compute_total(*item_prices, tax_rate=0.08, **surcharges) -> float:
    """subtotal=sum(item_prices); tax=subtotal*tax_rate; + sum(surcharges.values()), rounded to 2dp."""
    raise NotImplementedError


def apply_discount(price, pct=0.10) -> float:
    """round(price * (1 - pct), 2)."""
    raise NotImplementedError
