import pathlib


def list_entries(directory: str) -> list[str]:
    return sorted(p.name for p in pathlib.Path(directory).iterdir())


def build_path(directory: str, filename: str) -> pathlib.Path:
    return pathlib.Path(directory) / filename


def read_and_write_pathlib(path: str, content: str) -> str:
    pathlib.Path(path).write_text(content)
    return pathlib.Path(path).read_text()


def find_txt_files(root: str) -> list[str]:
    return sorted(p.name for p in pathlib.Path(root).rglob("*.txt"))
