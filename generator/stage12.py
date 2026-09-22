"""
Stage 12 -- Requests + Threading.

Coverage plan (each item exercised by the trainee's own code >=3 times):
  keywords: requests.get(), response.json(), threading.Thread, .start(),
            .join(), threading.Lock
  modules:  requests, threading
  methods:  requests.post(), response.raise_for_status(),
            requests.Session(), concurrent.futures.ThreadPoolExecutor
  concepts: sessions & connection reuse, retry/backoff strategies,
            race conditions & deadlocks

Every test mocks requests.get/requests.post/Session methods -- NEVER point
one of these at a live endpoint (see README, "Git hook integration").
"""

STAGE = "stage12"
TOPIC = "Requests + Threading"
OVERVIEW = (
    "Five exercises covering the requests library and Python threading "
    "from Topic 12 at least three times each: basic HTTP calls, sessions "
    "and manual retry/backoff, raw threading.Thread, locks guarding shared "
    "state against race conditions, and ThreadPoolExecutor as the "
    "higher-level alternative to managing threads by hand."
)

EXERCISES = [
    {
        "name": "exercise01",
        "title": "Requests Basics",
        "summary": "requests.get() x3, response.json() x3, requests.post(), raise_for_status()",
        "readme": (
            "Implement:\n\n"
            "- `fetch_json(url: str) -> dict` -- `requests.get(url).json()`.\n"
            "- `fetch_status_code(url: str) -> int` -- "
            "`requests.get(url).status_code`.\n"
            "- `post_data(url: str, payload: dict) -> dict` -- "
            "`requests.post(url, json=payload).json()`.\n"
            "- `fetch_with_raise(url: str) -> dict` -- `r = requests.get(url)`; "
            "`r.raise_for_status()` (raises `requests.HTTPError` for a 4xx/5xx "
            "status instead of silently returning the error body); then "
            "`return r.json()`.\n\n"
            "The tests never touch the network -- they patch `requests.get`/"
            "`requests.post` with a fake response object. **Never** point "
            "one of these functions at a live URL from a test or a git hook; "
            "see the README's \"Git hook integration\" section.\n\n"
            "See the Study Reference presentation, Topic 12, for the theory."
        ),
        "stub": '''\
import requests


def fetch_json(url: str) -> dict:
    """requests.get(url).json()."""
    raise NotImplementedError


def fetch_status_code(url: str) -> int:
    """requests.get(url).status_code."""
    raise NotImplementedError


def post_data(url: str, payload: dict) -> dict:
    """requests.post(url, json=payload).json()."""
    raise NotImplementedError


def fetch_with_raise(url: str) -> dict:
    """requests.get(url), then r.raise_for_status(), then r.json()."""
    raise NotImplementedError
''',
        "reference": '''\
import requests


def fetch_json(url: str) -> dict:
    return requests.get(url).json()


def fetch_status_code(url: str) -> int:
    return requests.get(url).status_code


def post_data(url: str, payload: dict) -> dict:
    return requests.post(url, json=payload).json()


def fetch_with_raise(url: str) -> dict:
    r = requests.get(url)
    r.raise_for_status()
    return r.json()
''',
        "test": '''\
from unittest.mock import Mock, patch
import pytest
import requests
from exercises.stage12.exercise01.solution import (
    fetch_json,
    fetch_status_code,
    post_data,
    fetch_with_raise,
)


def _fake_response(json_data=None, status_code=200, raise_error=False):
    response = Mock()
    response.json.return_value = json_data or {}
    response.status_code = status_code
    if raise_error:
        response.raise_for_status.side_effect = requests.HTTPError("boom")
    else:
        response.raise_for_status.return_value = None
    return response


def test_fetch_json():
    with patch("requests.get", return_value=_fake_response({"id": 1})) as mock_get:
        result = fetch_json("https://example.test/api")
    mock_get.assert_called_once_with("https://example.test/api")
    assert result == {"id": 1}


def test_fetch_status_code():
    with patch("requests.get", return_value=_fake_response(status_code=404)):
        assert fetch_status_code("https://example.test/api") == 404


def test_post_data():
    with patch("requests.post", return_value=_fake_response({"created": True})) as mock_post:
        result = post_data("https://example.test/api", {"name": "Ada"})
    mock_post.assert_called_once_with("https://example.test/api", json={"name": "Ada"})
    assert result == {"created": True}


def test_fetch_with_raise_success():
    with patch("requests.get", return_value=_fake_response({"ok": True})):
        assert fetch_with_raise("https://example.test/api") == {"ok": True}


def test_fetch_with_raise_propagates_http_error():
    with patch("requests.get", return_value=_fake_response(raise_error=True)):
        with pytest.raises(requests.HTTPError):
            fetch_with_raise("https://example.test/api")
''',
    },
    {
        "name": "exercise02",
        "title": "Sessions and Retry/Backoff",
        "summary": "requests.Session() x3, retry/backoff strategy",
        "readme": (
            "Implement:\n\n"
            "- `make_default_session()` -- `requests.Session()`.\n"
            "- `create_session_with_headers(headers: dict)` -- build a "
            "`requests.Session()`, call `.headers.update(headers)` on it, "
            "and return it.\n"
            "- `fetch_multiple_with_session(urls: list[str]) -> list` -- "
            "`with requests.Session() as session:` then `[session.get(u)"
            ".json() for u in urls]`. A `Session` reuses its underlying TCP "
            "connection across requests instead of opening a fresh one "
            "every time -- **connection reuse** -- which matters a lot when "
            "you're about to make several requests to the same host.\n"
            "- `fetch_with_retry(url: str, max_attempts: int) -> dict` -- "
            "loop up to `max_attempts` times: `try`: `r = requests.get(url)`, "
            "`r.raise_for_status()`, `return r.json()`; `except "
            "requests.exceptions.RequestException:` if this was the last "
            "attempt, re-`raise`; otherwise `time.sleep(0.01 * (2 ** "
            "attempt))` (**exponential backoff**: wait longer after each "
            "failure) and try again.\n\n"
            "See the Study Reference presentation, Topic 12, for the theory."
        ),
        "stub": '''\
import time
import requests


def make_default_session():
    """requests.Session()."""
    raise NotImplementedError


def create_session_with_headers(headers: dict):
    """A requests.Session() with .headers.update(headers) applied."""
    raise NotImplementedError


def fetch_multiple_with_session(urls: list) -> list:
    """with requests.Session() as session: [session.get(u).json() for u in urls]."""
    raise NotImplementedError


def fetch_with_retry(url: str, max_attempts: int) -> dict:
    """Retry requests.get(url) up to max_attempts times with exponential backoff."""
    raise NotImplementedError
''',
        "reference": '''\
import time
import requests


def make_default_session():
    return requests.Session()


def create_session_with_headers(headers: dict):
    session = requests.Session()
    session.headers.update(headers)
    return session


def fetch_multiple_with_session(urls: list) -> list:
    with requests.Session() as session:
        return [session.get(u).json() for u in urls]


def fetch_with_retry(url: str, max_attempts: int) -> dict:
    for attempt in range(max_attempts):
        try:
            r = requests.get(url)
            r.raise_for_status()
            return r.json()
        except requests.exceptions.RequestException:
            if attempt == max_attempts - 1:
                raise
            time.sleep(0.01 * (2 ** attempt))
''',
        "test": '''\
from unittest.mock import Mock, patch
import pytest
import requests
from exercises.stage12.exercise02.solution import (
    make_default_session,
    create_session_with_headers,
    fetch_multiple_with_session,
    fetch_with_retry,
)


def test_make_default_session():
    assert isinstance(make_default_session(), requests.Session)


def test_create_session_with_headers():
    session = create_session_with_headers({"Authorization": "Bearer token"})
    assert session.headers["Authorization"] == "Bearer token"


def test_fetch_multiple_with_session():
    fake_response = Mock()
    fake_response.json.return_value = {"ok": True}
    with patch.object(requests.Session, "get", return_value=fake_response) as mock_get:
        result = fetch_multiple_with_session(["https://a.test", "https://b.test"])
    assert result == [{"ok": True}, {"ok": True}]
    assert mock_get.call_count == 2


def test_fetch_with_retry_succeeds_after_failures(monkeypatch):
    monkeypatch.setattr("time.sleep", lambda seconds: None)
    fake_response = Mock()
    fake_response.raise_for_status.return_value = None
    fake_response.json.return_value = {"ok": True}

    call_count = {"n": 0}

    def flaky_get(url):
        call_count["n"] += 1
        if call_count["n"] < 3:
            raise requests.exceptions.ConnectionError("boom")
        return fake_response

    with patch("requests.get", side_effect=flaky_get):
        result = fetch_with_retry("https://example.test", max_attempts=5)
    assert result == {"ok": True}
    assert call_count["n"] == 3


def test_fetch_with_retry_raises_after_exhausting_attempts(monkeypatch):
    monkeypatch.setattr("time.sleep", lambda seconds: None)
    with patch("requests.get", side_effect=requests.exceptions.ConnectionError("boom")):
        with pytest.raises(requests.exceptions.RequestException):
            fetch_with_retry("https://example.test", max_attempts=3)
''',
    },
    {
        "name": "exercise03",
        "title": "Threading Basics",
        "summary": "threading.Thread x3, .start() x3, .join() x3",
        "readme": (
            "Implement:\n\n"
            "- `run_in_background(func, *args) -> threading.Thread` -- "
            "`t = threading.Thread(target=func, args=args)`; `t.start()`; "
            "return `t`.\n"
            "- `wait_for_all(threads: list) -> None` -- `for t in threads: "
            "t.join()`.\n"
            "- `run_and_wait(funcs: list) -> None` -- create one "
            "`threading.Thread(target=f)` per function in `funcs`, "
            "`.start()` every one, **then** `.join()` every one (start them "
            "all first, so they actually run concurrently -- starting and "
            "immediately joining each one in the same loop would run them "
            "one at a time, defeating the point).\n\n"
            "See the Study Reference presentation, Topic 12, for the theory."
        ),
        "stub": '''\
import threading


def run_in_background(func, *args) -> threading.Thread:
    """threading.Thread(target=func, args=args), started, then returned."""
    raise NotImplementedError


def wait_for_all(threads: list) -> None:
    """t.join() for every thread in threads."""
    raise NotImplementedError


def run_and_wait(funcs: list) -> None:
    """Start every func as its own thread, THEN join all of them."""
    raise NotImplementedError
''',
        "reference": '''\
import threading


def run_in_background(func, *args) -> threading.Thread:
    t = threading.Thread(target=func, args=args)
    t.start()
    return t


def wait_for_all(threads: list) -> None:
    for t in threads:
        t.join()


def run_and_wait(funcs: list) -> None:
    threads = [threading.Thread(target=f) for f in funcs]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
''',
        "test": '''\
import threading
import time
from exercises.stage12.exercise03.solution import run_in_background, wait_for_all, run_and_wait


def test_run_in_background_runs_the_function():
    result = []
    t = run_in_background(lambda x: result.append(x), 42)
    t.join()
    assert result == [42]


def test_wait_for_all_blocks_until_every_thread_finishes():
    results = []

    def slow_append(n):
        time.sleep(0.01)
        results.append(n)

    threads = [threading.Thread(target=slow_append, args=(i,)) for i in range(5)]
    for t in threads:
        t.start()
    wait_for_all(threads)
    assert sorted(results) == [0, 1, 2, 3, 4]


def test_run_and_wait_runs_concurrently_and_completes():
    results = []
    funcs = [lambda i=i: results.append(i) for i in range(5)]
    run_and_wait(funcs)
    assert sorted(results) == [0, 1, 2, 3, 4]
''',
    },
    {
        "name": "exercise04",
        "title": "Locks and Race Conditions",
        "summary": "threading.Lock x3, race conditions",
        "readme": (
            "Implement three things protected by a `threading.Lock`:\n\n"
            "- `SafeCounter.__init__(self)` -- `self._lock = threading.Lock()`, "
            "`self._value = 0`. `increment(self) -> None` -- "
            "`with self._lock: self._value += 1`. Without the lock, two "
            "threads could both read the current value, both compute "
            "`value + 1`, and both write it back -- one increment silently "
            "lost. This is a **race condition**; the lock makes "
            "`+= 1` effectively atomic across threads.\n"
            "- `SafeList.__init__(self)` -- `self._lock = threading.Lock()`, "
            "`self._items = []`. `append_safe(self, item) -> None` -- "
            "`with self._lock: self._items.append(item)`.\n"
            "- `transfer_funds(accounts: dict, lock: threading.Lock, "
            "from_key, to_key, amount) -> None` -- `with lock: "
            "accounts[from_key] -= amount; accounts[to_key] += amount` -- "
            "the classic bank-transfer example: without the lock, a "
            "concurrent transfer could interleave between the two lines "
            "and leave the books unbalanced.\n"
            "- `parallel_increment(counter, times: int, num_threads: int) -> None` "
            "-- split `times` calls to `counter.increment()` evenly across "
            "`num_threads` threads, start them all, then join them all. "
            "Used by the tests to prove `SafeCounter` ends up with the "
            "*exact* right total even under real concurrency.\n\n"
            "See the Study Reference presentation, Topic 12, for the theory."
        ),
        "stub": '''\
import threading


class SafeCounter:
    def __init__(self):
        self._lock = threading.Lock()
        self._value = 0

    def increment(self) -> None:
        """with self._lock: self._value += 1."""
        raise NotImplementedError

    @property
    def value(self) -> int:
        return self._value


class SafeList:
    def __init__(self):
        self._lock = threading.Lock()
        self._items = []

    def append_safe(self, item) -> None:
        """with self._lock: self._items.append(item)."""
        raise NotImplementedError

    @property
    def items(self) -> list:
        return self._items


def transfer_funds(accounts: dict, lock: threading.Lock, from_key, to_key, amount) -> None:
    """with lock: accounts[from_key] -= amount; accounts[to_key] += amount."""
    raise NotImplementedError


def parallel_increment(counter, times: int, num_threads: int) -> None:
    """Split `times` counter.increment() calls across num_threads threads; start then join all."""
    raise NotImplementedError
''',
        "reference": '''\
import threading


class SafeCounter:
    def __init__(self):
        self._lock = threading.Lock()
        self._value = 0

    def increment(self) -> None:
        with self._lock:
            self._value += 1

    @property
    def value(self) -> int:
        return self._value


class SafeList:
    def __init__(self):
        self._lock = threading.Lock()
        self._items = []

    def append_safe(self, item) -> None:
        with self._lock:
            self._items.append(item)

    @property
    def items(self) -> list:
        return self._items


def transfer_funds(accounts: dict, lock: threading.Lock, from_key, to_key, amount) -> None:
    with lock:
        accounts[from_key] -= amount
        accounts[to_key] += amount


def parallel_increment(counter, times: int, num_threads: int) -> None:
    per_thread = times // num_threads

    def worker():
        for _ in range(per_thread):
            counter.increment()

    threads = [threading.Thread(target=worker) for _ in range(num_threads)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
''',
        "test": '''\
import threading
from exercises.stage12.exercise04.solution import (
    SafeCounter,
    SafeList,
    transfer_funds,
    parallel_increment,
)


def test_safe_counter_survives_real_concurrency():
    counter = SafeCounter()
    parallel_increment(counter, times=2000, num_threads=10)
    assert counter.value == 2000


def test_safe_list_append_from_many_threads():
    safe_list = SafeList()
    threads = [threading.Thread(target=safe_list.append_safe, args=(i,)) for i in range(50)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert sorted(safe_list.items) == list(range(50))


def test_transfer_funds_keeps_books_balanced():
    accounts = {"alice": 1000, "bob": 0}
    lock = threading.Lock()
    threads = [
        threading.Thread(target=transfer_funds, args=(accounts, lock, "alice", "bob", 10))
        for _ in range(50)
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert accounts["alice"] == 500
    assert accounts["bob"] == 500
    assert accounts["alice"] + accounts["bob"] == 1000
''',
    },
    {
        "name": "exercise05",
        "title": "ThreadPoolExecutor",
        "summary": "concurrent.futures.ThreadPoolExecutor x3",
        "readme": (
            "Implement three functions using "
            "`concurrent.futures.ThreadPoolExecutor` -- a higher-level "
            "alternative to managing `threading.Thread` objects by hand: "
            "you submit work and it handles the thread pool for you.\n\n"
            "- `fetch_all_concurrently(urls: list[str]) -> list` -- "
            "`with concurrent.futures.ThreadPoolExecutor(max_workers=4) as "
            "executor: return list(executor.map(lambda u: requests.get(u)"
            ".json(), urls))`.\n"
            "- `run_tasks_with_pool(funcs: list) -> list` -- "
            "`with concurrent.futures.ThreadPoolExecutor() as executor: "
            "return list(executor.map(lambda f: f(), funcs))` (run a list "
            "of zero-arg callables, collect their results in order).\n"
            "- `compute_squares_concurrently(numbers: list[int]) -> list[int]` "
            "-- `with concurrent.futures.ThreadPoolExecutor() as executor: "
            "return list(executor.map(lambda x: x ** 2, numbers))`.\n\n"
            "`executor.map` is the thread-pool equivalent of the builtin "
            "`map()` -- same call-once-per-item, results-in-order contract, "
            "just spread across worker threads instead of running serially.\n\n"
            "See the Study Reference presentation, Topic 12, for the theory."
        ),
        "stub": '''\
import concurrent.futures
import requests


def fetch_all_concurrently(urls: list) -> list:
    """ThreadPoolExecutor(max_workers=4).map(lambda u: requests.get(u).json(), urls)."""
    raise NotImplementedError


def run_tasks_with_pool(funcs: list) -> list:
    """ThreadPoolExecutor().map(lambda f: f(), funcs)."""
    raise NotImplementedError


def compute_squares_concurrently(numbers: list) -> list:
    """ThreadPoolExecutor().map(lambda x: x ** 2, numbers)."""
    raise NotImplementedError
''',
        "reference": '''\
import concurrent.futures
import requests


def fetch_all_concurrently(urls: list) -> list:
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        return list(executor.map(lambda u: requests.get(u).json(), urls))


def run_tasks_with_pool(funcs: list) -> list:
    with concurrent.futures.ThreadPoolExecutor() as executor:
        return list(executor.map(lambda f: f(), funcs))


def compute_squares_concurrently(numbers: list) -> list:
    with concurrent.futures.ThreadPoolExecutor() as executor:
        return list(executor.map(lambda x: x ** 2, numbers))
''',
        "test": '''\
from unittest.mock import Mock, patch
from exercises.stage12.exercise05.solution import (
    fetch_all_concurrently,
    run_tasks_with_pool,
    compute_squares_concurrently,
)


def test_fetch_all_concurrently():
    fake_response = Mock()
    fake_response.json.return_value = {"ok": True}
    with patch("requests.get", return_value=fake_response) as mock_get:
        result = fetch_all_concurrently(["https://a.test", "https://b.test", "https://c.test"])
    assert result == [{"ok": True}, {"ok": True}, {"ok": True}]
    assert mock_get.call_count == 3


def test_run_tasks_with_pool_preserves_order():
    funcs = [lambda i=i: i * 10 for i in range(5)]
    assert run_tasks_with_pool(funcs) == [0, 10, 20, 30, 40]


def test_compute_squares_concurrently():
    assert compute_squares_concurrently([1, 2, 3, 4]) == [1, 4, 9, 16]
''',
    },
]
