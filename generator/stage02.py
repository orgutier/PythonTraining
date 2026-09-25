"""
Stage 2 -- Control Flow.

Tier-named convention (see generator/stage01.py for the full rationale):
minimum two exercises per Basic/Mid/Advanced tier, script-style (plain
top-level code, no function to implement) wherever the tier's own content
doesn't itself require one. Stage 2 still hasn't taught `def` (that's
Stage 3), so every exercise here is script-style *except* tier3_advanced01,
which is deliberately class-based -- writing a custom iterator is this
tier's own named learning objective (see data.js's Advanced tier text:
"custom iterable/iterator class... the iterator protocol").

Coverage:
  Basic:    if/elif/else, while, for + range(), break, continue, pass,
            nested loops
  Mid:      for...else / while...else, short-circuit and/or, ternary
            expressions, zip()
  Advanced: a custom iterator class (__iter__/__next__/StopIteration),
            itertools (chain, cycle, islice)
"""
from generator.common import SCRIPT_INSTRUCTIONS

STAGE = "stage02"
TOPIC = "Control Flow"
OVERVIEW = (
    "Six exercises, two per tier, plus no separate setup exercise (Stage 1 "
    "already covered that). Every one is a small scenario -- a grid scan, a "
    "bus manifest, a restock check, a round-robin scheduler -- that forces "
    "combining several of that tier's control-flow tools at once, not a "
    "single isolated demo."
)

