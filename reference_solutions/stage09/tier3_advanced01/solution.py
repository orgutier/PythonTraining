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
