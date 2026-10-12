# Testing Without a Framework: Catch the Bug

Every other exercise in this stage asked you to implement something. This one asks you to **verify** something -- the instinct you'll need for the rest of your career, long before (and long after) any test framework is involved. You will **not** import `pytest`, `unittest`, or anything like them in this file -- just plain Python comparisons.

Given, don't modify (both pairs below are *supposed* to compute the same thing -- at least one of each pair has a bug; your job is to catch it by testing, not to fix it):

```python
price_text = "19.99"
quantity_text = "3"
discount_flag_text = "False"

target_total_v1 = float(price_text) * int(quantity_text)
target_total_v2 = float(price_text) + int(quantity_text)

target_is_discounted_v1 = discount_flag_text == "True"
target_is_discounted_v2 = bool(discount_flag_text)
```

The spec each pair is supposed to meet:

- **total** should equal `price * quantity`.
- **is_discounted** should be `True` only if `discount_flag_text` is literally the string `"True"`.

Write plain top-level code that:

- Builds `check_results` -- a list of `(description, passed)` tuples, `description` a short string and `passed` a `bool` -- with **exactly one entry per target value above** (four total): compute the expected value from the spec yourself (e.g. `float(price_text) * int(quantity_text)`), compare it against the target with `==`, and append the result. No `assert` -- a failing comparison should become a recorded `False`, not a crash that stops the remaining checks from running.
- `total_checks` -- `len(check_results)`.
- `passed_checks` -- how many entries in `check_results` passed.
- `failed_descriptions` -- the `description` of every entry that did **not** pass, in order.

If you did this right, `passed_checks` won't be `4` -- and that's the point: a check written against the *spec* (not against "whatever the target already returns") is what catches a real bug instead of just rubber-stamping it.

See the Study Reference presentation, Topic 1, for the theory.
