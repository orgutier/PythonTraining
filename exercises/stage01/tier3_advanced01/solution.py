"""
Python Fundamentals -- Exact Ledger vs. Float Drift
Write plain top-level code below -- no function/class wrapper needed (or expected) for this one. Assign your answers to the exact variable names named in README.md; the tests import this module and read those variables directly.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage01_tier3_advanced01.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage01/tier3_advanced01/ and import it as a submodule (e.g.
`from exercises.stage01.tier3_advanced01 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""
from decimal import Decimal
import math

price_each_text = "19.99"
quantity_text = "7"

# Write your code here: cast price_each_text/quantity_text, compute
# float_total and exact_total (Decimal built FROM THE STRINGS), the two
# totals_are_* comparisons, and the 0.1+0.2 textbook demo. See README.md.

price_each_float:float = float(price_each_text)
quantity:int = int(quantity_text)

float_total: float = price_each_float * quantity
exact_total: Decimal = Decimal(price_each_text) * Decimal(quantity_text) 

totals_are_exactly_equal = float(exact_total) == float_total
totals_are_close: bool = math.isclose(float(exact_total), float_total)

point_one_plus_point_two:float = 0.1+0.2
is_exactly_point_three: bool = point_one_plus_point_two == 0.3
is_close_to_point_three: bool = math.isclose(point_one_plus_point_two,0.3)

print(exact_total)