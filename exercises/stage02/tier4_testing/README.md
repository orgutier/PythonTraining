# Testing Without a Framework: Catch the Bug

Every other exercise in this stage asked you to implement something. This one asks you to **verify** something. You will **not** import `pytest`, `unittest`, or anything like them in this file -- just plain Python comparisons and loops.

Given, don't modify (both pairs below are *supposed* to compute the same thing over `numbers`/`threshold` -- at least one of each pair has a bug; your job is to catch it by testing, not to fix it):

```python
numbers = [4, 7, 2, 9, 3, 5, 8]
threshold = 5

target_count_v1 = 0
for n in numbers:
    if n > threshold:
        target_count_v1 += 1

target_count_v2 = 0
for n in numbers:
    if n >= threshold:
        target_count_v2 += 1

target_first_over_v1 = None
for n in numbers:
    if n > threshold:
        target_first_over_v1 = n
        break

target_first_over_v2 = None
for n in numbers:
    if n > threshold:
        target_first_over_v2 = n
```

The spec each pair is supposed to meet:

- **count** should be how many numbers are **strictly greater than** `threshold`.
- **first_over** should be the **first** number strictly greater than `threshold`, in iteration order.

Write plain top-level code that:

- Builds `check_results` -- a list of `(description, passed)` tuples -- with **exactly one entry per target value above** (four total): compute the expected value from the spec yourself (a comprehension or your own loop is fine), compare it against the target with `==`, and append the result. No `assert` -- a failing comparison should become a recorded `False`, not a crash.
- `total_checks` -- `len(check_results)`.
- `passed_checks` -- how many entries in `check_results` passed.
- `failed_descriptions` -- the `description` of every entry that did **not** pass, in order.

See the Study Reference presentation, Topic 2, for the theory.
