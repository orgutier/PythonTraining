# Warehouse Grid Scanner

A warehouse floor is mapped as rows of characters -- given, don't modify:

```python
grid_rows = ["..#..", ".##..", "?.#.#", "?????", "#..X."]
```
`"#"` is an obstacle, `"."` is empty floor, `"?"` is deliberately unmapped (ignore it, don't count it as anything), and any other character is invalid data.

Using nested `for` loops over `range(len(...))` (index both the rows and each row's characters -- no `enumerate()` yet), `if`/`elif`/`else`, `continue`, and `pass`, write plain top-level code that computes:

- `obstacle_count` -- total `"#"` characters across the whole grid.
- `unmapped_count` -- total `"?"` characters across the whole grid.
- `invalid_char_count` -- total characters that are none of `"#"`/`"."`/`"?"`.
- `first_obstacle_row`, `first_obstacle_col` -- the row/column indices of the very first `"#"` found (scanning row by row, left to right within a row); `-1`/`-1` if none. Track this with an `if first_obstacle_row == -1:` guard inside the obstacle branch -- don't overwrite it once set.
- `rows_skipped` -- **before** scanning a row's individual characters, `continue` straight past any row that's entirely `"?????"` (all-unmapped) -- there's nothing to learn from scanning it character by character, so skip it outright and count the skip.

Use `elif ...: pass` for the `"?"` case inside the character-by-character scan (rows that aren't *entirely* unmapped can still contain individual `"?"` cells) -- an explicit, documented no-op, not an accident.

Then, **separately**, use a `while` loop (not the `for` loops above) to scan the grid **from the bottom up** and find `last_obstacle_row` -- the index of the last row (searching backward) that contains at least one `"#"` (`"#" in grid_rows[i]`); `break` the moment you find one. `-1` if none.
