"""
Stage 1 -- Python Fundamentals.

Pilot of the tier-named exercise convention: a minimum of two exercises per
Basic/Mid/Advanced tier, each folder prefixed with its tier number so a
plain directory listing sorts in learning order --
"tier1_basicNN"/"tier2_midNN"/"tier3_advancedNN" -- instead of a flat
"exercise01".."exercise06" sequence, plus a "tier0_hello_world" exercise for
the stage's Setup sub-stage. Every exercise here is deliberately
**script-style**: plain top-level statements assigning specific
module-level variable names, not a function/class to implement -- Stage 1
hasn't taught `def` yet (that's Stage 3), so there's no reason to wrap
anything in a function here. Tests import the module and read those
variables directly (see generator/common.py's SCRIPT_INSTRUCTIONS).

Coverage plan (every item below is exercised by the trainee's own code,
generally 2+ times across these 7 exercises):

  Basic:    int, float, str, bool, None, True, False, print(), input(),
            type(), isinstance(), and, or, not, is, in, x: int = 5
  Mid:      f-strings, the walrus operator (:=), augmented assignment (+=),
            chained comparisons, operator precedence
  Advanced: arbitrary-precision ints, small-int caching, string interning,
            IEEE-754 float imprecision, Decimal, math.isclose()
"""
from generator.common import SCRIPT_INSTRUCTIONS

STAGE = "stage01"
TOPIC = "Python Fundamentals"
OVERVIEW = (
    "Seven small exercises, each in its own folder: tier0_hello_world (Setup), then "
    "two apiece for the Basic, Mid, and Advanced tiers. Every one is plain "
    "top-level code -- no function to implement -- since Stage 1 hasn't "
    "introduced `def` yet. Each is a small, self-contained scenario (never "
    "just \"print this value\") that forces you to actually combine that "
    "tier's tools, not just demonstrate one in isolation."
)

