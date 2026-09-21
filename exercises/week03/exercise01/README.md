# Recursion Basics

Implement two classic recursive functions:

- `factorial(n: int) -> int` -- `n!`. **Must** be recursive, not a loop: base case `n in (0, 1)` returns `1`; otherwise `n * factorial(n - 1)`. Raise `ValueError` for negative `n`.
- `fibonacci(n: int) -> int` -- the nth Fibonacci number (0-indexed). **Must** be recursive: base case `n in (0, 1)` returns `n`; otherwise `fibonacci(n - 1) + fibonacci(n - 2)`.

The tests only check the *output* -- an iterative version would technically pass -- but the point of this exercise is the recursive pattern itself (base case + a call to yourself on a smaller input), which the next seven exercises' closures and decorators build on.

See the Study Reference presentation, Topic 3, for the theory.
