"""
Week 3 -- Functions.

Coverage plan (each item exercised by the trainee's own code >=3 times):
  keywords: def, return, ->, *args, **kwargs, lambda, global, nonlocal, yield
  modules:  functools
  methods:  functools.wraps(), functools.lru_cache(), functools.partial()
  concepts: closures, decorators, keyword-only arguments,
            positional-only parameters
"""

WEEK = "week03"
TOPIC = "Functions"
OVERVIEW = (
    "Eight exercises covering every function-definition keyword and "
    "functools tool from Topic 3 at least three times each -- including "
    "the two argument styles (keyword-only, positional-only) most people "
    "never write on purpose until they hit a library that requires them."
)

EXERCISES = [
    {
        "name": "exercise01",
        "title": "Recursion Basics",
        "summary": "def, return, ->, recursion",
        "readme": (
            "Implement two classic recursive functions:\n\n"
            "- `factorial(n: int) -> int` -- `n!`. **Must** be recursive, not a "
            "loop: base case `n in (0, 1)` returns `1`; otherwise "
            "`n * factorial(n - 1)`. Raise `ValueError` for negative `n`.\n"
            "- `fibonacci(n: int) -> int` -- the nth Fibonacci number (0-indexed). "
            "**Must** be recursive: base case `n in (0, 1)` returns `n`; "
            "otherwise `fibonacci(n - 1) + fibonacci(n - 2)`.\n\n"
            "The tests only check the *output* -- an iterative version would "
            "technically pass -- but the point of this exercise is the recursive "
            "pattern itself (base case + a call to yourself on a smaller input), "
            "which the next seven exercises' closures and decorators build on.\n\n"
            "See the Study Reference presentation, Topic 3, for the theory."
        ),
        "stub": '''\
def factorial(n: int) -> int:
    """n! -- MUST be implemented recursively. Raise ValueError if n < 0."""
    raise NotImplementedError


def fibonacci(n: int) -> int:
    """nth Fibonacci number (0-indexed) -- MUST be implemented recursively."""
    raise NotImplementedError
''',
        "reference": '''\
def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("factorial is not defined for negative numbers")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("fibonacci is not defined for negative numbers")
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
''',
        "test": '''\
import pytest
from exercises.week03.exercise01.solution import factorial, fibonacci


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120


def test_factorial_negative_raises():
    with pytest.raises(ValueError):
        factorial(-1)


def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(10) == 55
''',
    },
    {
        "name": "exercise02",
        "title": "Args and Kwargs",
        "summary": "*args, **kwargs",
        "readme": (
            "Implement:\n\n"
            "- `sum_all(*args: int) -> int` -- sum any number of positional "
            "arguments: `sum_all(1, 2, 3) == 6`.\n"
            "- `build_config(**kwargs) -> dict` -- return the keyword arguments "
            "as a plain dict: `build_config(host=\"x\", port=1) == "
            "{\"host\": \"x\", \"port\": 1}`.\n"
            "- `describe_call(*args, **kwargs) -> str` -- return "
            "`f\"args={args}, kwargs={kwargs}\"` (both packed into their "
            "respective tuple/dict).\n\n"
            "See the Study Reference presentation, Topic 3, for the theory."
        ),
        "stub": '''\
def sum_all(*args: int) -> int:
    """Sum any number of positional int arguments."""
    raise NotImplementedError


def build_config(**kwargs) -> dict:
    """Return the keyword arguments as a plain dict."""
    raise NotImplementedError


def describe_call(*args, **kwargs) -> str:
    """f"args={args}, kwargs={kwargs}"."""
    raise NotImplementedError
''',
        "reference": '''\
def sum_all(*args: int) -> int:
    return sum(args)


def build_config(**kwargs) -> dict:
    return dict(kwargs)


def describe_call(*args, **kwargs) -> str:
    return f"args={args}, kwargs={kwargs}"
''',
        "test": '''\
from exercises.week03.exercise02.solution import sum_all, build_config, describe_call


def test_sum_all():
    assert sum_all(1, 2, 3) == 6
    assert sum_all() == 0


def test_build_config():
    assert build_config(host="x", port=1) == {"host": "x", "port": 1}


def test_describe_call():
    assert describe_call(1, 2, key="value") == "args=(1, 2), kwargs={'key': 'value'}"
''',
    },
    {
        "name": "exercise03",
        "title": "Lambdas and Higher-Order Functions",
        "summary": "lambda x3, functions that take/return callables",
        "readme": (
            "Implement:\n\n"
            "- `make_multiplier(factor: int)` -- return a one-argument callable "
            "equivalent to `lambda x: x * factor`, built with an actual `lambda`.\n"
            "- `sort_by_length(words: list[str]) -> list[str]` -- "
            "`sorted(words, key=lambda w: len(w))`.\n"
            "- `top_scorer(records: list[dict]) -> dict` -- "
            "`max(records, key=lambda r: r[\"score\"])`.\n\n"
            "All three use a `lambda` -- short, throwaway functions passed "
            "directly where a callable is expected, instead of a separate "
            "`def`.\n\n"
            "See the Study Reference presentation, Topic 3, for the theory."
        ),
        "stub": '''\
def make_multiplier(factor: int):
    """Return a one-arg callable that multiplies its input by factor (a lambda)."""
    raise NotImplementedError


def sort_by_length(words: list[str]) -> list[str]:
    """Words sorted shortest to longest, via sorted(..., key=lambda ...)."""
    raise NotImplementedError


def top_scorer(records: list[dict]) -> dict:
    """The record with the highest "score", via max(..., key=lambda ...)."""
    raise NotImplementedError
''',
        "reference": '''\
def make_multiplier(factor: int):
    return lambda x: x * factor


def sort_by_length(words: list[str]) -> list[str]:
    return sorted(words, key=lambda w: len(w))


def top_scorer(records: list[dict]) -> dict:
    return max(records, key=lambda r: r["score"])
''',
        "test": '''\
from exercises.week03.exercise03.solution import (
    make_multiplier,
    sort_by_length,
    top_scorer,
)


def test_make_multiplier():
    double = make_multiplier(2)
    assert double(5) == 10
    triple = make_multiplier(3)
    assert triple(5) == 15


def test_sort_by_length():
    assert sort_by_length(["ccc", "a", "bb"]) == ["a", "bb", "ccc"]


def test_top_scorer():
    records = [{"name": "a", "score": 10}, {"name": "b", "score": 30}, {"name": "c", "score": 20}]
    assert top_scorer(records) == {"name": "b", "score": 30}
''',
    },
    {
        "name": "exercise04",
        "title": "Scope: global and nonlocal",
        "summary": "global x3, nonlocal x3, closures",
        "readme": (
            "Implement a module-level counter using `global`, and three closures "
            "using `nonlocal`:\n\n"
            "- `_counter = 0` (module-level variable, already in the stub).\n"
            "- `increment_counter() -> int` -- `global _counter`, `_counter += 1`, "
            "return the new value.\n"
            "- `reset_counter() -> None` -- `global _counter`, set it back to `0`.\n"
            "- `set_counter(value: int) -> None` -- `global _counter`, set it "
            "directly to `value`.\n"
            "- `get_counter() -> int` -- return `_counter`. No `global` needed "
            "here: `global` is only required when *assigning* to a module-level "
            "name from inside a function, not when reading it.\n"
            "- `make_counter()` -- return a zero-arg function that returns "
            "`1, 2, 3, ...` on successive calls: a local `count = 0` inside "
            "`make_counter`, an inner `counter()` that does `nonlocal count; "
            "count += 1; return count`. This is a **closure**: each call to "
            "`make_counter()` creates a fresh, independent `count`.\n"
            "- `make_accumulator(start: int = 0)` -- return a one-arg `add(x)` "
            "closure that adds `x` to a running total (starting at `start`) and "
            "returns the new total, using `nonlocal`.\n"
            "- `make_toggle(initial: bool = False)` -- return a zero-arg closure "
            "that flips and returns a running bool each call, using `nonlocal`.\n\n"
            "See the Study Reference presentation, Topic 3, for the theory."
        ),
        "stub": '''\
_counter = 0


def increment_counter() -> int:
    """global _counter; increment it by 1 and return the new value."""
    raise NotImplementedError


def reset_counter() -> None:
    """global _counter; set it back to 0."""
    raise NotImplementedError


def set_counter(value: int) -> None:
    """global _counter; set it directly to value."""
    raise NotImplementedError


def get_counter() -> int:
    """Return _counter (no `global` needed -- this only reads it)."""
    raise NotImplementedError


def make_counter():
    """Return a zero-arg closure yielding 1, 2, 3, ... on successive calls (nonlocal)."""
    raise NotImplementedError


def make_accumulator(start: int = 0):
    """Return a one-arg closure add(x) that accumulates a running total (nonlocal)."""
    raise NotImplementedError


def make_toggle(initial: bool = False):
    """Return a zero-arg closure that flips/returns a running bool each call (nonlocal)."""
    raise NotImplementedError
''',
        "reference": '''\
_counter = 0


def increment_counter() -> int:
    global _counter
    _counter += 1
    return _counter


def reset_counter() -> None:
    global _counter
    _counter = 0


def set_counter(value: int) -> None:
    global _counter
    _counter = value


def get_counter() -> int:
    return _counter


def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


def make_accumulator(start: int = 0):
    total = start

    def add(x):
        nonlocal total
        total += x
        return total

    return add


def make_toggle(initial: bool = False):
    state = initial

    def toggle():
        nonlocal state
        state = not state
        return state

    return toggle
''',
        "test": '''\
from exercises.week03.exercise04.solution import (
    increment_counter,
    reset_counter,
    set_counter,
    get_counter,
    make_counter,
    make_accumulator,
    make_toggle,
)


def test_increment_and_reset_counter():
    reset_counter()
    assert get_counter() == 0
    assert increment_counter() == 1
    assert increment_counter() == 2
    reset_counter()
    assert get_counter() == 0


def test_set_counter():
    set_counter(100)
    assert get_counter() == 100
    reset_counter()


def test_make_counter_is_independent_per_closure():
    counter_a = make_counter()
    counter_b = make_counter()
    assert counter_a() == 1
    assert counter_a() == 2
    assert counter_b() == 1


def test_make_accumulator():
    acc = make_accumulator(10)
    assert acc(5) == 15
    assert acc(5) == 20


def test_make_toggle():
    toggle = make_toggle()
    assert toggle() is True
    assert toggle() is False
    assert toggle() is True
''',
    },
    {
        "name": "exercise05",
        "title": "Decorators",
        "summary": "decorators x3, functools.wraps() x3",
        "readme": (
            "Implement three decorators, each preserving the wrapped function's "
            "`__name__`/`__doc__` with `functools.wraps`:\n\n"
            "- `log_calls(func)` -- wraps `func` so `wrapper.calls` counts how "
            "many times it's been called (start it at `0`, increment inside the "
            "wrapper, still call and return `func(*args, **kwargs)`).\n"
            "- `count_calls(func)` -- same idea, but track the count in a closure "
            "variable (`nonlocal`) instead of an attribute, exposed as a zero-arg "
            "`wrapper.call_count()` method you attach after defining `wrapper`.\n"
            "- `uppercase_result(func)` -- call `func`, and if the result is a "
            "`str`, return it `.upper()`-ed; otherwise return it unchanged.\n\n"
            "Every wrapper must be decorated with `@functools.wraps(func)` so "
            "`wrapper.__name__`/`wrapper.__doc__` still report the *original* "
            "function's name and docstring, not `\"wrapper\"`.\n\n"
            "See the Study Reference presentation, Topic 3, for the theory."
        ),
        "stub": '''\
import functools


def log_calls(func):
    """Decorator: wrapper.calls counts calls to func. Use functools.wraps(func)."""
    raise NotImplementedError


def count_calls(func):
    """Decorator: wrapper.call_count() (a zero-arg method) returns the call count via a closure. Use functools.wraps(func)."""
    raise NotImplementedError


def uppercase_result(func):
    """Decorator: uppercase func's result if it's a str, else pass it through. Use functools.wraps(func)."""
    raise NotImplementedError
''',
        "reference": '''\
import functools


def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


def count_calls(func):
    count = 0

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        return func(*args, **kwargs)

    wrapper.call_count = lambda: count
    return wrapper


def uppercase_result(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper() if isinstance(result, str) else result

    return wrapper
''',
        "test": '''\
from exercises.week03.exercise05.solution import log_calls, count_calls, uppercase_result


def test_log_calls_tracks_call_count():
    @log_calls
    def add(a, b):
        return a + b

    assert add(1, 2) == 3
    assert add(2, 2) == 4
    assert add.calls == 2


def test_log_calls_preserves_metadata():
    @log_calls
    def greet(name):
        """Say hello."""
        return f"hi {name}"

    assert greet.__name__ == "greet"
    assert greet.__doc__ == "Say hello."


def test_count_calls():
    @count_calls
    def noop():
        return None

    noop()
    noop()
    noop()
    assert noop.call_count() == 3


def test_uppercase_result():
    @uppercase_result
    def shout(msg):
        return msg

    assert shout("hello") == "HELLO"


def test_uppercase_result_passthrough_non_str():
    @uppercase_result
    def give_number():
        return 42

    assert give_number() == 42
''',
    },
    {
        "name": "exercise06",
        "title": "Functools Toolbox",
        "summary": "functools.lru_cache() x3, functools.partial() x3",
        "readme": (
            "Implement three `functools.lru_cache`-decorated functions and three "
            "helpers built around `functools.partial`:\n\n"
            "- `cached_fibonacci(n: int) -> int` -- recursive Fibonacci, decorated "
            "with `@functools.lru_cache(maxsize=None)`.\n"
            "- `cached_is_prime(n: int) -> bool` -- primality check, same "
            "decorator.\n"
            "- `cached_factorial(n: int) -> int` -- recursive factorial, same "
            "decorator.\n\n"
            "- `add(a: int, b: int) -> int` / `multiply(a: int, b: int) -> int` / "
            "`format_currency(amount: float, symbol: str) -> str` "
            "(`f\"{symbol}{amount:.2f}\"`) -- three plain two-argument helpers.\n"
            "- `make_adder(n: int)` -- return `functools.partial(add, n)`.\n"
            "- `make_multiplier_via_partial(n: int)` -- return "
            "`functools.partial(multiply, n)`.\n"
            "- `make_usd_formatter()` -- return "
            "`functools.partial(format_currency, symbol=\"$\")`.\n\n"
            "The tests check `hasattr(fn, \"cache_info\")` and "
            "`isinstance(fn, functools.partial)` respectively -- those only pass "
            "if you actually used the decorator/`functools.partial`, not just a "
            "hand-written equivalent.\n\n"
            "See the Study Reference presentation, Topic 3, for the theory."
        ),
        "stub": '''\
import functools


def cached_fibonacci(n: int) -> int:
    """Recursive Fibonacci, decorated with functools.lru_cache(maxsize=None)."""
    raise NotImplementedError


def cached_is_prime(n: int) -> bool:
    """Primality check, decorated with functools.lru_cache(maxsize=None)."""
    raise NotImplementedError


def cached_factorial(n: int) -> int:
    """Recursive factorial, decorated with functools.lru_cache(maxsize=None)."""
    raise NotImplementedError


def add(a: int, b: int) -> int:
    raise NotImplementedError


def multiply(a: int, b: int) -> int:
    raise NotImplementedError


def format_currency(amount: float, symbol: str) -> str:
    """f"{symbol}{amount:.2f}"."""
    raise NotImplementedError


def make_adder(n: int):
    """functools.partial(add, n)."""
    raise NotImplementedError


def make_multiplier_via_partial(n: int):
    """functools.partial(multiply, n)."""
    raise NotImplementedError


def make_usd_formatter():
    """functools.partial(format_currency, symbol="$")."""
    raise NotImplementedError
''',
        "reference": '''\
import functools


@functools.lru_cache(maxsize=None)
def cached_fibonacci(n: int) -> int:
    if n in (0, 1):
        return n
    return cached_fibonacci(n - 1) + cached_fibonacci(n - 2)


@functools.lru_cache(maxsize=None)
def cached_is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


@functools.lru_cache(maxsize=None)
def cached_factorial(n: int) -> int:
    if n in (0, 1):
        return 1
    return n * cached_factorial(n - 1)


def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b


def format_currency(amount: float, symbol: str) -> str:
    return f"{symbol}{amount:.2f}"


def make_adder(n: int):
    return functools.partial(add, n)


def make_multiplier_via_partial(n: int):
    return functools.partial(multiply, n)


def make_usd_formatter():
    return functools.partial(format_currency, symbol="$")
''',
        "test": '''\
import functools
from exercises.week03.exercise06.solution import (
    cached_fibonacci,
    cached_is_prime,
    cached_factorial,
    make_adder,
    make_multiplier_via_partial,
    make_usd_formatter,
)


def test_cached_fibonacci_correctness_and_caching():
    assert cached_fibonacci(10) == 55
    assert hasattr(cached_fibonacci, "cache_info")


def test_cached_is_prime_correctness_and_caching():
    assert cached_is_prime(17) is True
    assert cached_is_prime(18) is False
    assert hasattr(cached_is_prime, "cache_info")


def test_cached_factorial_correctness_and_caching():
    assert cached_factorial(5) == 120
    assert hasattr(cached_factorial, "cache_info")


def test_make_adder():
    add5 = make_adder(5)
    assert add5(3) == 8
    assert isinstance(add5, functools.partial)


def test_make_multiplier_via_partial():
    times3 = make_multiplier_via_partial(3)
    assert times3(4) == 12
    assert isinstance(times3, functools.partial)


def test_make_usd_formatter():
    usd = make_usd_formatter()
    assert usd(9.5) == "$9.50"
    assert isinstance(usd, functools.partial)
''',
    },
    {
        "name": "exercise07",
        "title": "Signature Styles",
        "summary": "keyword-only arguments x3, positional-only parameters x3",
        "readme": (
            "Implement four functions using Python's `/` and `*` signature "
            "markers:\n\n"
            "- `compute_area(length, width, *, unit=\"m\") -> str` -- return "
            "`f\"{length * width}{unit}^2\"`. `unit` is **keyword-only** (it "
            "comes after the bare `*`): `compute_area(2, 3, \"cm\")` must raise "
            "`TypeError`; `compute_area(2, 3, unit=\"cm\")` must work.\n"
            "- `divide(a, b, /, *, precision=2) -> float` -- return "
            "`round(a / b, precision)`. `a`/`b` are **positional-only** (before "
            "the `/`); `precision` is keyword-only.\n"
            "- `connect(host, port, /, *, timeout=30, retries=3) -> dict` -- "
            "return `{\"host\": host, \"port\": port, \"timeout\": timeout, "
            "\"retries\": retries}`. Same pattern, two positional-only and two "
            "keyword-only parameters.\n"
            "- `scale_point(x, y, /, factor=1.0) -> tuple` -- return "
            "`(x * factor, y * factor)`. `x`/`y` are positional-only; `factor` "
            "is a normal parameter (callable either positionally or by "
            "keyword) -- not everything after `/` has to also be after `*`.\n\n"
            "See the Study Reference presentation, Topic 3, for the theory."
        ),
        "stub": '''\
def compute_area(length, width, *, unit="m") -> str:
    """f"{length*width}{unit}^2" -- unit is keyword-only."""
    raise NotImplementedError


def divide(a, b, /, *, precision=2) -> float:
    """round(a / b, precision) -- a, b positional-only; precision keyword-only."""
    raise NotImplementedError


def connect(host, port, /, *, timeout=30, retries=3) -> dict:
    """{"host":..., "port":..., "timeout":..., "retries":...} -- host/port positional-only, timeout/retries keyword-only."""
    raise NotImplementedError


def scale_point(x, y, /, factor=1.0) -> tuple:
    """(x*factor, y*factor) -- x, y positional-only; factor is a normal parameter."""
    raise NotImplementedError
''',
        "reference": '''\
def compute_area(length, width, *, unit="m") -> str:
    return f"{length * width}{unit}^2"


def divide(a, b, /, *, precision=2) -> float:
    return round(a / b, precision)


def connect(host, port, /, *, timeout=30, retries=3) -> dict:
    return {"host": host, "port": port, "timeout": timeout, "retries": retries}


def scale_point(x, y, /, factor=1.0) -> tuple:
    return (x * factor, y * factor)
''',
        "test": '''\
import pytest
from exercises.week03.exercise07.solution import compute_area, divide, connect, scale_point


def test_compute_area_default_unit():
    assert compute_area(2, 3) == "6m^2"


def test_compute_area_custom_unit_keyword_only():
    assert compute_area(2, 3, unit="cm") == "6cm^2"


def test_compute_area_unit_must_be_keyword():
    with pytest.raises(TypeError):
        compute_area(2, 3, "cm")


def test_divide():
    assert divide(10, 3, precision=3) == 3.333


def test_divide_positional_only_enforced():
    with pytest.raises(TypeError):
        divide(a=7, b=2)


def test_divide_precision_keyword_only_enforced():
    with pytest.raises(TypeError):
        divide(7, 2, 3)


def test_connect_defaults():
    assert connect("localhost", 8080) == {
        "host": "localhost", "port": 8080, "timeout": 30, "retries": 3,
    }


def test_connect_keyword_only_overrides():
    result = connect("localhost", 8080, timeout=5, retries=1)
    assert result == {"host": "localhost", "port": 8080, "timeout": 5, "retries": 1}


def test_connect_positional_only_enforced():
    with pytest.raises(TypeError):
        connect(host="localhost", port=8080)


def test_scale_point_default_factor():
    assert scale_point(2, 3) == (2, 3)


def test_scale_point_with_factor_positional_or_keyword():
    assert scale_point(2, 3, 2) == (4, 6)
    assert scale_point(2, 3, factor=2) == (4, 6)


def test_scale_point_positional_only_enforced():
    with pytest.raises(TypeError):
        scale_point(x=2, y=3)
''',
    },
    {
        "name": "exercise08",
        "title": "Generators",
        "summary": "yield x3",
        "readme": (
            "Implement three generator functions and a consumer:\n\n"
            "- `count_up_to(n: int)` -- `yield 1, 2, ..., n` one at a time (a "
            "`for` loop with a `yield` inside, not a `return`ed list).\n"
            "- `evens_only(numbers: list[int])` -- `yield` only the even numbers "
            "from `numbers`, in order.\n"
            "- `infinite_counter()` -- `yield 0, 1, 2, 3, ...` **forever**, no "
            "stopping condition (`while True: yield i; i += 1`). Never call "
            "`list()` on this one -- it doesn't stop.\n"
            "- `take(iterable, n: int) -> list` -- return the first `n` items "
            "from any iterable (including an infinite one), via "
            "`list(itertools.islice(iterable, n))`. This is how you safely "
            "consume `infinite_counter()`.\n\n"
            "A generator function is any function whose body contains `yield` -- "
            "calling it doesn't run any code immediately, it just returns a "
            "generator object; the body only executes as you pull values out "
            "with `next()` (or a `for` loop, or `itertools.islice`).\n\n"
            "See the Study Reference presentation, Topic 3, for the theory."
        ),
        "stub": '''\
def count_up_to(n: int):
    """Generator: yield 1, 2, ..., n."""
    raise NotImplementedError


def evens_only(numbers: list[int]):
    """Generator: yield only the even numbers from numbers, in order."""
    raise NotImplementedError


def infinite_counter():
    """Generator: yield 0, 1, 2, 3, ... forever. Consume with take(), never list()."""
    raise NotImplementedError


def take(iterable, n: int) -> list:
    """First n items of iterable, via itertools.islice(iterable, n)."""
    raise NotImplementedError
''',
        "reference": '''\
import itertools


def count_up_to(n: int):
    for i in range(1, n + 1):
        yield i


def evens_only(numbers: list[int]):
    for n in numbers:
        if n % 2 == 0:
            yield n


def infinite_counter():
    i = 0
    while True:
        yield i
        i += 1


def take(iterable, n: int) -> list:
    return list(itertools.islice(iterable, n))
''',
        "test": '''\
from exercises.week03.exercise08.solution import (
    count_up_to,
    evens_only,
    infinite_counter,
    take,
)


def test_count_up_to():
    assert list(count_up_to(5)) == [1, 2, 3, 4, 5]


def test_count_up_to_is_lazy_generator():
    gen = count_up_to(3)
    assert hasattr(gen, "__next__")
    assert next(gen) == 1
    assert next(gen) == 2


def test_evens_only():
    assert list(evens_only([1, 2, 3, 4, 5, 6])) == [2, 4, 6]


def test_infinite_counter_via_take():
    assert take(infinite_counter(), 5) == [0, 1, 2, 3, 4]


def test_take_with_finite_generator():
    assert take(count_up_to(100), 3) == [1, 2, 3]
''',
    },
]
