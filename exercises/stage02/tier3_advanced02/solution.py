"""
Control Flow -- Round-Robin Task Scheduler
Write plain top-level code below -- no function/class wrapper needed (or expected) for this one. Assign your answers to the exact variable names named in README.md; the tests import this module and read those variables directly.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage02_tier3_advanced02.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage02/tier3_advanced02/ and import it as a submodule (e.g.
`from exercises.stage02.tier3_advanced02 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import itertools

workers = ["alpha", "beta", "gamma"]
morning_tasks = ["t1", "t2", "t3"]
afternoon_tasks = ["t4", "t5", "t6", "t7"]

raise NotImplementedError  # delete this line once you've written the code below

# Write your code here: all_tasks (itertools.chain), assignments (zip +
# itertools.cycle), first_three_assignments (itertools.islice),
# worker_task_counts (plain for-loop + dict.get). See README.md.
