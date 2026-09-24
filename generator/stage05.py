"""
Stage 5 -- Files, Exceptions, Regex.

Rolled onto the tier-named exercise convention: a minimum of two exercises
per Basic/Mid/Advanced tier. All exercises here are function-based (plus a
handful of small classes for the exception hierarchies and class-based
context managers, which are inherently class-shaped content).

Coverage plan (every item below is exercised by the trainee's own code,
generally 2+ times across these 6 exercises):

  Basic:    open(), with, as, try, except, finally, raise, Exception,
            re.search(), re.findall(), re.match(), re.sub()
  Mid:      re.compile(), contextlib module, exception chaining
            (raise ... from ...), exception hierarchies, regex named groups
  Advanced: contextlib.contextmanager, __enter__, __exit__, custom context
            managers
"""

STAGE = "stage05"
TOPIC = "Files, Exceptions, Regex"
OVERVIEW = (
    "Six exercises, two per tier: file I/O and everyday try/except/finally/"
    "raise plus basic regex in Basic; custom exception hierarchies with "
    "raise ... from ... chaining, and compiled named-group regex, in Mid; "
    "both ways to write a context manager -- a class with __enter__/"
    "__exit__, and @contextlib.contextmanager -- in Advanced."
)

EXERCISES = [
    {
        "name": "basic01",
        "title": "Session Log Files",
        "summary": "open(), with, as",
        "readme": (
            "Implement four small file-handling functions, each using "
            "`with open(...) as f:` (never a bare `open()`/`close()` "
            "pair):\n\n"
            "- `write_lines(path: str, lines: list[str]) -> None` -- open "
            "`path` for writing (`\"w\"`), write each line followed by "
            "`\"\\n\"`.\n"
            "- `read_lines(path: str) -> list[str]` -- open `path` for "
            "reading, return `f.read().splitlines()`.\n"
            "- `append_line(path: str, line: str) -> None` -- open `path` "
            "for appending (`\"a\"`), write `line + \"\\n\"`.\n"
            "- `count_lines(path: str) -> int` -- open `path` for reading, "
            "return how many lines it has.\n\n"
            "See the Study Reference presentation, Topic 5 (Basic tier), "
            "for the theory."
        ),
        "stub": '''\
def write_lines(path: str, lines: list[str]) -> None:
    """Open path for writing and write each line, each followed by "\\n"."""
    raise NotImplementedError


def read_lines(path: str) -> list[str]:
    """Open path for reading; return f.read().splitlines()."""
    raise NotImplementedError


def append_line(path: str, line: str) -> None:
    """Open path in append mode ("a") and write line + "\\n"."""
    raise NotImplementedError


def count_lines(path: str) -> int:
    """Open path for reading and return how many lines it has."""
    raise NotImplementedError
''',
        "reference": '''\
def write_lines(path: str, lines: list[str]) -> None:
    with open(path, "w") as f:
        for line in lines:
            f.write(line + "\\n")


def read_lines(path: str) -> list[str]:
    with open(path) as f:
        return f.read().splitlines()


def append_line(path: str, line: str) -> None:
    with open(path, "a") as f:
        f.write(line + "\\n")


def count_lines(path: str) -> int:
    with open(path) as f:
        return len(f.read().splitlines())
''',
        "test": '''\
from exercises.stage05.basic01.solution import (
    write_lines,
    read_lines,
    append_line,
    count_lines,
)


def test_write_and_read_lines(tmp_path):
    """write_lines/read_lines must each use `with open(...) as f:` -- writing "line\\n" per entry, reading via f.read().splitlines()."""
    path = str(tmp_path / "data.txt")
    write_lines(path, ["a", "b", "c"])
    assert read_lines(path) == ["a", "b", "c"]


def test_append_line(tmp_path):
    """append_line opens in "a" mode and writes line + "\\n" without truncating existing content."""
    path = str(tmp_path / "data.txt")
    write_lines(path, ["a"])
    append_line(path, "b")
    assert read_lines(path) == ["a", "b"]


def test_count_lines(tmp_path):
    """count_lines opens for reading and returns the number of lines."""
    path = str(tmp_path / "data.txt")
    write_lines(path, ["a", "b", "c", "d"])
    assert count_lines(path) == 4
''',
    },
    {
        "name": "basic02",
        "title": "Support Ticket Intake",
        "summary": "try, except, finally, raise, Exception, re.search(), re.findall(), re.match(), re.sub()",
        "readme": (
            "A support inbox's raw ticket text needs scanning and cleaning. "
            "Implement:\n\n"
            "- `extract_ticket_ids(text: str) -> list[str]` -- "
            "`re.findall(r\"TICKET-\\d+\", text)`.\n"
            "- `contains_urgent_flag(text: str) -> bool` -- "
            "`re.search(r\"\\bURGENT\\b\", text) is not None`.\n"
            "- `clean_ticket_text(text: str) -> str` -- "
            "`re.sub(r\"\\s+\", \" \", text).strip()` (collapse whitespace "
            "runs to a single space).\n"
            "- `looks_like_ticket_id(text: str) -> bool` -- "
            "`re.match(r\"TICKET-\\d+$\", text) is not None` (`re.match` only "
            "anchors at the **start**, and `$` anchors the **end**, so this "
            "is `True` only if `text` is *entirely* a ticket id, unlike "
            "`extract_ticket_ids` above which finds ids anywhere).\n"
            "- `parse_priority(raw: str) -> int` -- "
            "`try: return int(raw)` `except ValueError: raise "
            "Exception(f\"invalid priority: {raw!r}\")` (catch the specific "
            "error, then `raise` a plain `Exception` with a clearer "
            "message).\n"
            "- `parse_priority_with_default(raw: str, default: int = 0) -> int` "
            "-- `try: return int(raw)` `except ValueError: return default` "
            "`finally:` increment the module-level `_parse_attempts` "
            "counter -- `finally` runs whether or not the `except` fired, "
            "which is exactly why it's the right place to count *every* "
            "attempt.\n"
            "- `get_parse_attempts() -> int` -- read `_parse_attempts`.\n\n"
            "See the Study Reference presentation, Topic 5 (Basic tier), "
            "for the theory."
        ),
        "stub": '''\
import re


def extract_ticket_ids(text: str) -> list[str]:
    r"""re.findall(r"TICKET-\d+", text)."""
    raise NotImplementedError


def contains_urgent_flag(text: str) -> bool:
    r"""re.search(r"\bURGENT\b", text) is not None."""
    raise NotImplementedError


def clean_ticket_text(text: str) -> str:
    r"""re.sub(r"\s+", " ", text).strip()."""
    raise NotImplementedError


def looks_like_ticket_id(text: str) -> bool:
    r"""re.match(r"TICKET-\d+$", text) is not None -- the WHOLE text must be one ticket id."""
    raise NotImplementedError


def parse_priority(raw: str) -> int:
    """int(raw); on ValueError, raise a plain Exception with a clearer message."""
    raise NotImplementedError


_parse_attempts = 0


def parse_priority_with_default(raw: str, default: int = 0) -> int:
    """int(raw), or default on ValueError; always count the attempt in finally."""
    raise NotImplementedError


def get_parse_attempts() -> int:
    """Return _parse_attempts."""
    raise NotImplementedError
''',
        "reference": '''\
import re


def extract_ticket_ids(text: str) -> list[str]:
    return re.findall(r"TICKET-\\d+", text)


def contains_urgent_flag(text: str) -> bool:
    return re.search(r"\\bURGENT\\b", text) is not None


def clean_ticket_text(text: str) -> str:
    return re.sub(r"\\s+", " ", text).strip()


def looks_like_ticket_id(text: str) -> bool:
    return re.match(r"TICKET-\\d+$", text) is not None


def parse_priority(raw: str) -> int:
    try:
        return int(raw)
    except ValueError:
        raise Exception(f"invalid priority: {raw!r}")


_parse_attempts = 0


def parse_priority_with_default(raw: str, default: int = 0) -> int:
    global _parse_attempts
    try:
        return int(raw)
    except ValueError:
        return default
    finally:
        _parse_attempts += 1


def get_parse_attempts() -> int:
    return _parse_attempts
''',
        "test": '''\
import pytest
from exercises.stage05.basic02.solution import (
    extract_ticket_ids,
    contains_urgent_flag,
    clean_ticket_text,
    looks_like_ticket_id,
    parse_priority,
    parse_priority_with_default,
    get_parse_attempts,
)

TEXT = "TICKET-101 is URGENT, also TICKET-202 reported.  Please   check."


def test_extract_ticket_ids():
    r"""extract_ticket_ids == re.findall(r"TICKET-\d+", text)."""
    assert extract_ticket_ids(TEXT) == ["TICKET-101", "TICKET-202"]


def test_contains_urgent_flag():
    r"""contains_urgent_flag uses re.search with a \bURGENT\b word-boundary pattern."""
    assert contains_urgent_flag(TEXT) is True
    assert contains_urgent_flag("nothing to see here") is False


def test_clean_ticket_text_collapses_whitespace():
    r"""clean_ticket_text uses re.sub(r"\s+", " ", text).strip()."""
    assert clean_ticket_text(TEXT) == (
        "TICKET-101 is URGENT, also TICKET-202 reported. Please check."
    )


def test_looks_like_ticket_id_requires_whole_string_match():
    """looks_like_ticket_id must anchor at both start (re.match) and end ($) -- only a bare ticket id matches."""
    assert looks_like_ticket_id("TICKET-101") is True
    assert looks_like_ticket_id("TICKET-101 is URGENT") is False


def test_parse_priority_raises_plain_exception():
    """parse_priority catches ValueError and re-raises as a plain Exception with a clearer message."""
    assert parse_priority("5") == 5
    with pytest.raises(Exception):
        parse_priority("abc")


def test_parse_priority_with_default_and_finally_counts_every_attempt():
    """parse_priority_with_default falls back to default on ValueError, and finally must count BOTH the success and the failure."""
    _ = get_parse_attempts()
    parse_priority_with_default("abc", default=3)
    after_failure = get_parse_attempts()
    parse_priority_with_default("7", default=3)
    after_success = get_parse_attempts()
    assert after_success == after_failure + 1
    assert parse_priority_with_default("abc", default=3) == 3
    assert parse_priority_with_default("7", default=3) == 7
''',
    },
    {
        "name": "mid01",
        "title": "Order Validation Pipeline",
        "summary": "exception hierarchies, exception chaining (raise ... from ...)",
        "readme": (
            "Implement a small order-processing pipeline with a two-level "
            "custom exception hierarchy:\n\n"
            "```python\n"
            "class OrderError(Exception): pass\n"
            "class OrderValidationError(OrderError): pass  # bad input\n"
            "class OrderProcessingError(OrderError): pass  # bad business state\n"
            "```\n\n"
            "Implement:\n\n"
            "- `parse_order_quantity(raw: str) -> int` -- `try: qty = "
            "int(raw)` `except ValueError as e: raise "
            "OrderValidationError(f\"invalid quantity: {raw!r}\") from e` "
            "(chained -- there's a real underlying `ValueError` to point "
            "to). Then, separately, if `qty <= 0`: `raise "
            "OrderValidationError(f\"quantity must be positive: {qty}\")` "
            "(no `from` here -- this isn't wrapping another exception, it's "
            "a fresh validation failure). Otherwise return `qty`.\n"
            "- `apply_bulk_discount(quantity: int, discount_pct_raw: str) -> float` "
            "-- `try: pct = float(discount_pct_raw)` `except ValueError as "
            "e: raise OrderProcessingError(f\"invalid discount: "
            "{discount_pct_raw!r}\") from e`. Then if `not (0 <= pct <= "
            "100)`: `raise OrderProcessingError(f\"discount out of range: "
            "{pct}\") from None` -- `from None` **explicitly suppresses** "
            "chaining (there's no underlying exception here, just an "
            "out-of-range value). Otherwise return "
            "`quantity * (1 - pct / 100)`.\n"
            "- `fulfill_order(quantity: int, stock: int) -> int` -- if "
            "`quantity > stock`: `raise OrderProcessingError(f\"insufficient "
            "stock: need {quantity}, have {stock}\")`; otherwise return "
            "`stock - quantity`.\n\n"
            "The chained exception is available afterward as "
            "`exc.__cause__` (`None` when `from None` was used) -- that's "
            "what the tests check, along with `OrderValidationError`/"
            "`OrderProcessingError` both being `OrderError` subclasses.\n\n"
            "See the Study Reference presentation, Topic 5 (Mid tier), for "
            "the theory."
        ),
        "stub": '''\
class OrderError(Exception):
    pass


class OrderValidationError(OrderError):
    pass


class OrderProcessingError(OrderError):
    pass


def parse_order_quantity(raw: str) -> int:
    """int(raw) (chain ValueError via `from e`); then validate qty > 0 (raise directly, no chain)."""
    raise NotImplementedError


def apply_bulk_discount(quantity: int, discount_pct_raw: str) -> float:
    """float(discount_pct_raw) (chain ValueError via `from e`); validate 0..100 (raise ... from None if not)."""
    raise NotImplementedError


def fulfill_order(quantity: int, stock: int) -> int:
    """stock - quantity, or raise OrderProcessingError if quantity > stock."""
    raise NotImplementedError
''',
        "reference": '''\
class OrderError(Exception):
    pass


class OrderValidationError(OrderError):
    pass


class OrderProcessingError(OrderError):
    pass


def parse_order_quantity(raw: str) -> int:
    try:
        qty = int(raw)
    except ValueError as e:
        raise OrderValidationError(f"invalid quantity: {raw!r}") from e
    if qty <= 0:
        raise OrderValidationError(f"quantity must be positive: {qty}")
    return qty


def apply_bulk_discount(quantity: int, discount_pct_raw: str) -> float:
    try:
        pct = float(discount_pct_raw)
    except ValueError as e:
        raise OrderProcessingError(f"invalid discount: {discount_pct_raw!r}") from e
    if not (0 <= pct <= 100):
        raise OrderProcessingError(f"discount out of range: {pct}") from None
    return quantity * (1 - pct / 100)


def fulfill_order(quantity: int, stock: int) -> int:
    if quantity > stock:
        raise OrderProcessingError(f"insufficient stock: need {quantity}, have {stock}")
    return stock - quantity
''',
        "test": '''\
import pytest
from exercises.stage05.mid01.solution import (
    OrderError,
    OrderValidationError,
    OrderProcessingError,
    parse_order_quantity,
    apply_bulk_discount,
    fulfill_order,
)


def test_hierarchy():
    """OrderValidationError and OrderProcessingError must both be OrderError, which must be an Exception."""
    assert issubclass(OrderValidationError, OrderError)
    assert issubclass(OrderProcessingError, OrderError)
    assert issubclass(OrderError, Exception)


def test_parse_order_quantity_valid():
    """parse_order_quantity("5") == 5."""
    assert parse_order_quantity("5") == 5


def test_parse_order_quantity_chains_value_error():
    """A non-numeric quantity chains the underlying ValueError via `from e`."""
    with pytest.raises(OrderValidationError) as exc_info:
        parse_order_quantity("abc")
    assert isinstance(exc_info.value.__cause__, ValueError)


def test_parse_order_quantity_non_positive_does_not_chain():
    """A non-positive quantity is a fresh validation failure -- no `from`, so __cause__ is None."""
    with pytest.raises(OrderValidationError) as exc_info:
        parse_order_quantity("-3")
    assert exc_info.value.__cause__ is None


def test_apply_bulk_discount_valid():
    """apply_bulk_discount(10, "20") == 10 * (1 - 0.2)."""
    assert apply_bulk_discount(10, "20") == pytest.approx(8.0)


def test_apply_bulk_discount_chains_value_error():
    """A non-numeric discount chains the underlying ValueError via `from e`."""
    with pytest.raises(OrderProcessingError) as exc_info:
        apply_bulk_discount(10, "abc")
    assert isinstance(exc_info.value.__cause__, ValueError)


def test_apply_bulk_discount_out_of_range_suppresses_chaining():
    """An out-of-range discount uses `from None` -- __cause__ must be None."""
    with pytest.raises(OrderProcessingError) as exc_info:
        apply_bulk_discount(10, "150")
    assert exc_info.value.__cause__ is None


def test_fulfill_order():
    """fulfill_order returns stock - quantity, or raises OrderProcessingError if quantity exceeds stock."""
    assert fulfill_order(3, 10) == 7
    with pytest.raises(OrderProcessingError):
        fulfill_order(20, 10)
''',
    },
    {
        "name": "mid02",
        "title": "Config and Log Parsers",
        "summary": "re.compile(), regex named groups",
        "readme": (
            "Three module-level **compiled** patterns (`re.compile(...)`), "
            "each with **named groups** (`(?P<name>...)`), each paired with "
            "a parser that returns `match.groupdict()`:\n\n"
            "```python\n"
            'LINE_PATTERN = re.compile(r"(?P<key>\\w+)=(?P<value>.+)")\n'
            'DATE_PATTERN = re.compile(r"(?P<year>\\d{4})-(?P<month>\\d{2})-(?P<day>\\d{2})")\n'
            'LOG_PATTERN = re.compile(r"(?P<level>\\w+): (?P<message>.+)")\n'
            "```\n\n"
            "Compiling once at module level (instead of calling "
            "`re.match`/`re.search` with a raw pattern string every time) "
            "is the idiomatic move for a pattern you'll reuse across many "
            "calls.\n\n"
            "Implement:\n\n"
            "- `parse_config_line(line: str) -> dict` -- "
            "`LINE_PATTERN.match(line)`; if it's `None`, `raise "
            "ValueError(...)`; otherwise return `match.groupdict()` "
            "(`{\"key\": ..., \"value\": ...}`).\n"
            "- `find_date(text: str) -> dict` -- `DATE_PATTERN.search(text)` "
            "(search anywhere in `text`, not just at the start); `raise "
            "ValueError(...)` if none found; otherwise "
            "`match.groupdict()` (`{\"year\": ..., \"month\": ..., "
            "\"day\": ...}`).\n"
            "- `parse_log_entry(line: str) -> dict` -- `LOG_PATTERN.match(line)`; "
            "`raise ValueError(...)` if it doesn't match; otherwise "
            "`match.groupdict()` (`{\"level\": ..., \"message\": ...}`).\n\n"
            "Named groups turn `match.group(1)`, `match.group(2)`, ... into "
            "self-documenting keys in `match.groupdict()` -- much easier to "
            "read (and to keep correct after editing the pattern) than "
            "counting parentheses.\n\n"
            "See the Study Reference presentation, Topic 5 (Mid tier), for "
            "the theory."
        ),
        "stub": '''\
import re

LINE_PATTERN = re.compile(r"(?P<key>\\w+)=(?P<value>.+)")
DATE_PATTERN = re.compile(r"(?P<year>\\d{4})-(?P<month>\\d{2})-(?P<day>\\d{2})")
LOG_PATTERN = re.compile(r"(?P<level>\\w+): (?P<message>.+)")


def parse_config_line(line: str) -> dict:
    """LINE_PATTERN.match(line).groupdict(); ValueError if no match."""
    raise NotImplementedError


def find_date(text: str) -> dict:
    """DATE_PATTERN.search(text).groupdict(); ValueError if none found."""
    raise NotImplementedError


def parse_log_entry(line: str) -> dict:
    """LOG_PATTERN.match(line).groupdict(); ValueError if no match."""
    raise NotImplementedError
''',
        "reference": '''\
import re

LINE_PATTERN = re.compile(r"(?P<key>\\w+)=(?P<value>.+)")
DATE_PATTERN = re.compile(r"(?P<year>\\d{4})-(?P<month>\\d{2})-(?P<day>\\d{2})")
LOG_PATTERN = re.compile(r"(?P<level>\\w+): (?P<message>.+)")


def parse_config_line(line: str) -> dict:
    match = LINE_PATTERN.match(line)
    if match is None:
        raise ValueError(f"unparseable config line: {line!r}")
    return match.groupdict()


def find_date(text: str) -> dict:
    match = DATE_PATTERN.search(text)
    if match is None:
        raise ValueError(f"no date found in: {text!r}")
    return match.groupdict()


def parse_log_entry(line: str) -> dict:
    match = LOG_PATTERN.match(line)
    if match is None:
        raise ValueError(f"unparseable log entry: {line!r}")
    return match.groupdict()
''',
        "test": '''\
import pytest
from exercises.stage05.mid02.solution import parse_config_line, find_date, parse_log_entry


def test_parse_config_line_uses_compiled_pattern_and_named_groups():
    """parse_config_line matches LINE_PATTERN (a compiled, named-group pattern) and returns groupdict()."""
    assert parse_config_line("host=localhost") == {"key": "host", "value": "localhost"}


def test_parse_config_line_invalid_raises():
    """No match against LINE_PATTERN must raise ValueError."""
    with pytest.raises(ValueError):
        parse_config_line("not-key-value")


def test_find_date_searches_anywhere_in_text():
    """find_date uses DATE_PATTERN.search (not .match), so it finds a date anywhere in the text."""
    result = find_date("event happened on 2024-03-15 in the evening")
    assert result == {"year": "2024", "month": "03", "day": "15"}


def test_find_date_none_found_raises():
    """No date found must raise ValueError."""
    with pytest.raises(ValueError):
        find_date("no date here")


def test_parse_log_entry_uses_compiled_pattern_and_named_groups():
    """parse_log_entry matches LOG_PATTERN and returns its groupdict()."""
    assert parse_log_entry("ERROR: disk full") == {"level": "ERROR", "message": "disk full"}


def test_parse_log_entry_invalid_raises():
    """No match against LOG_PATTERN must raise ValueError."""
    with pytest.raises(ValueError):
        parse_log_entry("not a log line")
''',
    },
    {
        "name": "advanced01",
        "title": "Class-Based Context Managers",
        "summary": "__enter__/__exit__",
        "readme": (
            "Implement three class-based context managers:\n\n"
            "- `Timer` -- `__enter__` records `self._start = time.time()` "
            "and returns `self`; `__exit__` sets `self.elapsed = "
            "time.time() - self._start` and returns `False` (never "
            "suppress an exception).\n"
            "- `SuppressErrors` -- `__init__(self, exc_type)` stores it; "
            "`__enter__` returns `None`; `__exit__(self, exc_type, "
            "exc_val, exc_tb)` returns `True` (suppress) only if an "
            "exception occurred **and** it's a subclass of the stored "
            "type, else `False` (let it propagate).\n"
            "- `FileLineCounter` -- `__init__(self, path)` stores it; "
            "`__enter__` opens the file and returns the file object; "
            "`__exit__` closes it and returns `False`. This is roughly "
            "what `with open(...) as f:` does under the hood.\n\n"
            "A class-based context manager's `__exit__` receives "
            "`(exc_type, exc_val, exc_tb)` describing any exception that "
            "happened inside the `with` block (all `None` if nothing went "
            "wrong) -- returning a truthy value from `__exit__` is what "
            "swallows that exception instead of letting it propagate.\n\n"
            "See the Study Reference presentation, Topic 5 (Advanced "
            "tier), for the theory."
        ),
        "stub": '''\
import time


class Timer:
    def __enter__(self):
        """Record self._start = time.time(); return self."""
        raise NotImplementedError

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Set self.elapsed = time.time() - self._start; return False."""
        raise NotImplementedError


class SuppressErrors:
    def __init__(self, exc_type):
        self.exc_type = exc_type

    def __enter__(self):
        raise NotImplementedError

    def __exit__(self, exc_type, exc_val, exc_tb):
        """True (suppress) if exc_type is a subclass of self.exc_type, else False."""
        raise NotImplementedError


class FileLineCounter:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        """Open self.path and return the file object."""
        raise NotImplementedError

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close the file; return False."""
        raise NotImplementedError
''',
        "reference": '''\
import time


class Timer:
    def __enter__(self):
        self._start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.time() - self._start
        return False


class SuppressErrors:
    def __init__(self, exc_type):
        self.exc_type = exc_type

    def __enter__(self):
        return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        return exc_type is not None and issubclass(exc_type, self.exc_type)


class FileLineCounter:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self._f = open(self.path)
        return self._f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._f.close()
        return False
''',
        "test": '''\
import pytest
from exercises.stage05.advanced01.solution import Timer, SuppressErrors, FileLineCounter


def test_timer_records_elapsed():
    """Timer.__enter__ returns self and records _start; __exit__ sets .elapsed."""
    with Timer() as t:
        pass
    assert hasattr(t, "elapsed")
    assert t.elapsed >= 0


def test_suppress_errors_suppresses_matching_type():
    """SuppressErrors.__exit__ returns True for a matching exception type, so it must not propagate."""
    with SuppressErrors(ValueError):
        raise ValueError("boom")


def test_suppress_errors_lets_other_types_propagate():
    """SuppressErrors.__exit__ returns False for a non-matching type, so it must propagate."""
    with pytest.raises(TypeError):
        with SuppressErrors(ValueError):
            raise TypeError("nope")


def test_file_line_counter(tmp_path):
    """FileLineCounter.__enter__ opens and returns the file object; __exit__ closes it."""
    path = tmp_path / "data.txt"
    path.write_text("a\\nb\\nc\\n")
    with FileLineCounter(str(path)) as f:
        lines = f.read().splitlines()
    assert lines == ["a", "b", "c"]
''',
    },
    {
        "name": "advanced02",
        "title": "Generator-Based Context Managers",
        "summary": "@contextlib.contextmanager",
        "readme": (
            "Implement three `@contextlib.contextmanager`-decorated "
            "generator functions -- the lighter-weight alternative to "
            "writing a full `__enter__`/`__exit__` class:\n\n"
            "- `temporary_value(obj, attr, value)` -- save "
            "`getattr(obj, attr)`, `setattr(obj, attr, value)`, `yield`, "
            "then in a `finally:` restore the original value -- even if "
            "the `with`-block raised.\n"
            "- `suppress_and_log(log: list, *exc_types)` -- `try: yield` "
            "`except exc_types as e: log.append(str(e))` (swallows a "
            "matching exception, recording it instead of letting it "
            "propagate).\n"
            "- `timing_block(results: list)` -- record `time.time()` "
            "before `yield`; in a `finally:`, "
            "`results.append(time.time() - start)`.\n\n"
            "Everything before the `yield` runs as `__enter__`; everything "
            "after (particularly inside a `finally:`) runs as `__exit__` "
            "-- a `try`/`finally` wrapped around a single `yield` is how "
            "`@contextlib.contextmanager` turns an ordinary generator "
            "function into a context manager, without writing a class at "
            "all.\n\n"
            "See the Study Reference presentation, Topic 5 (Advanced "
            "tier), for the theory."
        ),
        "stub": '''\
import contextlib
import time


@contextlib.contextmanager
def temporary_value(obj, attr, value):
    """Temporarily set obj.attr to value, restoring the original in a finally."""
    raise NotImplementedError


@contextlib.contextmanager
def suppress_and_log(log: list, *exc_types):
    """Swallow a matching exception, appending str(e) to log instead of propagating."""
    raise NotImplementedError


@contextlib.contextmanager
def timing_block(results: list):
    """Append the elapsed seconds of the with-block to results, via finally."""
    raise NotImplementedError
''',
        "reference": '''\
import contextlib
import time


@contextlib.contextmanager
def temporary_value(obj, attr, value):
    original = getattr(obj, attr)
    setattr(obj, attr, value)
    try:
        yield
    finally:
        setattr(obj, attr, original)


@contextlib.contextmanager
def suppress_and_log(log: list, *exc_types):
    try:
        yield
    except exc_types as e:
        log.append(str(e))


@contextlib.contextmanager
def timing_block(results: list):
    start = time.time()
    try:
        yield
    finally:
        results.append(time.time() - start)
''',
        "test": '''\
import pytest
from exercises.stage05.advanced02.solution import temporary_value, suppress_and_log, timing_block


class _Config:
    debug = False


def test_temporary_value_restores_after_block():
    """temporary_value sets obj.attr for the duration of the with-block, then restores the original."""
    cfg = _Config()
    with temporary_value(cfg, "debug", True):
        assert cfg.debug is True
    assert cfg.debug is False


def test_temporary_value_restores_even_on_exception():
    """The finally inside temporary_value must restore the original value even when the with-block raises."""
    # ValueError, not RuntimeError: NotImplementedError (what an unfinished
    # stub raises) is itself a RuntimeError subclass, so a RuntimeError here
    # would let pytest.raises(RuntimeError) accidentally match an
    # unimplemented temporary_value() instead of only a correct one.
    cfg = _Config()
    with pytest.raises(ValueError):
        with temporary_value(cfg, "debug", True):
            raise ValueError("boom")
    assert cfg.debug is False


def test_suppress_and_log():
    """suppress_and_log catches a matching exception and records str(e) instead of propagating."""
    log = []
    with suppress_and_log(log, ValueError):
        raise ValueError("bad input")
    assert log == ["bad input"]


def test_timing_block():
    """timing_block appends one elapsed-seconds entry via its finally block."""
    results = []
    with timing_block(results):
        pass
    assert len(results) == 1
    assert results[0] >= 0
''',
    },
]
