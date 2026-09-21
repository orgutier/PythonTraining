"""
Week 5 -- Files, Exceptions, Regex.

Coverage plan (each item exercised by the trainee's own code >=3 times):
  keywords: open(), with, as, try, except, finally, raise, Exception,
            re.search(), re.findall(), re.compile()
  dunders:  __enter__, __exit__
  modules:  re, contextlib
  methods:  re.match(), re.sub(), contextlib.contextmanager
  concepts: exception chaining (raise ... from ...), exception hierarchies,
            custom context managers, regex named groups
"""

WEEK = "week05"
TOPIC = "Files, Exceptions, Regex"
OVERVIEW = (
    "Six exercises covering file I/O, the full try/except/finally/raise "
    "toolkit (including exception chaining and custom hierarchies), every "
    "common re function, and both ways to write a context manager -- a "
    "class with __enter__/__exit__, and @contextlib.contextmanager."
)

EXERCISES = [
    {
        "name": "exercise01",
        "title": "File Basics",
        "summary": "open(), with, as -- x3 each",
        "readme": (
            "Implement four small file-handling functions, each using "
            "`with open(...) as f:` (never a bare `open()`/`close()` pair):\n\n"
            "- `write_lines(path: str, lines: list[str]) -> None` -- open "
            "`path` for writing (`\"w\"`), write each line followed by `\"\\n\"`.\n"
            "- `read_lines(path: str) -> list[str]` -- open `path` for reading, "
            "return `f.read().splitlines()`.\n"
            "- `append_line(path: str, line: str) -> None` -- open `path` for "
            "appending (`\"a\"`), write `line + \"\\n\"`.\n"
            "- `count_lines(path: str) -> int` -- open `path` for reading, "
            "return how many lines it has.\n\n"
            "See the Study Reference presentation, Topic 5, for the theory."
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
from exercises.week05.exercise01.solution import (
    write_lines,
    read_lines,
    append_line,
    count_lines,
)


def test_write_and_read_lines(tmp_path):
    path = str(tmp_path / "data.txt")
    write_lines(path, ["a", "b", "c"])
    assert read_lines(path) == ["a", "b", "c"]


def test_append_line(tmp_path):
    path = str(tmp_path / "data.txt")
    write_lines(path, ["a"])
    append_line(path, "b")
    assert read_lines(path) == ["a", "b"]


def test_count_lines(tmp_path):
    path = str(tmp_path / "data.txt")
    write_lines(path, ["a", "b", "c", "d"])
    assert count_lines(path) == 4
''',
    },
    {
        "name": "exercise02",
        "title": "Exceptions and Hierarchies",
        "summary": "try, except, finally, raise, Exception, exception hierarchies",
        "readme": (
            "Implement:\n\n"
            "- `ValidationError(Exception)` -- an empty custom exception class "
            "(`class ValidationError(Exception): pass`).\n"
            "- `NegativeValueError(ValidationError)` -- another empty class, "
            "this time subclassing `ValidationError` (not `Exception` "
            "directly) -- a two-level hierarchy: `NegativeValueError` **is a** "
            "`ValidationError` **is a** `Exception`.\n"
            "- `validate_positive(n: int) -> int` -- return `n` if `n >= 0`, "
            "else `raise NegativeValueError(f\"negative value: {n}\")`.\n"
            "- `safe_parse_int(s: str)` -- `try: return int(s)` `except "
            "ValueError: return None`.\n"
            "- `divide_with_cleanup(a: float, b: float) -> float` -- "
            "`try: return a / b` `except ZeroDivisionError: raise` (re-raise "
            "unchanged) `finally:` increment the module-level `_attempts` "
            "counter -- `finally` runs whether or not an exception occurred, "
            "which is exactly why it's the right place to count *every* "
            "attempt, successful or not.\n"
            "- `get_attempts() -> int` / `reset_attempts() -> None` -- read/"
            "reset `_attempts`.\n\n"
            "See the Study Reference presentation, Topic 5, for the theory."
        ),
        "stub": '''\
class ValidationError(Exception):
    pass


class NegativeValueError(ValidationError):
    pass


def validate_positive(n: int) -> int:
    """Return n if n >= 0, else raise NegativeValueError."""
    raise NotImplementedError


def safe_parse_int(s: str):
    """int(s), or None if that raises ValueError."""
    raise NotImplementedError


_attempts = 0


def divide_with_cleanup(a: float, b: float) -> float:
    """a / b; re-raise ZeroDivisionError unchanged; always count the attempt in finally."""
    raise NotImplementedError


def get_attempts() -> int:
    raise NotImplementedError


def reset_attempts() -> None:
    raise NotImplementedError
''',
        "reference": '''\
class ValidationError(Exception):
    pass


class NegativeValueError(ValidationError):
    pass


def validate_positive(n: int) -> int:
    if n < 0:
        raise NegativeValueError(f"negative value: {n}")
    return n


def safe_parse_int(s: str):
    try:
        return int(s)
    except ValueError:
        return None


_attempts = 0


def divide_with_cleanup(a: float, b: float) -> float:
    global _attempts
    try:
        return a / b
    except ZeroDivisionError:
        raise
    finally:
        _attempts += 1


def get_attempts() -> int:
    return _attempts


def reset_attempts() -> None:
    global _attempts
    _attempts = 0
''',
        "test": '''\
import pytest
from exercises.week05.exercise02.solution import (
    ValidationError,
    NegativeValueError,
    validate_positive,
    safe_parse_int,
    divide_with_cleanup,
    get_attempts,
    reset_attempts,
)


def test_validate_positive_passthrough():
    assert validate_positive(5) == 5


def test_validate_positive_raises_negative_value_error():
    with pytest.raises(NegativeValueError):
        validate_positive(-1)


def test_negative_value_error_is_a_validation_error():
    assert issubclass(NegativeValueError, ValidationError)
    assert issubclass(ValidationError, Exception)


def test_safe_parse_int_valid():
    assert safe_parse_int("42") == 42


def test_safe_parse_int_invalid():
    assert safe_parse_int("nope") is None


def test_divide_with_cleanup_success():
    reset_attempts()
    assert divide_with_cleanup(10, 2) == 5.0
    assert get_attempts() == 1


def test_divide_with_cleanup_counts_failed_attempts_too():
    reset_attempts()
    with pytest.raises(ZeroDivisionError):
        divide_with_cleanup(10, 0)
    assert get_attempts() == 1
''',
    },
    {
        "name": "exercise03",
        "title": "Exception Chaining",
        "summary": "raise ... from ... x3",
        "readme": (
            "Implement three functions that catch a low-level exception and "
            "re-raise a higher-level, more meaningful one **chained** to it "
            "with `raise ... from ...`:\n\n"
            "- `ConfigError(Exception)` / `ConfigParseError(ConfigError)` -- "
            "`load_config_value(raw: str) -> int`: `try: return int(raw)` "
            "`except ValueError as e: raise ConfigParseError(f\"bad config "
            "value: {raw!r}\") from e`.\n"
            "- `NetworkError(Exception)` / `RetryError(Exception)` -- "
            "`fetch_with_retry_simulation(should_fail: bool) -> str`: if "
            "`should_fail`, `raise NetworkError(\"connection refused\")`; catch "
            "that and `raise RetryError(\"failed after retries\") from e`; if "
            "`should_fail` is `False`, just `return \"ok\"`.\n"
            "- `ScoreError(Exception)` -- `parse_score(raw: str) -> int`: parse "
            "`raw` as `int`; on `ValueError as e`, `raise ScoreError(f\"invalid "
            "score: {raw!r}\") from e`. Then if the parsed score isn't in "
            "`0..100`, `raise ScoreError(f\"score out of range: {score}\") "
            "from None` -- `from None` **explicitly suppresses** chaining "
            "(there's no underlying exception to chain to here, just a "
            "validation failure), which is the other legal form of this "
            "syntax.\n\n"
            "The chained exception is available afterward as "
            "`exc.__cause__` -- that's what the tests check.\n\n"
            "See the Study Reference presentation, Topic 5, for the theory."
        ),
        "stub": '''\
class ConfigError(Exception):
    pass


class ConfigParseError(ConfigError):
    pass


def load_config_value(raw: str) -> int:
    """int(raw); on ValueError, raise ConfigParseError(...) from e."""
    raise NotImplementedError


class NetworkError(Exception):
    pass


class RetryError(Exception):
    pass


def fetch_with_retry_simulation(should_fail: bool) -> str:
    """"ok" normally; if should_fail, raise NetworkError, catch it, raise RetryError(...) from e."""
    raise NotImplementedError


class ScoreError(Exception):
    pass


def parse_score(raw: str) -> int:
    """int(raw) (chain ValueError via `from e`); validate 0..100 (raise ... from None if not)."""
    raise NotImplementedError
''',
        "reference": '''\
class ConfigError(Exception):
    pass


class ConfigParseError(ConfigError):
    pass


def load_config_value(raw: str) -> int:
    try:
        return int(raw)
    except ValueError as e:
        raise ConfigParseError(f"bad config value: {raw!r}") from e


class NetworkError(Exception):
    pass


class RetryError(Exception):
    pass


def fetch_with_retry_simulation(should_fail: bool) -> str:
    try:
        if should_fail:
            raise NetworkError("connection refused")
        return "ok"
    except NetworkError as e:
        raise RetryError("failed after retries") from e


class ScoreError(Exception):
    pass


def parse_score(raw: str) -> int:
    try:
        score = int(raw)
    except ValueError as e:
        raise ScoreError(f"invalid score: {raw!r}") from e
    if not (0 <= score <= 100):
        raise ScoreError(f"score out of range: {score}") from None
    return score
''',
        "test": '''\
import pytest
from exercises.week05.exercise03.solution import (
    ConfigError,
    ConfigParseError,
    load_config_value,
    NetworkError,
    RetryError,
    fetch_with_retry_simulation,
    ScoreError,
    parse_score,
)


def test_load_config_value_valid():
    assert load_config_value("42") == 42


def test_load_config_value_chains_value_error():
    with pytest.raises(ConfigParseError) as exc_info:
        load_config_value("abc")
    assert isinstance(exc_info.value.__cause__, ValueError)
    assert isinstance(exc_info.value, ConfigError)


def test_fetch_with_retry_simulation_success():
    assert fetch_with_retry_simulation(False) == "ok"


def test_fetch_with_retry_simulation_chains_network_error():
    with pytest.raises(RetryError) as exc_info:
        fetch_with_retry_simulation(True)
    assert isinstance(exc_info.value.__cause__, NetworkError)


def test_parse_score_valid():
    assert parse_score("85") == 85


def test_parse_score_chains_value_error():
    with pytest.raises(ScoreError) as exc_info:
        parse_score("abc")
    assert isinstance(exc_info.value.__cause__, ValueError)


def test_parse_score_out_of_range_suppresses_chaining():
    with pytest.raises(ScoreError) as exc_info:
        parse_score("150")
    assert exc_info.value.__cause__ is None
''',
    },
    {
        "name": "exercise04",
        "title": "Regex Basics",
        "summary": "re.search(), re.findall(), re.match(), re.sub(), re.compile()",
        "readme": (
            "Implement:\n\n"
            "- `contains_digit(text: str) -> bool` -- "
            "`re.search(r\"\\d\", text) is not None`.\n"
            "- `find_all_numbers(text: str) -> list[str]` -- "
            "`re.findall(r\"\\d+\", text)`.\n"
            "- `starts_with_word(text: str, word: str) -> bool` -- "
            "`re.match(re.escape(word), text) is not None` (`re.match` only "
            "anchors at the *start* of the string, unlike `re.search`).\n"
            "- `normalize_whitespace(text: str) -> str` -- "
            "`re.sub(r\"\\s+\", \" \", text).strip()` (collapse runs of "
            "whitespace to a single space).\n"
            "- `EMAIL_PATTERN` (module level) -- "
            "`re.compile(r\"[\\w.+-]+@[\\w-]+\\.[\\w.-]+\")`, and "
            "`extract_emails(text: str) -> list[str]` -- `EMAIL_PATTERN.findall(text)`. "
            "Compiling once at module level (instead of calling `re.search`/`re.findall` "
            "with a raw string every time) is the idiomatic move when a pattern is reused.\n\n"
            "See the Study Reference presentation, Topic 5, for the theory."
        ),
        "stub": '''\
import re

EMAIL_PATTERN = re.compile(r"[\\w.+-]+@[\\w-]+\\.[\\w.-]+")


def contains_digit(text: str) -> bool:
    """re.search(r"\\d", text) is not None."""
    raise NotImplementedError


def find_all_numbers(text: str) -> list[str]:
    """re.findall(r"\\d+", text)."""
    raise NotImplementedError


def starts_with_word(text: str, word: str) -> bool:
    """re.match(re.escape(word), text) is not None."""
    raise NotImplementedError


def normalize_whitespace(text: str) -> str:
    """re.sub(r"\\s+", " ", text).strip()."""
    raise NotImplementedError


def extract_emails(text: str) -> list[str]:
    """EMAIL_PATTERN.findall(text)."""
    raise NotImplementedError
''',
        "reference": '''\
import re

EMAIL_PATTERN = re.compile(r"[\\w.+-]+@[\\w-]+\\.[\\w.-]+")


def contains_digit(text: str) -> bool:
    return re.search(r"\\d", text) is not None


def find_all_numbers(text: str) -> list[str]:
    return re.findall(r"\\d+", text)


def starts_with_word(text: str, word: str) -> bool:
    return re.match(re.escape(word), text) is not None


def normalize_whitespace(text: str) -> str:
    return re.sub(r"\\s+", " ", text).strip()


def extract_emails(text: str) -> list[str]:
    return EMAIL_PATTERN.findall(text)
''',
        "test": '''\
from exercises.week05.exercise04.solution import (
    contains_digit,
    find_all_numbers,
    starts_with_word,
    normalize_whitespace,
    extract_emails,
)


def test_contains_digit():
    assert contains_digit("room 42") is True
    assert contains_digit("no numbers here") is False


def test_find_all_numbers():
    assert find_all_numbers("a1 b22 c333") == ["1", "22", "333"]


def test_starts_with_word():
    assert starts_with_word("hello world", "hello") is True
    assert starts_with_word("say hello", "hello") is False


def test_normalize_whitespace():
    assert normalize_whitespace("a   b\\t\\tc\\n\\nd") == "a b c d"


def test_extract_emails():
    text = "contact ada@example.com or grace@nav.mil for details"
    assert extract_emails(text) == ["ada@example.com", "grace@nav.mil"]
''',
    },
    {
        "name": "exercise05",
        "title": "Regex Named Groups",
        "summary": "regex named groups x3",
        "readme": (
            "Implement three parsers, each using `re` **named groups** "
            "(`(?P<name>...)`) and returning `match.groupdict()`:\n\n"
            "- `parse_log_line(line: str) -> dict` -- parse `\"LEVEL: message\"` "
            "(e.g. `\"ERROR: disk full\"`) with "
            "`re.match(r\"(?P<level>\\w+): (?P<message>.+)\", line)`. Raise "
            "`ValueError` if it doesn't match.\n"
            "- `parse_date(text: str) -> dict` -- find the first `YYYY-MM-DD` "
            "date anywhere in `text` with `re.search(r\"(?P<year>\\d{4})-"
            "(?P<month>\\d{2})-(?P<day>\\d{2})\", text)`. Raise `ValueError` "
            "if none is found.\n"
            "- `parse_key_value(text: str) -> dict` -- parse `\"key=value\"` "
            "with `re.match(r\"(?P<key>\\w+)=(?P<value>.+)\", text)`. Raise "
            "`ValueError` if it doesn't match.\n\n"
            "Named groups turn `match.group(1)`, `match.group(2)`, ... into "
            "self-documenting keys in `match.groupdict()` -- much easier to "
            "read (and to keep correct after editing the pattern) than "
            "counting parentheses.\n\n"
            "See the Study Reference presentation, Topic 5, for the theory."
        ),
        "stub": '''\
import re


def parse_log_line(line: str) -> dict:
    """{"level": ..., "message": ...} via re.match + named groups; ValueError if no match."""
    raise NotImplementedError


def parse_date(text: str) -> dict:
    """{"year": ..., "month": ..., "day": ...} via re.search + named groups; ValueError if none found."""
    raise NotImplementedError


def parse_key_value(text: str) -> dict:
    """{"key": ..., "value": ...} via re.match + named groups; ValueError if no match."""
    raise NotImplementedError
''',
        "reference": '''\
import re


def parse_log_line(line: str) -> dict:
    match = re.match(r"(?P<level>\\w+): (?P<message>.+)", line)
    if match is None:
        raise ValueError(f"unparseable log line: {line!r}")
    return match.groupdict()


def parse_date(text: str) -> dict:
    match = re.search(r"(?P<year>\\d{4})-(?P<month>\\d{2})-(?P<day>\\d{2})", text)
    if match is None:
        raise ValueError(f"no date found in: {text!r}")
    return match.groupdict()


def parse_key_value(text: str) -> dict:
    match = re.match(r"(?P<key>\\w+)=(?P<value>.+)", text)
    if match is None:
        raise ValueError(f"unparseable key=value: {text!r}")
    return match.groupdict()
''',
        "test": '''\
import pytest
from exercises.week05.exercise05.solution import parse_log_line, parse_date, parse_key_value


def test_parse_log_line():
    assert parse_log_line("ERROR: disk full") == {"level": "ERROR", "message": "disk full"}


def test_parse_log_line_invalid_raises():
    with pytest.raises(ValueError):
        parse_log_line("not a log line")


def test_parse_date():
    result = parse_date("event happened on 2024-03-15 in the evening")
    assert result == {"year": "2024", "month": "03", "day": "15"}


def test_parse_date_none_found_raises():
    with pytest.raises(ValueError):
        parse_date("no date here")


def test_parse_key_value():
    assert parse_key_value("host=localhost") == {"key": "host", "value": "localhost"}


def test_parse_key_value_invalid_raises():
    with pytest.raises(ValueError):
        parse_key_value("not-key-value")
''',
    },
    {
        "name": "exercise06",
        "title": "Context Managers",
        "summary": "__enter__/__exit__ x3, @contextlib.contextmanager x3",
        "readme": (
            "Implement three class-based context managers and three "
            "generator-based ones:\n\n"
            "- `Timer` -- `__enter__` records `self._start = time.time()` and "
            "returns `self`; `__exit__` sets `self.elapsed = time.time() - "
            "self._start` and returns `False` (never suppress).\n"
            "- `SuppressErrors` -- `__init__(self, exc_type)` stores it; "
            "`__enter__` returns `None`; `__exit__(self, exc_type, exc_val, "
            "exc_tb)` returns `True` (suppress) only if an exception occurred "
            "**and** it's an instance of the stored type, else `False`.\n"
            "- `FileLineCounter` -- `__init__(self, path)` stores it; "
            "`__enter__` opens the file and returns the file object; "
            "`__exit__` closes it and returns `False`. This is what `with "
            "open(...) as f:` does under the hood.\n\n"
            "- `temporary_value(obj, attr, value)` (`@contextlib.contextmanager`) "
            "-- save `getattr(obj, attr)`, `setattr(obj, attr, value)`, "
            "`yield`, then in a `finally:` restore the original value -- even "
            "if the with-block raised.\n"
            "- `suppress_and_log(log: list, *exc_types)` -- `try: yield` "
            "`except exc_types as e: log.append(str(e))` (swallows a matching "
            "exception, recording it instead of propagating).\n"
            "- `timing_block(results: list)` -- record `time.time()` before "
            "`yield`; in a `finally:`, `results.append(time.time() - start)`.\n\n"
            "See the Study Reference presentation, Topic 5, for the theory."
        ),
        "stub": '''\
import contextlib
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
        """True (suppress) if exc_type matches self.exc_type, else False."""
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
from exercises.week05.exercise06.solution import (
    Timer,
    SuppressErrors,
    FileLineCounter,
    temporary_value,
    suppress_and_log,
    timing_block,
)


def test_timer_records_elapsed():
    with Timer() as t:
        pass
    assert hasattr(t, "elapsed")
    assert t.elapsed >= 0


def test_suppress_errors_suppresses_matching_type():
    with SuppressErrors(ValueError):
        raise ValueError("boom")


def test_suppress_errors_lets_other_types_propagate():
    with pytest.raises(TypeError):
        with SuppressErrors(ValueError):
            raise TypeError("nope")


def test_file_line_counter(tmp_path):
    path = tmp_path / "data.txt"
    path.write_text("a\\nb\\nc\\n")
    with FileLineCounter(str(path)) as f:
        lines = f.read().splitlines()
    assert lines == ["a", "b", "c"]


class _Config:
    debug = False


def test_temporary_value_restores_after_block():
    cfg = _Config()
    with temporary_value(cfg, "debug", True):
        assert cfg.debug is True
    assert cfg.debug is False


def test_temporary_value_restores_even_on_exception():
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
    log = []
    with suppress_and_log(log, ValueError):
        raise ValueError("bad input")
    assert log == ["bad input"]


def test_timing_block():
    results = []
    with timing_block(results):
        pass
    assert len(results) == 1
    assert results[0] >= 0
''',
    },
]
