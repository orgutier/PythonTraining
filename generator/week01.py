"""
Week 1 -- Python Fundamentals.

Coverage plan (every item below is exercised by the trainee's own code in
at least 3 separate places across these 6 exercises -- not just mentioned
in a docstring):

  keywords/builtins: int, float, str, bool, None, True, False, print(),
                      input(), type(), isinstance(), and, or, not, is, in,
                      annotated assignment (`x: int = 5`)
  concepts:           type hints, mutability vs immutability,
                      identity vs equality
"""

WEEK = "week01"
TOPIC = "Python Fundamentals"
OVERVIEW = (
    "Six small exercises, each in its own folder. Together they touch every "
    "keyword, builtin, and concept from Topic 1 of the presentation at least "
    "three times, so nothing here is a one-shot demo -- you'll see `isinstance()`, "
    "`is`, `type()`, and the rest again and again in slightly different shapes."
)

EXERCISES = [
    {
        "name": "exercise01",
        "title": "Profile Basics",
        "summary": "variables, type-hinted parameters, type(), print()",
        "readme": (
            "Implement three small functions:\n\n"
            "- `build_profile(name: str, age: int, height_m: float, is_student: bool) -> dict` "
            "-- return a dict with keys `name`, `age`, `height_m`, `is_student` holding "
            "those four values unchanged.\n"
            "- `value_kind(x) -> str` -- return `type(x).__name__` (e.g. `\"int\"`, "
            "`\"str\"`). This is your first use of `type()`; Exercise 3 goes deeper.\n"
            "- `display_profile(profile: dict) -> None` -- `print()` a single line in "
            "the exact form `\"NAME is AGE years old, HEIGHT_Mm tall, student=IS_STUDENT\"` "
            "(e.g. `\"Ada is 30 years old, 1.7m tall, student=False\"`). Nothing to return.\n\n"
            "All four parameters above use annotated types (`name: str`, `age: int`, ...) "
            "-- keep doing that in every function you write this week; it's not optional "
            "decoration, `isinstance()` checks later in the week assume callers respect it.\n\n"
            "See the Study Reference presentation, Topic 1, for the theory."
        ),
        "stub": '''\
def build_profile(name: str, age: int, height_m: float, is_student: bool) -> dict:
    """Return {"name": name, "age": age, "height_m": height_m, "is_student": is_student}."""
    raise NotImplementedError


def value_kind(x) -> str:
    """Return the name of x's type, e.g. value_kind(5) == "int"."""
    raise NotImplementedError


def display_profile(profile: dict) -> None:
    """Print "NAME is AGE years old, HEIGHT_Mm tall, student=IS_STUDENT"."""
    raise NotImplementedError
''',
        "reference": '''\
def build_profile(name: str, age: int, height_m: float, is_student: bool) -> dict:
    return {"name": name, "age": age, "height_m": height_m, "is_student": is_student}


def value_kind(x) -> str:
    return type(x).__name__


def display_profile(profile: dict) -> None:
    print(
        f"{profile['name']} is {profile['age']} years old, "
        f"{profile['height_m']}m tall, student={profile['is_student']}"
    )
''',
        "test": '''\
from exercises.week01.exercise01.solution import (
    build_profile,
    value_kind,
    display_profile,
)


def test_build_profile():
    profile = build_profile("Ada", 30, 1.7, False)
    assert profile == {"name": "Ada", "age": 30, "height_m": 1.7, "is_student": False}


def test_value_kind_int():
    assert value_kind(5) == "int"


def test_value_kind_str():
    assert value_kind("hi") == "str"


def test_value_kind_float():
    assert value_kind(3.14) == "float"


def test_display_profile(capsys):
    display_profile({"name": "Ada", "age": 30, "height_m": 1.7, "is_student": False})
    out = capsys.readouterr().out
    assert out == "Ada is 30 years old, 1.7m tall, student=False\\n"
''',
    },
    {
        "name": "exercise02",
        "title": "Temperature and BMI",
        "summary": "float arithmetic, isinstance() with a bool-exclusion twist",
        "readme": (
            "Implement:\n\n"
            "- `celsius_to_fahrenheit(celsius: float) -> float` -- the standard "
            "conversion `celsius * 9 / 5 + 32`.\n"
            "- `bmi_calculator(weight_kg: float, height_m: float) -> float` -- "
            "`weight_kg / height_m ** 2`, rounded to 2 decimals.\n"
            "- `validate_measurement(value) -> bool` -- return `True` only if `value` "
            "is an `int` or `float` **and not** a `bool`. This matters because in "
            "Python `bool` is a subclass of `int`, so `isinstance(True, int)` is "
            "`True` -- a naive `isinstance(value, (int, float))` check would wrongly "
            "accept `True`/`False` as measurements. You have to check `isinstance()` "
            "twice and combine the two with `and`/`not`.\n\n"
            "See the Study Reference presentation, Topic 1, for the theory."
        ),
        "stub": '''\
def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a Celsius temperature to Fahrenheit."""
    raise NotImplementedError


def bmi_calculator(weight_kg: float, height_m: float) -> float:
    """Return BMI = weight_kg / height_m ** 2, rounded to 2 decimals."""
    raise NotImplementedError


def validate_measurement(value) -> bool:
    """True if value is an int or float, but explicitly NOT a bool."""
    raise NotImplementedError
''',
        "reference": '''\
def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32


def bmi_calculator(weight_kg: float, height_m: float) -> float:
    return round(weight_kg / height_m ** 2, 2)


def validate_measurement(value) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)
''',
        "test": '''\
from exercises.week01.exercise02.solution import (
    celsius_to_fahrenheit,
    bmi_calculator,
    validate_measurement,
)


def test_celsius_to_fahrenheit_freezing():
    assert celsius_to_fahrenheit(0) == 32.0


def test_celsius_to_fahrenheit_boiling():
    assert celsius_to_fahrenheit(100) == 212.0


def test_bmi_calculator():
    assert abs(bmi_calculator(70, 1.75) - 22.86) < 0.01


def test_validate_measurement_accepts_int_and_float():
    assert validate_measurement(70) is True
    assert validate_measurement(1.75) is True


def test_validate_measurement_rejects_bool():
    assert validate_measurement(True) is False
    assert validate_measurement(False) is False


def test_validate_measurement_rejects_str():
    assert validate_measurement("70") is False
''',
    },
    {
        "name": "exercise03",
        "title": "Type Inspector",
        "summary": "type() vs isinstance(), None, bool-before-int classification, print()",
        "readme": (
            "Implement:\n\n"
            "- `describe_value(value) -> str` -- if `value is None`, return the exact "
            "string `\"None (the absence of a value)\"`. Otherwise return "
            "`f\"{value!r} is a {type(value).__name__}\"` (use `type()`, not "
            "`isinstance()`, here).\n"
            "- `print_type_report(value) -> None` -- `print()` the result of "
            "`describe_value(value)`. Nothing to return.\n"
            "- `classify_values(values: list) -> dict` -- return a dict with keys "
            "`\"ints\"`, `\"floats\"`, `\"strs\"`, `\"bools\"`, `\"nones\"`, each mapped "
            "to a list of the matching items from `values`, preserving order. **`bool` "
            "must be checked before `int`**: since `True`/`False` are technically ints, "
            "checking `isinstance(v, int)` first would put them in the wrong bucket. "
            "Use `type(v) is bool` (not `isinstance`) to catch booleans precisely, "
            "then `isinstance(v, int)` / `isinstance(v, float)` / `isinstance(v, str)` "
            "for the rest, and `v is None` for the last bucket.\n\n"
            "See the Study Reference presentation, Topic 1, for the theory."
        ),
        "stub": '''\
def describe_value(value) -> str:
    """"None (the absence of a value)" for None, else f"{value!r} is a {type(value).__name__}"."""
    raise NotImplementedError


def print_type_report(value) -> None:
    """print(describe_value(value))."""
    raise NotImplementedError


def classify_values(values: list) -> dict:
    """Bucket values into {"ints": [...], "floats": [...], "strs": [...], "bools": [...], "nones": [...]}."""
    raise NotImplementedError
''',
        "reference": '''\
def describe_value(value) -> str:
    if value is None:
        return "None (the absence of a value)"
    return f"{value!r} is a {type(value).__name__}"


def print_type_report(value) -> None:
    print(describe_value(value))


def classify_values(values: list) -> dict:
    buckets = {"ints": [], "floats": [], "strs": [], "bools": [], "nones": []}
    for v in values:
        if v is None:
            buckets["nones"].append(v)
        elif type(v) is bool:
            buckets["bools"].append(v)
        elif isinstance(v, int):
            buckets["ints"].append(v)
        elif isinstance(v, float):
            buckets["floats"].append(v)
        elif isinstance(v, str):
            buckets["strs"].append(v)
    return buckets
''',
        "test": '''\
from exercises.week01.exercise03.solution import (
    describe_value,
    print_type_report,
    classify_values,
)


def test_describe_value_none():
    assert describe_value(None) == "None (the absence of a value)"


def test_describe_value_int():
    assert describe_value(5) == "5 is a int"


def test_describe_value_str():
    assert describe_value("hi") == "'hi' is a str"


def test_print_type_report(capsys):
    print_type_report(5)
    assert capsys.readouterr().out == "5 is a int\\n"


def test_classify_values_separates_bool_from_int():
    result = classify_values([1, 2, True, False, 3.5, "x", None])
    assert result["ints"] == [1, 2]
    assert result["bools"] == [True, False]
    assert result["floats"] == [3.5]
    assert result["strs"] == ["x"]
    assert result["nones"] == [None]
''',
    },
    {
        "name": "exercise04",
        "title": "Boolean Logic",
        "summary": "and, or, not, in, is/is not, explicit True/False",
        "readme": (
            "Implement four small boolean/string functions:\n\n"
            "- `can_enter_venue(age, has_ticket: bool, is_vip: bool) -> bool` -- `True` "
            "only if `age` is known (`age is not None`) **and** `age >= 18`, **and** "
            "(`has_ticket` **or** `is_vip`).\n"
            "- `access_level(has_ticket: bool, is_vip: bool, is_staff: bool) -> str` -- "
            "return `\"backstage\"` if `is_staff` **or** `is_vip`; else `\"general\"` if "
            "`has_ticket`; else `\"denied\"`.\n"
            "- `is_valid_choice(choice, allowed: list[str]) -> bool` -- `True` only if "
            "`choice` is a `str` (`isinstance`) **and** `choice` is **in** `allowed` "
            "**and not** an empty string.\n"
            "- `toggle_flag(flag: bool) -> bool` -- **must** use the literal keywords "
            "`True`/`False` (via an `if flag is True: ... else: ...`), not the `not` "
            "operator, even though `not flag` would be shorter. The point here is "
            "practicing the `True`/`False` literals directly, and `is True` as the "
            "idiomatic way to compare against the singleton.\n\n"
            "See the Study Reference presentation, Topic 1, for the theory."
        ),
        "stub": '''\
def can_enter_venue(age, has_ticket: bool, is_vip: bool) -> bool:
    """True if age is known and >= 18, and (has_ticket or is_vip)."""
    raise NotImplementedError


def access_level(has_ticket: bool, is_vip: bool, is_staff: bool) -> str:
    """"backstage" if staff/vip, else "general" if has_ticket, else "denied"."""
    raise NotImplementedError


def is_valid_choice(choice, allowed: list[str]) -> bool:
    """True if choice is a non-empty str that appears in allowed."""
    raise NotImplementedError


def toggle_flag(flag: bool) -> bool:
    """Opposite of flag -- implement with `if flag is True: ... else: ...`, not `not`."""
    raise NotImplementedError
''',
        "reference": '''\
def can_enter_venue(age, has_ticket: bool, is_vip: bool) -> bool:
    return (age is not None and age >= 18) and (has_ticket or is_vip)


def access_level(has_ticket: bool, is_vip: bool, is_staff: bool) -> str:
    if is_staff or is_vip:
        return "backstage"
    if has_ticket:
        return "general"
    return "denied"


def is_valid_choice(choice, allowed: list[str]) -> bool:
    return isinstance(choice, str) and choice in allowed and not choice == ""


def toggle_flag(flag: bool) -> bool:
    if flag is True:
        return False
    return True
''',
        "test": '''\
from exercises.week01.exercise04.solution import (
    can_enter_venue,
    access_level,
    is_valid_choice,
    toggle_flag,
)


def test_can_enter_venue_adult_with_ticket():
    assert can_enter_venue(20, True, False) is True


def test_can_enter_venue_minor_rejected():
    assert can_enter_venue(15, True, True) is False


def test_can_enter_venue_unknown_age_rejected():
    assert can_enter_venue(None, True, True) is False


def test_can_enter_venue_vip_without_ticket():
    assert can_enter_venue(25, False, True) is True


def test_access_level_backstage_for_staff():
    assert access_level(False, False, True) == "backstage"


def test_access_level_general_for_ticket_only():
    assert access_level(True, False, False) == "general"


def test_access_level_denied():
    assert access_level(False, False, False) == "denied"


def test_is_valid_choice_true():
    assert is_valid_choice("red", ["red", "blue"]) is True


def test_is_valid_choice_not_in_list():
    assert is_valid_choice("green", ["red", "blue"]) is False


def test_is_valid_choice_empty_string():
    assert is_valid_choice("", ["", "blue"]) is False


def test_is_valid_choice_non_string():
    assert is_valid_choice(5, ["red", "blue"]) is False


def test_toggle_flag():
    assert toggle_flag(True) is False
    assert toggle_flag(False) is True
''',
    },
    {
        "name": "exercise05",
        "title": "CLI Interaction",
        "summary": "input(), print(), composing small functions",
        "readme": (
            "Implement five functions that model a tiny command-line interaction "
            "(these are exactly the building blocks `tools/cli.py` itself is built "
            "from -- see the Appendix topic in the presentation for more):\n\n"
            "- `ask_name() -> str` -- `return input(\"What is your name? \")`.\n"
            "- `ask_age() -> int` -- `return int(input(\"How old are you? \"))`.\n"
            "- `ask_yes_no(prompt: str) -> bool` -- read `input(prompt)`, "
            "`.strip().lower()` it, and return `True` only if the result is `\"y\"` "
            "**or** `\"yes\"` (use `in (\"y\", \"yes\")`).\n"
            "- `greet(name: str) -> None` -- `print(f\"Hello, {name}!\")`.\n"
            "- `greeting_flow() -> str` -- call `ask_name()`, pass the result to "
            "`greet()`, then return the name.\n\n"
            "The tests simulate a user typing by patching `builtins.input` with "
            "`monkeypatch` and capture `print()` output with `capsys` -- you don't "
            "need to do anything special in your code for that; just call the real "
            "`input()`/`print()` builtins normally.\n\n"
            "See the Study Reference presentation, Topic 1, for the theory."
        ),
        "stub": '''\
def ask_name() -> str:
    """Prompt "What is your name? " and return the typed string."""
    raise NotImplementedError


def ask_age() -> int:
    """Prompt "How old are you? " and return the typed answer as an int."""
    raise NotImplementedError


def ask_yes_no(prompt: str) -> bool:
    """Prompt with `prompt`; True if the (lowercased, stripped) answer is "y" or "yes"."""
    raise NotImplementedError


def greet(name: str) -> None:
    """print(f"Hello, {name}!")."""
    raise NotImplementedError


def greeting_flow() -> str:
    """ask_name(), greet() it, then return the name."""
    raise NotImplementedError
''',
        "reference": '''\
def ask_name() -> str:
    return input("What is your name? ")


def ask_age() -> int:
    return int(input("How old are you? "))


def ask_yes_no(prompt: str) -> bool:
    answer = input(prompt).strip().lower()
    return answer in ("y", "yes")


def greet(name: str) -> None:
    print(f"Hello, {name}!")


def greeting_flow() -> str:
    name = ask_name()
    greet(name)
    return name
''',
        "test": '''\
from exercises.week01.exercise05.solution import (
    ask_name,
    ask_age,
    ask_yes_no,
    greet,
    greeting_flow,
)


def test_ask_name(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda prompt="": "Ada")
    assert ask_name() == "Ada"


def test_ask_age(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda prompt="": "30")
    assert ask_age() == 30


def test_ask_yes_no_true_for_y(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda prompt="": "y")
    assert ask_yes_no("Continue? ") is True


def test_ask_yes_no_true_for_yes_mixed_case(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda prompt="": "YES")
    assert ask_yes_no("Continue? ") is True


def test_ask_yes_no_false_for_no(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda prompt="": "n")
    assert ask_yes_no("Continue? ") is False


def test_greet(capsys):
    greet("Ada")
    assert capsys.readouterr().out == "Hello, Ada!\\n"


def test_greeting_flow(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda prompt="": "Ada")
    result = greeting_flow()
    assert result == "Ada"
    assert capsys.readouterr().out == "Hello, Ada!\\n"
''',
    },
    {
        "name": "exercise06",
        "title": "Mutability and Identity",
        "summary": "mutability vs immutability, identity (is) vs equality (==), None",
        "readme": (
            "Implement five functions that make mutability and identity concrete "
            "instead of abstract:\n\n"
            "- `append_and_return(lst: list, item) -> list` -- `lst.append(item)` "
            "then `return lst`. Because lists are mutable, the object you return is "
            "the *same* object the caller passed in.\n"
            "- `concat_strings(a: str, b: str) -> str` -- `return a + b`. Because "
            "strings are immutable, the result is always a *new* object, never `a` "
            "or `b` themselves.\n"
            "- `same_object(a, b) -> bool` -- `return a is b` (identity, not equality).\n"
            "- `equal_but_not_identical() -> tuple` -- return a tuple of two separately "
            "built but `==`-equal lists, e.g. `([1, 2, 3], [1, 2, 3])`, to demonstrate "
            "equality without identity.\n"
            "- `default_if_none(value, default)` -- `return default if value is None "
            "else value`.\n\n"
            "See the Study Reference presentation, Topic 1 (mutability vs immutability, "
            "identity vs equality), for the theory."
        ),
        "stub": '''\
def append_and_return(lst: list, item) -> list:
    """Mutate lst in place (append item) and return that same object."""
    raise NotImplementedError


def concat_strings(a: str, b: str) -> str:
    """Return a + b -- always a new string object (str is immutable)."""
    raise NotImplementedError


def same_object(a, b) -> bool:
    """True if a and b are the identical object (use `is`, not `==`)."""
    raise NotImplementedError


def equal_but_not_identical() -> tuple:
    """Return two separately-built, `==`-equal lists that are NOT the same object."""
    raise NotImplementedError


def default_if_none(value, default):
    """Return default if value is None, else value unchanged."""
    raise NotImplementedError
''',
        "reference": '''\
def append_and_return(lst: list, item) -> list:
    lst.append(item)
    return lst


def concat_strings(a: str, b: str) -> str:
    return a + b


def same_object(a, b) -> bool:
    return a is b


def equal_but_not_identical() -> tuple:
    return ([1, 2, 3], [1, 2, 3])


def default_if_none(value, default):
    return default if value is None else value
''',
        "test": '''\
from exercises.week01.exercise06.solution import (
    append_and_return,
    concat_strings,
    same_object,
    equal_but_not_identical,
    default_if_none,
)


def test_append_and_return_mutates_in_place_and_is_same_object():
    original = [1, 2]
    result = append_and_return(original, 3)
    assert result == [1, 2, 3]
    assert result is original


def test_concat_strings_returns_new_object():
    a = "foo"
    b = "bar"
    result = concat_strings(a, b)
    assert result == "foobar"
    assert result is not a
    assert result is not b


def test_same_object_true_for_shared_reference():
    x = [1, 2, 3]
    y = x
    assert same_object(x, y) is True


def test_same_object_false_for_equal_but_distinct_objects():
    x = [1, 2, 3]
    y = [1, 2, 3]
    assert x == y
    assert same_object(x, y) is False


def test_equal_but_not_identical():
    l1, l2 = equal_but_not_identical()
    assert l1 == l2
    assert l1 is not l2


def test_default_if_none_uses_default_for_none():
    assert default_if_none(None, "fallback") == "fallback"


def test_default_if_none_keeps_real_value():
    assert default_if_none(0, "fallback") == 0
''',
    },
]