EXERCISES = [
    {
        "name": "tier0_hello_world",
        "title": "Hello, World! (Environment Check)",
        "summary": "print(), variable assignment, string concatenation -- confirms your environment and this repo's test runner both work",
        "instructions": SCRIPT_INSTRUCTIONS,
        "readme": (
            "The very first program you'll run in this course. It exists purely "
            "to prove your Python install, virtual environment, and this repo's "
            "test runner (`python tools/cli.py test stage01_hello_world`) all "
            "actually work, before we get into any real content.\n\n"
            "Write two lines of code, in order, right in `solution.py` (no "
            "function -- just plain statements):\n\n"
            "1. Assign a variable `greeting` set to exactly `\"Hello, World!\"`, "
            "then `print(greeting)`.\n"
            "2. Assign a variable `author_name` to your own name as a "
            "non-empty string (e.g. `\"Ada\"`), then print a second line built "
            "with string **concatenation** (not an f-string -- those aren't "
            "introduced until the Mid tier): "
            "`print(\"This is \" + author_name + \"'s first Python program.\")`.\n\n"
            "That's it. If `python tools/cli.py test stage01_hello_world` "
            "passes, your setup is good and you're ready for the Basic tier."
        ),
        "stub": '''\
raise NotImplementedError  # delete this line once you've written the two lines below

# Write your code here: assign `greeting` and `author_name`, and print both
# lines exactly as described in README.md.
''',
        "reference": '''\
greeting = "Hello, World!"
print(greeting)

author_name = "Ada"
print("This is " + author_name + "'s first Python program.")
''',
        "test": '''\
import sys


def test_hello_world_variables_and_output(capsys):
    """greeting == "Hello, World!"; author_name is a non-empty str; two print() lines match exactly (concatenation, no f-strings)."""
    sys.modules.pop("exercises.stage01.tier0_hello_world.solution", None)
    import exercises.stage01.tier0_hello_world.solution as solution

    assert solution.greeting == "Hello, World!"
    assert isinstance(solution.author_name, str)
    assert solution.author_name != ""

    out = capsys.readouterr().out
    lines = out.rstrip("\\n").split("\\n")
    assert lines[0] == "Hello, World!"
    assert lines[1] == "This is " + solution.author_name + "'s first Python program."
''',
    },
    {
        "name": "tier1_basic01",
        "title": "Road Trip Fuel Ledger",
        "summary": "explicit int()/float() casting, arithmetic operators, isinstance(), no f-strings yet",
        "instructions": SCRIPT_INSTRUCTIONS,
        "readme": (
            "Four friends are splitting the fuel cost of a road trip. The raw "
            "trip data below arrives as **strings** (as if read from a form) "
            "-- do not modify these four given lines:\n\n"
            "```python\n"
            'distance_km_text = "742.5"\n'
            'fuel_efficiency_l_per_100km_text = "6.8"\n'
            'fuel_price_per_liter_text = "1.53"\n'
            'passengers_text = "3"\n'
            "```\n\n"
            "Using only what the Basic tier has covered so far (arithmetic "
            "operators, explicit `int()`/`float()` casting, comparison "
            "operators, `isinstance()`, `type()`, `print()`) -- **no "
            "`if`/`for`/`while`, no f-strings, no `+=`** (all of those are "
            "Mid/Advanced-tier tools, saved for later exercises) -- write "
            "plain top-level code that computes:\n\n"
            "- `distance_km`, `fuel_efficiency_l_per_100km`, "
            "`fuel_price_per_liter` (each cast to `float`) and `passengers` "
            "(cast to `int`).\n"
            "- `is_price_a_float` -- `True` iff `fuel_price_per_liter` is a "
            "genuine `float` (use `isinstance()`; this should obviously be "
            "`True` here, but writing the check is the point -- you'll rely "
            "on this exact pattern again once the numbers aren't guaranteed "
            "like they are here).\n"
            "- `total_fuel_liters` -- liters needed for the whole trip: "
            "`distance_km / 100 * fuel_efficiency_l_per_100km`.\n"
            "- `total_cost` -- `total_fuel_liters * fuel_price_per_liter`.\n"
            "- `cost_per_passenger` -- `total_cost / passengers`.\n\n"
            "Finish with one `print()` call summarizing the trip, built with "
            "string concatenation and `str()` (still no f-strings) -- "
            'something like `"Total cost: " + str(total_cost)`.'
        ),
        "stub": '''\
distance_km_text = "742.5"
fuel_efficiency_l_per_100km_text = "6.8"
fuel_price_per_liter_text = "1.53"
passengers_text = "3"

raise NotImplementedError  # delete this line once you've written the code below

# Write your code here: cast the four values above, compute
# is_price_a_float/total_fuel_liters/total_cost/cost_per_passenger, and
# print a one-line summary. See README.md for the exact requirements.
''',
        "reference": '''\
distance_km_text = "742.5"
fuel_efficiency_l_per_100km_text = "6.8"
fuel_price_per_liter_text = "1.53"
passengers_text = "3"

distance_km = float(distance_km_text)
fuel_efficiency_l_per_100km = float(fuel_efficiency_l_per_100km_text)
fuel_price_per_liter = float(fuel_price_per_liter_text)
passengers = int(passengers_text)

is_price_a_float = isinstance(fuel_price_per_liter, float)

total_fuel_liters = distance_km / 100 * fuel_efficiency_l_per_100km
total_cost = total_fuel_liters * fuel_price_per_liter
cost_per_passenger = total_cost / passengers

print("Total cost: " + str(total_cost) + ", per passenger: " + str(cost_per_passenger))
''',
        "test": '''\
import pytest

import exercises.stage01.tier1_basic01.solution as solution


def test_casts_to_correct_types():
    """distance_km/fuel_efficiency_l_per_100km/fuel_price_per_liter are float() casts; passengers is an int() cast (not a bool)."""
    assert isinstance(solution.distance_km, float)
    assert isinstance(solution.fuel_efficiency_l_per_100km, float)
    assert isinstance(solution.fuel_price_per_liter, float)
    assert isinstance(solution.passengers, int)
    assert not isinstance(solution.passengers, bool)


def test_is_price_a_float_flag():
    """is_price_a_float must be isinstance(fuel_price_per_liter, float) -- not just truthy, the exact isinstance() check."""
    assert solution.is_price_a_float is True


def test_total_fuel_liters():
    """total_fuel_liters == distance_km / 100 * fuel_efficiency_l_per_100km."""
    assert solution.total_fuel_liters == pytest.approx(50.49)


def test_total_cost():
    """total_cost == total_fuel_liters * fuel_price_per_liter."""
    assert solution.total_cost == pytest.approx(77.2497)


def test_cost_per_passenger():
    """cost_per_passenger == total_cost / passengers."""
    assert solution.cost_per_passenger == pytest.approx(25.7499)
''',
    },
    {
        "name": "tier1_basic02",
        "title": "Digital Clock Decoder",
        "summary": "// and % chained together, explicit bool-from-string casting (avoiding the bool(str) trap)",
        "instructions": SCRIPT_INSTRUCTIONS,
        "readme": (
            "A monitoring system logs elapsed time as a raw seconds count, "
            "and a daylight-saving flag as literal text -- both as strings, "
            "don't modify:\n\n"
            "```python\n"
            'total_seconds_text = "9384"\n'
            'is_daylight_saving_text = "False"\n'
            "```\n\n"
            "Using only Basic-tier tools, write plain top-level code that "
            "computes:\n\n"
            "- `total_seconds` -- `total_seconds_text` cast to `int`.\n"
            "- `hours`, `minutes`, `seconds` -- decompose `total_seconds` "
            "into hours/minutes/seconds using `//` and `%` (chain them: get "
            "`hours` and a remainder, then get `minutes` from that remainder "
            "and a second remainder, then `seconds` from that).\n"
            "- `is_daylight_saving` -- a genuine `bool`, `True` only if "
            '`is_daylight_saving_text` is literally the text `"True"`. '
            '**Do not write `bool(is_daylight_saving_text)`** -- in Python, '
            '`bool("False")` is `True`, because *any* non-empty string is '
            'truthy, including the string `"False"` itself. Compare the '
            'text against the string `"True"` instead (`==`) to get a '
            "correct result.\n\n"
            "Finish with one `print()` call (concatenation + `str()`, no "
            "f-strings yet) summarizing the decoded time, e.g. something "
            'like `"9384s = " + str(hours) + "h " + str(minutes) + "m " + '
            'str(seconds) + "s"`.'
        ),
        "stub": '''\
total_seconds_text = "9384"
is_daylight_saving_text = "False"

raise NotImplementedError  # delete this line once you've written the code below

# Write your code here: cast total_seconds, decompose it into
# hours/minutes/seconds with // and %, correctly derive is_daylight_saving
# (watch the bool("False") trap!), and print a summary. See README.md.
''',
        "reference": '''\
total_seconds_text = "9384"
is_daylight_saving_text = "False"

total_seconds = int(total_seconds_text)

hours = total_seconds // 3600
remaining_after_hours = total_seconds % 3600
minutes = remaining_after_hours // 60
seconds = remaining_after_hours % 60

is_daylight_saving = is_daylight_saving_text == "True"

print(
    str(total_seconds) + "s = " + str(hours) + "h " + str(minutes) + "m " +
    str(seconds) + "s"
)
''',
        "test": '''\
import exercises.stage01.tier1_basic02.solution as solution


def test_total_seconds_cast():
    """total_seconds == int(total_seconds_text)."""
    assert solution.total_seconds == 9384
    assert isinstance(solution.total_seconds, int)


def test_decomposition():
    """hours/minutes/seconds chain // and % on total_seconds (3600, then 60)."""
    assert solution.hours == 2
    assert solution.minutes == 36
    assert solution.seconds == 24


def test_decomposition_reconstructs_total():
    """hours*3600 + minutes*60 + seconds must reconstruct total_seconds exactly."""
    assert solution.hours * 3600 + solution.minutes * 60 + solution.seconds == 9384


def test_is_daylight_saving_avoids_bool_string_trap():
    """is_daylight_saving must be (text == "True"), NOT bool(text) -- bool("False") is True, that's the trap."""
    assert solution.is_daylight_saving is False
''',
    },
    {
        "name": "tier2_mid01",
        "title": "Precision Price Comparator",
        "summary": "operator precedence, chained comparisons, the walrus operator, f-strings, augmented assignment",
        "instructions": SCRIPT_INSTRUCTIONS,
        "readme": (
            "Two suppliers quote prices for the same part; you're comparing "
            "them for a bulk order. Given, don't modify:\n\n"
            "```python\n"
            'price_a_text = "19.99"\n'
            'price_b_text = "18.995"\n'
            'quantity_text = "4"\n'
            "```\n\n"
            "Using Mid-tier tools this time (f-strings, the walrus operator, "
            "chained comparisons, augmented assignment, operator precedence "
            "-- still no `if`/`for`/`while`), write plain top-level code "
            "that computes:\n\n"
            "- `price_a`, `price_b` (`float`), `quantity` (`int`).\n"
            "- `savings_message` -- an f-string that computes the total "
            "savings of buying `quantity` units from the cheaper supplier "
            "**using the walrus operator inside the f-string's expression** "
            "to both compute and capture a `savings` value in one go, e.g. "
            'shaped like `f"...{(savings := abs(price_a - price_b) * '
            'quantity):.2f}..."`. After this line, `savings` must exist as '
            "its own module-level name too (that's exactly what the walrus "
            "operator gives you -- the assignment happens as a side effect "
            "of evaluating the f-string expression, so you're not computing "
            "the value twice).\n"
            "- `both_under_20` -- `True` iff *both* prices are in `[0, 20)`, "
            "written as **one chained comparison** per price, combined with "
            "`and` (`0 <= price_a < 20 and 0 <= price_b < 20`).\n"
            "- `total_cost` -- start it at `0.0`, then use **augmented "
            "assignment** (`+=`) twice, once per supplier's "
            "`price * quantity`, to build up the total (don't just write "
            "`price_a * quantity + price_b * quantity` directly -- the "
            "point here is practicing `+=`).\n"
            "- `weighted_score` -- `2 + 3 * price_a ** 2`, written in "
            "exactly that form so you have to get the precedence right "
            "(`**` binds tighter than `*`, which binds tighter than `+`) "
            "rather than adding parentheses to force the order yourself.\n\n"
            "Finish with `print(savings_message)`."
        ),
        "stub": '''\
price_a_text = "19.99"
price_b_text = "18.995"
quantity_text = "4"

raise NotImplementedError  # delete this line once you've written the code below

# Write your code here: cast the three values above, then compute
# savings_message (walrus + f-string), both_under_20 (chained comparison),
# total_cost (+=, twice), and weighted_score (precedence-sensitive).
# See README.md for the exact requirements.
''',
        "reference": '''\
price_a_text = "19.99"
price_b_text = "18.995"
quantity_text = "4"

price_a = float(price_a_text)
price_b = float(price_b_text)
quantity = int(quantity_text)

savings_message = f"Switching suppliers saves {(savings := abs(price_a - price_b) * quantity):.2f}"

both_under_20 = 0 <= price_a < 20 and 0 <= price_b < 20

total_cost = 0.0
total_cost += price_a * quantity
total_cost += price_b * quantity

weighted_score = 2 + 3 * price_a ** 2

print(savings_message)
''',
        "test": '''\
import pytest

import exercises.stage01.tier2_mid01.solution as solution


def test_casts_to_correct_types():
    """price_a/price_b are float() casts, quantity is an int() cast."""
    assert isinstance(solution.price_a, float)
    assert isinstance(solution.price_b, float)
    assert isinstance(solution.quantity, int)


def test_walrus_computed_savings_is_exposed_as_module_variable():
    """The walrus assignment inside savings_message's f-string must expose `savings` as its own module-level name too."""
    assert solution.savings == pytest.approx(3.98)


def test_savings_message_contains_the_formatted_value():
    """savings_message is an f-string containing the walrus-computed, :.2f-formatted savings value."""
    assert "3.98" in solution.savings_message


def test_both_under_20_chained_comparison():
    """both_under_20 must be a single chained comparison (0 <= price < 20) for each price, joined with `and`."""
    assert solution.both_under_20 is True


def test_total_cost_via_augmented_assignment():
    """total_cost starts at 0.0 and is built up with two `+=` statements, not a single expression."""
    assert solution.total_cost == pytest.approx(155.94)


def test_weighted_score_respects_operator_precedence():
    """weighted_score == 2 + 3 * price_a ** 2, written exactly in that form (no extra parentheses)."""
    assert solution.weighted_score == pytest.approx(1200.8003)
''',
    },
    {
        "name": "tier2_mid02",
        "title": "Marathon Pace Report",
        "summary": "more precedence/walrus/chained-comparison/augmented-assignment practice, a different scenario",
        "instructions": SCRIPT_INSTRUCTIONS,
        "readme": (
            "A runner's marathon result needs analyzing. Given, don't "
            "modify:\n\n"
            "```python\n"
            'race_distance_km_text = "42.195"\n'
            'elapsed_minutes_text = "255"\n'
            'target_minutes_text = "240"\n'
            "```\n\n"
            "Same Mid-tier toolbox as the previous exercise, different "
            "combination -- write plain top-level code that computes:\n\n"
            "- `race_distance_km` (`float`), `elapsed_minutes`, "
            "`target_minutes` (`int`).\n"
            "- `pace_min_per_km` -- `elapsed_minutes / race_distance_km`.\n"
            "- `pace_report` -- an f-string that uses the **walrus "
            "operator** to compute and capture `minutes_over` "
            "(`elapsed_minutes - target_minutes`) as part of building the "
            'message, e.g. shaped like `f"...{(minutes_over := '
            'elapsed_minutes - target_minutes)}...{pace_min_per_km:.2f}..."`. '
            "`minutes_over` must exist as its own module-level name "
            "afterward.\n"
            "- `minutes_over_per_km` -- `minutes_over / race_distance_km`, "
            "computed using the `minutes_over` the walrus operator gave you "
            "(don't recompute `elapsed_minutes - target_minutes` a second "
            "time).\n"
            "- `on_pace` -- `True` iff `pace_min_per_km` is strictly "
            "greater than `0` and at most `6.5`, written as **one chained "
            "comparison**: `0 < pace_min_per_km <= 6.5`.\n"
            "- `total_penalty_seconds` -- start it at `0`, then use "
            "**augmented assignment** twice: add a flat `30`, then add "
            "`minutes_over * 2`.\n"
            "- `fatigue_index` -- `2 + 3 * pace_min_per_km ** 2`, written "
            "in exactly that form (precedence, no extra parentheses).\n\n"
            "Finish with `print(pace_report)`."
        ),
        "stub": '''\
race_distance_km_text = "42.195"
elapsed_minutes_text = "255"
target_minutes_text = "240"

raise NotImplementedError  # delete this line once you've written the code below

# Write your code here: cast the three values above, then compute
# pace_min_per_km, pace_report (walrus + f-string), minutes_over_per_km,
# on_pace (chained comparison), total_penalty_seconds (+=, twice), and
# fatigue_index (precedence-sensitive). See README.md.
''',
        "reference": '''\
race_distance_km_text = "42.195"
elapsed_minutes_text = "255"
target_minutes_text = "240"

race_distance_km = float(race_distance_km_text)
elapsed_minutes = int(elapsed_minutes_text)
target_minutes = int(target_minutes_text)

pace_min_per_km = elapsed_minutes / race_distance_km

pace_report = (
    f"{(minutes_over := elapsed_minutes - target_minutes)} minutes over target, "
    f"averaging {pace_min_per_km:.2f} min/km"
)

minutes_over_per_km = minutes_over / race_distance_km

on_pace = 0 < pace_min_per_km <= 6.5

total_penalty_seconds = 0
total_penalty_seconds += 30
total_penalty_seconds += minutes_over * 2

fatigue_index = 2 + 3 * pace_min_per_km ** 2

print(pace_report)
''',
        "test": '''\
import pytest

import exercises.stage01.tier2_mid02.solution as solution


def test_casts_to_correct_types():
    """race_distance_km is a float() cast; elapsed_minutes/target_minutes are int() casts."""
    assert isinstance(solution.race_distance_km, float)
    assert isinstance(solution.elapsed_minutes, int)
    assert isinstance(solution.target_minutes, int)


def test_pace_min_per_km():
    """pace_min_per_km == elapsed_minutes / race_distance_km."""
    assert solution.pace_min_per_km == pytest.approx(6.04337)


def test_walrus_computed_minutes_over_is_exposed_as_module_variable():
    """The walrus assignment inside pace_report's f-string must expose `minutes_over` as its own module-level name too."""
    assert solution.minutes_over == 15


def test_pace_report_contains_minutes_over_and_formatted_pace():
    """pace_report is an f-string containing both the walrus-computed minutes_over and the :.2f-formatted pace."""
    assert "15" in solution.pace_report
    assert "6.04" in solution.pace_report


def test_minutes_over_per_km_reuses_walrus_value():
    """minutes_over_per_km == minutes_over / race_distance_km -- reusing the walrus value, not recomputing elapsed_minutes - target_minutes."""
    assert solution.minutes_over_per_km == pytest.approx(0.35549, abs=1e-4)


def test_on_pace_chained_comparison():
    """on_pace must be one chained comparison: 0 < pace_min_per_km <= 6.5."""
    assert solution.on_pace is True


def test_total_penalty_seconds_via_augmented_assignment():
    """total_penalty_seconds starts at 0 and is built up with two `+=` statements (a flat 30, then minutes_over * 2)."""
    assert solution.total_penalty_seconds == 60


def test_fatigue_index_respects_operator_precedence():
    """fatigue_index == 2 + 3 * pace_min_per_km ** 2, written exactly in that form (no extra parentheses)."""
    assert solution.fatigue_index == pytest.approx(111.56697)
''',
    },
    {
        "name": "tier3_advanced01",
        "title": "Exact Ledger vs. Float Drift",
        "summary": "Decimal built from string (not float), math.isclose() vs ==, the classic 0.1+0.2 case",
        "instructions": SCRIPT_INSTRUCTIONS,
        "readme": (
            "An invoicing system needs exact currency totals, but float "
            "arithmetic can't reliably give you that. Given, don't "
            "modify:\n\n"
            "```python\n"
            'price_each_text = "19.99"\n'
            'quantity_text = "7"\n'
            "```\n\n"
            "Using Advanced-tier tools (`decimal.Decimal`, "
            "`math.isclose`), write plain top-level code that computes:\n\n"
            "- `price_each_float` (`float`), `quantity` (`int`).\n"
            "- `float_total` -- `price_each_float * quantity`, plain float "
            "arithmetic.\n"
            "- `exact_total` -- a `decimal.Decimal`, built from "
            "`Decimal(price_each_text) * Decimal(quantity_text)` -- "
            "**construct both `Decimal`s from the original string text, "
            "not from the float** (`Decimal(price_each_float)` would "
            "already have inherited the float's rounding error before you "
            "even start).\n"
            "- `totals_are_exactly_equal` -- "
            "`float(exact_total) == float_total`.\n"
            "- `totals_are_close` -- "
            "`math.isclose(float(exact_total), float_total)`. "
            "(`math.isclose` is the correct way to compare floats; a bare "
            "`==` is not reliable, which is exactly what the previous two "
            "variables demonstrate.)\n"
            "- The textbook version of the same lesson, with fixed "
            "literals (not derived from the ledger above): "
            "`point_one_plus_point_two = 0.1 + 0.2`, "
            "`is_exactly_point_three = point_one_plus_point_two == 0.3`, "
            "and `is_close_to_point_three = "
            "math.isclose(point_one_plus_point_two, 0.3)`.\n\n"
            "Finish with one `print()` call (f-strings are fine now) "
            "reporting `exact_total` and whether the two totals matched "
            "exactly."
        ),
        "stub": '''\
price_each_text = "19.99"
quantity_text = "7"

raise NotImplementedError  # delete this line once you've written the code below

# Write your code here: cast price_each_text/quantity_text, compute
# float_total and exact_total (Decimal built FROM THE STRINGS), the two
# totals_are_* comparisons, and the 0.1+0.2 textbook demo. See README.md.
''',
        "reference": '''\
import math
from decimal import Decimal

price_each_text = "19.99"
quantity_text = "7"

price_each_float = float(price_each_text)
quantity = int(quantity_text)

float_total = price_each_float * quantity
exact_total = Decimal(price_each_text) * Decimal(quantity_text)

totals_are_exactly_equal = float(exact_total) == float_total
totals_are_close = math.isclose(float(exact_total), float_total)

point_one_plus_point_two = 0.1 + 0.2
is_exactly_point_three = point_one_plus_point_two == 0.3
is_close_to_point_three = math.isclose(point_one_plus_point_two, 0.3)

print(f"Exact total: {exact_total}, exactly matched float total: {totals_are_exactly_equal}")
''',
        "test": '''\
import math
from decimal import Decimal

import exercises.stage01.tier3_advanced01.solution as solution


def test_casts_and_float_total():
    """price_each_float is a float() cast, quantity is an int() cast; float_total is plain float arithmetic."""
    assert isinstance(solution.price_each_float, float)
    assert isinstance(solution.quantity, int)
    assert solution.float_total == solution.price_each_float * 7


def test_exact_total_is_precise_decimal():
    """exact_total must be Decimal(price_each_text) * Decimal(quantity_text) -- built from the STRINGS, not the float."""
    assert solution.exact_total == Decimal("139.93")


def test_totals_are_not_exactly_equal_due_to_float_drift():
    """totals_are_exactly_equal == (float(exact_total) == float_total) -- this is False; that's the whole point."""
    assert solution.totals_are_exactly_equal is False


def test_totals_are_close():
    """totals_are_close == math.isclose(float(exact_total), float_total) -- the correct way to compare these."""
    assert solution.totals_are_close is True


def test_point_one_plus_point_two_textbook_case():
    """The classic case: 0.1 + 0.2 != 0.3 exactly, but math.isclose() says they're close."""
    assert solution.is_exactly_point_three is False
    assert solution.is_close_to_point_three is True
    assert math.isclose(solution.point_one_plus_point_two, 0.3)
''',
    },
    {
        "name": "tier3_advanced02",
        "title": "Big Numbers and String Identity",
        "summary": "arbitrary-precision integers, small-int caching, string interning (and its limits)",
        "instructions": SCRIPT_INSTRUCTIONS,
        "readme": (
            "Given, don't modify:\n\n"
            "```python\n"
            'base_text = "97"\n'
            'exponent_text = "42"\n'
            "```\n\n"
            "Using Advanced-tier tools, write plain top-level code that "
            "computes:\n\n"
            "- `base`, `exponent` (`int`).\n"
            "- `huge_power` -- `base ** exponent`. Python integers have "
            "arbitrary precision, so this doesn't overflow no matter how "
            "large it gets.\n"
            "- `huge_power_digit_count` -- `len(str(huge_power))`, proving "
            "`huge_power` is genuinely bigger than any fixed-width integer "
            "could hold.\n"
            "- `small_int_a`, `small_int_b` -- both set to the literal "
            "`100`.\n"
            "- `small_ints_share_identity` -- `small_int_a is "
            "small_int_b`. CPython caches small integers (`-5` to `256`), "
            "so this is `True`.\n"
            "- `large_int_from_literal`, `large_int_from_conversion` -- "
            "the first is the literal `1_000_000`; the second is "
            '`int("1000000")` (built at runtime, **not** a second literal '
            "-- two identical literals in the same file can get folded "
            "into a single cached object by the compiler, which would "
            "defeat the point of this exercise).\n"
            "- `large_ints_share_identity` -- `large_int_from_literal is "
            "large_int_from_conversion`. Large integers are **not** "
            "guaranteed to be cached, so (with the runtime-constructed "
            "value above) this is `False`.\n"
            "- `string_literal_a`, `string_literal_b` -- both set to the "
            'literal `"python_stage01"`.\n'
            "- `string_literals_share_identity` -- `string_literal_a is "
            "string_literal_b`. Simple string literals are interned at "
            "compile time, so this is `True`.\n"
            "- `string_built_at_runtime` -- "
            '`"".join(["python_", "stage01"])` (same text, built '
            "dynamically).\n"
            "- `runtime_string_shares_identity` -- `string_literal_a is "
            "string_built_at_runtime`. Dynamically built strings are "
            "**not** automatically interned, so this is `False` even "
            "though the two strings are `==`-equal.\n\n"
            "Finish with one `print()` call reporting "
            "`huge_power_digit_count`."
        ),
        "stub": '''\
base_text = "97"
exponent_text = "42"

raise NotImplementedError  # delete this line once you've written the code below

# Write your code here: cast base/exponent, compute huge_power and its
# digit count, then work through the small-int-caching, large-int, and
# string-interning identity checks described in README.md.
''',
        "reference": '''\
base_text = "97"
exponent_text = "42"

base = int(base_text)
exponent = int(exponent_text)

huge_power = base ** exponent
huge_power_digit_count = len(str(huge_power))

small_int_a = 100
small_int_b = 100
small_ints_share_identity = small_int_a is small_int_b

large_int_from_literal = 1_000_000
large_int_from_conversion = int("1000000")
large_ints_share_identity = large_int_from_literal is large_int_from_conversion

string_literal_a = "python_stage01"
string_literal_b = "python_stage01"
string_literals_share_identity = string_literal_a is string_literal_b

string_built_at_runtime = "".join(["python_", "stage01"])
runtime_string_shares_identity = string_literal_a is string_built_at_runtime

print(f"huge_power has {huge_power_digit_count} digits")
''',
        "test": '''\
import exercises.stage01.tier3_advanced02.solution as solution


def test_huge_power_has_arbitrary_precision():
    """huge_power == base ** exponent, with no overflow; huge_power_digit_count == len(str(huge_power))."""
    assert solution.huge_power == 97 ** 42
    assert solution.huge_power_digit_count > 19  # bigger than any 64-bit int could hold


def test_small_int_caching():
    """small_ints_share_identity == (small_int_a is small_int_b) -- both literal 100s; CPython caches -5..256."""
    assert solution.small_ints_share_identity is True


def test_large_ints_not_guaranteed_cached():
    """large_int_from_conversion must be int("1000000") at RUNTIME, not a second literal -- large ints aren't guaranteed cached."""
    assert solution.large_int_from_literal == solution.large_int_from_conversion
    assert solution.large_ints_share_identity is False


def test_string_literal_interning():
    """string_literals_share_identity == (string_literal_a is string_literal_b) -- both literal "python_stage01"; simple literals are interned."""
    assert solution.string_literals_share_identity is True


def test_runtime_built_string_not_interned():
    """string_built_at_runtime must be "".join([...]) built dynamically -- equal to string_literal_a by value, but not the same object."""
    assert solution.string_literal_a == solution.string_built_at_runtime
    assert solution.runtime_string_shares_identity is False
''',
    },
    {
        "name": "tier4_testing",
        "title": "Testing Without a Framework: Catch the Bug",
        "summary": "manual, framework-free verification -- plain comparisons, no assert, no pytest",
        "instructions": SCRIPT_INSTRUCTIONS,
        "readme": (
            "Every other exercise in this stage asked you to implement "
            "something. This one asks you to **verify** something -- the "
            "instinct you'll need for the rest of your career, long before "
            "(and long after) any test framework is involved. You will "
            "**not** import `pytest`, `unittest`, or anything like them in "
            "this file -- just plain Python comparisons.\n\n"
            "Given, don't modify (both pairs below are *supposed* to "
            "compute the same thing -- at least one of each pair has a "
            "bug; your job is to catch it by testing, not to fix it):\n\n"
            "```python\n"
            'price_text = "19.99"\n'
            'quantity_text = "3"\n'
            'discount_flag_text = "False"\n\n'
            "target_total_v1 = float(price_text) * int(quantity_text)\n"
            "target_total_v2 = float(price_text) + int(quantity_text)\n\n"
            'target_is_discounted_v1 = discount_flag_text == "True"\n'
            "target_is_discounted_v2 = bool(discount_flag_text)\n"
            "```\n\n"
            "The spec each pair is supposed to meet:\n\n"
            "- **total** should equal `price * quantity`.\n"
            '- **is_discounted** should be `True` only if `discount_flag_text` '
            'is literally the string `"True"`.\n\n'
            "Write plain top-level code that:\n\n"
            "- Builds `check_results` -- a list of `(description, passed)` "
            "tuples, `description` a short string and `passed` a `bool` -- "
            "with **exactly one entry per target value above** (four "
            "total): compute the expected value from the spec yourself "
            "(e.g. `float(price_text) * int(quantity_text)`), compare it "
            "against the target with `==`, and append the result. No "
            "`assert` -- a failing comparison should become a recorded "
            "`False`, not a crash that stops the remaining checks from "
            "running.\n"
            "- `total_checks` -- `len(check_results)`.\n"
            "- `passed_checks` -- how many entries in `check_results` "
            "passed.\n"
            "- `failed_descriptions` -- the `description` of every entry "
            "that did **not** pass, in order.\n\n"
            "If you did this right, `passed_checks` won't be `4` -- and "
            "that's the point: a check written against the *spec* (not "
            "against \"whatever the target already returns\") is what "
            "catches a real bug instead of just rubber-stamping it.\n\n"
            "See the Study Reference presentation, Topic 1, for the theory."
        ),
        "stub": '''\
price_text = "19.99"
quantity_text = "3"
discount_flag_text = "False"

target_total_v1 = float(price_text) * int(quantity_text)
target_total_v2 = float(price_text) + int(quantity_text)

target_is_discounted_v1 = discount_flag_text == "True"
target_is_discounted_v2 = bool(discount_flag_text)

raise NotImplementedError  # delete this line once you've written the code below

# Write your code here: build check_results (a list of (description, bool)
# tuples) using plain comparisons against the spec in README.md -- no
# assert, no test framework -- then compute total_checks/passed_checks/
# failed_descriptions from check_results.
''',
        "reference": '''\
price_text = "19.99"
quantity_text = "3"
discount_flag_text = "False"

target_total_v1 = float(price_text) * int(quantity_text)
target_total_v2 = float(price_text) + int(quantity_text)

target_is_discounted_v1 = discount_flag_text == "True"
target_is_discounted_v2 = bool(discount_flag_text)

check_results = []

expected_total = float(price_text) * int(quantity_text)
check_results.append(("target_total_v1 meets spec", target_total_v1 == expected_total))
check_results.append(("target_total_v2 meets spec", target_total_v2 == expected_total))

expected_is_discounted = discount_flag_text == "True"
check_results.append(("target_is_discounted_v1 meets spec", target_is_discounted_v1 == expected_is_discounted))
check_results.append(("target_is_discounted_v2 meets spec", target_is_discounted_v2 == expected_is_discounted))

total_checks = len(check_results)
passed_checks = sum(1 for _, ok in check_results if ok)
failed_descriptions = [desc for desc, ok in check_results if not ok]
''',
        "test": '''\
import exercises.stage01.tier4_testing.solution as solution


def test_check_results_has_one_entry_per_target_value():
    """check_results must have exactly four (description, bool) entries, one per target value in README.md."""
    assert len(solution.check_results) == 4


def test_check_results_entries_are_description_bool_pairs():
    """Each check_results entry must be a (str, bool) tuple, not a raised assert."""
    for entry in solution.check_results:
        assert isinstance(entry, tuple) and len(entry) == 2
        description, passed = entry
        assert isinstance(description, str) and description != ""
        assert isinstance(passed, bool)


def test_total_and_passed_checks_reflect_the_real_bugs():
    """total_checks == 4; passed_checks == 2 -- the v1 variants meet spec, the v2 variants don't."""
    assert solution.total_checks == 4
    assert solution.passed_checks == 2


def test_failed_descriptions_derived_from_check_results():
    """failed_descriptions must be exactly the descriptions of the failing entries in check_results, in order."""
    expected = [desc for desc, ok in solution.check_results if not ok]
    assert solution.failed_descriptions == expected
    assert len(solution.failed_descriptions) == 2
''',
    },
]
