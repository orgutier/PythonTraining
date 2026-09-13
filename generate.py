"""
Generates the full exercises/ , reference_solutions/ , and tests/ trees
for the PythonTraining repo. Run once from the repo root.
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

# Each entry: (week, topic_name, stub_code, reference_code, test_code, readme_body)
WEEKS = []

def add(week, topic, stub, reference, test, readme):
    WEEKS.append((week, topic, stub, reference, test, readme))

STUB_HEADER = '''"""
{topic}
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in tests/test_{week}.py
imports directly from here.
"""


'''

# ------------------------------------------------------------------ WEEK 01
add(
"week01", "Python Fundamentals",
STUB_HEADER.format(topic="Week 1 - Python Fundamentals", week="week01") + '''\
def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a Celsius temperature to Fahrenheit."""
    raise NotImplementedError


def bmi_calculator(weight_kg: float, height_m: float) -> float:
    """Return BMI = weight_kg / height_m ** 2, rounded to 2 decimals."""
    raise NotImplementedError
''',
'''\
def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32


def bmi_calculator(weight_kg: float, height_m: float) -> float:
    return round(weight_kg / height_m ** 2, 2)
''',
'''\
from exercises.week01.solution import celsius_to_fahrenheit, bmi_calculator


def test_celsius_to_fahrenheit_freezing():
    assert celsius_to_fahrenheit(0) == 32.0


def test_celsius_to_fahrenheit_boiling():
    assert celsius_to_fahrenheit(100) == 212.0


def test_bmi_calculator():
    assert abs(bmi_calculator(70, 1.75) - 22.86) < 0.01
''',
"Write two small functions using annotated parameters and return types. "
"See the Study Reference presentation, Topic 1, for the theory."
)

# ------------------------------------------------------------------ WEEK 02
add(
"week02", "Control Flow",
STUB_HEADER.format(topic="Week 2 - Control Flow", week="week02") + '''\
def fizzbuzz(n: int) -> list[str]:
    """Return a list of strings 1..n applying the Fizz/Buzz/FizzBuzz rule."""
    raise NotImplementedError


def is_prime(n: int) -> bool:
    """Return True if n is a prime number."""
    raise NotImplementedError
''',
'''\
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
            return False
    return True
''',
'''\
from exercises.week02.solution import fizzbuzz, is_prime


def test_fizzbuzz():
    assert fizzbuzz(15) == [
        "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
        "11", "Fizz", "13", "14", "FizzBuzz",
    ]


def test_is_prime():
    assert is_prime(1) is False
    assert is_prime(2) is True
    assert is_prime(17) is True
    assert is_prime(18) is False
''',
"Nested loops and off-by-one errors are the most common mistakes here -- "
"work through the pattern on paper first if it's not clicking."
)

# ------------------------------------------------------------------ WEEK 03
add(
"week03", "Functions",
STUB_HEADER.format(topic="Week 3 - Functions", week="week03") + '''\
def factorial(n: int) -> int:
    """Return n! -- MUST be implemented recursively."""
    raise NotImplementedError


