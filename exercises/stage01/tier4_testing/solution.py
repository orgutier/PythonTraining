"""
Python Fundamentals -- Testing Without a Framework: Catch the Bug
Write plain top-level code below -- no function/class wrapper needed (or expected) for this one. Assign your answers to the exact variable names named in README.md; the tests import this module and read those variables directly.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage01_tier4_testing.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage01/tier4_testing/ and import it as a submodule (e.g.
`from exercises.stage01.tier4_testing import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


from typing import Tuple


price_text = "19.99"
quantity_text = "3"
discount_flag_text = "False"

target_total_v1 = float(price_text) * int(quantity_text)
target_total_v2 = float(price_text) + int(quantity_text)


target_is_discounted_v1 = discount_flag_text == "True"
target_is_discounted_v2 = bool(discount_flag_text)

print(target_is_discounted_v1, target_is_discounted_v2)

# Write your code here: build check_results (a list of (description, bool)
# tuples) using plain comparisons against the spec in README.md -- no
# assert, no test framework -- then compute total_checks/passed_checks/
# failed_descriptions from check_results.


expected_total = float(price_text) * int(quantity_text)
expected_discounted = discount_flag_text == "True"

check_results: list[tuple[str, bool]] = [
    ("target_total_v1", expected_total == target_total_v1),
    ("target_total_v2", expected_total == target_total_v2),
    ("target_is_discounted_v1", expected_discounted == target_is_discounted_v1),
    ("target_is_discounted_v2", expected_discounted == target_is_discounted_v2),
]

#sumar los resultados de las comprobaciones
total_checks = len(check_results)
passed_checks = 0
failed_descriptions = []

for description, result in check_results:
    if result:
        passed_checks +=1
    else:
        failed_descriptions.append(description)
    

print(f"Total checks: {total_checks}")
print(f"Passed checks: {passed_checks}")
print(f"Failed checks: {failed_descriptions}")
