"""
Python Fundamentals -- Digital Clock Decoder
Write plain top-level code below -- no function/class wrapper needed (or expected) for this one. Assign your answers to the exact variable names named in README.md; the tests import this module and read those variables directly.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage01_tier1_basic02.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage01/tier1_basic02/ and import it as a submodule (e.g.
`from exercises.stage01.tier1_basic02 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


total_seconds_text = "9384"
is_daylight_saving_text = "False"

total_seconds = int(total_seconds_text)
is_daylight_saving = is_daylight_saving_text == "True"

hours = int(total_seconds // 3600)
minutes = int((total_seconds % 3600) // 60)
seconds = int(total_seconds % 60)

print(str(total_seconds) + "s = " + str(hours) + "h " + str(minutes) + "m " + str(seconds) + "s")

# Write your code here: cast total_seconds, decompose it into
# hours/minutes/seconds with // and %, correctly derive is_daylight_saving
# (watch the bool("False") trap!), and print a summary. See README.md.
