import os
import json
import datetime
import pathlib


def scan_directory_report(root: str) -> dict:
    """
    Walk root, reporting size and modified time per file.

    Edge cases handled:
      - Empty directory -> {"total_files": 0, "total_size": 0, "files": []}.
      - Files nested several subdirectories deep -> still found, since
        os.walk recurses into every subdirectory by default.
    """
    files = []
    for dirpath, dirnames, filenames in os.walk(root):
        for name in filenames:
            full_path = os.path.join(dirpath, name)
            files.append({
                "path": full_path,
                "size": os.path.getsize(full_path),
                "modified": datetime.datetime.fromtimestamp(os.path.getmtime(full_path)),
            })
    files.sort(key=lambda f: f["path"])
    return {
        "total_files": len(files),
        "total_size": sum(f["size"] for f in files),
        "files": files,
    }


def _json_default(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    raise TypeError(f"not JSON serializable: {obj!r}")


def save_report(report: dict, path: str) -> None:
    with open(path, "w") as f:
        json.dump(report, f, default=_json_default)


def load_report(path: str) -> dict:
    with open(path) as f:
        report = json.load(f)
    for entry in report["files"]:
        entry["modified"] = datetime.datetime.fromisoformat(entry["modified"])
    return report


def list_py_files_pathlib(root: str) -> list:
    return sorted(str(p) for p in pathlib.Path(root).rglob("*.py"))
