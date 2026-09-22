# Exam 3 -- Product Analytics & Photo Pipeline API

Covers: Stages 10-13

An evaluation exam, not a graded exercise: it exists to prove you can
combine Stage 10-13 material (Pandas, OpenCV, Requests + Threading, and
FastAPI) in one connected system, not four separate snippets. Unlike the
stage exercises, this is not required to move on -- treat it as a
checkpoint.

Build the backend of a small product-analytics tool: crunch sales data
with pandas, preprocess product photos with OpenCV, fetch photo metadata
concurrently over HTTP, and serve the results from a FastAPI app.

## What to implement

All of it lives in `solution.py`.

### Stage 10 -- Pandas

- **`sales_by_category(df)`** -- `groupby("category")` total `"revenue"`,
  descending, as a fresh `DataFrame` with a reset integer index (no row
  loops).
- **`pivot_revenue_by_region_and_month(df)`** -- `df.pivot_table(values="revenue",
  index="region", columns="month", aggfunc="sum", fill_value=0)`.
- **`merge_with_targets(sales_df, targets_df)`** -- `sales_by_category(sales_df)`
  merged with `targets_df` on `"category"` (`df.merge`), plus a new
  **vectorized** column `"pct_of_target"` (`revenue / target` -- no
  `.apply()` with a row lambda).
- **`flag_underperforming(merged_df, threshold=0.5)`** -- boolean-index
  `merged_df` down to rows where `pct_of_target < threshold`.

### Stage 11 -- OpenCV

- **`preprocess_product_photo(image)`** -- grayscale -> Gaussian blur ->
  binary threshold; return `{"gray": ..., "blurred": ..., "thresh": ...}`.
- **`crop_to_largest_contour(image)`** -- threshold the image (reuse
  `preprocess_product_photo`), find contours, crop `image` to the
  bounding box of the largest one; return the original `image` unchanged
  if no contours are found.
- **`compute_brightness(image)`** -- mean grayscale pixel value, as a
  plain `float`.

### Stage 12 -- Requests + Threading

- **`ThreadSafeCounter`** -- a `threading.Lock`-protected counter with
  `increment()` and a `value` property; safe to call from multiple
  threads at once.
- **`fetch_all_metadata_concurrently(session, urls, counter, max_workers=4)`**
  -- fetch every url's JSON via `session.get(url).json()` (`session` is
  swappable -- tests pass a mock, never real network), incrementing
  `counter` once per successful fetch, using
  `concurrent.futures.ThreadPoolExecutor` -- results returned **in the
  same order as `urls`**.

### Stage 13 -- FastAPI

- **`SalesSummary`** -- a Pydantic `BaseModel` (`category: str`,
  `revenue: float`).
- **`get_sales_dataframe()`** / **`get_targets_dataframe()`** /
  **`get_photo_counter()`** -- dependency-provider functions reading this
  module's data (a test can swap what they return by reassigning the
  module-level `_sales_df`/`_targets_df`/`_photo_counter` before making a
  request).
- **`app`** -- a `FastAPI()` instance with:
  - `GET /sales/summary` -- injects `get_sales_dataframe` via `Depends()`,
    returns `sales_by_category(df)` as a list of `SalesSummary`.
  - `GET /sales/underperforming?threshold=` -- `threshold` is a
    `Query()`-validated `float` (default `0.5`, must be between 0 and 1);
    injects both dataframes via `Depends()`, returns
    `flag_underperforming(merge_with_targets(...), threshold)` as JSON
    records.
  - `GET /photos/fetch-count` -- injects `get_photo_counter` via
    `Depends()`, returns `{"count": counter.value}`.

## Grading

`python tools/cli.py test exam03` runs `tests/test_exam03.py` -- the same
correctness check as any exercise or challenge. A green run only proves
the happy path and documented edge cases; whether you actually used the
required technique (vectorized pandas ops, `Depends()`-injected state,
etc.) for each piece is a code-review job pytest can't fully verify.
