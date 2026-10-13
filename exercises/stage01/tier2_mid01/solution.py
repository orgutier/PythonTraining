"""
Python Fundamentals -- Precision Price Comparator
Write plain top-level code below -- no function/class wrapper needed (or expected) for this one. Assign your answers to the exact variable names named in README.md; the tests import this module and read those variables directly.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage01_tier2_mid01.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage01/tier2_mid01/ and import it as a submodule (e.g.
`from exercises.stage01.tier2_mid01 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""

price_a_text = "19.99"
price_b_text = "18.995"
quantity_text = "4"

# Write your code here: cast the three values above, then compute
# savings_message (walrus + f-string), both_under_20 (chained comparison),
# total_cost (+=, twice), and weighted_score (precedence-sensitive).
# See README.md for the exact requirements.

price_a= float(price_a_text)
price_b= float(price_b_text)
quantity= int(quantity_text)

savings_message = f"{(savings := abs(price_a - price_b)*quantity):.2f}."

print(savings)


both_under_20 = 0 <= price_a < 20 and 0 <= price_b < 20

total_cost = 0
total_cost += price_a * quantity
total_cost += price_b * quantity

weighted_score = 2 + 3 * price_a **2

print(weighted_score)