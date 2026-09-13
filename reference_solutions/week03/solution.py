def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("factorial is not defined for negative numbers")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("fibonacci is not defined for negative numbers")
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
