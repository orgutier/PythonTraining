# Digit & List Utilities

Implement two small recursive functions and two `lambda`s:

- `count_digits(n: int) -> int` -- the number of digits in a non-negative `n`, **implemented recursively**: base case `n < 10` returns `1`; otherwise `1 + count_digits(n // 10)`.
- `sum_of_squares_recursive(numbers: list) -> int` -- the sum of each number squared, **implemented recursively** over the list: base case `not numbers` returns `0`; otherwise `numbers[0] ** 2 + sum_of_squares_recursive(numbers[1:])`.
- `square` -- a `lambda` equivalent to `lambda x: x * x`.
- `is_even` -- a `lambda` equivalent to `lambda x: x % 2 == 0`.

The two functions must actually recurse (call themselves on a smaller input) rather than use a loop -- that's the point of this exercise, and it's what the tests are checking for by construction (small inputs where a loop would be indistinguishable in output, but the pattern is what Stage 3 is teaching).

See the Study Reference presentation, Topic 3 (Basic tier), for the theory.
