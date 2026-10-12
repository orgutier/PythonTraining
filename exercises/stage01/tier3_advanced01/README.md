# Exact Ledger vs. Float Drift

An invoicing system needs exact currency totals, but float arithmetic can't reliably give you that. Given, don't modify:

```python
price_each_text = "19.99"
quantity_text = "7"
```

Using Advanced-tier tools (`decimal.Decimal`, `math.isclose`), write plain top-level code that computes:

- `price_each_float` (`float`), `quantity` (`int`).
- `float_total` -- `price_each_float * quantity`, plain float arithmetic.
- `exact_total` -- a `decimal.Decimal`, built from `Decimal(price_each_text) * Decimal(quantity_text)` -- **construct both `Decimal`s from the original string text, not from the float** (`Decimal(price_each_float)` would already have inherited the float's rounding error before you even start).
- `totals_are_exactly_equal` -- `float(exact_total) == float_total`.
- `totals_are_close` -- `math.isclose(float(exact_total), float_total)`. (`math.isclose` is the correct way to compare floats; a bare `==` is not reliable, which is exactly what the previous two variables demonstrate.)
- The textbook version of the same lesson, with fixed literals (not derived from the ledger above): `point_one_plus_point_two = 0.1 + 0.2`, `is_exactly_point_three = point_one_plus_point_two == 0.3`, and `is_close_to_point_three = math.isclose(point_one_plus_point_two, 0.3)`.

Finish with one `print()` call (f-strings are fine now) reporting `exact_total` and whether the two totals matched exactly.
