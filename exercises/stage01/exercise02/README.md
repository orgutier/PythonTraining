# Temperature and BMI

Implement:

- `celsius_to_fahrenheit(celsius: float) -> float` -- the standard conversion `celsius * 9 / 5 + 32`.
- `bmi_calculator(weight_kg: float, height_m: float) -> float` -- `weight_kg / height_m ** 2`, rounded to 2 decimals.
- `validate_measurement(value) -> bool` -- return `True` only if `value` is an `int` or `float` **and not** a `bool`. This matters because in Python `bool` is a subclass of `int`, so `isinstance(True, int)` is `True` -- a naive `isinstance(value, (int, float))` check would wrongly accept `True`/`False` as measurements. You have to check `isinstance()` twice and combine the two with `and`/`not`.

See the Study Reference presentation, Topic 1, for the theory.
