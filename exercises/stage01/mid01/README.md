# Precision Price Comparator

Two suppliers quote prices for the same part; you're comparing them for a bulk order. Given, don't modify:

```python
price_a_text = "19.99"
price_b_text = "18.995"
quantity_text = "4"
```

Using Mid-tier tools this time (f-strings, the walrus operator, chained comparisons, augmented assignment, operator precedence -- still no `if`/`for`/`while`), write plain top-level code that computes:

- `price_a`, `price_b` (`float`), `quantity` (`int`).
- `savings_message` -- an f-string that computes the total savings of buying `quantity` units from the cheaper supplier **using the walrus operator inside the f-string's expression** to both compute and capture a `savings` value in one go, e.g. shaped like `f"...{(savings := abs(price_a - price_b) * quantity):.2f}..."`. After this line, `savings` must exist as its own module-level name too (that's exactly what the walrus operator gives you -- the assignment happens as a side effect of evaluating the f-string expression, so you're not computing the value twice).
- `both_under_20` -- `True` iff *both* prices are in `[0, 20)`, written as **one chained comparison** per price, combined with `and` (`0 <= price_a < 20 and 0 <= price_b < 20`).
- `total_cost` -- start it at `0.0`, then use **augmented assignment** (`+=`) twice, once per supplier's `price * quantity`, to build up the total (don't just write `price_a * quantity + price_b * quantity` directly -- the point here is practicing `+=`).
- `weighted_score` -- `2 + 3 * price_a ** 2`, written in exactly that form so you have to get the precedence right (`**` binds tighter than `*`, which binds tighter than `+`) rather than adding parentheses to force the order yourself.

Finish with `print(savings_message)`.
