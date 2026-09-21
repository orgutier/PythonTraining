import datetime
from challenges.challenge17.solution import (
    scan_directory_report,
    save_report,
    load_report,
    list_py_files_pathlib,
)


def _make_tree(tmp_path):
    (tmp_path / "a.py").write_text("x = 1")
    sub = tmp_path / "sub"
    sub.mkdir()
    (sub / "b.py").write_text("y = 2")
    (sub / "c.txt").write_text("hello")
    return tmp_path


def test_scan_directory_report_basic(tmp_path):
    _make_tree(tmp_path)
    report = scan_directory_report(str(tmp_path))
    assert report["total_files"] == 3
    assert report["total_size"] == len("x = 1") + len("y = 2") + len("hello")
    assert all(isinstance(f["modified"], datetime.datetime) for f in report["files"])


def test_scan_directory_report_empty(tmp_path):
    report = scan_directory_report(str(tmp_path))
    assert report == {"total_files": 0, "total_size": 0, "files": []}


def test_scan_directory_report_sorted_by_path(tmp_path):
    _make_tree(tmp_path)
    report = scan_directory_report(str(tmp_path))
    paths = [f["path"] for f in report["files"]]
    assert paths == sorted(paths)


def test_save_and_load_report_roundtrip(tmp_path):
    _make_tree(tmp_path)
    report = scan_directory_report(str(tmp_path))
    out_path = str(tmp_path / "report.json")
    save_report(report, out_path)
    loaded = load_report(out_path)
    assert loaded["total_files"] == report["total_files"]
    assert isinstance(loaded["files"][0]["modified"], datetime.datetime)


def test_list_py_files_pathlib(tmp_path):
    _make_tree(tmp_path)
    result = list_py_files_pathlib(str(tmp_path))
    assert len(result) == 2
    assert all(p.endswith(".py") for p in result)
