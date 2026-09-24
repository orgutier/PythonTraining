def write_lines(path: str, lines: list[str]) -> None:
    with open(path, "w") as f:
        for line in lines:
            f.write(line + "\n")


def read_lines(path: str) -> list[str]:
    with open(path) as f:
        return f.read().splitlines()


def append_line(path: str, line: str) -> None:
    with open(path, "a") as f:
        f.write(line + "\n")


def count_lines(path: str) -> int:
    with open(path) as f:
        return len(f.read().splitlines())
