# Marathon Pace Report

A runner's marathon result needs analyzing. Given, don't modify:

```python
race_distance_km_text = "42.195"
elapsed_minutes_text = "255"
target_minutes_text = "240"
```

Same Mid-tier toolbox as the previous exercise, different combination -- write plain top-level code that computes:

- `race_distance_km` (`float`), `elapsed_minutes`, `target_minutes` (`int`).
- `pace_min_per_km` -- `elapsed_minutes / race_distance_km`.
- `pace_report` -- an f-string that uses the **walrus operator** to compute and capture `minutes_over` (`elapsed_minutes - target_minutes`) as part of building the message, e.g. shaped like `f"...{(minutes_over := elapsed_minutes - target_minutes)}...{pace_min_per_km:.2f}..."`. `minutes_over` must exist as its own module-level name afterward.
- `minutes_over_per_km` -- `minutes_over / race_distance_km`, computed using the `minutes_over` the walrus operator gave you (don't recompute `elapsed_minutes - target_minutes` a second time).
- `on_pace` -- `True` iff `pace_min_per_km` is strictly greater than `0` and at most `6.5`, written as **one chained comparison**: `0 < pace_min_per_km <= 6.5`.
- `total_penalty_seconds` -- start it at `0`, then use **augmented assignment** twice: add a flat `30`, then add `minutes_over * 2`.
- `fatigue_index` -- `2 + 3 * pace_min_per_km ** 2`, written in exactly that form (precedence, no extra parentheses).

Finish with `print(pace_report)`.
