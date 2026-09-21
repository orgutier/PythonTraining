# Number Patterns

Implement:

- `fizzbuzz(n: int) -> list[str]` -- the classic: for `1..n`, `"FizzBuzz"` if divisible by 15, `"Fizz"` by 3, `"Buzz"` by 5, else `str(i)`.
- `is_prime(n: int) -> bool` -- implement with a `for...else`: loop `i` over `range(2, int(n ** 0.5) + 1)`, `break` the moment you find a factor; the loop's `else` clause (which only runs if the loop finished *without* breaking) is where you return `True`. This is the cleanest way to express "found something -> stop early" vs. "searched everything, found nothing" without a separate flag variable.

See the Study Reference presentation, Topic 2, for the theory.
