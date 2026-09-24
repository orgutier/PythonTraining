# Recursing with os.walk: File Discovery

`os.walk(root)` yields `(dirpath, dirnames, filenames)` for the root directory and every subdirectory beneath it, one level per iteration -- the classic way to process an entire directory tree without recursing yourself. Implement:

- `find_all_py_files(root: str) -> list[str]` -- walk `root` with `os.walk(root)`, collecting the full path (`os.path.join(dirpath, name)`) of every file ending in `.py`; return the sorted list.
- `count_files_by_extension(root: str) -> dict` -- walk `root` with `os.walk`, building `{extension: count}` via `os.path.splitext(name)`.

See the Study Reference presentation, Topic 9 (Advanced tier), for the theory.
