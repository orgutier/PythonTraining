# Functools Toolbox

Implement three `functools.lru_cache`-decorated functions and three helpers built around `functools.partial`:

- `cached_fibonacci(n: int) -> int` -- recursive Fibonacci, decorated with `@functools.lru_cache(maxsize=None)`.
- `cached_is_prime(n: int) -> bool` -- primality check, same decorator.
- `cached_factorial(n: int) -> int` -- recursive factorial, same decorator.

- `add(a: int, b: int) -> int` / `multiply(a: int, b: int) -> int` / `format_currency(amount: float, symbol: str) -> str` (`f"{symbol}{amount:.2f}"`) -- three plain two-argument helpers.
- `make_adder(n: int)` -- return `functools.partial(add, n)`.
- `make_multiplier_via_partial(n: int)` -- return `functools.partial(multiply, n)`.
- `make_usd_formatter()` -- return `functools.partial(format_currency, symbol="$")`.

The tests check `hasattr(fn, "cache_info")` and `isinstance(fn, functools.partial)` respectively -- those only pass if you actually used the decorator/`functools.partial`, not just a hand-written equivalent.

See the Study Reference presentation, Topic 3, for the theory.