def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number (0-indexed)."""
    raise NotImplementedError
''',
'''\
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
'''\
import pytest
from exercises.week03.solution import factorial, fibonacci


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

# NOTE: this test suite checks OUTPUT correctness only. Whether the
# implementation is actually recursive (as the exercise asks) is a soft,
# human-reviewed requirement -- an iterative solution will still pass here.
''',
"factorial() and fibonacci() must be recursive, not just correct -- the "
"point of this exercise is the recursive pattern itself."
)

# ------------------------------------------------------------------ WEEK 04
add(
"week04", "Data Structures",
STUB_HEADER.format(topic="Week 4 - Data Structures", week="week04") + '''\
def word_frequency(text: str) -> dict[str, int]:
    """
    Return a case-insensitive word -> count dictionary.
    Punctuation should not be counted as part of a word.
    Try to use a comprehension somewhere in your implementation.
    """
    raise NotImplementedError
''',
'''\
import re


def word_frequency(text: str) -> dict[str, int]:
    words = re.findall(r"[a-zA-Z']+", text.lower())
    return {word: words.count(word) for word in set(words)}
''',
'''\
from exercises.week04.solution import word_frequency


def test_word_frequency():
    result = word_frequency("The cat sat. The cat ran.")
    assert result == {"the": 2, "cat": 2, "sat": 1, "ran": 1}

# NOTE: "uses a comprehension" is a soft/manual review item, not enforced here.
''',
"Extract word counts from free text. Case-insensitive, punctuation-free."
)

# ------------------------------------------------------------------ WEEK 05
add(
"week05", "Files, Exceptions, Regex",
STUB_HEADER.format(topic="Week 5 - Files, Exceptions, Regex", week="week05") + '''\
def extract_emails(text: str) -> list[str]:
    """Return every email address found in text, in order of appearance."""
    raise NotImplementedError


class InvalidLogLineError(Exception):
    """Raised when a log line does not match the expected format."""


def parse_log_line(line: str) -> dict:
    """
    Parse a log line of the form "YYYY-MM-DD LEVEL message" into
    {"date": ..., "level": ..., "message": ...}.
    Raise InvalidLogLineError if the line doesn't match.
    """
    raise NotImplementedError
''',
'''\
import re


def extract_emails(text: str) -> list[str]:
    return re.findall(r"[\\w.+-]+@[\\w-]+\\.[\\w.-]+", text)


class InvalidLogLineError(Exception):
    """Raised when a log line does not match the expected format."""


def parse_log_line(line: str) -> dict:
    match = re.match(r"^(\\d{4}-\\d{2}-\\d{2})\\s+(\\w+)\\s+(.+)$", line)
    if not match:
        raise InvalidLogLineError(f"Malformed log line: {line!r}")
    date, level, message = match.groups()
    return {"date": date, "level": level, "message": message}
''',
'''\
import pytest
from exercises.week05.solution import (
    extract_emails,
    parse_log_line,
    InvalidLogLineError,
)


def test_extract_emails():
    text = "Contact a@x.com or b@y.org, cc c@z.net"
    assert extract_emails(text) == ["a@x.com", "b@y.org", "c@z.net"]


def test_parse_log_line_valid():
    result = parse_log_line("2024-01-01 ERROR disk full")
    assert result == {"date": "2024-01-01", "level": "ERROR", "message": "disk full"}


def test_parse_log_line_invalid():
    with pytest.raises(InvalidLogLineError):
        parse_log_line("garbage")
''',
"Build a small log-line parser with a custom exception, plus a regex-based "
"email extractor."
)

# ------------------------------------------------------------------ WEEK 06
add(
"week06", "OOP I - Classes, Encapsulation, Properties",
STUB_HEADER.format(topic="Week 6 - OOP I", week="week06") + '''\
class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        raise NotImplementedError

    @property
    def balance(self) -> float:
        raise NotImplementedError

    @balance.setter
    def balance(self, value: float) -> None:
        """Must raise ValueError if value is negative."""
        raise NotImplementedError

    @staticmethod
    def is_valid_amount(amount: float) -> bool:
        raise NotImplementedError
''',
'''\
class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self._balance = 0.0
        self.balance = balance  # goes through the setter for validation

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, value: float) -> None:
        if not BankAccount.is_valid_amount(value):
            raise ValueError("balance cannot be negative")
        self._balance = value

    @staticmethod
    def is_valid_amount(amount: float) -> bool:
        return amount >= 0
''',
'''\
import pytest
from exercises.week06.solution import BankAccount


def test_bank_account_balance():
    acct = BankAccount("Ana", 100)
    assert acct.balance == 100


def test_bank_account_negative_raises():
    acct = BankAccount("Ana", 100)
    with pytest.raises(ValueError):
        acct.balance = -50


def test_is_valid_amount():
    assert BankAccount.is_valid_amount(-5) is False
    assert BankAccount.is_valid_amount(10) is True
''',
"A validated @property, plus @staticmethod. This is also where decorators "
"get explained properly for the first time -- see the presentation."
)

# ------------------------------------------------------------------ WEEK 07
add(
"week07", "OOP II - Inheritance, Polymorphism, Abstraction",
STUB_HEADER.format(topic="Week 7 - OOP II", week="week07") + '''\
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        ...


class Circle(Shape):
    def __init__(self, radius: float):
        raise NotImplementedError

    def area(self) -> float:
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        raise NotImplementedError

    def area(self) -> float:
        raise NotImplementedError
''',
'''\
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        ...


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height
''',
'''\
import pytest
from exercises.week07.solution import Shape, Circle, Rectangle


def test_circle_area():
    assert abs(Circle(2).area() - 12.566) < 0.01


def test_rectangle_area():
    assert Rectangle(3, 4).area() == 12


def test_shape_is_abstract():
    with pytest.raises(TypeError):
        Shape()
''',
"Abstract base classes with abc/@abstractmethod, plus concrete subclasses."
)

# ------------------------------------------------------------------ WEEK 08
add(
"week08", "The Python Data Model",
STUB_HEADER.format(topic="Week 8 - The Python Data Model", week="week08") + '''\
class Vector:
    def __init__(self, x: float, y: float):
        raise NotImplementedError

    def __add__(self, other: "Vector") -> "Vector":
        raise NotImplementedError

    def __eq__(self, other) -> bool:
        raise NotImplementedError

    def __repr__(self) -> str:
        raise NotImplementedError


class Deck:
    def __init__(self, cards: list):
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def __getitem__(self, index: int):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError
''',
'''\
class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other) -> bool:
        return isinstance(other, Vector) and self.x == other.x and self.y == other.y

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"


class Deck:
    def __init__(self, cards: list):
        self._cards = list(cards)

    def __len__(self) -> int:
        return len(self._cards)

    def __getitem__(self, index: int):
        return self._cards[index]

    def __iter__(self):
        return iter(self._cards)
''',
'''\
from exercises.week08.solution import Vector, Deck


def test_vector_add():
    assert Vector(1, 2) + Vector(3, 4) == Vector(4, 6)


def test_vector_repr():
    assert repr(Vector(1, 2)) == "Vector(1, 2)"


def test_deck_len_getitem_iter():
    deck = Deck([1, 2, 3])
    assert len(deck) == 3
    assert deck[0] == 1
    assert list(deck) == [1, 2, 3]
''',
"The payoff week -- len()/+/[]/for as protocol calls to dunder methods."
)

# ------------------------------------------------------------------ WEEK 09
add(
"week09", "OS, JSON, Datetime, XML",
STUB_HEADER.format(topic="Week 9 - OS, JSON, Datetime, XML", week="week09") + '''\
def read_config(path: str) -> dict:
    raise NotImplementedError


def write_config(path: str, data: dict) -> None:
    raise NotImplementedError


def timestamp_now() -> str:
    """Return the current UTC time as an ISO-8601 string."""
    raise NotImplementedError


def parse_xml_titles(xml_string: str) -> list[str]:
    """Return the text of every <title> element in xml_string, in order."""
    raise NotImplementedError
''',
'''\
import json
from datetime import datetime, timezone
import xml.etree.ElementTree as ET


def read_config(path: str) -> dict:
    with open(path, "r") as f:
        return json.load(f)


def write_config(path: str, data: dict) -> None:
    with open(path, "w") as f:
        json.dump(data, f)


def timestamp_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def parse_xml_titles(xml_string: str) -> list[str]:
    root = ET.fromstring(xml_string)
    return [el.text for el in root.findall(".//title")]
''',
'''\
import re
from exercises.week09.solution import (
    read_config,
    write_config,
    timestamp_now,
    parse_xml_titles,
)


def test_config_roundtrip(tmp_path):
    p = tmp_path / "config.json"
    write_config(str(p), {"a": 1})
    assert read_config(str(p)) == {"a": 1}


def test_timestamp_now_format():
    ts = timestamp_now()
    assert re.match(r"\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}", ts)


def test_parse_xml_titles():
    xml = (
        "<library>"
        "<book><title>A</title></book>"
        "<book><title>B</title></book>"
        "<book><title>C</title></book>"
        "</library>"
    )
    assert parse_xml_titles(xml) == ["A", "B", "C"]
''',
"Four everyday stdlib modules in one exercise: os/json/datetime/xml."
)

# ------------------------------------------------------------------ WEEK 10
add(
"week10", "Pandas",
STUB_HEADER.format(topic="Week 10 - Pandas", week="week10") + '''\
import pandas as pd


def load_sales_data(path: str) -> pd.DataFrame:
    raise NotImplementedError


def total_sales_by_region(df: pd.DataFrame) -> pd.Series:
    raise NotImplementedError


def top_n_products(df: pd.DataFrame, n: int) -> pd.DataFrame:
    raise NotImplementedError
''',
'''\
import pandas as pd


def load_sales_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def total_sales_by_region(df: pd.DataFrame) -> pd.Series:
    return df.groupby("region")["sales"].sum()


def top_n_products(df: pd.DataFrame, n: int) -> pd.DataFrame:
    return df.sort_values("sales", ascending=False).head(n)
''',
'''\
import pytest
from exercises.week10.solution import (
    load_sales_data,
    total_sales_by_region,
    top_n_products,
)


@pytest.fixture
def sample_csv(tmp_path):
    content = (
        "product,region,sales\\n"
        "Widget,East,100\\n"
        "Gadget,West,200\\n"
        "Widget,West,150\\n"
        "Gizmo,East,50\\n"
    )
    p = tmp_path / "sales.csv"
    p.write_text(content)
    return str(p)


def test_total_sales_by_region(sample_csv):
    df = load_sales_data(sample_csv)
    result = total_sales_by_region(df)
    assert result["East"] == 150
    assert result["West"] == 350


def test_top_n_products(sample_csv):
    df = load_sales_data(sample_csv)
    top2 = top_n_products(df, 2)
    assert list(top2["product"]) == ["Gadget", "Widget"]
''',
"Real pandas: groupby aggregation and sorting, not just read_csv."
)

# ------------------------------------------------------------------ WEEK 11
add(
"week11", "OpenCV",
STUB_HEADER.format(topic="Week 11 - OpenCV", week="week11") + '''\
def to_grayscale(input_path: str, output_path: str) -> None:
    raise NotImplementedError


def resize_image(input_path: str, output_path: str, width: int, height: int) -> None:
    raise NotImplementedError


def draw_rectangle(input_path: str, output_path: str, top_left: tuple, bottom_right: tuple) -> None:
    raise NotImplementedError
''',
'''\
import cv2


def to_grayscale(input_path: str, output_path: str) -> None:
    img = cv2.imread(input_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(output_path, gray)


def resize_image(input_path: str, output_path: str, width: int, height: int) -> None:
    img = cv2.imread(input_path)
    resized = cv2.resize(img, (width, height))
    cv2.imwrite(output_path, resized)


def draw_rectangle(input_path: str, output_path: str, top_left: tuple, bottom_right: tuple) -> None:
    img = cv2.imread(input_path)
    cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)
    cv2.imwrite(output_path, img)
''',
'''\
import numpy as np
import cv2
import pytest
from exercises.week11.solution import to_grayscale, resize_image, draw_rectangle


@pytest.fixture
def sample_image(tmp_path):
    img = np.zeros((50, 80, 3), dtype=np.uint8)
    img[:] = (100, 150, 200)
    path = tmp_path / "input.png"
    cv2.imwrite(str(path), img)
    return str(path)


def test_to_grayscale(sample_image, tmp_path):
    out = str(tmp_path / "gray.png")
    to_grayscale(sample_image, out)
    result = cv2.imread(out, cv2.IMREAD_UNCHANGED)
    assert result.ndim == 2


def test_resize_image(sample_image, tmp_path):
    out = str(tmp_path / "resized.png")
    resize_image(sample_image, out, 40, 20)
    result = cv2.imread(out)
    assert result.shape[:2] == (20, 40)


def test_draw_rectangle(sample_image, tmp_path):
    out = str(tmp_path / "rect.png")
    draw_rectangle(sample_image, out, (5, 5), (20, 20))
    before = cv2.imread(sample_image)
    after = cv2.imread(out)
    assert not (before == after).all()
''',
"Images as NumPy arrays: grayscale conversion, resizing, drawing. Test "
"images are generated in-memory, no external photo file needed."
)

# ------------------------------------------------------------------ WEEK 12
add(
"week12", "Requests + Threading",
STUB_HEADER.format(topic="Week 12 - Requests + Threading", week="week12") + '''\
import threading
import requests


class APIError(Exception):
    """Raised when the API responds with a non-200 status code."""


def fetch_user_name(user_id: int) -> str:
    raise NotImplementedError


def fetch_many(user_ids: list[int]) -> dict[int, str]:
    """Fetch multiple user names concurrently using threading."""
    raise NotImplementedError
''',
'''\
import threading
import requests


class APIError(Exception):
    """Raised when the API responds with a non-200 status code."""


def fetch_user_name(user_id: int) -> str:
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    if response.status_code != 200:
        raise APIError(f"Request failed with status {response.status_code}")
    return response.json()["name"]


def fetch_many(user_ids: list[int]) -> dict[int, str]:
    results = {}
    lock = threading.Lock()

    def worker(uid):
        name = fetch_user_name(uid)
        with lock:
            results[uid] = name

    threads = [threading.Thread(target=worker, args=(uid,)) for uid in user_ids]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return results
''',
'''\
from unittest.mock import patch, MagicMock
import pytest
from exercises.week12.solution import fetch_user_name, fetch_many, APIError


def _mock_response(status_code, json_data):
    mock = MagicMock()
    mock.status_code = status_code
    mock.json.return_value = json_data
    return mock


@patch("exercises.week12.solution.requests.get")
def test_fetch_user_name_success(mock_get):
    mock_get.return_value = _mock_response(200, {"name": "Leanne Graham"})
    assert fetch_user_name(1) == "Leanne Graham"


@patch("exercises.week12.solution.requests.get")
def test_fetch_user_name_failure(mock_get):
    mock_get.return_value = _mock_response(404, {})
    with pytest.raises(APIError):
        fetch_user_name(1)


@patch("exercises.week12.solution.requests.get")
def test_fetch_many(mock_get):
    mock_get.return_value = _mock_response(200, {"name": "Same Name"})
    result = fetch_many([1, 2, 3])
    assert result == {1: "Same Name", 2: "Same Name", 3: "Same Name"}

# NOTE: requests.get is mocked -- this hook never touches a live endpoint.
# fetch_many is checked via deterministic shared-state, not timing.
''',
"Client-side HTTP with requests, fanned out across threads. All network "
"calls are mocked in the test suite -- never hits a live endpoint."
)

# ------------------------------------------------------------------ WEEK 13
add(
"week13", "Local API Endpoints (FastAPI)",
STUB_HEADER.format(topic="Week 13 - FastAPI", week="week13") + '''\
from fastapi import FastAPI

app = FastAPI()


@app.get("/hello/{name}")
def say_hello(name: str) -> dict:
    raise NotImplementedError


@app.get("/add")
def add(a: int, b: int) -> dict:
    raise NotImplementedError
''',
'''\
from fastapi import FastAPI

app = FastAPI()


@app.get("/hello/{name}")
def say_hello(name: str) -> dict:
    return {"message": f"Hello, {name}!"}


@app.get("/add")
def add(a: int, b: int) -> dict:
    return {"result": a + b}
''',
'''\
from fastapi.testclient import TestClient
from exercises.week13.solution import app

client = TestClient(app)


def test_say_hello():
    response = client.get("/hello/World")
    assert response.json() == {"message": "Hello, World!"}


def test_add():
    response = client.get("/add", params={"a": 2, "b": 3})
    assert response.json() == {"result": 5}
''',
"Build two working endpoints and view them live at /docs when you run "
"`uvicorn solution:app --reload` from this folder."
)

# ------------------------------------------------------------------ WEEK 14
add(
"week14", "Capstone",
STUB_HEADER.format(topic="Week 14 - Capstone", week="week14") + '''\
class Book:
    def __init__(self, title: str, author: str, isbn: str):
        raise NotImplementedError

    def __repr__(self) -> str:
        raise NotImplementedError

    def __eq__(self, other) -> bool:
        """Two books are equal if they share the same isbn."""
        raise NotImplementedError


class Library:
    def __init__(self):
        raise NotImplementedError

    def add_book(self, book: Book) -> None:
        raise NotImplementedError

    def find_by_author(self, author: str) -> list[Book]:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def __contains__(self, isbn: str) -> bool:
        raise NotImplementedError

    def save_to_json(self, path: str) -> None:
        raise NotImplementedError

    def load_from_json(self, path: str) -> None:
        raise NotImplementedError
''',
'''\
import json


class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __repr__(self) -> str:
        return f"Book({self.title!r}, {self.author!r}, {self.isbn!r})"

    def __eq__(self, other) -> bool:
        return isinstance(other, Book) and self.isbn == other.isbn


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book: Book) -> None:
        self._books.append(book)

    def find_by_author(self, author: str) -> list:
        return [b for b in self._books if b.author == author]

    def __len__(self) -> int:
        return len(self._books)

    def __contains__(self, isbn: str) -> bool:
        return any(b.isbn == isbn for b in self._books)

    def save_to_json(self, path: str) -> None:
        data = [{"title": b.title, "author": b.author, "isbn": b.isbn} for b in self._books]
        with open(path, "w") as f:
            json.dump(data, f)

    def load_from_json(self, path: str) -> None:
        with open(path) as f:
            data = json.load(f)
        self._books = [Book(**d) for d in data]
''',
'''\
from exercises.week14.solution import Book, Library


def test_add_and_len():
    lib = Library()
    lib.add_book(Book("Dune", "Herbert", "111"))
    assert len(lib) == 1


def test_find_by_author():
    lib = Library()
    lib.add_book(Book("Dune", "Herbert", "111"))
    lib.add_book(Book("Foundation", "Asimov", "222"))
    result = lib.find_by_author("Herbert")
    assert len(result) == 1
    assert result[0].isbn == "111"


def test_contains():
    lib = Library()
    lib.add_book(Book("Dune", "Herbert", "111"))
    assert "111" in lib


def test_save_and_load_roundtrip(tmp_path):
    lib = Library()
    lib.add_book(Book("Dune", "Herbert", "111"))
    path = str(tmp_path / "lib.json")
    lib.save_to_json(path)

    new_lib = Library()
    new_lib.load_from_json(path)
    assert len(new_lib) == 1
    assert new_lib._books[0].title == "Dune"
''',
"Final project: a small Library/Book system with JSON persistence. "
"pandas/requests/opencv/FastAPI usage is bonus scope here, not required."
)


def main():
    for week, topic, stub, reference, test, readme_body in WEEKS:
        ex_dir = os.path.join(ROOT, "exercises", week)
        ref_dir = os.path.join(ROOT, "reference_solutions", week)
        os.makedirs(ex_dir, exist_ok=True)
        os.makedirs(ref_dir, exist_ok=True)

        with open(os.path.join(ex_dir, "solution.py"), "w") as f:
            f.write(stub)
        with open(os.path.join(ex_dir, "README.md"), "w") as f:
            f.write(f"# {topic}\n\n{readme_body}\n")
        with open(os.path.join(ref_dir, "solution.py"), "w") as f:
            f.write(reference)
        with open(os.path.join(ROOT, "tests", f"test_{week}.py"), "w") as f:
            f.write(test)

    print(f"Generated {len(WEEKS)} weeks.")


if __name__ == "__main__":
    main()
