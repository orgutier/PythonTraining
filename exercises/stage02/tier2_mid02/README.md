# Inventory Restock Matcher

A stockroom inventory -- given, don't modify:

```python
item_names = ["bolts", "screws", "washers", "nuts"]
stock_levels = [12, 0, 5, 3]
reorder_threshold = 4
```

(`stock_levels[i]` is `item_names[i]`'s current stock.)

Same Mid-tier toolbox as the previous exercise, a different combination -- write plain top-level code that computes:

- `out_of_stock_index` -- a **`while...else`** loop: walk an index `i` from `0`, `break` the moment `stock_levels[i] == 0`; the loop's `else` clause (reached only if the `while` condition ran out without a `break`) sets `i = -1`. Assign `out_of_stock_index = i` after the loop.
- `needs_urgent_reorder` -- **one short-circuit `and` expression**: `out_of_stock_index != -1 and item_names[out_of_stock_index] != ""`. The `!= -1` check must come first -- it's what makes indexing `item_names[out_of_stock_index]` safe.
- `stock_status` -- a **ternary expression**: `"critical"` if `out_of_stock_index != -1` else `"ok"`.
- `low_stock_items` -- a plain `for` loop using **`zip(item_names, stock_levels)`** to walk both lists together, collecting every name whose stock is strictly below `reorder_threshold`.
