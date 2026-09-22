"""
Stage 9 -- OS, JSON, Datetime, XML.

Coverage plan (each item exercised by the trainee's own code >=3 times):
  keywords: os.listdir, os.path, json.load/dump, datetime.now/isoformat,
            ElementTree.parse/findall
  modules:  os, json, pathlib, datetime, xml.etree.ElementTree
  methods:  os.walk(), pathlib.Path, json.dumps(default=...)
  concepts: pathlib as the modern os.path alternative,
            timezone-aware vs naive datetimes
"""

STAGE = "stage09"
TOPIC = "OS, JSON, Datetime, XML"
OVERVIEW = (
    "Seven exercises tour the everyday stdlib modules from Topic 9 -- "
    "filesystem access two ways (os.path and pathlib), JSON round-tripping "
    "and custom encoding, naive vs. timezone-aware datetimes, and parsing/"
    "building XML with ElementTree -- each at least three times."
)

EXERCISES = [
    {
        "name": "exercise01",
        "title": "os.path and pathlib Basics",
        "summary": "os.listdir, os.path x2, pathlib.Path x2",
        "readme": (
            "Implement:\n\n"
            "- `list_files(directory: str) -> list[str]` -- "
            "`sorted(os.listdir(directory))`.\n"
            "- `join_path(directory: str, filename: str) -> str` -- "
            "`os.path.join(directory, filename)`.\n"
            "- `file_exists(path: str) -> bool` -- `os.path.exists(path)`.\n"
            "- `list_files_pathlib(directory: str) -> list[str]` -- "
            "`sorted(p.name for p in pathlib.Path(directory).iterdir())` -- "
            "the `pathlib` equivalent of `list_files` above.\n"
            "- `read_text_pathlib(path: str) -> str` -- "
            "`pathlib.Path(path).read_text()`.\n\n"
            "`pathlib.Path` objects support `/` for joining "
            "(`Path(directory) / filename`), have `.read_text()`/`.write_text()` "
            "built in, and are generally the modern, more readable "
            "alternative to `os.path`'s string-joining functions -- both are "
            "shown here so you recognize either style in the wild.\n\n"
            "See the Study Reference presentation, Topic 9, for the theory."
        ),
        "stub": '''\
import os
import pathlib


def list_files(directory: str) -> list[str]:
    """sorted(os.listdir(directory))."""
    raise NotImplementedError


def join_path(directory: str, filename: str) -> str:
    """os.path.join(directory, filename)."""
    raise NotImplementedError


def file_exists(path: str) -> bool:
    """os.path.exists(path)."""
    raise NotImplementedError


def list_files_pathlib(directory: str) -> list[str]:
    """sorted(p.name for p in pathlib.Path(directory).iterdir())."""
    raise NotImplementedError


def read_text_pathlib(path: str) -> str:
    """pathlib.Path(path).read_text()."""
    raise NotImplementedError
''',
        "reference": '''\
import os
import pathlib


def list_files(directory: str) -> list[str]:
    return sorted(os.listdir(directory))


def join_path(directory: str, filename: str) -> str:
    return os.path.join(directory, filename)


def file_exists(path: str) -> bool:
    return os.path.exists(path)


def list_files_pathlib(directory: str) -> list[str]:
    return sorted(p.name for p in pathlib.Path(directory).iterdir())


def read_text_pathlib(path: str) -> str:
    return pathlib.Path(path).read_text()
''',
        "test": '''\
from exercises.stage09.exercise01.solution import (
    list_files,
    join_path,
    file_exists,
    list_files_pathlib,
    read_text_pathlib,
)


def test_list_files(tmp_path):
    (tmp_path / "b.txt").write_text("b")
    (tmp_path / "a.txt").write_text("a")
    assert list_files(str(tmp_path)) == ["a.txt", "b.txt"]


def test_join_path():
    assert join_path("dir", "file.txt") in ("dir/file.txt", "dir\\\\file.txt")


def test_file_exists(tmp_path):
    (tmp_path / "a.txt").write_text("a")
    assert file_exists(str(tmp_path / "a.txt")) is True
    assert file_exists(str(tmp_path / "missing.txt")) is False


def test_list_files_pathlib(tmp_path):
    (tmp_path / "b.txt").write_text("b")
    (tmp_path / "a.txt").write_text("a")
    assert list_files_pathlib(str(tmp_path)) == ["a.txt", "b.txt"]


def test_read_text_pathlib(tmp_path):
    path = tmp_path / "a.txt"
    path.write_text("hello")
    assert read_text_pathlib(str(path)) == "hello"
''',
    },
    {
        "name": "exercise02",
        "title": "Recursive Traversal",
        "summary": "os.walk() x3, pathlib.Path glob",
        "readme": (
            "Implement:\n\n"
            "- `find_all_py_files(root: str) -> list[str]` -- walk `root` "
            "with `os.walk(root)`, collecting the full path "
            "(`os.path.join(dirpath, name)`) of every file ending in "
            "`.py`; return the sorted list.\n"
            "- `count_files_by_extension(root: str) -> dict` -- walk `root` "
            "with `os.walk`, building `{extension: count}` via "
            "`os.path.splitext(name)`.\n"
            "- `total_size_of_directory(root: str) -> int` -- walk `root` "
            "with `os.walk`, summing `os.path.getsize(...)` over every file.\n"
            "- `find_txt_files_pathlib(root: str) -> list[str]` -- the "
            "`pathlib` equivalent of a recursive search: "
            "`sorted(p.name for p in pathlib.Path(root).rglob(\"*.txt\"))`.\n\n"
            "`os.walk` yields `(dirpath, dirnames, filenames)` for the root "
            "directory and every subdirectory beneath it, one level per "
            "iteration -- the classic way to process an entire directory "
            "tree without recursing yourself.\n\n"
            "See the Study Reference presentation, Topic 9, for the theory."
        ),
        "stub": '''\
import os
import pathlib


def find_all_py_files(root: str) -> list[str]:
    """Every .py file under root (os.walk), full paths, sorted."""
    raise NotImplementedError


def count_files_by_extension(root: str) -> dict:
    """{extension: count} for every file under root (os.walk)."""
    raise NotImplementedError


def total_size_of_directory(root: str) -> int:
    """Sum of os.path.getsize() over every file under root (os.walk)."""
    raise NotImplementedError


def find_txt_files_pathlib(root: str) -> list[str]:
    """sorted(p.name for p in pathlib.Path(root).rglob("*.txt"))."""
    raise NotImplementedError
''',
        "reference": '''\
import os
import pathlib


def find_all_py_files(root: str) -> list[str]:
    result = []
    for dirpath, dirnames, filenames in os.walk(root):
        for name in filenames:
            if name.endswith(".py"):
                result.append(os.path.join(dirpath, name))
    return sorted(result)


def count_files_by_extension(root: str) -> dict:
    counts = {}
    for dirpath, dirnames, filenames in os.walk(root):
        for name in filenames:
            ext = os.path.splitext(name)[1]
            counts[ext] = counts.get(ext, 0) + 1
    return counts


def total_size_of_directory(root: str) -> int:
    total = 0
    for dirpath, dirnames, filenames in os.walk(root):
        for name in filenames:
            total += os.path.getsize(os.path.join(dirpath, name))
    return total


def find_txt_files_pathlib(root: str) -> list[str]:
    return sorted(p.name for p in pathlib.Path(root).rglob("*.txt"))
''',
        "test": '''\
from exercises.stage09.exercise02.solution import (
    find_all_py_files,
    count_files_by_extension,
    total_size_of_directory,
    find_txt_files_pathlib,
)


def _make_tree(tmp_path):
    (tmp_path / "a.py").write_text("x = 1")
    (tmp_path / "b.txt").write_text("hello")
    sub = tmp_path / "sub"
    sub.mkdir()
    (sub / "c.py").write_text("y = 2")
    (sub / "d.txt").write_text("world")
    return tmp_path


def test_find_all_py_files(tmp_path):
    _make_tree(tmp_path)
    result = find_all_py_files(str(tmp_path))
    assert len(result) == 2
    assert all(p.endswith(".py") for p in result)


def test_count_files_by_extension(tmp_path):
    _make_tree(tmp_path)
    result = count_files_by_extension(str(tmp_path))
    assert result == {".py": 2, ".txt": 2}


def test_total_size_of_directory(tmp_path):
    _make_tree(tmp_path)
    assert total_size_of_directory(str(tmp_path)) == len("x = 1") + len("hello") + len("y = 2") + len("world")


def test_find_txt_files_pathlib(tmp_path):
    _make_tree(tmp_path)
    assert find_txt_files_pathlib(str(tmp_path)) == ["b.txt", "d.txt"]
''',
    },
    {
        "name": "exercise03",
        "title": "JSON Basics",
        "summary": "json.load/dump x2, json.loads/dumps",
        "readme": (
            "Implement:\n\n"
            "- `save_json(path: str, data) -> None` -- "
            "`with open(path, \"w\") as f: json.dump(data, f)`.\n"
            "- `load_json(path: str)` -- `with open(path) as f: return "
            "json.load(f)`.\n"
            "- `to_json_string(data) -> str` -- `json.dumps(data)` (the "
            "string version of `dump`, no file involved).\n"
            "- `from_json_string(text: str)` -- `json.loads(text)` (the "
            "string version of `load`).\n\n"
            "See the Study Reference presentation, Topic 9, for the theory."
        ),
        "stub": '''\
import json


def save_json(path: str, data) -> None:
    """with open(path, "w") as f: json.dump(data, f)."""
    raise NotImplementedError


def load_json(path: str):
    """with open(path) as f: return json.load(f)."""
    raise NotImplementedError


def to_json_string(data) -> str:
    """json.dumps(data)."""
    raise NotImplementedError


def from_json_string(text: str):
    """json.loads(text)."""
    raise NotImplementedError
''',
        "reference": '''\
import json


def save_json(path: str, data) -> None:
    with open(path, "w") as f:
        json.dump(data, f)


def load_json(path: str):
    with open(path) as f:
        return json.load(f)


def to_json_string(data) -> str:
    return json.dumps(data)


def from_json_string(text: str):
    return json.loads(text)
''',
        "test": '''\
from exercises.stage09.exercise03.solution import (
    save_json,
    load_json,
    to_json_string,
    from_json_string,
)


def test_save_and_load_json_roundtrip(tmp_path):
    path = str(tmp_path / "data.json")
    save_json(path, {"name": "Ada", "age": 30})
    assert load_json(path) == {"name": "Ada", "age": 30}


def test_to_and_from_json_string_roundtrip():
    text = to_json_string({"x": 1, "y": [1, 2, 3]})
    assert from_json_string(text) == {"x": 1, "y": [1, 2, 3]}
''',
    },
    {
        "name": "exercise04",
        "title": "Custom JSON Encoding",
        "summary": "json.dumps(default=...) x3",
        "readme": (
            "`json.dumps` only knows how to serialize the handful of builtin "
            "types (`dict`, `list`, `str`, `int`/`float`, `bool`, `None`). "
            "For anything else, pass a `default=` function: it receives the "
            "unrecognized object and must return something JSON-serializable "
            "(or raise `TypeError`). Implement three:\n\n"
            "- `point_default(obj)` -- if `obj` is a `Point` (already "
            "defined, with `.x`/`.y`), return `{\"x\": obj.x, \"y\": obj.y}`; "
            "else `raise TypeError(f\"not JSON serializable: {obj!r}\")`. "
            "`serialize_with_points(data) -> str` -- "
            "`json.dumps(data, default=point_default)`.\n"
            "- `datetime_default(obj)` -- if `obj` is a `datetime.datetime`, "
            "return `obj.isoformat()`; else raise the same `TypeError`. "
            "`serialize_with_datetimes(data) -> str` -- "
            "`json.dumps(data, default=datetime_default)`.\n"
            "- `set_default(obj)` -- if `obj` is a `set`, return "
            "`sorted(obj)` (JSON has no set type, only arrays); else raise. "
            "`serialize_with_sets(data) -> str` -- "
            "`json.dumps(data, default=set_default)`.\n\n"
            "See the Study Reference presentation, Topic 9, for the theory."
        ),
        "stub": '''\
import json
import datetime


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def point_default(obj):
    """{"x": obj.x, "y": obj.y} for a Point, else raise TypeError."""
    raise NotImplementedError


def serialize_with_points(data) -> str:
    """json.dumps(data, default=point_default)."""
    raise NotImplementedError


def datetime_default(obj):
    """obj.isoformat() for a datetime.datetime, else raise TypeError."""
    raise NotImplementedError


def serialize_with_datetimes(data) -> str:
    """json.dumps(data, default=datetime_default)."""
    raise NotImplementedError


def set_default(obj):
    """sorted(obj) for a set, else raise TypeError."""
    raise NotImplementedError


def serialize_with_sets(data) -> str:
    """json.dumps(data, default=set_default)."""
    raise NotImplementedError
''',
        "reference": '''\
import json
import datetime


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def point_default(obj):
    if isinstance(obj, Point):
        return {"x": obj.x, "y": obj.y}
    raise TypeError(f"not JSON serializable: {obj!r}")


def serialize_with_points(data) -> str:
    return json.dumps(data, default=point_default)


def datetime_default(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    raise TypeError(f"not JSON serializable: {obj!r}")


def serialize_with_datetimes(data) -> str:
    return json.dumps(data, default=datetime_default)


def set_default(obj):
    if isinstance(obj, set):
        return sorted(obj)
    raise TypeError(f"not JSON serializable: {obj!r}")


def serialize_with_sets(data) -> str:
    return json.dumps(data, default=set_default)
''',
        "test": '''\
import json
import datetime
from exercises.stage09.exercise04.solution import (
    Point,
    serialize_with_points,
    serialize_with_datetimes,
    serialize_with_sets,
)


def test_serialize_with_points():
    result = serialize_with_points({"origin": Point(0, 0)})
    assert json.loads(result) == {"origin": {"x": 0, "y": 0}}


def test_serialize_with_datetimes():
    dt = datetime.datetime(2024, 1, 1, 12, 0, 0)
    result = serialize_with_datetimes({"created": dt})
    assert json.loads(result) == {"created": "2024-01-01T12:00:00"}


def test_serialize_with_sets():
    result = serialize_with_sets({"tags": {"b", "a", "c"}})
    assert json.loads(result) == {"tags": ["a", "b", "c"]}
''',
    },
    {
        "name": "exercise05",
        "title": "Datetime Basics",
        "summary": "datetime.now()/isoformat(), strftime, fromisoformat, arithmetic",
        "readme": (
            "Implement:\n\n"
            "- `current_timestamp_iso() -> str` -- "
            "`datetime.datetime.now().isoformat()`.\n"
            "- `format_date(dt) -> str` -- `dt.strftime(\"%Y-%m-%d\")`.\n"
            "- `parse_iso(text: str)` -- `datetime.datetime.fromisoformat(text)` "
            "(the inverse of `.isoformat()`).\n"
            "- `days_between(d1, d2) -> int` -- `(d2 - d1).days` (subtracting "
            "two `datetime`/`date` objects gives a `timedelta`, which has a "
            "`.days` attribute).\n\n"
            "See the Study Reference presentation, Topic 9, for the theory."
        ),
        "stub": '''\
import datetime


def current_timestamp_iso() -> str:
    """datetime.datetime.now().isoformat()."""
    raise NotImplementedError


def format_date(dt) -> str:
    """dt.strftime("%Y-%m-%d")."""
    raise NotImplementedError


def parse_iso(text: str):
    """datetime.datetime.fromisoformat(text)."""
    raise NotImplementedError


def days_between(d1, d2) -> int:
    """(d2 - d1).days."""
    raise NotImplementedError
''',
        "reference": '''\
import datetime


def current_timestamp_iso() -> str:
    return datetime.datetime.now().isoformat()


def format_date(dt) -> str:
    return dt.strftime("%Y-%m-%d")


def parse_iso(text: str):
    return datetime.datetime.fromisoformat(text)


def days_between(d1, d2) -> int:
    return (d2 - d1).days
''',
        "test": '''\
import datetime
from exercises.stage09.exercise05.solution import (
    current_timestamp_iso,
    format_date,
    parse_iso,
    days_between,
)


def test_current_timestamp_iso_is_parseable():
    text = current_timestamp_iso()
    parsed = datetime.datetime.fromisoformat(text)
    assert isinstance(parsed, datetime.datetime)


def test_format_date():
    dt = datetime.datetime(2024, 3, 15)
    assert format_date(dt) == "2024-03-15"


def test_parse_iso():
    result = parse_iso("2024-03-15T12:00:00")
    assert result == datetime.datetime(2024, 3, 15, 12, 0, 0)


def test_days_between():
    d1 = datetime.date(2024, 1, 1)
    d2 = datetime.date(2024, 1, 11)
    assert days_between(d1, d2) == 10
''',
    },
    {
        "name": "exercise06",
        "title": "Timezone-Aware vs. Naive Datetimes",
        "summary": "datetime.now() x2 more, isoformat x1 more, timezone-aware vs naive",
        "readme": (
            "Implement:\n\n"
            "- `naive_now()` -- `datetime.datetime.now()` -- **naive**: no "
            "timezone information at all.\n"
            "- `aware_now_utc()` -- `datetime.datetime.now(datetime.timezone.utc)` "
            "-- **aware**: explicitly anchored to UTC.\n"
            "- `is_timezone_aware(dt) -> bool` -- `dt.tzinfo is not None and "
            "dt.tzinfo.utcoffset(dt) is not None` (the official recipe -- "
            "just checking `dt.tzinfo is not None` isn't quite enough in "
            "every edge case, though it's right for the objects these "
            "exercises produce).\n"
            "- `to_utc_isoformat(dt) -> str` -- `dt.astimezone(datetime.timezone.utc)"
            ".isoformat()` (only works on an *aware* `dt` -- converting a naive "
            "one raises, since there's no original timezone to convert "
            "*from*).\n"
            "- `make_aware(dt, tz)` -- `dt.replace(tzinfo=tz)` (attaches a "
            "timezone to a naive datetime *without* shifting the clock time "
            "-- for that, you'd use `.astimezone()` instead).\n\n"
            "Comparing or subtracting a naive and an aware `datetime` raises "
            "`TypeError` -- Python refuses to guess which timezone the naive "
            "one is in, which is exactly why mixing the two is a classic bug "
            "source in real code.\n\n"
            "See the Study Reference presentation, Topic 9, for the theory."
        ),
        "stub": '''\
import datetime


def naive_now():
    """datetime.datetime.now() -- no timezone info."""
    raise NotImplementedError


def aware_now_utc():
    """datetime.datetime.now(datetime.timezone.utc)."""
    raise NotImplementedError


def is_timezone_aware(dt) -> bool:
    """dt.tzinfo is not None and dt.tzinfo.utcoffset(dt) is not None."""
    raise NotImplementedError


def to_utc_isoformat(dt) -> str:
    """dt.astimezone(datetime.timezone.utc).isoformat()."""
    raise NotImplementedError


def make_aware(dt, tz):
    """dt.replace(tzinfo=tz)."""
    raise NotImplementedError
''',
        "reference": '''\
import datetime


def naive_now():
    return datetime.datetime.now()


def aware_now_utc():
    return datetime.datetime.now(datetime.timezone.utc)


def is_timezone_aware(dt) -> bool:
    return dt.tzinfo is not None and dt.tzinfo.utcoffset(dt) is not None


def to_utc_isoformat(dt) -> str:
    return dt.astimezone(datetime.timezone.utc).isoformat()


def make_aware(dt, tz):
    return dt.replace(tzinfo=tz)
''',
        "test": '''\
import datetime
from exercises.stage09.exercise06.solution import (
    naive_now,
    aware_now_utc,
    is_timezone_aware,
    to_utc_isoformat,
    make_aware,
)


def test_naive_now_is_not_aware():
    assert is_timezone_aware(naive_now()) is False


def test_aware_now_utc_is_aware():
    assert is_timezone_aware(aware_now_utc()) is True


def test_make_aware():
    naive = datetime.datetime(2024, 1, 1, 12, 0, 0)
    aware = make_aware(naive, datetime.timezone.utc)
    assert is_timezone_aware(aware) is True
    assert aware.year == 2024 and aware.hour == 12


def test_to_utc_isoformat():
    aware = datetime.datetime(2024, 1, 1, 12, 0, 0, tzinfo=datetime.timezone.utc)
    assert to_utc_isoformat(aware) == "2024-01-01T12:00:00+00:00"


def test_naive_and_aware_cannot_be_compared():
    import pytest
    with pytest.raises(TypeError):
        naive_now() < aware_now_utc()
''',
    },
    {
        "name": "exercise07",
        "title": "XML with ElementTree",
        "summary": "ElementTree.parse/findall x3, building XML",
        "readme": (
            "Implement four functions using `xml.etree.ElementTree`:\n\n"
            "- `parse_xml_titles(path: str) -> list[str]` -- "
            "`ET.parse(path).getroot()`, then `[el.text for el in "
            "root.findall(\".//title\")]` (`.//title` finds every `<title>` "
            "element anywhere in the tree, at any depth).\n"
            "- `parse_xml_string_titles(xml_string: str) -> list[str]` -- "
            "same idea, but parse an in-memory string with `ET.fromstring(...)` "
            "instead of a file with `ET.parse(...)`.\n"
            "- `count_elements(path: str, tag: str) -> int` -- "
            "`len(root.findall(f\".//{tag}\"))`.\n"
            "- `get_attribute_values(path: str, tag: str, attr: str) -> list[str]` "
            "-- `[el.get(attr) for el in root.findall(f\".//{tag}\")]`.\n"
            "- `build_simple_xml(items: list[str]) -> str` -- build a tree "
            "from scratch: `root = ET.Element(\"items\")`; for each item, "
            "`child = ET.SubElement(root, \"item\")` then `child.text = item`; "
            "return `ET.tostring(root, encoding=\"unicode\")`.\n\n"
            "See the Study Reference presentation, Topic 9, for the theory."
        ),
        "stub": '''\
import xml.etree.ElementTree as ET


def parse_xml_titles(path: str) -> list[str]:
    """ET.parse(path).getroot(), then every <title> element's text."""
    raise NotImplementedError


def parse_xml_string_titles(xml_string: str) -> list[str]:
    """Same as parse_xml_titles, but via ET.fromstring(xml_string)."""
    raise NotImplementedError


def count_elements(path: str, tag: str) -> int:
    """How many <tag> elements exist anywhere in the tree."""
    raise NotImplementedError


def get_attribute_values(path: str, tag: str, attr: str) -> list[str]:
    """The attr attribute of every <tag> element."""
    raise NotImplementedError


def build_simple_xml(items: list[str]) -> str:
    """<items><item>...</item>...</items>, via ET.Element/SubElement/tostring."""
    raise NotImplementedError
''',
        "reference": '''\
import xml.etree.ElementTree as ET


def parse_xml_titles(path: str) -> list[str]:
    root = ET.parse(path).getroot()
    return [el.text for el in root.findall(".//title")]


def parse_xml_string_titles(xml_string: str) -> list[str]:
    root = ET.fromstring(xml_string)
    return [el.text for el in root.findall(".//title")]


def count_elements(path: str, tag: str) -> int:
    root = ET.parse(path).getroot()
    return len(root.findall(f".//{tag}"))


def get_attribute_values(path: str, tag: str, attr: str) -> list[str]:
    root = ET.parse(path).getroot()
    return [el.get(attr) for el in root.findall(f".//{tag}")]


def build_simple_xml(items: list[str]) -> str:
    root = ET.Element("items")
    for item in items:
        child = ET.SubElement(root, "item")
        child.text = item
    return ET.tostring(root, encoding="unicode")
''',
        "test": '''\
import xml.etree.ElementTree as ET
from exercises.stage09.exercise07.solution import (
    parse_xml_titles,
    parse_xml_string_titles,
    count_elements,
    get_attribute_values,
    build_simple_xml,
)

LIBRARY_XML = (
    '<library>'
    '<book id="1"><title>Dune</title></book>'
    '<book id="2"><title>Foundation</title></book>'
    "</library>"
)


def test_parse_xml_titles(tmp_path):
    path = tmp_path / "library.xml"
    path.write_text(LIBRARY_XML)
    assert parse_xml_titles(str(path)) == ["Dune", "Foundation"]


def test_parse_xml_string_titles():
    assert parse_xml_string_titles(LIBRARY_XML) == ["Dune", "Foundation"]


def test_count_elements(tmp_path):
    path = tmp_path / "library.xml"
    path.write_text(LIBRARY_XML)
    assert count_elements(str(path), "book") == 2


def test_get_attribute_values(tmp_path):
    path = tmp_path / "library.xml"
    path.write_text(LIBRARY_XML)
    assert get_attribute_values(str(path), "book", "id") == ["1", "2"]


def test_build_simple_xml():
    xml_string = build_simple_xml(["a", "b"])
    root = ET.fromstring(xml_string)
    items = root.findall("item")
    assert [el.text for el in items] == ["a", "b"]
''',
    },
]
