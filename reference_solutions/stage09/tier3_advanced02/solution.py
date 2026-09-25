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