EXERCISES = [
    {
        "name": "tier1_basic01",
        "title": "Warehouse Grid Scanner",
        "summary": "nested for + range(), if/elif/else, continue, pass, while + break",
        "instructions": SCRIPT_INSTRUCTIONS,
        "readme": (
            "A warehouse floor is mapped as rows of characters -- given, "
            "don't modify:\n\n"
            "```python\n"
            'grid_rows = ["..#..", ".##..", "?.#.#", "?????", "#..X."]\n'
            "```\n"
            '`"#"` is an obstacle, `"."` is empty floor, `"?"` is '
            'deliberately unmapped (ignore it, don\'t count it as anything), '
            "and any other character is invalid data.\n\n"
            "Using nested `for` loops over `range(len(...))` (index both "
            "the rows and each row's characters -- no `enumerate()` yet), "
            "`if`/`elif`/`else`, `continue`, and `pass`, write plain "
            "top-level code that computes:\n\n"
            "- `obstacle_count` -- total `\"#\"` characters across the "
            "whole grid.\n"
            "- `unmapped_count` -- total `\"?\"` characters across the "
            "whole grid.\n"
            "- `invalid_char_count` -- total characters that are none of "
            '`"#"`/`"."`/`"?"`.\n'
            "- `first_obstacle_row`, `first_obstacle_col` -- the row/column "
            "indices of the very first `\"#\"` found (scanning row by row, "
            "left to right within a row); `-1`/`-1` if none. Track this "
            "with an `if first_obstacle_row == -1:` guard inside the "
            "obstacle branch -- don't overwrite it once set.\n"
            "- `rows_skipped` -- **before** scanning a row's individual "
            'characters, `continue` straight past any row that\'s entirely '
            '`"?????"` (all-unmapped) -- there\'s nothing to learn from '
            "scanning it character by character, so skip it outright and "
            "count the skip.\n\n"
            "Use `elif ...: pass` for the `\"?\"` case inside the "
            "character-by-character scan (rows that aren't *entirely* "
            "unmapped can still contain individual `\"?\"` cells) -- an "
            "explicit, documented no-op, not an accident.\n\n"
            "Then, **separately**, use a `while` loop (not the `for` loops "
            "above) to scan the grid **from the bottom up** and find "
            "`last_obstacle_row` -- the index of the last row (searching "
            "backward) that contains at least one `\"#\"` (`\"#\" in "
            "grid_rows[i]`); `break` the moment you find one. `-1` if none."
        ),
        "stub": '''\
grid_rows = ["..#..", ".##..", "?.#.#", "?????", "#..X."]

raise NotImplementedError  # delete this line once you've written the code below

# Write your code here: nested for-loops (with continue/pass) for
# obstacle_count/unmapped_count/invalid_char_count/first_obstacle_row/
# first_obstacle_col/rows_skipped, then a separate while-loop (with break)
# for last_obstacle_row. See README.md for the exact requirements.
''',
        "reference": '''\
grid_rows = ["..#..", ".##..", "?.#.#", "?????", "#..X."]

obstacle_count = 0
unmapped_count = 0
invalid_char_count = 0
first_obstacle_row = -1
first_obstacle_col = -1
rows_skipped = 0

for row_index in range(len(grid_rows)):
    row = grid_rows[row_index]
    if row == "?????":
        rows_skipped += 1
        continue
    for col_index in range(len(row)):
        char = row[col_index]
        if char == "#":
            obstacle_count += 1
            if first_obstacle_row == -1:
                first_obstacle_row = row_index
                first_obstacle_col = col_index
        elif char == "?":
            pass
        elif char == ".":
            pass
        else:
            invalid_char_count += 1
        if char == "?":
            unmapped_count += 1

last_obstacle_row = -1
row_cursor = len(grid_rows) - 1
while row_cursor >= 0:
    if "#" in grid_rows[row_cursor]:
        last_obstacle_row = row_cursor
        break
    row_cursor -= 1
''',
        "test": '''\
import exercises.stage02.tier1_basic01.solution as solution


def test_obstacle_count():
    """obstacle_count == total "#" characters across the grid."""
    assert solution.obstacle_count == 6


def test_unmapped_count():
    """unmapped_count == total "?" characters, only from rows NOT skipped entirely."""
    assert solution.unmapped_count == 1


def test_invalid_char_count():
    """invalid_char_count == total characters that are none of "#"/"."/"?"."""
    assert solution.invalid_char_count == 1


def test_first_obstacle_position():
    """first_obstacle_row/col == the first "#" found scanning row by row, left to right."""
    assert solution.first_obstacle_row == 0
    assert solution.first_obstacle_col == 2


def test_rows_skipped():
    """rows_skipped counts rows that are entirely "?????", skipped via continue before the inner scan."""
    assert solution.rows_skipped == 1


def test_last_obstacle_row_via_while_and_break():
    """last_obstacle_row is found by a SEPARATE while-loop scanning from the bottom, breaking on the first hit."""
    assert solution.last_obstacle_row == 4
''',
    },
    {
        "name": "tier1_basic02",
        "title": "Bus Route Ticket Counter",
        "summary": "while as the main loop, if/elif/else, break, continue, pass, nested for",
        "instructions": SCRIPT_INSTRUCTIONS,
        "readme": (
            "A bus's boarding log is a list of event strings -- given, "
            "don't modify:\n\n"
            "```python\n"
            'events = ["IN:2", "IN:1", "OUT:1", "SKIP", "BAD", "IN:5", "OUT:2", "IN:0", "OUT:10"]\n'
            "capacity = 6\n"
            "```\n\n"
            'Each event is `"IN:n"` (n people board), `"OUT:n"` (n people '
            'leave), `"SKIP"` (an empty stop, nothing happens), or -- '
            "anything else -- malformed data to be silently ignored.\n\n"
            "Process `events` **in order with a `while` loop** (an index "
            "cursor, not a `for`), tracking `passengers` starting at `0`:\n\n"
            '- `"IN:n"` -- if adding `n` would push `passengers` over '
            "`capacity`, the trip ends immediately: set `trip_ended_early "
            "= True` and `break` (don't add those n people at all). "
            "Otherwise add them.\n"
            '- `"OUT:n"` -- subtract `n` from `passengers`; if that would '
            "go negative, clamp it to `0` (people can't un-leave).\n"
            '- `"SKIP"` -- advance the cursor and `continue` immediately, '
            "no other change.\n"
            "- anything else -- explicitly do nothing (`pass`); this is "
            "malformed data, not a stop that affects the count.\n\n"
            "`trip_ended_early` must start `False` (only the overflow case "
            "sets it `True`).\n\n"
            "Then, **separately**, using nested `for` loops (not the "
            "`while` loop above), compute the bus's total seat count: "
            "given `sections = 3`, `rows_per_section = 2`, "
            "`seats_per_row = 2` (all given, don't modify), loop over "
            "sections and, for each, over its rows, adding `seats_per_row` "
            "to a running `total_seats` each time. Then set "
            "`capacity_is_valid = capacity <= total_seats`."
        ),
        "stub": '''\
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
''',
        "reference": '''\
events = ["IN:2", "IN:1", "OUT:1", "SKIP", "BAD", "IN:5", "OUT:2", "IN:0", "OUT:10"]
capacity = 6
sections = 3
rows_per_section = 2
seats_per_row = 2

passengers = 0
trip_ended_early = False
i = 0
while i < len(events):
    event = events[i]
    if event.startswith("IN:"):
        n = int(event.split(":")[1])
        if passengers + n > capacity:
            trip_ended_early = True
            break
        passengers += n
    elif event.startswith("OUT:"):
        n = int(event.split(":")[1])
        passengers -= n
        if passengers < 0:
            passengers = 0
    elif event == "SKIP":
        i += 1
        continue
    else:
        pass
    i += 1

total_seats = 0
for section in range(sections):
    for row in range(rows_per_section):
        total_seats += seats_per_row

capacity_is_valid = capacity <= total_seats
''',
        "test": '''\
import exercises.stage02.tier1_basic02.solution as solution


def test_passengers_after_processing():
    """passengers reflects IN:/OUT: events up to (not including) the one that triggers overflow."""
    assert solution.passengers == 2


def test_trip_ended_early_flag():
    """trip_ended_early is True once an IN:n would push passengers over capacity."""
    assert solution.trip_ended_early is True


def test_skip_event_uses_continue():
    """A "SKIP" event must be a no-op -- passengers unaffected either way."""
    # passengers already covers this indirectly: 2+1-1=2, SKIP contributes nothing.
    assert solution.passengers == 2


def test_bad_event_uses_pass_not_a_crash():
    """A malformed event ("BAD") must be silently ignored (pass), not raise or change state."""
    assert solution.passengers == 2


def test_total_seats_via_nested_for():
    """total_seats == sections * rows_per_section * seats_per_row, built with nested for-loops and +=."""
    assert solution.total_seats == 12


def test_capacity_is_valid():
    """capacity_is_valid == (capacity <= total_seats)."""
    assert solution.capacity_is_valid is True
''',
    },
    {
        "name": "tier2_mid01",
        "title": "Shift Coverage Checker",
        "summary": "for...else, a short-circuit guard, a ternary, zip()",
        "instructions": SCRIPT_INSTRUCTIONS,
        "readme": (
            "A shift roster -- given, don't modify:\n\n"
            "```python\n"
            'scheduled_names = ["Ana", "Ben", "Cy", "Dee", "Ella"]\n'
            'checked_in_names = ["Ben", "Dee", "Ana"]\n'
            "shift_hours = [8, 6, 10, 4, 9]\n"
            "max_hours = 9\n"
            "```\n\n"
            "(`shift_hours[i]` is `scheduled_names[i]`'s scheduled hours.)\n\n"
            "Using Mid-tier tools, write plain top-level code that "
            "computes:\n\n"
            "- `all_checked_in` -- a **`for...else`** loop over "
            "`scheduled_names`: if a name isn't in `checked_in_names`, set "
            "`all_checked_in = False` and `break`; the loop's `else` "
            "clause (only reached if the loop never broke) sets "
            "`all_checked_in = True`. Don't pre-initialize "
            "`all_checked_in` before the loop -- both branches set it, so "
            "it doesn't need one.\n"
            "- `missing_list` -- a plain `for` loop collecting every "
            "scheduled name **not** in `checked_in_names`, in order (not a "
            "comprehension -- those aren't introduced until Stage 4).\n"
            "- `first_missing_has_long_shift` -- **one short-circuit `and` "
            "expression**: `len(missing_list) > 0 and "
            "shift_hours[scheduled_names.index(missing_list[0])] > "
            "max_hours`. The `len(...) > 0` check must come first -- it's "
            "what makes indexing `missing_list[0]` safe on the right side.\n"
            "- `coverage_status` -- a **ternary expression**: `\"full\"` if "
            "`missing_list` is empty, else `\"short-staffed\"`.\n"
            "- `overtime_names` -- a plain `for` loop using **`zip(scheduled_names, "
            "shift_hours)`** to walk both lists together, collecting every "
            "name whose hours exceed `max_hours`."
        ),
        "stub": '''\
scheduled_names = ["Ana", "Ben", "Cy", "Dee", "Ella"]
checked_in_names = ["Ben", "Dee", "Ana"]
shift_hours = [8, 6, 10, 4, 9]
max_hours = 9

raise NotImplementedError  # delete this line once you've written the code below

# Write your code here: all_checked_in (for...else), missing_list (plain
# for loop), first_missing_has_long_shift (short-circuit and), coverage_status
# (ternary), overtime_names (for + zip()). See README.md.
''',
        "reference": '''\
scheduled_names = ["Ana", "Ben", "Cy", "Dee", "Ella"]
checked_in_names = ["Ben", "Dee", "Ana"]
shift_hours = [8, 6, 10, 4, 9]
max_hours = 9

for name in scheduled_names:
    if name not in checked_in_names:
        all_checked_in = False
        break
else:
    all_checked_in = True

missing_list = []
for name in scheduled_names:
    if name not in checked_in_names:
        missing_list.append(name)

first_missing_has_long_shift = (
    len(missing_list) > 0
    and shift_hours[scheduled_names.index(missing_list[0])] > max_hours
)

coverage_status = "full" if len(missing_list) == 0 else "short-staffed"

overtime_names = []
for name, hours in zip(scheduled_names, shift_hours):
    if hours > max_hours:
        overtime_names.append(name)
''',
        "test": '''\
import exercises.stage02.tier2_mid01.solution as solution


def test_all_checked_in_via_for_else():
    """all_checked_in must be False as soon as a scheduled name isn't checked in (for...else, break)."""
    assert solution.all_checked_in is False


def test_missing_list():
    """missing_list == every scheduled name not in checked_in_names, in original order."""
    assert solution.missing_list == ["Cy", "Ella"]


def test_first_missing_has_long_shift_short_circuit():
    """One `and` expression: len(missing_list) > 0 guards indexing missing_list[0] safely."""
    assert solution.first_missing_has_long_shift is True


def test_coverage_status_ternary():
    """coverage_status == "full" if missing_list is empty else "short-staffed", as a ternary expression."""
    assert solution.coverage_status == "short-staffed"


def test_overtime_names_via_zip():
    """overtime_names built by walking zip(scheduled_names, shift_hours), not manual indexing."""
    assert solution.overtime_names == ["Cy"]
''',
    },
    {
        "name": "tier2_mid02",
        "title": "Inventory Restock Matcher",
        "summary": "while...else, a short-circuit guard, a ternary, zip() -- a different combination",
        "instructions": SCRIPT_INSTRUCTIONS,
        "readme": (
            "A stockroom inventory -- given, don't modify:\n\n"
            "```python\n"
            'item_names = ["bolts", "screws", "washers", "nuts"]\n'
            "stock_levels = [12, 0, 5, 3]\n"
            "reorder_threshold = 4\n"
            "```\n\n"
            "(`stock_levels[i]` is `item_names[i]`'s current stock.)\n\n"
            "Same Mid-tier toolbox as the previous exercise, a different "
            "combination -- write plain top-level code that computes:\n\n"
            "- `out_of_stock_index` -- a **`while...else`** loop: walk an "
            "index `i` from `0`, `break` the moment `stock_levels[i] == 0`; "
            "the loop's `else` clause (reached only if the `while` "
            "condition ran out without a `break`) sets `i = -1`. Assign "
            "`out_of_stock_index = i` after the loop.\n"
            "- `needs_urgent_reorder` -- **one short-circuit `and` "
            "expression**: `out_of_stock_index != -1 and "
            "item_names[out_of_stock_index] != \"\"`. The `!= -1` check "
            "must come first -- it's what makes indexing "
            "`item_names[out_of_stock_index]` safe.\n"
            "- `stock_status` -- a **ternary expression**: `\"critical\"` "
            "if `out_of_stock_index != -1` else `\"ok\"`.\n"
            "- `low_stock_items` -- a plain `for` loop using "
            "**`zip(item_names, stock_levels)`** to walk both lists "
            "together, collecting every name whose stock is strictly below "
            "`reorder_threshold`."
        ),
        "stub": '''\
item_names = ["bolts", "screws", "washers", "nuts"]
stock_levels = [12, 0, 5, 3]
reorder_threshold = 4

raise NotImplementedError  # delete this line once you've written the code below

# Write your code here: out_of_stock_index (while...else), needs_urgent_reorder
# (short-circuit and), stock_status (ternary), low_stock_items (for + zip()).
# See README.md.
''',
        "reference": '''\
item_names = ["bolts", "screws", "washers", "nuts"]
stock_levels = [12, 0, 5, 3]
reorder_threshold = 4

i = 0
while i < len(stock_levels):
    if stock_levels[i] == 0:
        break
    i += 1
else:
    i = -1
out_of_stock_index = i

needs_urgent_reorder = out_of_stock_index != -1 and item_names[out_of_stock_index] != ""

stock_status = "critical" if out_of_stock_index != -1 else "ok"

low_stock_items = []
for name, level in zip(item_names, stock_levels):
    if level < reorder_threshold:
        low_stock_items.append(name)
''',
        "test": '''\
import exercises.stage02.tier2_mid02.solution as solution


def test_out_of_stock_index_via_while_else():
    """out_of_stock_index is the first index where stock_levels[i] == 0 (while...else, break)."""
    assert solution.out_of_stock_index == 1


def test_needs_urgent_reorder_short_circuit():
    """One `and` expression: out_of_stock_index != -1 guards the item_names indexing on the right."""
    assert solution.needs_urgent_reorder is True


def test_stock_status_ternary():
    """stock_status == "critical" if out_of_stock_index != -1 else "ok", as a ternary expression."""
    assert solution.stock_status == "critical"


def test_low_stock_items_via_zip():
    """low_stock_items built by walking zip(item_names, stock_levels), not manual indexing."""
    assert solution.low_stock_items == ["screws", "nuts"]
''',
    },
    {
        "name": "tier3_advanced01",
        "title": "Custom Iterator: CountdownTimer",
        "summary": "a class implementing the iterator protocol (__iter__/__next__/StopIteration) by hand",
        "readme": (
            "Implement a class `CountdownTimer` that is its own iterator, "
            "counting down from `start` to `0` **inclusive**:\n\n"
            "- `__init__(self, start)` -- store `start` and a `current` "
            "counter beginning at `start`.\n"
            "- `__iter__(self)` -- an iterator is required to return "
            "itself from `__iter__`: `return self`.\n"
            "- `__next__(self)` -- if `current < 0`, `raise StopIteration` "
            "(the iterator is exhausted -- this must keep happening on "
            "every subsequent call, not just the first time past the "
            "end). Otherwise, save `current`'s value, decrement `current` "
            "by 1, and return the saved value.\n\n"
            "This is the exact protocol `for x in some_iterator:` relies "
            "on under the hood: it calls `__iter__` once, then `__next__` "
            "repeatedly until `StopIteration` is raised. `list(CountdownTimer(3))` "
            "should give `[3, 2, 1, 0]`."
        ),
        "stub": '''\
class CountdownTimer:
    """Counts down from `start` to 0 inclusive; is its own iterator."""

    def __init__(self, start):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    def __next__(self):
        raise NotImplementedError
''',
        "reference": '''\
class CountdownTimer:
    """Counts down from `start` to 0 inclusive; is its own iterator."""

    def __init__(self, start):
        self.start = start
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value
''',
        "test": '''\
import pytest

from exercises.stage02.tier3_advanced01.solution import CountdownTimer


def test_list_of_countdown_timer():
    """list(CountdownTimer(3)) walks __iter__ then __next__ repeatedly -- [3, 2, 1, 0]."""
    assert list(CountdownTimer(3)) == [3, 2, 1, 0]


def test_iter_returns_self():
    """__iter__ must return self -- CountdownTimer is its own iterator."""
    timer = CountdownTimer(2)
    assert iter(timer) is timer


def test_next_raises_stopiteration_when_exhausted():
    """__next__ must raise StopIteration once current < 0."""
    timer = CountdownTimer(0)
    assert next(timer) == 0
    with pytest.raises(StopIteration):
        next(timer)


def test_next_keeps_raising_after_exhaustion():
    """Calling __next__ again after StopIteration must raise StopIteration again, not resume or crash."""
    timer = CountdownTimer(0)
    next(timer)
    with pytest.raises(StopIteration):
        next(timer)
    with pytest.raises(StopIteration):
        next(timer)


def test_for_loop_consumes_it_correctly():
    """A real `for` loop must consume the whole sequence via the protocol, not just list()."""
    collected = []
    for value in CountdownTimer(2):
        collected.append(value)
    assert collected == [2, 1, 0]
''',
    },
    {
        "name": "tier3_advanced02",
        "title": "Round-Robin Task Scheduler",
        "summary": "itertools.chain + itertools.cycle + itertools.islice, combined",
        "instructions": SCRIPT_INSTRUCTIONS,
        "readme": (
            "Given, don't modify:\n\n"
            "```python\n"
            'workers = ["alpha", "beta", "gamma"]\n'
            'morning_tasks = ["t1", "t2", "t3"]\n'
            'afternoon_tasks = ["t4", "t5", "t6", "t7"]\n'
            "```\n\n"
            "Using `itertools`, write plain top-level code that computes:\n\n"
            "- `all_tasks` -- `morning_tasks` followed by `afternoon_tasks`, "
            "via `list(itertools.chain(morning_tasks, afternoon_tasks))` "
            "(not `morning_tasks + afternoon_tasks`).\n"
            "- `assignments` -- each task in `all_tasks` paired round-robin "
            "with a worker, via `list(zip(all_tasks, "
            "itertools.cycle(workers)))`. Because `itertools.cycle` repeats "
            "`workers` forever and `zip` stops at the shorter of its two "
            "inputs, this naturally stops once `all_tasks` runs out, cycling "
            "back through `workers` as many times as needed.\n"
            "- `first_three_assignments` -- just the first 3 pairs of "
            "`assignments`, via `list(itertools.islice(assignments, 3))` "
            "(not `assignments[:3]`).\n"
            "- `worker_task_counts` -- a `dict` mapping each worker to how "
            "many tasks they were assigned, built with a plain `for "
            "task, worker in assignments:` loop and "
            "`worker_task_counts[worker] = worker_task_counts.get(worker, 0) + 1`."
        ),
        "stub": '''\
import itertools

workers = ["alpha", "beta", "gamma"]
morning_tasks = ["t1", "t2", "t3"]
afternoon_tasks = ["t4", "t5", "t6", "t7"]

raise NotImplementedError  # delete this line once you've written the code below

# Write your code here: all_tasks (itertools.chain), assignments (zip +
# itertools.cycle), first_three_assignments (itertools.islice),
# worker_task_counts (plain for-loop + dict.get). See README.md.
''',
        "reference": '''\
import itertools

workers = ["alpha", "beta", "gamma"]
morning_tasks = ["t1", "t2", "t3"]
afternoon_tasks = ["t4", "t5", "t6", "t7"]

all_tasks = list(itertools.chain(morning_tasks, afternoon_tasks))
assignments = list(zip(all_tasks, itertools.cycle(workers)))
first_three_assignments = list(itertools.islice(assignments, 3))

worker_task_counts = {}
for task, worker in assignments:
    worker_task_counts[worker] = worker_task_counts.get(worker, 0) + 1
''',
        "test": '''\
import exercises.stage02.tier3_advanced02.solution as solution


def test_all_tasks_via_chain():
    """all_tasks == morning_tasks followed by afternoon_tasks, via itertools.chain."""
    assert solution.all_tasks == ["t1", "t2", "t3", "t4", "t5", "t6", "t7"]


def test_assignments_round_robin_via_cycle():
    """assignments pairs each task with a worker, cycling through workers via itertools.cycle."""
    assert solution.assignments == [
        ("t1", "alpha"), ("t2", "beta"), ("t3", "gamma"),
        ("t4", "alpha"), ("t5", "beta"), ("t6", "gamma"), ("t7", "alpha"),
    ]


def test_first_three_assignments_via_islice():
    """first_three_assignments == the first 3 of assignments, via itertools.islice."""
    assert solution.first_three_assignments == [("t1", "alpha"), ("t2", "beta"), ("t3", "gamma")]


def test_worker_task_counts():
    """worker_task_counts tallies assignments per worker via dict.get(..., 0) + 1."""
    assert solution.worker_task_counts == {"alpha": 3, "beta": 2, "gamma": 2}
''',
    },
]
