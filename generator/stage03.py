"""
Stage 3 -- Functions.

Rolled onto the tier-named exercise convention: a minimum of two exercises
per Basic/Mid/Advanced tier, each folder prefixed with its tier number so a
plain directory listing sorts in learning order --
"tier1_basicNN"/"tier2_midNN"/"tier3_advancedNN" -- instead of a flat
"exercise01".."exercise08" sequence. Unlike Stage 1/2, these
exercises are naturally **function-based** (not script-style) -- Stage 3's
entire content IS function definitions, so wrapping the work in `def`s is
exactly the point, not something to avoid.

Coverage plan (every item below is exercised by the trainee's own code,
generally 2+ times across these 6 exercises):

  Basic:    def, parameters, return, default args, *args, **kwargs,
            return type hints, basic recursion, lambda
  Mid:      keyword-only arguments, positional-only parameters,
            docstrings & introspection, closures, a simple decorator
  Advanced: functools (wraps, lru_cache, partial), generator functions
            (yield), LEGB scoping (global/local shadowing), the mutable-
            default-argument bug
"""

STAGE = "stage03"
TOPIC = "Functions"
OVERVIEW = (
    "Six exercises, two per tier. Every one is function-based -- Stage 3's "
    "whole subject is writing functions, so (unlike Stage 1/2) there's no "
    "reason to dodge `def` here. Each exercise is a small, realistic "
    "scenario combining several of that tier's specific tools at once."
)

