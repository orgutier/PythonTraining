# Shift Coverage Checker

A shift roster -- given, don't modify:

```python
scheduled_names = ["Ana", "Ben", "Cy", "Dee", "Ella"]
checked_in_names = ["Ben", "Dee", "Ana"]
shift_hours = [8, 6, 10, 4, 9]
max_hours = 9
```

(`shift_hours[i]` is `scheduled_names[i]`'s scheduled hours.)

Using Mid-tier tools, write plain top-level code that computes:

- `all_checked_in` -- a **`for...else`** loop over `scheduled_names`: if a name isn't in `checked_in_names`, set `all_checked_in = False` and `break`; the loop's `else` clause (only reached if the loop never broke) sets `all_checked_in = True`. Don't pre-initialize `all_checked_in` before the loop -- both branches set it, so it doesn't need one.
- `missing_list` -- a plain `for` loop collecting every scheduled name **not** in `checked_in_names`, in order (not a comprehension -- those aren't introduced until Stage 4).
- `first_missing_has_long_shift` -- **one short-circuit `and` expression**: `len(missing_list) > 0 and shift_hours[scheduled_names.index(missing_list[0])] > max_hours`. The `len(...) > 0` check must come first -- it's what makes indexing `missing_list[0]` safe on the right side.
- `coverage_status` -- a **ternary expression**: `"full"` if `missing_list` is empty, else `"short-staffed"`.
- `overtime_names` -- a plain `for` loop using **`zip(scheduled_names, shift_hours)`** to walk both lists together, collecting every name whose hours exceed `max_hours`.
