# pathlib: The Modern os.path Alternative

Redo the filesystem operations from the Basic tier's `os.path`/`os.listdir` using `pathlib.Path` instead -- the modern, more readable alternative. Implement:

- `list_entries(directory: str) -> list[str]` -- `sorted(p.name for p in pathlib.Path(directory).iterdir())` -- the `pathlib` equivalent of `os.listdir`.
- `build_path(directory: str, filename: str) -> pathlib.Path` -- `pathlib.Path(directory) / filename`. `pathlib.Path` supports `/` for joining paths -- no `os.path.join(...)` call needed.
- `read_and_write_pathlib(path: str, content: str) -> str` -- `pathlib.Path(path).write_text(content)`, then return `pathlib.Path(path).read_text()`. `.read_text()`/`.write_text()` are built directly into `Path`, unlike `os.path`, which only gives you path strings and leaves actually opening files to `open()`.
- `find_txt_files(root: str) -> list[str]` -- `sorted(p.name for p in pathlib.Path(root).rglob("*.txt"))` (a recursive glob -- searches `root` and every subdirectory beneath it for files matching `*.txt`, no `os.walk` loop needed).

See the Study Reference presentation, Topic 9 (Mid tier), for the theory.
