def compute_area(length, width, *, unit="m") -> str:
    return f"{length * width}{unit}^2"


def divide(a, b, /, *, precision=2) -> float:
    return round(a / b, precision)


def connect(host, port, /, *, timeout=30, retries=3) -> dict:
    return {"host": host, "port": port, "timeout": timeout, "retries": retries}


def scale_point(x, y, /, factor=1.0) -> tuple:
    return (x * factor, y * factor)
