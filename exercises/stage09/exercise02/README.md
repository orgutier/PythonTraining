# Recursive Traversal

Implement:

- `find_all_py_files(root: str) -> list[str]` -- walk `root` with `os.walk(root)`, collecting the full path (`os.path.join(dirpath, name)`) of every file ending in `.py`; return the sorted list.
- `count_files_by_extension(root: str) -> dict` -- walk `root` with `os.walk`, building `{extension: count}` via `os.path.splitext(name)`.
- `total_size_of_directory(root: str) -> int` -- walk `root` with `os.walk`, summing `os.path.getsize(...)` over every file.
- `find_txt_files_pathlib(root: str) -> list[str]` -- the `pathlib` equivalent of a recursive search: `sorted(p.name for p in pathlib.Path(root).rglob("*.txt"))`.

`os.walk` yields `(dirpath, dirnames, filenames)` for the root directory and every subdirectory beneath it, one level per iteration -- the classic way to process an entire directory tree without recursing yourself.

See the Study Reference presentation, Topic 9, for the theory.
