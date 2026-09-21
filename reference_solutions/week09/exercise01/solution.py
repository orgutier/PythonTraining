import os
import pathlib


def list_files(directory: str) -> list[str]:
    return sorted(os.listdir(directory))


def join_path(directory: str, filename: str) -> str:
    return os.path.join(directory, filename)


def file_exists(path: str) -> bool:
    return os.path.exists(path)


def list_files_pathlib(directory: str) -> list[str]:
    return sorted(p.name for p in pathlib.Path(directory).iterdir())


def read_text_pathlib(path: str) -> str:
    return pathlib.Path(path).read_text()
