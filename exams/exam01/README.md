# Exam 1 -- Order Processing Pipeline

Covers: Stages 1-4

An evaluation exam, not a graded exercise: it exists to prove you can
combine Stage 1-4 material (Python Fundamentals, Control Flow, Functions,
Data Structures) in one piece of working code, the way a real script
would, instead of drilling each idea in isolation. Unlike the stage
exercises, this is not required to move on -- treat it as a checkpoint.

Build a small order-processing pipeline for a store's inventory. It's one
connected system: inventory lines get parsed, control flow finds and
reports on stock, functions compute prices and shipping, and the results
get grouped and ranked with the right data structures.

## What to implement

All of it lives in `solution.py`. Each function/class below is
independently testable, but several build on each other (e.g.
`process_order` feeds `group_orders_by_customer`).

### Stage 1 -- Python Fundamentals

- **`parse_inventory_line(line)`** -- parse a CSV-ish line
  `"SKU,name,price,qty,tag1|tag2|tag3"` into
  `{"sku": str, "name": str, "price": float, "qty": int, "tags": set}`.
  No `try/except` numeric-detection shortcuts: validate and convert using
  `str.strip()`/`str.split()`/explicit numeric parsing. Raise `ValueError`
  (with a message naming the problem) if the line doesn't have exactly 5
  comma-separated fields. Use `is`/`is not` (never `==`/`!=`) anywhere you
  check something against `None`.

### Stage 2 -- Control Flow

- **`find_item_by_sku(inventory, sku)`** -- a `for...else` search: return
  the matching item `dict`, or `None` from the `else` clause when the
  loop finishes without a `break`.
- **`restock_report(inventory, threshold)`** -- a `while...else` loop
  (pop items from the front of a working copy) collecting `(name, qty)`
  for every item with `qty < threshold`; the `else` clause -- reached
  because the loop drains normally, never via `break` -- appends
  `("__complete__", True)` as the last entry, proving it ran.
- **`label_stock_levels(inventory)`** -- using `enumerate()`, return
  `[(index, name, label), ...]` where `label` comes from one chained
  ternary per item: `"OUT"` if `qty == 0`, else `"LOW"` if `qty < 10`,
  else `"OK"`.
- **`zip_orders_with_customers(order_totals, customers)`** -- `zip()` the
  two equal-length lists into `[(customer, total), ...]`.
- **`is_valid_order(qty, sku, inventory_skus)`** -- one boolean
  *expression* (no `if`) combining `and`/`not`: quantity positive, sku
  known, and not a discontinued sku (prefixed `"DISCONTINUED-"`).

### Stage 3 -- Functions

- **`make_discount_policy(rate)`** -- a closure: returns a function
  `price -> discounted_price` that captures `rate` (no default-arg
  smuggling).
- **`memoize(fn)`** -- a decorator, `functools.wraps`-preserving, that
  caches by positional args (a plain hand-rolled cache, not
  `lru_cache` -- that's exercised separately in `cached_shipping_rate`).
- **`cached_shipping_rate`** -- a `functools.lru_cache`-decorated function
  `(distance_km) -> float` computing a shipping rate.
- **`apply_shipping(*, weight_kg, base_rate=5.0, **surcharges)`** --
  keyword-only parameters; sum any extra keyword surcharges on top of
  `base_rate + weight_kg * 0.5`.
- **`process_order(sku, qty, /, *, unit_price)`** -- `sku`/`qty`
  positional-only, `unit_price` keyword-only; returns
  `qty * unit_price`.

### Stage 4 -- Data Structures

- **`Order`** -- a frozen `dataclasses.dataclass` (or
  `collections.namedtuple`) with fields `customer`, `sku`, `qty`,
  `total`.
- **`group_orders_by_customer(orders)`** -- a `collections.defaultdict`
  mapping customer -> list of their `Order`s.
- **`top_selling_skus(orders, n)`** -- `collections.Counter`, weighted by
  `qty`, returning the `n` best-selling skus via `.most_common(n)`.
- **`common_tags(item_a, item_b)`** -- the set intersection of two
  inventory items' `"tags"`.
- **`sorted_inventory_by_price(inventory)`** -- `inventory` sorted
  ascending by `"price"` using `sorted(..., key=...)` (never mutate the
  input list).

## Grading

`python tools/cli.py test exam01` runs `tests/test_exam01.py` -- the same
correctness check as any exercise or challenge. As with the interview
challenges, a green run only proves the happy path and documented edge
cases; the specific technique called out for each function above
(`for...else`, positional-only params, `lru_cache`, etc.) is a
code-review job pytest can't fully verify.
