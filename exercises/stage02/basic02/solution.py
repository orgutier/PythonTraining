"""
Control Flow -- Bus Route Ticket Counter
Write plain top-level code below -- no function/class wrapper needed (or expected) for this one. Assign your answers to the exact variable names named in README.md; the tests import this module and read those variables directly.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage02_basic02.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage02/basic02/ and import it as a submodule (e.g.
`from exercises.stage02.basic02 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


events = ["IN:2", "IN:1", "OUT:1", "SKIP", "BAD", "IN:5", "OUT:2", "IN:0", "OUT:10"]
capacity = 6
sections = 3
rows_per_section = 2
seats_per_row = 2

raise NotImplementedError  # delete this line once you've written the code below

# Write your code here: a while-loop processing `events` into `passengers`
# and `trip_ended_early`, then a SEPARATE nested for-loop computing
# `total_seats` and `capacity_is_valid`. See README.md for the exact
# requirements.
