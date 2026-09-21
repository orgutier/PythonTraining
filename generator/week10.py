"""
Week 10 -- Pandas.

Coverage plan (each item exercised by the trainee's own code >=3 times):
  keywords: pd.read_csv, df.head(), df.groupby(), df.sort_values(),
            df.merge()
  modules:  pandas
  methods:  df.info(), df.describe(), df.apply(), df.pivot_table()
  concepts: boolean indexing, multi-indexing,
            dtype-based memory optimization
"""

WEEK = "week10"
TOPIC = "Pandas"
OVERVIEW = (
    "Five exercises built around a small sales dataset, covering every "
    "core DataFrame operation from Topic 10 at least three times: reading "
    "and inspecting, boolean-indexing filters, sorting/grouping, merging/"
    "pivoting, and row-wise transformation with .apply()."
)

EXERCISES = [
    {
        "name": "exercise01",
        "title": "Reading and Inspecting",
        "summary": "pd.read_csv, df.head(), df.describe(), df.info()",
        "readme": (
            "Implement:\n\n"
            "- `load_csv(path: str) -> pd.DataFrame` -- `pd.read_csv(path)`.\n"
            "- `preview_rows(df: pd.DataFrame, n: int) -> pd.DataFrame` -- "
            "`df.head(n)`.\n"
            "- `summarize(df: pd.DataFrame) -> pd.DataFrame` -- "
            "`df.describe()` (count/mean/std/min/max/quartiles for every "
            "numeric column).\n"
            "- `capture_info(df: pd.DataFrame) -> str` -- `df.info()` "
            "prints straight to stdout and returns `None`, so to actually "
            "*get* the text back, redirect it: `buf = io.StringIO(); "
            "df.info(buf=buf); return buf.getvalue()`.\n\n"
            "See the Study Reference presentation, Topic 10, for the theory."
        ),
        "stub": '''\
import io
import pandas as pd


def load_csv(path: str) -> pd.DataFrame:
    """pd.read_csv(path)."""
    raise NotImplementedError


def preview_rows(df: pd.DataFrame, n: int) -> pd.DataFrame:
    """df.head(n)."""
    raise NotImplementedError


def summarize(df: pd.DataFrame) -> pd.DataFrame:
    """df.describe()."""
    raise NotImplementedError


def capture_info(df: pd.DataFrame) -> str:
    """df.info() redirected into a string via io.StringIO()."""
    raise NotImplementedError
''',
        "reference": '''\
import io
import pandas as pd


def load_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def preview_rows(df: pd.DataFrame, n: int) -> pd.DataFrame:
    return df.head(n)


def summarize(df: pd.DataFrame) -> pd.DataFrame:
    return df.describe()


def capture_info(df: pd.DataFrame) -> str:
    buf = io.StringIO()
    df.info(buf=buf)
    return buf.getvalue()
''',
        "test": '''\
import pandas as pd
from exercises.week10.exercise01.solution import (
    load_csv,
    preview_rows,
    summarize,
    capture_info,
)


def test_load_csv(tmp_path):
    path = tmp_path / "data.csv"
    path.write_text("name,sales\\nAda,100\\nGrace,200\\n")
    df = load_csv(str(path))
    assert list(df.columns) == ["name", "sales"]
    assert len(df) == 2


def test_preview_rows():
    df = pd.DataFrame({"x": range(10)})
    assert len(preview_rows(df, 3)) == 3


def test_summarize():
    df = pd.DataFrame({"sales": [10, 20, 30]})
    result = summarize(df)
    assert result.loc["mean", "sales"] == 20.0


def test_capture_info():
    df = pd.DataFrame({"x": [1, 2, 3]})
    text = capture_info(df)
    assert "RangeIndex" in text
''',
    },
    {
        "name": "exercise02",
        "title": "Boolean Indexing",
        "summary": "boolean indexing x3",
        "readme": (
            "Implement three filters on a sales DataFrame (columns "
            "`region`, `product`, `sales`):\n\n"
            "- `filter_by_region(df, region: str) -> pd.DataFrame` -- "
            "`df[df[\"region\"] == region]`.\n"
            "- `filter_high_sales(df, threshold: float) -> pd.DataFrame` -- "
            "`df[df[\"sales\"] > threshold]`.\n"
            "- `filter_multiple_conditions(df, region: str, threshold: float) "
            "-> pd.DataFrame` -- both at once: "
            "`df[(df[\"region\"] == region) & (df[\"sales\"] > threshold)]` "
            "(note `&`, not `and` -- pandas boolean masks need the "
            "element-wise operator, and each condition needs its own "
            "parentheses).\n\n"
            "`df[boolean_series]` -- indexing a DataFrame with a same-length "
            "`Series` of `True`/`False` -- keeps only the rows where it's "
            "`True`. This is **boolean indexing**, the pandas equivalent of "
            "a list comprehension's `if` filter.\n\n"
            "See the Study Reference presentation, Topic 10, for the theory."
        ),
        "stub": '''\
import pandas as pd


def filter_by_region(df: pd.DataFrame, region: str) -> pd.DataFrame:
    """df[df["region"] == region]."""
    raise NotImplementedError


def filter_high_sales(df: pd.DataFrame, threshold: float) -> pd.DataFrame:
    """df[df["sales"] > threshold]."""
    raise NotImplementedError


def filter_multiple_conditions(df: pd.DataFrame, region: str, threshold: float) -> pd.DataFrame:
    """df[(df["region"] == region) & (df["sales"] > threshold)]."""
    raise NotImplementedError
''',
        "reference": '''\
import pandas as pd


def filter_by_region(df: pd.DataFrame, region: str) -> pd.DataFrame:
    return df[df["region"] == region]


def filter_high_sales(df: pd.DataFrame, threshold: float) -> pd.DataFrame:
    return df[df["sales"] > threshold]


def filter_multiple_conditions(df: pd.DataFrame, region: str, threshold: float) -> pd.DataFrame:
    return df[(df["region"] == region) & (df["sales"] > threshold)]
''',
        "test": '''\
import pandas as pd
from exercises.week10.exercise02.solution import (
    filter_by_region,
    filter_high_sales,
    filter_multiple_conditions,
)


def _filter_sample_df():
    return pd.DataFrame({
        "region": ["east", "west", "east", "west"],
        "product": ["A", "B", "C", "D"],
        "sales": [100, 250, 50, 300],
    })


def test_filter_by_region():
    result = filter_by_region(_filter_sample_df(), "east")
    assert list(result["product"]) == ["A", "C"]


def test_filter_high_sales():
    result = filter_high_sales(_filter_sample_df(), 100)
    assert list(result["product"]) == ["B", "D"]


def test_filter_multiple_conditions():
    result = filter_multiple_conditions(_filter_sample_df(), "west", 100)
    assert list(result["product"]) == ["B", "D"]
''',
    },
    {
        "name": "exercise03",
        "title": "Sorting and Grouping",
        "summary": "df.sort_values() x3, df.groupby() x3, multi-indexing",
        "readme": (
            "Implement:\n\n"
            "- `sort_by_sales_desc(df) -> pd.DataFrame` -- "
            "`df.sort_values(\"sales\", ascending=False)`.\n"
            "- `sort_by_multiple(df) -> pd.DataFrame` -- "
            "`df.sort_values([\"region\", \"sales\"], ascending=[True, False])` "
            "(sort by `region` A-Z, and within each region by `sales` "
            "highest first).\n"
            "- `total_sales_by_region(df) -> pd.Series` -- "
            "`df.groupby(\"region\")[\"sales\"].sum()`.\n"
            "- `avg_sales_by_region_and_product(df) -> pd.Series` -- "
            "`df.groupby([\"region\", \"product\"])[\"sales\"].mean()` -- "
            "grouping by *two* columns produces a result indexed by a "
            "**`MultiIndex`** of `(region, product)` pairs, instead of a "
            "single flat index.\n"
            "- `orders_per_region_sorted(df) -> pd.Series` -- "
            "`df.groupby(\"region\").size().sort_values(ascending=False)` "
            "(how many rows per region, busiest region first).\n\n"
            "See the Study Reference presentation, Topic 10, for the theory."
        ),
        "stub": '''\
import pandas as pd


def sort_by_sales_desc(df: pd.DataFrame) -> pd.DataFrame:
    """df.sort_values("sales", ascending=False)."""
    raise NotImplementedError


def sort_by_multiple(df: pd.DataFrame) -> pd.DataFrame:
    """df.sort_values(["region", "sales"], ascending=[True, False])."""
    raise NotImplementedError


def total_sales_by_region(df: pd.DataFrame) -> pd.Series:
    """df.groupby("region")["sales"].sum()."""
    raise NotImplementedError


def avg_sales_by_region_and_product(df: pd.DataFrame) -> pd.Series:
    """df.groupby(["region", "product"])["sales"].mean() -- a MultiIndex result."""
    raise NotImplementedError


def orders_per_region_sorted(df: pd.DataFrame) -> pd.Series:
    """df.groupby("region").size().sort_values(ascending=False)."""
    raise NotImplementedError
''',
        "reference": '''\
import pandas as pd


def sort_by_sales_desc(df: pd.DataFrame) -> pd.DataFrame:
    return df.sort_values("sales", ascending=False)


def sort_by_multiple(df: pd.DataFrame) -> pd.DataFrame:
    return df.sort_values(["region", "sales"], ascending=[True, False])


def total_sales_by_region(df: pd.DataFrame) -> pd.Series:
    return df.groupby("region")["sales"].sum()


def avg_sales_by_region_and_product(df: pd.DataFrame) -> pd.Series:
    return df.groupby(["region", "product"])["sales"].mean()


def orders_per_region_sorted(df: pd.DataFrame) -> pd.Series:
    return df.groupby("region").size().sort_values(ascending=False)
''',
        "test": '''\
import pandas as pd
from exercises.week10.exercise03.solution import (
    sort_by_sales_desc,
    sort_by_multiple,
    total_sales_by_region,
    avg_sales_by_region_and_product,
    orders_per_region_sorted,
)


def _group_sample_df():
    return pd.DataFrame({
        "region": ["east", "west", "east", "west", "east"],
        "product": ["A", "A", "B", "B", "A"],
        "sales": [100, 250, 50, 300, 150],
    })


def test_sort_by_sales_desc():
    result = sort_by_sales_desc(_group_sample_df())
    assert list(result["sales"]) == [300, 250, 150, 100, 50]


def test_sort_by_multiple():
    result = sort_by_multiple(_group_sample_df())
    assert list(result["region"]) == ["east", "east", "east", "west", "west"]
    assert list(result["sales"])[:3] == [150, 100, 50]


def test_total_sales_by_region():
    result = total_sales_by_region(_group_sample_df())
    assert result["east"] == 300
    assert result["west"] == 550


def test_avg_sales_by_region_and_product_is_multi_indexed():
    result = avg_sales_by_region_and_product(_group_sample_df())
    assert isinstance(result.index, pd.MultiIndex)
    assert result[("east", "A")] == 125.0


def test_orders_per_region_sorted():
    result = orders_per_region_sorted(_group_sample_df())
    assert list(result.index) == ["east", "west"]
    assert list(result.values) == [3, 2]
''',
    },
    {
        "name": "exercise04",
        "title": "Merging and Pivoting",
        "summary": "df.merge() x3, df.pivot_table() x2",
        "readme": (
            "Implement:\n\n"
            "- `merge_customer_info(orders_df, customers_df) -> pd.DataFrame` "
            "-- `orders_df.merge(customers_df, on=\"customer_id\")` (an "
            "inner join by default -- only matching rows survive).\n"
            "- `merge_with_suffixes(df1, df2) -> pd.DataFrame` -- "
            "`df1.merge(df2, on=\"id\", how=\"left\", suffixes=(\"_left\", "
            "\"_right\"))` -- `how=\"left\"` keeps every row of `df1` even "
            "without a match; `suffixes` disambiguates any other "
            "same-named columns from each side.\n"
            "- `inner_join_products(orders_df, products_df) -> pd.DataFrame` "
            "-- `orders_df.merge(products_df, on=\"product_id\", how=\"inner\")`.\n"
            "- `sales_pivot_table(df) -> pd.DataFrame` -- "
            "`df.pivot_table(index=\"region\", columns=\"product\", "
            "values=\"sales\", aggfunc=\"sum\")` (regions as rows, products as "
            "columns, total sales as the cell values).\n"
            "- `sales_pivot_count(df) -> pd.DataFrame` -- same shape, but "
            "`aggfunc=\"count\"` instead of `\"sum\"` (how many orders per "
            "region/product, not their total).\n\n"
            "See the Study Reference presentation, Topic 10, for the theory."
        ),
        "stub": '''\
import pandas as pd


def merge_customer_info(orders_df: pd.DataFrame, customers_df: pd.DataFrame) -> pd.DataFrame:
    """orders_df.merge(customers_df, on="customer_id")."""
    raise NotImplementedError


def merge_with_suffixes(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    """df1.merge(df2, on="id", how="left", suffixes=("_left", "_right"))."""
    raise NotImplementedError


def inner_join_products(orders_df: pd.DataFrame, products_df: pd.DataFrame) -> pd.DataFrame:
    """orders_df.merge(products_df, on="product_id", how="inner")."""
    raise NotImplementedError


def sales_pivot_table(df: pd.DataFrame) -> pd.DataFrame:
    """df.pivot_table(index="region", columns="product", values="sales", aggfunc="sum")."""
    raise NotImplementedError


def sales_pivot_count(df: pd.DataFrame) -> pd.DataFrame:
    """Same shape as sales_pivot_table, but aggfunc="count"."""
    raise NotImplementedError
''',
        "reference": '''\
import pandas as pd


def merge_customer_info(orders_df: pd.DataFrame, customers_df: pd.DataFrame) -> pd.DataFrame:
    return orders_df.merge(customers_df, on="customer_id")


def merge_with_suffixes(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return df1.merge(df2, on="id", how="left", suffixes=("_left", "_right"))


def inner_join_products(orders_df: pd.DataFrame, products_df: pd.DataFrame) -> pd.DataFrame:
    return orders_df.merge(products_df, on="product_id", how="inner")


def sales_pivot_table(df: pd.DataFrame) -> pd.DataFrame:
    return df.pivot_table(index="region", columns="product", values="sales", aggfunc="sum")


def sales_pivot_count(df: pd.DataFrame) -> pd.DataFrame:
    return df.pivot_table(index="region", columns="product", values="sales", aggfunc="count")
''',
        "test": '''\
import pandas as pd
from exercises.week10.exercise04.solution import (
    merge_customer_info,
    merge_with_suffixes,
    inner_join_products,
    sales_pivot_table,
    sales_pivot_count,
)


def test_merge_customer_info():
    orders = pd.DataFrame({"customer_id": [1, 2], "amount": [50, 75]})
    customers = pd.DataFrame({"customer_id": [1, 2], "name": ["Ada", "Grace"]})
    result = merge_customer_info(orders, customers)
    assert list(result["name"]) == ["Ada", "Grace"]


def test_merge_with_suffixes_keeps_unmatched_left_rows():
    df1 = pd.DataFrame({"id": [1, 2, 3], "value": ["a", "b", "c"]})
    df2 = pd.DataFrame({"id": [1, 2], "value": ["x", "y"]})
    result = merge_with_suffixes(df1, df2)
    assert len(result) == 3
    assert "value_left" in result.columns and "value_right" in result.columns


def test_inner_join_products_drops_unmatched():
    orders = pd.DataFrame({"product_id": [1, 2, 3]})
    products = pd.DataFrame({"product_id": [1, 2], "name": ["Widget", "Gadget"]})
    result = inner_join_products(orders, products)
    assert len(result) == 2


def _pivot_sample_df():
    return pd.DataFrame({
        "region": ["east", "east", "west"],
        "product": ["A", "B", "A"],
        "sales": [100, 50, 200],
    })


def test_sales_pivot_table():
    result = sales_pivot_table(_pivot_sample_df())
    assert result.loc["east", "A"] == 100
    assert result.loc["west", "A"] == 200


def test_sales_pivot_count():
    result = sales_pivot_count(_pivot_sample_df())
    assert result.loc["east", "A"] == 1
''',
    },
    {
        "name": "exercise05",
        "title": "Apply and Dtype Optimization",
        "summary": "df.apply() x3, dtype-based memory optimization, multi-indexing (set_index)",
        "readme": (
            "Implement:\n\n"
            "- `add_sales_tax_column(df, rate: float) -> pd.DataFrame` -- "
            "return a copy with a new `\"total\"` column: `df[\"sales\"].apply"
            "(lambda x: round(x * (1 + rate), 2))`.\n"
            "- `categorize_sales(df) -> pd.DataFrame` -- return a copy with a "
            "new `\"tier\"` column via `df[\"sales\"].apply(categorize_amount)`, "
            "where `categorize_amount(x)` returns `\"low\"` (`x < 100`), "
            "`\"medium\"` (`100 <= x < 300`), or `\"high\"` (`x >= 300`).\n"
            "- `full_name_column(df) -> pd.DataFrame` -- return a copy with "
            "a new `\"full_name\"` column via **row-wise** apply: "
            "`df.apply(lambda row: f\"{row['first']} {row['last']}\", axis=1)` "
            "(`axis=1` runs the function once per *row* instead of once per "
            "column -- the other common shape of `.apply()`).\n"
            "- `optimize_dtypes(df) -> pd.DataFrame` -- return a copy with "
            "`region` cast to the `\"category\"` dtype (`df.astype({\"region\": "
            "\"category\"})`) -- a column with few distinct repeated string "
            "values takes far less memory as a `category` than as `object`.\n"
            "- `set_region_product_index(df) -> pd.DataFrame` -- "
            "`df.set_index([\"region\", \"product\"])` -- another way to get a "
            "`MultiIndex`, this time explicitly instead of as a side effect "
            "of `groupby`.\n\n"
            "See the Study Reference presentation, Topic 10, for the theory."
        ),
        "stub": '''\
import pandas as pd


def _categorize_amount(x):
    if x < 100:
        return "low"
    if x < 300:
        return "medium"
    return "high"


def add_sales_tax_column(df: pd.DataFrame, rate: float) -> pd.DataFrame:
    """Copy of df with a "total" column: sales * (1 + rate), via .apply()."""
    raise NotImplementedError


def categorize_sales(df: pd.DataFrame) -> pd.DataFrame:
    """Copy of df with a "tier" column: "low"/"medium"/"high", via .apply()."""
    raise NotImplementedError


def full_name_column(df: pd.DataFrame) -> pd.DataFrame:
    """Copy of df with a "full_name" column, via row-wise .apply(axis=1)."""
    raise NotImplementedError


def optimize_dtypes(df: pd.DataFrame) -> pd.DataFrame:
    """Copy of df with "region" cast to the "category" dtype."""
    raise NotImplementedError


def set_region_product_index(df: pd.DataFrame) -> pd.DataFrame:
    """df.set_index(["region", "product"])."""
    raise NotImplementedError
''',
        "reference": '''\
import pandas as pd


def _categorize_amount(x):
    if x < 100:
        return "low"
    if x < 300:
        return "medium"
    return "high"


def add_sales_tax_column(df: pd.DataFrame, rate: float) -> pd.DataFrame:
    result = df.copy()
    result["total"] = df["sales"].apply(lambda x: round(x * (1 + rate), 2))
    return result


def categorize_sales(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    result["tier"] = df["sales"].apply(_categorize_amount)
    return result


def full_name_column(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    result["full_name"] = df.apply(lambda row: f"{row['first']} {row['last']}", axis=1)
    return result


def optimize_dtypes(df: pd.DataFrame) -> pd.DataFrame:
    return df.astype({"region": "category"})


def set_region_product_index(df: pd.DataFrame) -> pd.DataFrame:
    return df.set_index(["region", "product"])
''',
        "test": '''\
import pandas as pd
from exercises.week10.exercise05.solution import (
    add_sales_tax_column,
    categorize_sales,
    full_name_column,
    optimize_dtypes,
    set_region_product_index,
)


def test_add_sales_tax_column():
    df = pd.DataFrame({"sales": [100, 200]})
    result = add_sales_tax_column(df, 0.1)
    assert list(result["total"]) == [110.0, 220.0]


def test_categorize_sales():
    df = pd.DataFrame({"sales": [50, 150, 350]})
    result = categorize_sales(df)
    assert list(result["tier"]) == ["low", "medium", "high"]


def test_full_name_column():
    df = pd.DataFrame({"first": ["Ada", "Grace"], "last": ["Lovelace", "Hopper"]})
    result = full_name_column(df)
    assert list(result["full_name"]) == ["Ada Lovelace", "Grace Hopper"]


def test_optimize_dtypes():
    df = pd.DataFrame({"region": ["east", "west", "east"]})
    result = optimize_dtypes(df)
    assert str(result["region"].dtype) == "category"


def test_set_region_product_index():
    df = pd.DataFrame({"region": ["east", "west"], "product": ["A", "B"], "sales": [1, 2]})
    result = set_region_product_index(df)
    assert isinstance(result.index, pd.MultiIndex)
    assert result.loc[("east", "A"), "sales"] == 1
''',
    },
]
