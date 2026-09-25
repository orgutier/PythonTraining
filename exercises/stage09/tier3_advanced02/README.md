# Recursing with os.walk: Size and Depth

Two more `os.walk`-based traversals. Implement:

- `total_size_of_directory(root: str) -> int` -- walk `root` with `os.walk`, summing `os.path.getsize(...)` over every file.
- `max_directory_depth(root: str) -> int` -- walk `root` with `os.walk`; for each `dirpath`, compute its depth relative to `root` (`0` for `root` itself, `1` for a direct subdirectory, and so on) via `os.path.relpath(dirpath, root)` (which is `"."` for `root` itself, or a path like `"sub/subsub"` whose `os.sep`-separated part count gives the depth); return the largest depth seen.

Same tool as the previous exercise, two different aggregations over the same kind of walk: one summing a number per file, the other tracking how deep the tree goes.

See the Study Reference presentation, Topic 9 (Advanced tier), for the theory.
