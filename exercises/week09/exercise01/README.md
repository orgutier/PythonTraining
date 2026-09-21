# os.path and pathlib Basics

Implement:

- `list_files(directory: str) -> list[str]` -- `sorted(os.listdir(directory))`.
- `join_path(directory: str, filename: str) -> str` -- `os.path.join(directory, filename)`.
- `file_exists(path: str) -> bool` -- `os.path.exists(path)`.
- `list_files_pathlib(directory: str) -> list[str]` -- `sorted(p.name for p in pathlib.Path(directory).iterdir())` -- the `pathlib` equivalent of `list_files` above.
- `read_text_pathlib(path: str) -> str` -- `pathlib.Path(path).read_text()`.

`pathlib.Path` objects support `/` for joining (`Path(directory) / filename`), have `.read_text()`/`.write_text()` built in, and are generally the modern, more readable alternative to `os.path`'s string-joining functions -- both are shown here so you recognize either style in the wild.

See the Study Reference presentation, Topic 9, for the theory.
