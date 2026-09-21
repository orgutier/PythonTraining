"""
Week 2 -- Control Flow.

Coverage plan (each item exercised by the trainee's own code >=3 times):
  keywords: if, elif, else, while, for, in, range(), break, continue, pass
  modules:  itertools
  methods:  zip(), enumerate()
  concepts: short-circuit evaluation, truthiness, ternary expression,
            for...else / while...else
"""

WEEK = "week02"
TOPIC = "Control Flow"
OVERVIEW = (
    "Seven exercises covering every conditional and loop construct from "
    "Topic 2 at least three times each, including the two idioms trainees "
    "usually only see once: for...else/while...else, and the and/or "
    "short-circuit guard pattern."
)

EXERCISES = [
    {
        "name": "exercise01",
        "title": "Number Patterns",
        "summary": "if/elif/else, for, range(), a first for...else",
        "readme": (
            "Implement:\n\n"
            "- `fizzbuzz(n: int) -> list[str]` -- the classic: for `1..n`, "
            "`\"FizzBuzz\"` if divisible by 15, `\"Fizz\"` by 3, `\"Buzz\"` by 5, "
            "else `str(i)`.\n"
            "- `is_prime(n: int) -> bool` -- implement with a `for...else`: loop "
            "`i` over `range(2, int(n ** 0.5) + 1)`, `break` the moment you find a "
            "factor; the loop's `else` clause (which only runs if the loop finished "
            "*without* breaking) is where you return `True`. This is the cleanest "
            "way to express \"found something -> stop early\" vs. \"searched "
            "everything, found nothing\" without a separate flag variable.\n\n"
            "See the Study Reference presentation, Topic 2, for the theory."
        ),
        "stub": '''\
def fizzbuzz(n: int) -> list[str]:
    """Return ["1", "2", "Fizz", "4", "Buzz", ...] for 1..n."""
    raise NotImplementedError


def is_prime(n: int) -> bool:
    """Return True if n is prime. Implement with for...else (see README)."""
    raise NotImplementedError
''',
        "reference": '''\
def fizzbuzz(n: int) -> list[str]:
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            break
    else:
        return True
    return False
''',
        "test": '''\
from exercises.week02.exercise01.solution import fizzbuzz, is_prime


def test_fizzbuzz():
    assert fizzbuzz(15) == [
        "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
        "11", "Fizz", "13", "14", "FizzBuzz",
    ]


def test_is_prime_true_cases():
    assert is_prime(2) is True
    assert is_prime(17) is True


def test_is_prime_false_cases():
    assert is_prime(1) is False
    assert is_prime(18) is False
''',
    },
    {
        "name": "exercise02",
        "title": "Loop Controls",
        "summary": "break, continue, while, pass",
        "readme": (
            "Implement:\n\n"
            "- `sum_until_negative(numbers: list[int]) -> int` -- sum numbers with "
            "a `for` loop, `break`-ing the instant you hit a negative one (don't "
            "include it in the sum).\n"
            "- `skip_multiples(numbers: list[int], factor: int) -> list[int]` -- "
            "`for` over numbers, `continue`-ing past (skipping) any multiple of "
            "`factor`, collecting the rest.\n"
            "- `countdown(n: int) -> list[int]` -- `[n, n-1, ..., 1]` built with a "
            "`while` loop (not `range`).\n"
            "- `safe_int_list(values: list) -> list[int]` -- try `int(v)` for each "
            "`v`; on `ValueError`/`TypeError`, silently skip it with "
            "`except (...): pass` and move on. This is the standard, idiomatic use "
            "of `pass`: an intentionally empty except block.\n\n"
            "See the Study Reference presentation, Topic 2, for the theory."
        ),
        "stub": '''\
def sum_until_negative(numbers: list[int]) -> int:
    """Sum numbers, stopping (break) at the first negative one."""
    raise NotImplementedError


def skip_multiples(numbers: list[int], factor: int) -> list[int]:
    """Return numbers with any multiple of factor skipped (continue)."""
    raise NotImplementedError


def countdown(n: int) -> list[int]:
    """[n, n-1, ..., 1] built with a while loop."""
    raise NotImplementedError


def safe_int_list(values: list) -> list[int]:
    """int(v) for each value, silently skipping ones that fail (except: pass)."""
    raise NotImplementedError
''',
        "reference": '''\
def sum_until_negative(numbers: list[int]) -> int:
    total = 0
    for n in numbers:
        if n < 0:
            break
        total += n
    return total


def skip_multiples(numbers: list[int], factor: int) -> list[int]:
    result = []
    for n in numbers:
        if n % factor == 0:
            continue
        result.append(n)
    return result


def countdown(n: int) -> list[int]:
    result = []
    while n >= 1:
        result.append(n)
        n -= 1
    return result


def safe_int_list(values: list) -> list[int]:
    result = []
    for v in values:
        try:
            result.append(int(v))
        except (ValueError, TypeError):
            pass
    return result
''',
        "test": '''\
from exercises.week02.exercise02.solution import (
    sum_until_negative,
    skip_multiples,
    countdown,
    safe_int_list,
)


def test_sum_until_negative():
    assert sum_until_negative([1, 2, 3, -1, 10]) == 6


def test_sum_until_negative_no_negatives():
    assert sum_until_negative([1, 2, 3]) == 6


def test_skip_multiples():
    assert skip_multiples([1, 2, 3, 4, 5, 6], 3) == [1, 2, 4, 5]


def test_countdown():
    assert countdown(5) == [5, 4, 3, 2, 1]


def test_safe_int_list():
    assert safe_int_list(["1", "2", "oops", "3", None]) == [1, 2, 3]
''',
    },
    {
        "name": "exercise03",
        "title": "Pairing and Indexing",
        "summary": "zip() x3, enumerate() x2",
        "readme": (
            "Implement:\n\n"
            "- `pair_names_scores(names: list[str], scores: list[int]) -> list[tuple]` "
            "-- `list(zip(names, scores))`.\n"
            "- `merge_records(keys: list[str], values: list) -> dict` -- "
            "`dict(zip(keys, values))`.\n"
            "- `count_equal_pairs(list1: list, list2: list) -> int` -- count "
            "positions where `list1[i] == list2[i]`, using `zip(list1, list2)` "
            "to walk both lists together (don't index manually).\n"
            "- `indexed_items(items: list[str]) -> list[str]` -- `[f\"{i}: {item}\" "
            "for i, item in enumerate(items)]`.\n"
            "- `labeled_from(items: list[str], start: int) -> dict` -- "
            "`{i: item for i, item in enumerate(items, start)}` (note the second "
            "argument to `enumerate` sets the starting index).\n\n"
            "See the Study Reference presentation, Topic 2, for the theory."
        ),
        "stub": '''\
def pair_names_scores(names: list[str], scores: list[int]) -> list[tuple]:
    """list(zip(names, scores))."""
    raise NotImplementedError


def merge_records(keys: list[str], values: list) -> dict:
    """dict(zip(keys, values))."""
    raise NotImplementedError


def count_equal_pairs(list1: list, list2: list) -> int:
    """Count positions i where list1[i] == list2[i], walking both with zip()."""
    raise NotImplementedError


def indexed_items(items: list[str]) -> list[str]:
    """[f"{i}: {item}" for i, item in enumerate(items)]."""
    raise NotImplementedError


def labeled_from(items: list[str], start: int) -> dict:
    """{i: item for i, item in enumerate(items, start)}."""
    raise NotImplementedError
''',
        "reference": '''\
def pair_names_scores(names: list[str], scores: list[int]) -> list[tuple]:
    return list(zip(names, scores))


def merge_records(keys: list[str], values: list) -> dict:
    return dict(zip(keys, values))


def count_equal_pairs(list1: list, list2: list) -> int:
    return sum(1 for a, b in zip(list1, list2) if a == b)


def indexed_items(items: list[str]) -> list[str]:
    return [f"{i}: {item}" for i, item in enumerate(items)]


def labeled_from(items: list[str], start: int) -> dict:
    return {i: item for i, item in enumerate(items, start)}
''',
        "test": '''\
from exercises.week02.exercise03.solution import (
    pair_names_scores,
    merge_records,
    count_equal_pairs,
    indexed_items,
    labeled_from,
)


def test_pair_names_scores():
    assert pair_names_scores(["a", "b"], [1, 2]) == [("a", 1), ("b", 2)]


def test_merge_records():
    assert merge_records(["x", "y"], [1, 2]) == {"x": 1, "y": 2}


def test_count_equal_pairs():
    assert count_equal_pairs([1, 2, 3], [1, 0, 3]) == 2


def test_indexed_items():
    assert indexed_items(["a", "b"]) == ["0: a", "1: b"]


def test_labeled_from():
    assert labeled_from(["a", "b"], 10) == {10: "a", 11: "b"}
''',
    },
    {
        "name": "exercise04",
        "title": "Ranges and Itertools",
        "summary": "range() with step, itertools.cycle/islice/chain/product",
        "readme": (
            "Implement:\n\n"
            "- `stepped_range(start: int, stop: int, step: int) -> list[int]` -- "
            "`list(range(start, stop, step))`.\n"
            "- `numbered_multiples(n: int, factor: int) -> list[str]` -- build the "
            "multiples of `factor` up to `n` with `range(factor, n + 1, factor)`, "
            "then label each with its position via `enumerate(...)`, returning "
            "`[f\"{i}: {v}\" for i, v in enumerate(multiples)]`.\n"
            "- `cycle_colors(colors: list[str], count: int) -> list[str]` -- the "
            "first `count` items of `colors` repeated forever, via "
            "`itertools.islice(itertools.cycle(colors), count)`.\n"
            "- `chain_lists(list1: list, list2: list) -> list` -- "
            "`list(itertools.chain(list1, list2))`.\n"
            "- `all_pairs(list1: list, list2: list) -> list[tuple]` -- every "
            "`(a, b)` combination, via `list(itertools.product(list1, list2))`.\n\n"
            "See the Study Reference presentation, Topic 2, for the theory."
        ),
        "stub": '''\
def stepped_range(start: int, stop: int, step: int) -> list[int]:
    """list(range(start, stop, step))."""
    raise NotImplementedError


def numbered_multiples(n: int, factor: int) -> list[str]:
    """Multiples of factor up to n, each labeled "i: value" via enumerate()."""
    raise NotImplementedError


def cycle_colors(colors: list[str], count: int) -> list[str]:
    """First `count` items of colors repeated forever (itertools.cycle + islice)."""
    raise NotImplementedError


def chain_lists(list1: list, list2: list) -> list:
    """list1 followed by list2, via itertools.chain (not list1 + list2)."""
    raise NotImplementedError


def all_pairs(list1: list, list2: list) -> list[tuple]:
    """Every (a, b) combination, via itertools.product."""
    raise NotImplementedError
''',
        "reference": '''\
import itertools


def stepped_range(start: int, stop: int, step: int) -> list[int]:
    return list(range(start, stop, step))


def numbered_multiples(n: int, factor: int) -> list[str]:
    multiples = list(range(factor, n + 1, factor))
    return [f"{i}: {v}" for i, v in enumerate(multiples)]


def cycle_colors(colors: list[str], count: int) -> list[str]:
    return list(itertools.islice(itertools.cycle(colors), count))


def chain_lists(list1: list, list2: list) -> list:
    return list(itertools.chain(list1, list2))


def all_pairs(list1: list, list2: list) -> list[tuple]:
    return list(itertools.product(list1, list2))
''',
        "test": '''\
from exercises.week02.exercise04.solution import (
    stepped_range,
    numbered_multiples,
    cycle_colors,
    chain_lists,
    all_pairs,
)


def test_stepped_range():
    assert stepped_range(0, 10, 2) == [0, 2, 4, 6, 8]


def test_numbered_multiples():
    assert numbered_multiples(12, 3) == ["0: 3", "1: 6", "2: 9", "3: 12"]


def test_cycle_colors():
    assert cycle_colors(["red", "green"], 5) == ["red", "green", "red", "green", "red"]


def test_chain_lists():
    assert chain_lists([1, 2], [3, 4]) == [1, 2, 3, 4]


def test_all_pairs():
    assert all_pairs([1, 2], ["a", "b"]) == [(1, "a"), (1, "b"), (2, "a"), (2, "b")]
''',
    },
    {
        "name": "exercise05",
        "title": "Short-Circuit Guards and Truthiness",
        "summary": "and-short-circuit x3, truthiness x3",
        "readme": (
            "Implement:\n\n"
            "- `is_valid_username(name) -> bool` -- `True` only if `name` is a "
            "non-empty `str` of length <= 20. Use one chained `and` expression: "
            "`isinstance(name, str) and len(name) > 0 and len(name) <= 20`. Because "
            "`and` short-circuits, `len(name)` never runs if `name` isn't a `str` "
            "in the first place -- that's the point, not just a style choice.\n"
            "- `has_valid_first_item(items: list) -> bool` -- `True` only if "
            "`items` is non-empty **and** its first item is truthy: "
            "`bool(items) and bool(items[0])`. The short-circuit here protects "
            "`items[0]` from ever running on an empty list.\n"
            "- `is_within_bounds(numbers: list[int], index: int) -> bool` -- "
            "`True` only if `0 <= index < len(numbers)` **and** "
            "`numbers[index] >= 0`. Same guard pattern: the bounds check must pass "
            "before `numbers[index]` is safe to evaluate.\n"
            "- `describe_truthiness(value) -> str` -- `\"truthy\"` if `value` "
            "(bare truthiness check, no `==`), else `\"falsy\"`.\n"
            "- `filter_truthy(values: list) -> list` -- `[v for v in values if v]`.\n"
            "- `count_falsy(values: list) -> int` -- `sum(1 for v in values if not v)`.\n\n"
            "See the Study Reference presentation, Topic 2, for the theory."
        ),
        "stub": '''\
def is_valid_username(name) -> bool:
    """Non-empty str, len <= 20 -- one chained `and` expression."""
    raise NotImplementedError


def has_valid_first_item(items: list) -> bool:
    """items is non-empty AND items[0] is truthy -- `and` guards items[0]."""
    raise NotImplementedError


def is_within_bounds(numbers: list[int], index: int) -> bool:
    """0 <= index < len(numbers) AND numbers[index] >= 0."""
    raise NotImplementedError


def describe_truthiness(value) -> str:
    """"truthy" or "falsy" based on bare truthiness of value."""
    raise NotImplementedError


def filter_truthy(values: list) -> list:
    """Only the truthy values, order preserved."""
    raise NotImplementedError


def count_falsy(values: list) -> int:
    """How many values are falsy."""
    raise NotImplementedError
''',
        "reference": '''\
def is_valid_username(name) -> bool:
    return isinstance(name, str) and len(name) > 0 and len(name) <= 20


def has_valid_first_item(items: list) -> bool:
    return bool(items) and bool(items[0])


def is_within_bounds(numbers: list[int], index: int) -> bool:
    return 0 <= index < len(numbers) and numbers[index] >= 0


def describe_truthiness(value) -> str:
    return "truthy" if value else "falsy"


def filter_truthy(values: list) -> list:
    return [v for v in values if v]


def count_falsy(values: list) -> int:
    return sum(1 for v in values if not v)
''',
        "test": '''\
from exercises.week02.exercise05.solution import (
    is_valid_username,
    has_valid_first_item,
    is_within_bounds,
    describe_truthiness,
    filter_truthy,
    count_falsy,
)


def test_is_valid_username_true():
    assert is_valid_username("ada") is True


def test_is_valid_username_rejects_non_str():
    assert is_valid_username(123) is False


def test_is_valid_username_rejects_empty():
    assert is_valid_username("") is False


def test_has_valid_first_item_empty_list_is_safe():
    assert has_valid_first_item([]) is False


def test_has_valid_first_item_truthy_first():
    assert has_valid_first_item([1, 2]) is True


def test_is_within_bounds_out_of_range_is_safe():
    assert is_within_bounds([1, 2, 3], 10) is False


def test_is_within_bounds_true():
    assert is_within_bounds([1, 2, 3], 1) is True


def test_describe_truthiness():
    assert describe_truthiness(0) == "falsy"
    assert describe_truthiness("hi") == "truthy"
    assert describe_truthiness([]) == "falsy"


def test_filter_truthy():
    assert filter_truthy([0, 1, "", "a", None, 2]) == [1, "a", 2]


def test_count_falsy():
    assert count_falsy([0, 1, "", "a", None, 2]) == 3
''',
    },
    {
        "name": "exercise06",
        "title": "Ternary Expressions",
        "summary": "conditional expressions x3",
        "readme": (
            "Implement three functions, each a single-line ternary "
            "(`X if COND else Y`) -- no `if` statements:\n\n"
            "- `grade_label(score: int) -> str` -- `\"pass\"` if `score >= 60`, "
            "else `\"fail\"`.\n"
            "- `abs_value(n: int) -> int` -- `n` if `n >= 0`, else `-n`.\n"
            "- `clamp_to_range(n: int, lo: int, hi: int) -> int` -- `n` clamped "
            "into `[lo, hi]`. Chain two ternaries: "
            "`lo if n < lo else hi if n > hi else n`.\n\n"
            "See the Study Reference presentation, Topic 2, for the theory."
        ),
        "stub": '''\
def grade_label(score: int) -> str:
    """"pass" if score >= 60 else "fail" -- as a ternary expression."""
    raise NotImplementedError


def abs_value(n: int) -> int:
    """n if n >= 0 else -n -- as a ternary expression."""
    raise NotImplementedError


def clamp_to_range(n: int, lo: int, hi: int) -> int:
    """n clamped into [lo, hi] -- as a chained ternary expression."""
    raise NotImplementedError
''',
        "reference": '''\
def grade_label(score: int) -> str:
    return "pass" if score >= 60 else "fail"


def abs_value(n: int) -> int:
    return n if n >= 0 else -n


def clamp_to_range(n: int, lo: int, hi: int) -> int:
    return lo if n < lo else hi if n > hi else n
''',
        "test": '''\
from exercises.week02.exercise06.solution import grade_label, abs_value, clamp_to_range


def test_grade_label():
    assert grade_label(75) == "pass"
    assert grade_label(50) == "fail"


def test_abs_value():
    assert abs_value(5) == 5
    assert abs_value(-5) == 5
    assert abs_value(0) == 0


def test_clamp_to_range():
    assert clamp_to_range(15, 0, 10) == 10
    assert clamp_to_range(-5, 0, 10) == 0
    assert clamp_to_range(5, 0, 10) == 5
''',
    },
    {
        "name": "exercise07",
        "title": "The else Clause on Loops",
        "summary": "for...else x2 more, while...else x3",
        "readme": (
            "`for` and `while` loops can both carry an `else` clause that runs "
            "only if the loop finished *without* hitting a `break`. Implement:\n\n"
            "- `contains_value(items: list, target) -> bool` -- `for...else`: "
            "`break` when `item == target` is found; the `else` clause returns "
            "`False`.\n"
            "- `all_positive(numbers: list[int]) -> bool` -- `for...else`: "
            "`break` the moment a non-positive number is found; the `else` clause "
            "returns `True` (every number was positive).\n"
            "- `find_first_negative_index(numbers: list[int]) -> int` -- "
            "`while...else`: walk an index `i` with a `while` loop, `break` when "
            "`numbers[i] < 0`; the `else` clause (loop ran out without breaking) "
            "returns `-1`.\n"
            "- `retry_until_success(attempts: list[bool]) -> bool` -- "
            "`while...else`: walk `attempts` with a `while` loop, `break` on the "
            "first `True`; the `else` clause returns `False` (never succeeded).\n"
            "- `first_positive_index(numbers: list[int]) -> int` -- `while...else`: "
            "same shape as `find_first_negative_index`, but for the first "
            "positive number; `else` returns `-1`.\n\n"
            "See the Study Reference presentation, Topic 2, for the theory."
        ),
        "stub": '''\
def contains_value(items: list, target) -> bool:
    """for...else: True if target is found in items."""
    raise NotImplementedError


def all_positive(numbers: list[int]) -> bool:
    """for...else: True if every number in numbers is > 0."""
    raise NotImplementedError


def find_first_negative_index(numbers: list[int]) -> int:
    """while...else: index of the first negative number, or -1."""
    raise NotImplementedError


def retry_until_success(attempts: list[bool]) -> bool:
    """while...else: True if any attempt is True, else False."""
    raise NotImplementedError


def first_positive_index(numbers: list[int]) -> int:
    """while...else: index of the first positive number, or -1."""
    raise NotImplementedError
''',
        "reference": '''\
def contains_value(items: list, target) -> bool:
    for item in items:
        if item == target:
            break
    else:
        return False
    return True


def all_positive(numbers: list[int]) -> bool:
    for n in numbers:
        if n <= 0:
            break
    else:
        return True
    return False


def find_first_negative_index(numbers: list[int]) -> int:
    i = 0
    while i < len(numbers):
        if numbers[i] < 0:
            break
        i += 1
    else:
        return -1
    return i


def retry_until_success(attempts: list[bool]) -> bool:
    i = 0
    while i < len(attempts):
        if attempts[i]:
            break
        i += 1
    else:
        return False
    return True


def first_positive_index(numbers: list[int]) -> int:
    i = 0
    while i < len(numbers):
        if numbers[i] > 0:
            break
        i += 1
    else:
        return -1
    return i
''',
        "test": '''\
from exercises.week02.exercise07.solution import (
    contains_value,
    all_positive,
    find_first_negative_index,
    retry_until_success,
    first_positive_index,
)


def test_contains_value_found():
    assert contains_value([1, 2, 3], 2) is True


def test_contains_value_not_found():
    assert contains_value([1, 2, 3], 9) is False


def test_all_positive_true():
    assert all_positive([1, 2, 3]) is True


def test_all_positive_false():
    assert all_positive([1, -2, 3]) is False


def test_find_first_negative_index_found():
    assert find_first_negative_index([1, 2, -3, 4]) == 2


def test_find_first_negative_index_none():
    assert find_first_negative_index([1, 2, 3]) == -1


def test_retry_until_success_true():
    assert retry_until_success([False, False, True]) is True


def test_retry_until_success_false():
    assert retry_until_success([False, False]) is False


def test_first_positive_index_found():
    assert first_positive_index([-1, -2, 3, 4]) == 2


def test_first_positive_index_none():
    assert first_positive_index([-1, -2]) == -1
''',
    },
]
