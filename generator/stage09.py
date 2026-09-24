"""
Stage 9 -- OS, JSON, Datetime, XML.

Rolled onto the tier-named exercise convention: a minimum of two exercises
per Basic/Mid/Advanced tier. All exercises are function-based -- this
stage is a tour of everyday stdlib modules, naturally expressed as
functions.

Coverage plan (every item below is exercised by the trainee's own code,
generally 2+ times across these 6 exercises):

  Basic:    os.listdir, os.path, json.load/dump, datetime.now/isoformat,
            ElementTree.parse/findall
  Mid:      pathlib.Path, json.dumps(default=...), pathlib as the modern
            os.path alternative, timezone-aware vs naive datetimes
  Advanced: os.walk()
"""

STAGE = "stage09"
TOPIC = "OS, JSON, Datetime, XML"
OVERVIEW = (
    "Six exercises, two per tier: a config-file manager (os.path + JSON) "
    "and a library catalog (datetime + XML) in Basic; pathlib as the "
    "modern os.path alternative, and timezone-aware timestamps serialized "
    "via a custom JSON encoder, in Mid; recursive directory traversal "
    "with os.walk() in Advanced."
)

EXERCISES = [
    {
        "name": "basic01",
        "title": "Config File Manager",
        "summary": "os.listdir, os.path, json.load/dump",
        "readme": (
            "A small JSON-backed config store, one file per named config, "
            "all living in one directory. Implement:\n\n"
            "- `config_path(directory: str, name: str) -> str` -- "
            "`os.path.join(directory, name + \".json\")`.\n"
            "- `config_exists(directory: str, name: str) -> bool` -- "
            "`os.path.exists(config_path(directory, name))`.\n"
            "- `save_config(directory: str, name: str, data: dict) -> None` "
            "-- `with open(config_path(directory, name), \"w\") as f: "
            "json.dump(data, f)`.\n"
            "- `load_config(directory: str, name: str) -> dict` -- "
            "`with open(config_path(directory, name)) as f: return "
            "json.load(f)`.\n"
            "- `list_config_names(directory: str) -> list[str]` -- "
            "`sorted(f[:-5] for f in os.listdir(directory) if "
            "f.endswith(\".json\"))` (strip the `.json` suffix off each "
            "matching filename).\n\n"
            "See the Study Reference presentation, Topic 9 (Basic tier), "
            "for the theory."
        ),
        "stub": '''\
import json
import os


def config_path(directory: str, name: str) -> str:
    """os.path.join(directory, name + ".json")."""
    raise NotImplementedError


def config_exists(directory: str, name: str) -> bool:
    """os.path.exists(config_path(directory, name))."""
    raise NotImplementedError


def save_config(directory: str, name: str, data: dict) -> None:
    """Write data as JSON to config_path(directory, name)."""
    raise NotImplementedError


def load_config(directory: str, name: str) -> dict:
    """Read and json.load the file at config_path(directory, name)."""
    raise NotImplementedError


def list_config_names(directory: str) -> list[str]:
    """sorted names (without ".json") of every *.json file in directory."""
    raise NotImplementedError
''',
        "reference": '''\
import json
import os


def config_path(directory: str, name: str) -> str:
    return os.path.join(directory, name + ".json")


def config_exists(directory: str, name: str) -> bool:
    return os.path.exists(config_path(directory, name))


def save_config(directory: str, name: str, data: dict) -> None:
    with open(config_path(directory, name), "w") as f:
        json.dump(data, f)


def load_config(directory: str, name: str) -> dict:
    with open(config_path(directory, name)) as f:
        return json.load(f)


def list_config_names(directory: str) -> list[str]:
    return sorted(f[:-5] for f in os.listdir(directory) if f.endswith(".json"))
''',
        "test": '''\
from exercises.stage09.basic01.solution import (
    config_path,
    config_exists,
    save_config,
    load_config,
    list_config_names,
)


def test_config_path_joins_directory_and_json_suffix():
    """config_path == os.path.join(directory, name + ".json")."""
    assert config_path("dir", "app") in ("dir/app.json", "dir\\\\app.json")


def test_config_exists_before_and_after_save(tmp_path):
    """config_exists uses os.path.exists against the computed config_path."""
    d = str(tmp_path)
    assert config_exists(d, "app") is False
    save_config(d, "app", {"debug": True})
    assert config_exists(d, "app") is True


def test_save_and_load_config_roundtrip(tmp_path):
    """save_config writes JSON; load_config reads it back via json.load."""
    d = str(tmp_path)
    save_config(d, "app", {"debug": True, "retries": 3})
    assert load_config(d, "app") == {"debug": True, "retries": 3}


def test_list_config_names_strips_json_suffix(tmp_path):
    """list_config_names must list only *.json files, sorted, with the suffix stripped."""
    d = str(tmp_path)
    save_config(d, "app", {})
    save_config(d, "db", {})
    (tmp_path / "notes.txt").write_text("ignore me")
    assert list_config_names(d) == ["app", "db"]
''',
    },
    {
        "name": "basic02",
        "title": "Library Catalog: Dates and XML",
        "summary": "datetime.now/isoformat, ElementTree.parse/findall",
        "readme": (
            "A tiny library catalog stored as XML, plus a timestamp "
            "helper. Given XML shaped like:\n\n"
            "```xml\n"
            "<library>\n"
            '  <book id="1"><title>Dune</title></book>\n'
            '  <book id="2"><title>Foundation</title></book>\n'
            "</library>\n"
            "```\n\n"
            "Implement:\n\n"
            "- `catalog_timestamp() -> str` -- "
            "`datetime.datetime.now().isoformat()`.\n"
            "- `parse_catalog_titles(path: str) -> list[str]` -- "
            "`ET.parse(path).getroot()`, then `[el.text for el in "
            "root.findall(\".//title\")]` (`.//title` finds every "
            "`<title>` element anywhere in the tree, at any depth).\n"
            "- `parse_catalog_titles_from_string(xml_string: str) -> list[str]` "
            "-- the same idea, but parse an in-memory string with "
            "`ET.fromstring(...)` instead of a file with `ET.parse(...)`.\n"
            "- `count_catalog_books(path: str) -> int` -- "
            "`len(root.findall(\".//book\"))`.\n\n"
            "See the Study Reference presentation, Topic 9 (Basic tier), "
            "for the theory."
        ),
        "stub": '''\
import datetime
import xml.etree.ElementTree as ET


def catalog_timestamp() -> str:
    """datetime.datetime.now().isoformat()."""
    raise NotImplementedError


def parse_catalog_titles(path: str) -> list[str]:
    """ET.parse(path).getroot(), then every <title> element's text."""
    raise NotImplementedError


def parse_catalog_titles_from_string(xml_string: str) -> list[str]:
    """Same as parse_catalog_titles, but via ET.fromstring(xml_string)."""
    raise NotImplementedError


def count_catalog_books(path: str) -> int:
    """How many <book> elements exist anywhere in the tree."""
    raise NotImplementedError
''',
        "reference": '''\
import datetime
import xml.etree.ElementTree as ET


def catalog_timestamp() -> str:
    return datetime.datetime.now().isoformat()


def parse_catalog_titles(path: str) -> list[str]:
    root = ET.parse(path).getroot()
    return [el.text for el in root.findall(".//title")]


def parse_catalog_titles_from_string(xml_string: str) -> list[str]:
    root = ET.fromstring(xml_string)
    return [el.text for el in root.findall(".//title")]


def count_catalog_books(path: str) -> int:
    root = ET.parse(path).getroot()
    return len(root.findall(".//book"))
''',
        "test": '''\
import datetime
from exercises.stage09.basic02.solution import (
    catalog_timestamp,
    parse_catalog_titles,
    parse_catalog_titles_from_string,
    count_catalog_books,
)

LIBRARY_XML = (
    "<library>"
    '<book id="1"><title>Dune</title></book>'
    '<book id="2"><title>Foundation</title></book>'
    "</library>"
)


def test_catalog_timestamp_is_parseable_isoformat():
    """catalog_timestamp must be a real datetime.now().isoformat() string."""
    text = catalog_timestamp()
    parsed = datetime.datetime.fromisoformat(text)
    assert isinstance(parsed, datetime.datetime)


def test_parse_catalog_titles(tmp_path):
    """parse_catalog_titles uses ET.parse + .//title to collect every title's text."""
    path = tmp_path / "library.xml"
    path.write_text(LIBRARY_XML)
    assert parse_catalog_titles(str(path)) == ["Dune", "Foundation"]


def test_parse_catalog_titles_from_string():
    """parse_catalog_titles_from_string uses ET.fromstring instead of ET.parse."""
    assert parse_catalog_titles_from_string(LIBRARY_XML) == ["Dune", "Foundation"]


def test_count_catalog_books(tmp_path):
    """count_catalog_books == len(root.findall(".//book"))."""
    path = tmp_path / "library.xml"
    path.write_text(LIBRARY_XML)
    assert count_catalog_books(str(path)) == 2
''',
    },
    {
        "name": "mid01",
        "title": "pathlib: The Modern os.path Alternative",
        "summary": "pathlib.Path, pathlib as the modern os.path alternative",
        "readme": (
            "Redo the filesystem operations from the Basic tier's "
            "`os.path`/`os.listdir` using `pathlib.Path` instead -- the "
            "modern, more readable alternative. Implement:\n\n"
            "- `list_entries(directory: str) -> list[str]` -- "
            "`sorted(p.name for p in pathlib.Path(directory).iterdir())` "
            "-- the `pathlib` equivalent of `os.listdir`.\n"
            "- `build_path(directory: str, filename: str) -> pathlib.Path` "
            "-- `pathlib.Path(directory) / filename`. `pathlib.Path` "
            "supports `/` for joining paths -- no `os.path.join(...)` "
            "call needed.\n"
            "- `read_and_write_pathlib(path: str, content: str) -> str` -- "
            "`pathlib.Path(path).write_text(content)`, then return "
            "`pathlib.Path(path).read_text()`. `.read_text()`/"
            "`.write_text()` are built directly into `Path`, unlike "
            "`os.path`, which only gives you path strings and leaves "
            "actually opening files to `open()`.\n"
            "- `find_txt_files(root: str) -> list[str]` -- "
            "`sorted(p.name for p in pathlib.Path(root).rglob(\"*.txt\"))` "
            "(a recursive glob -- searches `root` and every subdirectory "
            "beneath it for files matching `*.txt`, no `os.walk` loop "
            "needed).\n\n"
            "See the Study Reference presentation, Topic 9 (Mid tier), "
            "for the theory."
        ),
        "stub": '''\
import pathlib


def list_entries(directory: str) -> list[str]:
    """sorted(p.name for p in pathlib.Path(directory).iterdir())."""
    raise NotImplementedError


def build_path(directory: str, filename: str) -> pathlib.Path:
    """pathlib.Path(directory) / filename."""
    raise NotImplementedError


def read_and_write_pathlib(path: str, content: str) -> str:
    """Write content via Path.write_text, then return Path.read_text()."""
    raise NotImplementedError


def find_txt_files(root: str) -> list[str]:
    """sorted(p.name for p in pathlib.Path(root).rglob("*.txt"))."""
    raise NotImplementedError
''',
        "reference": '''\
import pathlib


def list_entries(directory: str) -> list[str]:
    return sorted(p.name for p in pathlib.Path(directory).iterdir())


def build_path(directory: str, filename: str) -> pathlib.Path:
    return pathlib.Path(directory) / filename


def read_and_write_pathlib(path: str, content: str) -> str:
    pathlib.Path(path).write_text(content)
    return pathlib.Path(path).read_text()


def find_txt_files(root: str) -> list[str]:
    return sorted(p.name for p in pathlib.Path(root).rglob("*.txt"))
''',
        "test": '''\
import pathlib
from exercises.stage09.mid01.solution import (
    list_entries,
    build_path,
    read_and_write_pathlib,
    find_txt_files,
)


def test_list_entries(tmp_path):
    """list_entries is the pathlib equivalent of os.listdir, via .iterdir()."""
    (tmp_path / "b.txt").write_text("b")
    (tmp_path / "a.txt").write_text("a")
    assert list_entries(str(tmp_path)) == ["a.txt", "b.txt"]


def test_build_path_uses_slash_operator_and_returns_a_path():
    """build_path must return an actual pathlib.Path, built with the / operator."""
    result = build_path("some/dir", "file.txt")
    assert isinstance(result, pathlib.Path)
    assert result.name == "file.txt"


def test_read_and_write_pathlib_roundtrip(tmp_path):
    """read_and_write_pathlib uses Path.write_text then Path.read_text, no open() needed."""
    path = tmp_path / "note.txt"
    result = read_and_write_pathlib(str(path), "hello")
    assert result == "hello"


def test_find_txt_files_recursive_glob(tmp_path):
    """find_txt_files uses Path.rglob("*.txt") to search recursively, with no manual os.walk loop."""
    (tmp_path / "a.txt").write_text("a")
    sub = tmp_path / "sub"
    sub.mkdir()
    (sub / "b.txt").write_text("b")
    (sub / "c.py").write_text("c")
    assert find_txt_files(str(tmp_path)) == ["a.txt", "b.txt"]
''',
    },
    {
        "name": "mid02",
        "title": "Timezone-Aware Timestamps in JSON",
        "summary": "json.dumps(default=...), timezone-aware vs naive datetimes",
        "readme": (
            "`datetime.datetime` isn't one of the handful of types "
            "`json.dumps` knows how to serialize natively -- and naive "
            "vs. timezone-aware matters even before you get that far. "
            "Implement:\n\n"
            "- `aware_now_utc()` -- "
            "`datetime.datetime.now(datetime.timezone.utc)` -- **aware**: "
            "explicitly anchored to UTC.\n"
            "- `is_timezone_aware(dt) -> bool` -- `dt.tzinfo is not None "
            "and dt.tzinfo.utcoffset(dt) is not None` (the official "
            "recipe -- just checking `dt.tzinfo is not None` isn't quite "
            "enough in every edge case, though it's right for the "
            "objects these exercises produce).\n"
            "- `make_aware(dt, tz)` -- `dt.replace(tzinfo=tz)` (attaches "
            "a timezone to a naive datetime *without* shifting the clock "
            "time -- for that, you'd use `.astimezone()` instead).\n"
            "- `datetime_default(obj)` -- if `obj` is a "
            "`datetime.datetime`, return `obj.isoformat()`; else "
            "`raise TypeError(f\"not JSON serializable: {obj!r}\")`. This "
            "is a `default=` function for `json.dumps`: it's called for "
            "any object `json.dumps` doesn't natively know how to "
            "handle, and must return something JSON-serializable (or "
            "raise).\n"
            "- `serialize_event(name: str, timestamp) -> str` -- "
            "`json.dumps({\"name\": name, \"timestamp\": timestamp}, "
            "default=datetime_default)`.\n\n"
            "Put together: build a naive `datetime`, make it "
            "timezone-aware with `make_aware`, then hand it to "
            "`serialize_event` -- `json.dumps` calls `datetime_default` "
            "under the hood to turn that aware datetime into an ISO "
            "string (complete with its `+00:00` UTC offset) in the JSON "
            "output.\n\n"
            "See the Study Reference presentation, Topic 9 (Mid tier), "
            "for the theory."
        ),
        "stub": '''\
import datetime
import json


def aware_now_utc():
    """datetime.datetime.now(datetime.timezone.utc)."""
    raise NotImplementedError


def is_timezone_aware(dt) -> bool:
    """dt.tzinfo is not None and dt.tzinfo.utcoffset(dt) is not None."""
    raise NotImplementedError


def make_aware(dt, tz):
    """dt.replace(tzinfo=tz)."""
    raise NotImplementedError


def datetime_default(obj):
    """obj.isoformat() for a datetime.datetime, else raise TypeError."""
    raise NotImplementedError


def serialize_event(name: str, timestamp) -> str:
    """json.dumps({"name": name, "timestamp": timestamp}, default=datetime_default)."""
    raise NotImplementedError
''',
        "reference": '''\
import datetime
import json


def aware_now_utc():
    return datetime.datetime.now(datetime.timezone.utc)


def is_timezone_aware(dt) -> bool:
    return dt.tzinfo is not None and dt.tzinfo.utcoffset(dt) is not None


def make_aware(dt, tz):
    return dt.replace(tzinfo=tz)


def datetime_default(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    raise TypeError(f"not JSON serializable: {obj!r}")


def serialize_event(name: str, timestamp) -> str:
    return json.dumps({"name": name, "timestamp": timestamp}, default=datetime_default)
''',
        "test": '''\
import json
import datetime
import pytest
from exercises.stage09.mid02.solution import (
    aware_now_utc,
    is_timezone_aware,
    make_aware,
    datetime_default,
    serialize_event,
)


def test_aware_now_utc_is_timezone_aware():
    """aware_now_utc() must produce a genuinely timezone-aware datetime."""
    assert is_timezone_aware(aware_now_utc()) is True


def test_make_aware_attaches_timezone_without_shifting_clock_time():
    """make_aware must attach tzinfo via .replace(), not shift the hour/minute."""
    naive = datetime.datetime(2024, 1, 1, 12, 0, 0)
    assert is_timezone_aware(naive) is False
    aware = make_aware(naive, datetime.timezone.utc)
    assert is_timezone_aware(aware) is True
    assert aware.hour == 12 and aware.year == 2024


def test_datetime_default_converts_to_isoformat():
    """datetime_default must return obj.isoformat() for a datetime.datetime."""
    dt = datetime.datetime(2024, 1, 1, 12, 0, 0, tzinfo=datetime.timezone.utc)
    assert datetime_default(dt) == "2024-01-01T12:00:00+00:00"


def test_datetime_default_raises_type_error_for_other_objects():
    """datetime_default must raise TypeError for anything that isn't a datetime.datetime."""
    with pytest.raises(TypeError):
        datetime_default("not a datetime")


def test_serialize_event_uses_datetime_default_under_the_hood():
    """serialize_event's json.dumps(default=datetime_default) must produce a valid JSON string with the ISO timestamp."""
    aware = make_aware(datetime.datetime(2024, 1, 1, 12, 0, 0), datetime.timezone.utc)
    result = serialize_event("launch", aware)
    assert json.loads(result) == {"name": "launch", "timestamp": "2024-01-01T12:00:00+00:00"}
''',
    },
    {
        "name": "advanced01",
        "title": "Recursing with os.walk: File Discovery",
        "summary": "os.walk()",
        "readme": (
            "`os.walk(root)` yields `(dirpath, dirnames, filenames)` for "
            "the root directory and every subdirectory beneath it, one "
            "level per iteration -- the classic way to process an entire "
            "directory tree without recursing yourself. Implement:\n\n"
            "- `find_all_py_files(root: str) -> list[str]` -- walk `root` "
            "with `os.walk(root)`, collecting the full path "
            "(`os.path.join(dirpath, name)`) of every file ending in "
            "`.py`; return the sorted list.\n"
            "- `count_files_by_extension(root: str) -> dict` -- walk "
            "`root` with `os.walk`, building `{extension: count}` via "
            "`os.path.splitext(name)`.\n\n"
            "See the Study Reference presentation, Topic 9 (Advanced "
            "tier), for the theory."
        ),
        "stub": '''\
import os


def find_all_py_files(root: str) -> list[str]:
    """Every .py file under root (os.walk), full paths, sorted."""
    raise NotImplementedError


def count_files_by_extension(root: str) -> dict:
    """{extension: count} for every file under root (os.walk)."""
    raise NotImplementedError
''',
        "reference": '''\
import os


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
''',
        "test": '''\
from exercises.stage09.advanced01.solution import find_all_py_files, count_files_by_extension


def _make_tree(tmp_path):
    (tmp_path / "a.py").write_text("x = 1")
    (tmp_path / "b.txt").write_text("hello")
    sub = tmp_path / "sub"
    sub.mkdir()
    (sub / "c.py").write_text("y = 2")
    (sub / "d.txt").write_text("world")
    return tmp_path


def test_find_all_py_files_walks_the_whole_tree(tmp_path):
    """find_all_py_files must use os.walk to find .py files at every depth, not just the top level."""
    _make_tree(tmp_path)
    result = find_all_py_files(str(tmp_path))
    assert len(result) == 2
    assert all(p.endswith(".py") for p in result)


def test_count_files_by_extension(tmp_path):
    """count_files_by_extension builds {extension: count} via os.walk + os.path.splitext."""
    _make_tree(tmp_path)
    result = count_files_by_extension(str(tmp_path))
    assert result == {".py": 2, ".txt": 2}
''',
    },
    {
        "name": "advanced02",
        "title": "Recursing with os.walk: Size and Depth",
        "summary": "os.walk() (two more scenarios)",
        "readme": (
            "Two more `os.walk`-based traversals. Implement:\n\n"
            "- `total_size_of_directory(root: str) -> int` -- walk `root` "
            "with `os.walk`, summing `os.path.getsize(...)` over every "
            "file.\n"
            "- `max_directory_depth(root: str) -> int` -- walk `root` "
            "with `os.walk`; for each `dirpath`, compute its depth "
            "relative to `root` (`0` for `root` itself, `1` for a direct "
            "subdirectory, and so on) via "
            "`os.path.relpath(dirpath, root)` (which is `\".\"` for "
            "`root` itself, or a path like `\"sub/subsub\"` whose "
            "`os.sep`-separated part count gives the depth); return the "
            "largest depth seen.\n\n"
            "Same tool as the previous exercise, two different "
            "aggregations over the same kind of walk: one summing a "
            "number per file, the other tracking how deep the tree goes.\n\n"
            "See the Study Reference presentation, Topic 9 (Advanced "
            "tier), for the theory."
        ),
        "stub": '''\
import os


def total_size_of_directory(root: str) -> int:
    """Sum of os.path.getsize() over every file under root (os.walk)."""
    raise NotImplementedError


def max_directory_depth(root: str) -> int:
    """Largest depth of any directory under root, via os.walk + os.path.relpath."""
    raise NotImplementedError
''',
        "reference": '''\
import os


def total_size_of_directory(root: str) -> int:
    total = 0
    for dirpath, dirnames, filenames in os.walk(root):
        for name in filenames:
            total += os.path.getsize(os.path.join(dirpath, name))
    return total


def max_directory_depth(root: str) -> int:
    max_depth = 0
    for dirpath, dirnames, filenames in os.walk(root):
        rel = os.path.relpath(dirpath, root)
        depth = 0 if rel == "." else len(rel.split(os.sep))
        max_depth = max(max_depth, depth)
    return max_depth
''',
        "test": '''\
from exercises.stage09.advanced02.solution import total_size_of_directory, max_directory_depth


def _make_tree(tmp_path):
    (tmp_path / "a.py").write_text("x = 1")
    (tmp_path / "b.txt").write_text("hello")
    sub = tmp_path / "sub"
    sub.mkdir()
    (sub / "c.py").write_text("y = 2")
    (sub / "d.txt").write_text("world")
    return tmp_path


def test_total_size_of_directory(tmp_path):
    """total_size_of_directory sums os.path.getsize() across every file found by os.walk."""
    _make_tree(tmp_path)
    assert total_size_of_directory(str(tmp_path)) == len("x = 1") + len("hello") + len("y = 2") + len("world")


def test_max_directory_depth_at_root_level(tmp_path):
    """A directory with only top-level files has max depth 0."""
    (tmp_path / "a.txt").write_text("a")
    assert max_directory_depth(str(tmp_path)) == 0


def test_max_directory_depth_with_nested_subdirectories(tmp_path):
    """max_directory_depth must track the deepest subdirectory reached during the os.walk."""
    sub = tmp_path / "sub"
    sub.mkdir()
    subsub = sub / "subsub"
    subsub.mkdir()
    (subsub / "deep.txt").write_text("deep")
    assert max_directory_depth(str(tmp_path)) == 2
''',
    },
]