EXERCISES = [
    {
        "name": "tier1_basic01",
        "title": "Order Total Calculator",
        "summary": "def, return, ->, default args, *args, **kwargs",
        "readme": (
            "Implement two order-pricing helpers:\n\n"
            "- `compute_total(*item_prices, tax_rate=0.08, **surcharges) -> float` "
            "-- `item_prices` is any number of positional prices (via `*args`); "
            "`tax_rate` is a keyword argument with a default of `0.08`; "
            "`surcharges` collects any number of extra named fees (via "
            "`**kwargs`, e.g. `shipping=5`, `handling=2`). Return "
            "`round(subtotal + tax + sum(surcharges.values()), 2)`, where "
            "`subtotal = sum(item_prices)` and `tax = subtotal * tax_rate`.\n"
            "- `apply_discount(price, pct=0.10) -> float` -- return "
            "`round(price * (1 - pct), 2)`. `pct` defaults to `0.10` (a 10% "
            "discount) but can be overridden.\n\n"
            "Both functions need a `-> float` return type hint on their "
            "signature, and `compute_total` must genuinely accept a variable "
            "number of prices and surcharges -- don't hardcode a fixed "
            "parameter list.\n\n"
            "See the Study Reference presentation, Topic 3 (Basic tier), for "
            "the theory."
        ),
        "stub": '''\
def compute_total(*item_prices, tax_rate=0.08, **surcharges) -> float:
    """subtotal=sum(item_prices); tax=subtotal*tax_rate; + sum(surcharges.values()), rounded to 2dp."""
    raise NotImplementedError


def apply_discount(price, pct=0.10) -> float:
    """round(price * (1 - pct), 2)."""
    raise NotImplementedError
''',
        "reference": '''\
def compute_total(*item_prices, tax_rate=0.08, **surcharges) -> float:
    subtotal = sum(item_prices)
    tax = subtotal * tax_rate
    return round(subtotal + tax + sum(surcharges.values()), 2)


def apply_discount(price, pct=0.10) -> float:
    return round(price * (1 - pct), 2)
''',
        "test": '''\
from exercises.stage03.tier1_basic01.solution import compute_total, apply_discount


def test_compute_total_with_surcharges_and_custom_tax_rate():
    """compute_total(*item_prices, tax_rate=..., **surcharges) combines *args, a keyword default override, and **kwargs surcharges."""
    assert compute_total(10, 20, 30, tax_rate=0.1, shipping=5, handling=2) == 73.0


def test_compute_total_default_tax_rate_no_surcharges():
    """compute_total() with no surcharges still applies the default tax_rate=0.08."""
    assert compute_total(50) == 54.0


def test_apply_discount_default_percentage():
    """apply_discount(price) uses the default pct=0.10."""
    assert apply_discount(100) == 90.0


def test_apply_discount_custom_percentage():
    """apply_discount(price, pct=...) overrides the default keyword argument."""
    assert apply_discount(100, 0.25) == 75.0
''',
    },
    {
        "name": "tier1_basic02",
        "title": "Digit & List Utilities",
        "summary": "basic recursion, lambda, return type hints",
        "readme": (
            "Implement two small recursive functions and two `lambda`s:\n\n"
            "- `count_digits(n: int) -> int` -- the number of digits in a "
            "non-negative `n`, **implemented recursively**: base case "
            "`n < 10` returns `1`; otherwise `1 + count_digits(n // 10)`.\n"
            "- `sum_of_squares_recursive(numbers: list) -> int` -- the sum of "
            "each number squared, **implemented recursively** over the list: "
            "base case `not numbers` returns `0`; otherwise "
            "`numbers[0] ** 2 + sum_of_squares_recursive(numbers[1:])`.\n"
            "- `square` -- a `lambda` equivalent to `lambda x: x * x`.\n"
            "- `is_even` -- a `lambda` equivalent to `lambda x: x % 2 == 0`.\n\n"
            "The two functions must actually recurse (call themselves on a "
            "smaller input) rather than use a loop -- that's the point of this "
            "exercise, and it's what the tests are checking for by construction "
            "(small inputs where a loop would be indistinguishable in output, "
            "but the pattern is what Stage 3 is teaching).\n\n"
            "See the Study Reference presentation, Topic 3 (Basic tier), for "
            "the theory."
        ),
        "stub": '''\
def count_digits(n: int) -> int:
    """Digit count of non-negative n -- MUST be implemented recursively (n < 10 base case)."""
    raise NotImplementedError


def sum_of_squares_recursive(numbers: list) -> int:
    """Sum of squares of numbers -- MUST be implemented recursively (empty-list base case)."""
    raise NotImplementedError


square = None  # TODO: replace with a lambda equivalent to `lambda x: x * x`
is_even = None  # TODO: replace with a lambda equivalent to `lambda x: x % 2 == 0`
''',
        "reference": '''\
def count_digits(n: int) -> int:
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)


def sum_of_squares_recursive(numbers: list) -> int:
    if not numbers:
        return 0
    return numbers[0] ** 2 + sum_of_squares_recursive(numbers[1:])


square = lambda x: x * x
is_even = lambda x: x % 2 == 0
''',
        "test": '''\
from exercises.stage03.tier1_basic02.solution import (
    count_digits,
    sum_of_squares_recursive,
    square,
    is_even,
)


def test_count_digits_recursive():
    """count_digits(n) must be recursive; check both a multi-digit and a single-digit input."""
    assert count_digits(12345) == 5
    assert count_digits(7) == 1


def test_sum_of_squares_recursive():
    """sum_of_squares_recursive(numbers) must be recursive; check a non-empty list and the empty-list base case."""
    assert sum_of_squares_recursive([1, 2, 3]) == 14
    assert sum_of_squares_recursive([]) == 0


def test_square_lambda():
    """square must be a lambda equivalent to `lambda x: x * x`."""
    assert square(6) == 36


def test_is_even_lambda():
    """is_even must be a lambda equivalent to `lambda x: x % 2 == 0`, returning real bools."""
    assert is_even(4) is True
    assert is_even(3) is False
''',
    },
    {
        "name": "tier2_mid01",
        "title": "Rate-Limited Logger Factory + Clamp",
        "summary": "closures, keyword-only args, positional-only params, docstrings & introspection",
        "readme": (
            "Implement:\n\n"
            "- `make_logger(*, prefix, max_entries=5)` -- `prefix` and "
            "`max_entries` are **keyword-only** (they come after the bare "
            "`*`). Return a one-argument `log(message)` **closure** that: "
            "appends `prefix + \": \" + message` to an internal list, and if "
            "the list now has more than `max_entries` items, drops the "
            "*oldest* one (`entries.pop(0)`). Each call to `log(...)` returns "
            "a copy of the current list (`list(entries)`), so you can observe "
            "it growing (and the oldest entry rolling off once it's over "
            "capacity).\n"
            "- `clamp(value, lo, hi, /) -> int|float` -- `value`, `lo`, `hi` "
            "are all **positional-only** (before the `/`). Return `lo` if "
            "`value < lo`, `hi` if `value > hi`, otherwise `value` unchanged.\n"
            "- `function_signature_info(fn) -> dict` -- introspect any "
            "function and return `{\"name\": fn.__name__, \"doc\": fn.__doc__}`.\n\n"
            "`make_logger`'s inner `log` function is a genuine closure: it "
            "must keep reading and mutating the *same* `entries` list across "
            "calls, defined once per `make_logger(...)` call (a fresh list "
            "each time `make_logger` itself is called).\n\n"
            "See the Study Reference presentation, Topic 3 (Mid tier), for "
            "the theory."
        ),
        "stub": '''\
def make_logger(*, prefix, max_entries=5):
    """Keyword-only prefix/max_entries. Return a log(message) closure over a capped entries list."""
    raise NotImplementedError


def clamp(value, lo, hi, /):
    """value/lo/hi positional-only. Clamp value into [lo, hi]."""
    raise NotImplementedError


def function_signature_info(fn) -> dict:
    """{"name": fn.__name__, "doc": fn.__doc__}."""
    raise NotImplementedError
''',
        "reference": '''\
def make_logger(*, prefix, max_entries=5):
    entries = []

    def log(message):
        entries.append(prefix + ": " + message)
        if len(entries) > max_entries:
            entries.pop(0)
        return list(entries)

    return log


def clamp(value, lo, hi, /):
    if value < lo:
        return lo
    if value > hi:
        return hi
    return value


def function_signature_info(fn) -> dict:
    return {"name": fn.__name__, "doc": fn.__doc__}
''',
        "test": '''\
import pytest
from exercises.stage03.tier2_mid01.solution import make_logger, clamp, function_signature_info


def test_make_logger_accumulates_and_caps_entries():
    """The log(message) closure appends prefix-prefixed entries and drops the oldest once past max_entries."""
    logger = make_logger(prefix="APP", max_entries=2)
    assert logger("a") == ["APP: a"]
    assert logger("b") == ["APP: a", "APP: b"]
    assert logger("c") == ["APP: b", "APP: c"]


def test_make_logger_prefix_and_max_entries_are_keyword_only():
    """prefix/max_entries must be keyword-only -- calling make_logger positionally must raise TypeError."""
    with pytest.raises(TypeError):
        make_logger("APP", 2)


def test_clamp_bounds_and_passthrough():
    """clamp(value, lo, hi) returns lo/hi/value depending on which side value falls, if any."""
    assert clamp(15, 0, 10) == 10
    assert clamp(-5, 0, 10) == 0
    assert clamp(5, 0, 10) == 5


def test_clamp_arguments_are_positional_only():
    """value/lo/hi must be positional-only -- calling clamp with keywords must raise TypeError."""
    with pytest.raises(TypeError):
        clamp(value=5, lo=0, hi=10)


def test_function_signature_info():
    """function_signature_info(fn) introspects fn.__name__ and fn.__doc__."""
    def sample():
        """A sample docstring."""

    assert function_signature_info(sample) == {"name": "sample", "doc": "A sample docstring."}
''',
    },
    {
        "name": "tier2_mid02",
        "title": "Call-Counting Decorator + Validated Config",
        "summary": "a simple decorator, closures, keyword-only args (a different scenario)",
        "readme": (
            "Implement:\n\n"
            "- `count_calls(fn)` -- a **decorator**. Return a `wrapper(*args, "
            "**kwargs)` that calls `fn(*args, **kwargs)` and returns its "
            "result, while tracking how many times it's been called as "
            "`wrapper.calls` (start it at `0` right after defining `wrapper`, "
            "increment it on every call).\n"
            "- `greet(name)` -- a plain (undecorated) function returning "
            '`"Hello, " + name`. It is deliberately **not** written as '
            "`@count_calls\\ndef greet(...)` in this file -- applying a "
            "still-unimplemented decorator with `@` syntax at import time "
            "would raise `NotImplementedError` immediately and crash the "
            "whole module before you'd even get to run a single test. The "
            "tests instead call `count_calls(greet)` themselves to check "
            "your decorator's behavior, exactly as you'd call it by hand "
            "anywhere else.\n"
            "- `make_validator(*, min_value, max_value=100)` -- `min_value` "
            "and `max_value` are **keyword-only**. Return a one-argument "
            "`validate(n)` **closure** that returns `True` iff "
            "`min_value <= n <= max_value`.\n\n"
            "`count_calls` is the simplest possible decorator shape: wrap, "
            "track state on the wrapper itself, still forward every call "
            "through to the original function and its return value.\n\n"
            "See the Study Reference presentation, Topic 3 (Mid tier), for "
            "the theory."
        ),
        "stub": '''\
def count_calls(fn):
    """Decorator: wrapper.calls counts calls to fn, starting at 0."""
    raise NotImplementedError


def greet(name):
    """"Hello, " + name -- deliberately NOT decorated with @count_calls here; see README."""
    raise NotImplementedError


def make_validator(*, min_value, max_value=100):
    """Keyword-only min_value/max_value. Return a validate(n) closure: min_value <= n <= max_value."""
    raise NotImplementedError
''',
        "reference": '''\
def count_calls(fn):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return fn(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


def greet(name):
    return "Hello, " + name


def make_validator(*, min_value, max_value=100):
    def validate(n):
        return min_value <= n <= max_value

    return validate
''',
        "test": '''\
import pytest
from exercises.stage03.tier2_mid02.solution import count_calls, greet, make_validator


def test_greet_returns_expected_message():
    """greet(name) returns "Hello, " + name."""
    assert greet("Ada") == "Hello, Ada"


def test_count_calls_tracks_call_count_on_wrapper():
    """count_calls(fn) returns a wrapper exposing wrapper.calls (incrementing by 1 per call) while still forwarding to fn."""
    tracked_greet = count_calls(greet)
    assert tracked_greet("Bo") == "Hello, Bo"
    assert tracked_greet("Cy") == "Hello, Cy"
    assert tracked_greet.calls == 2


def test_make_validator_default_max_value():
    """make_validator(min_value=...) uses the default max_value=100 and returns a validate(n) closure."""
    validate = make_validator(min_value=10)
    assert validate(5) is False
    assert validate(50) is True


def test_make_validator_custom_max_value():
    """make_validator(min_value=..., max_value=...) -- both bounds are honored by the returned closure."""
    validate = make_validator(min_value=0, max_value=10)
    assert validate(15) is False
    assert validate(5) is True


def test_make_validator_arguments_are_keyword_only():
    """min_value/max_value must be keyword-only -- calling make_validator positionally must raise TypeError."""
    with pytest.raises(TypeError):
        make_validator(0, 10)
''',
    },
    {
        "name": "tier3_advanced01",
        "title": "functools Toolkit",
        "summary": "functools.wraps, functools.lru_cache, functools.partial",
        "readme": (
            "Implement:\n\n"
            "- `logged(fn)` -- a decorator whose `wrapper` is decorated with "
            "`@functools.wraps(fn)` (so it preserves `fn`'s `__name__`/"
            "`__doc__`) and simply forwards every call: "
            "`return fn(*args, **kwargs)`.\n"
            "- `multiply(a, b)` -- a plain (undecorated) function, "
            '`"""Multiply two numbers."""`, returns `a * b`. It is '
            "deliberately **not** written as `@logged\\ndef multiply(...)` "
            "in this file -- applying a still-unimplemented decorator with "
            "`@` syntax at import time would raise `NotImplementedError` "
            "immediately and crash the whole module. The tests instead call "
            "`logged(multiply)` themselves to check your decorator's "
            "behavior.\n"
            "- `fib(n)` -- decorated with `@functools.lru_cache(maxsize=None)` "
            "(that decorator is already fully implemented by the standard "
            "library, so applying it at import time is safe), recursive "
            "Fibonacci (`n < 2` returns `n`, otherwise "
            "`fib(n - 1) + fib(n - 2)`).\n"
            "- `add_ten` -- `functools.partial(lambda a, b: a + b, b=10)`, a "
            "callable that adds `10` to whatever single argument it's given.\n\n"
            "Without `functools.wraps`, `logged(multiply).__name__` would be "
            '`"wrapper"` and its `__doc__` would be `None` -- the tests '
            "check exactly that this doesn't happen. Without "
            "`functools.lru_cache`, `fib(20)` would still be correct but "
            "`fib` wouldn't expose a `cache_info()` method.\n\n"
            "See the Study Reference presentation, Topic 3 (Advanced tier), "
            "for the theory."
        ),
        "stub": '''\
import functools


def logged(fn):
    """Decorator: functools.wraps(fn)-preserving passthrough wrapper."""
    raise NotImplementedError


def multiply(a, b):
    """Multiply two numbers. Deliberately NOT decorated with @logged here; see README."""
    raise NotImplementedError


@functools.lru_cache(maxsize=None)
def fib(n):
    """Recursive Fibonacci, cached with functools.lru_cache(maxsize=None)."""
    raise NotImplementedError


add_ten = None  # TODO: functools.partial(lambda a, b: a + b, b=10)
''',
        "reference": '''\
import functools


def logged(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)

    return wrapper


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


@functools.lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


add_ten = functools.partial(lambda a, b: a + b, b=10)
''',
        "test": '''\
from exercises.stage03.tier3_advanced01.solution import logged, multiply, fib, add_ten


def test_logged_preserves_metadata_via_functools_wraps():
    """logged(fn) must use functools.wraps(fn) so the wrapper's __name__/__doc__ still report the ORIGINAL function, not "wrapper"."""
    decorated = logged(multiply)
    assert decorated.__name__ == "multiply"
    assert decorated.__doc__ == "Multiply two numbers."


def test_logged_forwards_call_and_result():
    """The wrapper returned by logged(fn) must still actually call fn(*args, **kwargs) and return its result."""
    decorated = logged(multiply)
    assert decorated(3, 4) == 12


def test_fib_correctness():
    """fib(n) is the standard recursive Fibonacci definition."""
    assert fib(20) == 6765


def test_fib_is_lru_cached():
    """fib must be decorated with functools.lru_cache, exposing cache_info() with recorded hits."""
    fib(20)
    info = fib.cache_info()
    assert info.hits > 0


def test_add_ten_is_functools_partial():
    """add_ten must be functools.partial(lambda a, b: a + b, b=10), not a hand-written equivalent function."""
    import functools
    assert isinstance(add_ten, functools.partial)
    assert add_ten(5) == 15
''',
    },
    {
        "name": "tier3_advanced02",
        "title": "Generators, Scope & the Mutable-Default Trap",
        "summary": "yield / generator functions, global + LEGB scoping, the mutable-default-argument bug",
        "readme": (
            "Implement:\n\n"
            "- `batch_generator(items, batch_size)` -- a **generator "
            "function** (uses `yield`, not `return`) that yields successive "
            "slices of `items`, each of length `batch_size` (the last one "
            "may be shorter): "
            "`for i in range(0, len(items), batch_size): yield items[i:i + batch_size]`.\n"
            "- `counter = 0` (module-level, already in the stub) and "
            "`increment_global()` -- uses `global counter`, increments it by "
            "`1`, and returns the new value.\n"
            "- `make_local_shadow()` -- assigns a **local** variable also "
            "named `counter` set to `100` and returns it, **without** any "
            "`global` declaration. Because there's no `global`, this local "
            "assignment shadows the module-level `counter` inside this "
            "function only (LEGB: Python resolves the *assignment target* to "
            "a local name here) -- it must NOT change the module-level "
            "`counter`.\n"
            "- `append_bad(item, target=[])` -- **deliberately buggy**: "
            "`target.append(item); return target`. Because the default "
            "`[]` is created once, at function-definition time, and reused "
            "on every call that doesn't pass its own `target`, repeated "
            "calls silently accumulate into the *same* list.\n"
            "- `append_safe(item, target=None)` -- the fix: if `target is "
            "None: target = []`, then `target.append(item); return target`. "
            "A fresh list every time no `target` is supplied.\n\n"
            "This exercise is specifically about the traps: reading "
            "`increment_global`/`make_local_shadow` side by side shows "
            "`global` vs. ordinary local shadowing, and "
            "`append_bad`/`append_safe` side by side shows the classic "
            "mutable-default-argument bug and its fix.\n\n"
            "See the Study Reference presentation, Topic 3 (Advanced tier), "
            "for the theory."
        ),
        "stub": '''\
counter = 0


def batch_generator(items, batch_size):
    """Generator: yield successive batch_size-length slices of items."""
    raise NotImplementedError


def increment_global() -> int:
    """global counter; increment it by 1 and return the new value."""
    raise NotImplementedError


def make_local_shadow() -> int:
    """Assign a LOCAL counter = 100 (no `global`) and return it; must NOT touch the module-level counter."""
    raise NotImplementedError


def append_bad(item, target=[]):
    """Deliberately buggy: target.append(item); return target. Demonstrates the mutable-default-argument trap."""
    raise NotImplementedError


def append_safe(item, target=None):
    """Fixed version: if target is None: target = []; then append/return. A fresh list per call."""
    raise NotImplementedError
''',
        "reference": '''\
counter = 0


def batch_generator(items, batch_size):
    for i in range(0, len(items), batch_size):
        yield items[i:i + batch_size]


def increment_global() -> int:
    global counter
    counter += 1
    return counter


def make_local_shadow() -> int:
    counter = 100
    return counter


def append_bad(item, target=[]):
    target.append(item)
    return target


def append_safe(item, target=None):
    if target is None:
        target = []
    target.append(item)
    return target
''',
        "test": '''\
from exercises.stage03.tier3_advanced02.solution import (
    batch_generator,
    increment_global,
    make_local_shadow,
)
import exercises.stage03.tier3_advanced02.solution as solution


def test_batch_generator_yields_slices():
    """batch_generator must be a generator function (yield), splitting items into batch_size-length chunks."""
    assert list(batch_generator([1, 2, 3, 4, 5], 2)) == [[1, 2], [3, 4], [5]]


def test_batch_generator_is_lazy():
    """Calling batch_generator(...) must return a generator object, not a fully-built list."""
    gen = batch_generator([1, 2, 3], 1)
    assert hasattr(gen, "__next__")
    assert next(gen) == [1]


def test_increment_global_mutates_module_level_counter():
    """increment_global uses `global counter` to mutate the actual module-level name across calls."""
    solution.counter = 0
    assert increment_global() == 1
    assert increment_global() == 2
    assert solution.counter == 2


def test_make_local_shadow_does_not_affect_module_level_counter():
    """make_local_shadow's `counter = 100` is a LOCAL assignment (no `global`) -- module-level counter must be untouched."""
    solution.counter = 5
    assert make_local_shadow() == 100
    assert solution.counter == 5


def test_append_bad_demonstrates_mutable_default_argument_bug():
    """append_bad's default target=[] is a SHARED object reused across calls -- items accumulate silently."""
    first_call_result = solution.append_bad(1)
    second_call_result = solution.append_bad(2)
    assert second_call_result == [1, 2]
    assert first_call_result is second_call_result


def test_append_safe_gives_a_fresh_list_each_call():
    """append_safe's target=None sentinel must produce an independent list on every call with no target passed."""
    first_call_result = solution.append_safe(1)
    second_call_result = solution.append_safe(2)
    assert first_call_result == [1]
    assert second_call_result == [2]
''',
    },
]
