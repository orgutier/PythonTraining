"""
Python Fundamentals -- Road Trip Fuel Ledger
Write plain top-level code below -- no function/class wrapper needed (or expected) for this one. Assign your answers to the exact variable names named in README.md; the tests import this module and read those variables directly.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage01_tier1_basic01.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage01/tier1_basic01/ and import it as a submodule (e.g.
`from exercises.stage01.tier1_basic01 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


distance_km_text = "742.5"
fuel_efficiency_l_per_100km_text = "6.8"
fuel_price_per_liter_text = "1.53"
passengers_text = "3"

distance_km: float = float(distance_km_text)
fuel_efficiency_l_per_100km: float = float(fuel_efficiency_l_per_100km_text)
fuel_price_per_liter: float = float(fuel_price_per_liter_text)
passengers: int = int(passengers_text)

is_price_a_float: bool = isinstance(fuel_price_per_liter, float)
total_fuel_liters: float = distance_km * fuel_efficiency_l_per_100km / 100
total_cost: float = total_fuel_liters * fuel_price_per_liter
cost_per_passenger: float = total_cost / passengers

print("Total cost: " + str(total_cost) + ", Cost per passenger: " + str(cost_per_passenger))
