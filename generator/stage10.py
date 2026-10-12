"""
Stage 10 -- Pandas.

Rolled onto the tier-named exercise convention: a minimum of two exercises
per Basic/Mid/Advanced tier. All exercises are function-based, built
around small DataFrames -- this stage's whole subject is DataFrame
operations, naturally expressed as functions taking/returning a DataFrame.

Coverage plan (every item below is exercised by the trainee's own code,
generally 2+ times across these 6 exercises):

  Basic:    pd.read_csv, df.head(), df.describe(), pandas module
  Mid:      df.groupby(), df.sort_values(), df.merge(), boolean indexing
  Advanced: df.info(), df.apply(), df.pivot_table(), multi-indexing,
            dtype-based memory optimization
"""

STAGE = "stage10"
TOPIC = "Pandas"
OVERVIEW = (
    "Six exercises, two per tier, built around small sales/employee "
    "datasets: reading and inspecting in Basic; boolean-indexing filters "
    "plus sorting/grouping/merging in Mid; df.info(), pivot tables, "
    "multi-indexing (two ways), row-wise .apply(), and dtype optimization "
    "in Advanced."
)

EXERCISES = [
    {
        "name": "tier1_basic01",
        "title": "Reading and Inspecting Sales Data",
        "summary": "pd.read_csv, df.head(), df.describe()",
        "readme": (
            "Implement:\n\n"
            "- `load_csv(path: str) -> pd.DataFrame` -- "
            "`pd.read_csv(path)`.\n"
            "- `preview_rows(df: pd.DataFrame, n: int) -> pd.DataFrame` -- "
            "`df.head(n)`.\n"
            "- `summarize(df: pd.DataFrame) -> pd.DataFrame` -- "
            "`df.describe()` (count/mean/std/min/max/quartiles for every "
            "numeric column).\n\n"
            "See the Study Reference presentation, Topic 10 (Basic "
            "tier), for the theory."
        ),
        "stub": '''\
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
''',
        "reference": '''\
import pandas as pd


def load_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def preview_rows(df: pd.DataFrame, n: int) -> pd.DataFrame:
    return df.head(n)


def summarize(df: pd.DataFrame) -> pd.DataFrame:
    return df.describe()
''',
        "test": '''\
import pandas as pd
from exercises.stage10.tier1_basic01.solution import load_csv, preview_rows, summarize


def test_load_csv(tmp_path):
    """load_csv == pd.read_csv(path)."""
    path = tmp_path / "data.csv"
    path.write_text("name,sales\\nAda,100\\nGrace,200\\n")
    df = load_csv(str(path))
    assert list(df.columns) == ["name", "sales"]
    assert len(df) == 2


def test_preview_rows():
    """preview_rows == df.head(n)."""
    df = pd.DataFrame({"x": range(10)})
    assert len(preview_rows(df, 3)) == 3


def test_summarize():
    """summarize == df.describe(), with a "mean" row among others."""
    df = pd.DataFrame({"sales": [10, 20, 30]})
    result = summarize(df)
    assert result.loc["mean", "sales"] == 20.0
''',
    },
    {
        "name": "tier1_basic02",
        "title": "Reading and Inspecting Employee Data",
        "summary": "pd.read_csv, df.head(), df.describe() (a second dataset)",
        "readme": (
            "Same three operations as the previous exercise, on a "
            "different dataset (columns `name`, `salary`), plus two more "
            "everyday DataFrame introspection helpers:\n\n"
            "- `load_employees(path: str) -> pd.DataFrame` -- "
            "`pd.read_csv(path)`.\n"
            "- `preview_employees(df: pd.DataFrame, n: int) -> pd.DataFrame` "
            "-- `df.head(n)`.\n"
            "- `salary_summary(df: pd.DataFrame) -> pd.DataFrame` -- "
            "`df.describe()`.\n"
            "- `column_names(df: pd.DataFrame) -> list` -- "
            "`list(df.columns)`.\n"
            "- `row_count(df: pd.DataFrame) -> int` -- `len(df)`.\n\n"
            "See the Study Reference presentation, Topic 10 (Basic "
            "tier), for the theory."
        ),
        "stub": '''\
import pandas as pd


def load_employees(path: str) -> pd.DataFrame:
    """pd.read_csv(path)."""
    raise NotImplementedError


def preview_employees(df: pd.DataFrame, n: int) -> pd.DataFrame:
    """df.head(n)."""
    raise NotImplementedError


def salary_summary(df: pd.DataFrame) -> pd.DataFrame:
    """df.describe()."""
    raise NotImplementedError


def column_names(df: pd.DataFrame) -> list:
    """list(df.columns)."""
    raise NotImplementedError


def row_count(df: pd.DataFrame) -> int:
    """len(df)."""
    raise NotImplementedError
''',
        "reference": '''\
import pandas as pd


def load_employees(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def preview_employees(df: pd.DataFrame, n: int) -> pd.DataFrame:
    return df.head(n)


def salary_summary(df: pd.DataFrame) -> pd.DataFrame:
    return df.describe()


def column_names(df: pd.DataFrame) -> list:
    return list(df.columns)


def row_count(df: pd.DataFrame) -> int:
    return len(df)
''',
        "test": '''\
import pandas as pd
from exercises.stage10.tier1_basic02.solution import (
    load_employees,
    preview_employees,
    salary_summary,
    column_names,
    row_count,
)


def test_load_employees(tmp_path):
    """load_employees == pd.read_csv(path), on a different dataset shape."""
    path = tmp_path / "employees.csv"
    path.write_text("name,salary\\nAda,90000\\nGrace,95000\\nLinus,80000\\n")
    df = load_employees(str(path))
    assert list(df.columns) == ["name", "salary"]
    assert len(df) == 3


def test_preview_employees():
    """preview_employees == df.head(n)."""
    df = pd.DataFrame({"name": ["a", "b", "c", "d"], "salary": [1, 2, 3, 4]})
    assert len(preview_employees(df, 2)) == 2


def test_salary_summary():
    """salary_summary == df.describe()."""
    df = pd.DataFrame({"salary": [90000, 95000, 80000]})
    result = salary_summary(df)
    assert round(result.loc["mean", "salary"], 2) == 88333.33


def test_column_names():
    """column_names == list(df.columns)."""
    df = pd.DataFrame({"name": ["Ada"], "salary": [90000]})
    assert column_names(df) == ["name", "salary"]


def test_row_count():
    """row_count == len(df)."""
    df = pd.DataFrame({"name": ["Ada", "Grace"]})
    assert row_count(df) == 2
''',
    },
    {
        "name": "tier2_mid01",
        "title": "Boolean Indexing",
        "summary": "boolean indexing",
        "readme": (
            "Implement three filters on a sales DataFrame (columns "
            "`region`, `product`, `sales`):\n\n"
            "- `filter_by_region(df, region: str) -> pd.DataFrame` -- "
            "`df[df[\"region\"] == region]`.\n"
            "- `filter_high_sales(df, threshold: float) -> pd.DataFrame` "
            "-- `df[df[\"sales\"] > threshold]`.\n"
            "- `filter_multiple_conditions(df, region: str, threshold: "
            "float) -> pd.DataFrame` -- both at once: "
            "`df[(df[\"region\"] == region) & (df[\"sales\"] > "
            "threshold)]` (note `&`, not `and` -- pandas boolean masks "
            "need the element-wise operator, and each condition needs "
            "its own parentheses).\n\n"
            "`df[boolean_series]` -- indexing a DataFrame with a "
            "same-length `Series` of `True`/`False` -- keeps only the "
            "rows where it's `True`. This is **boolean indexing**, the "
            "pandas equivalent of a list comprehension's `if` filter.\n\n"
            "See the Study Reference presentation, Topic 10 (Mid tier), "
            "for the theory."
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
from exercises.stage10.tier2_mid01.solution import (
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
    """filter_by_region == df[df["region"] == region]."""
    result = filter_by_region(_filter_sample_df(), "east")
    assert list(result["product"]) == ["A", "C"]


def test_filter_high_sales():
    """filter_high_sales == df[df["sales"] > threshold]."""
    result = filter_high_sales(_filter_sample_df(), 100)
    assert list(result["product"]) == ["B", "D"]


def test_filter_multiple_conditions():
    """filter_multiple_conditions combines both masks with & (element-wise and), not the `and` keyword."""
    result = filter_multiple_conditions(_filter_sample_df(), "west", 100)
    assert list(result["product"]) == ["B", "D"]
''',
    },
    {
        "name": "tier2_mid02",
        "title": "Sorting, Grouping, and Merging",
        "summary": "df.sort_values(), df.groupby(), df.merge()",
        "readme": (
            "Implement:\n\n"
            "- `sort_by_sales_desc(df) -> pd.DataFrame` -- "
            "`df.sort_values(\"sales\", ascending=False)`.\n"
            "- `sort_by_multiple(df) -> pd.DataFrame` -- "
            "`df.sort_values([\"region\", \"sales\"], ascending=[True, "
            "False])` (sort by `region` A-Z, and within each region by "
            "`sales` highest first).\n"
            "- `total_sales_by_region(df) -> pd.Series` -- "
            "`df.groupby(\"region\")[\"sales\"].sum()`.\n"
            "- `merge_customer_info(orders_df, customers_df) -> "
            "pd.DataFrame` -- `orders_df.merge(customers_df, "
            "on=\"customer_id\")` (an inner join by default -- only "
            "matching rows survive).\n"
            "- `inner_join_products(orders_df, products_df) -> "
            "pd.DataFrame` -- `orders_df.merge(products_df, "
            "on=\"product_id\", how=\"inner\")`.\n\n"
            "See the Study Reference presentation, Topic 10 (Mid tier), "
            "for the theory."
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


def merge_customer_info(orders_df: pd.DataFrame, customers_df: pd.DataFrame) -> pd.DataFrame:
    """orders_df.merge(customers_df, on="customer_id")."""
    raise NotImplementedError


def inner_join_products(orders_df: pd.DataFrame, products_df: pd.DataFrame) -> pd.DataFrame:
    """orders_df.merge(products_df, on="product_id", how="inner")."""
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


def merge_customer_info(orders_df: pd.DataFrame, customers_df: pd.DataFrame) -> pd.DataFrame:
    return orders_df.merge(customers_df, on="customer_id")


def inner_join_products(orders_df: pd.DataFrame, products_df: pd.DataFrame) -> pd.DataFrame:
    return orders_df.merge(products_df, on="product_id", how="inner")
''',
        "test": '''\
import pandas as pd
from exercises.stage10.tier2_mid02.solution import (
    sort_by_sales_desc,
    sort_by_multiple,
    total_sales_by_region,
    merge_customer_info,
    inner_join_products,
)


def _group_sample_df():
    return pd.DataFrame({
        "region": ["east", "west", "east", "west", "east"],
        "product": ["A", "A", "B", "B", "A"],
        "sales": [100, 250, 50, 300, 150],
    })


def test_sort_by_sales_desc():
    """sort_by_sales_desc == df.sort_values("sales", ascending=False)."""
    result = sort_by_sales_desc(_group_sample_df())
    assert list(result["sales"]) == [300, 250, 150, 100, 50]


def test_sort_by_multiple():
    """sort_by_multiple sorts by region ascending, then sales descending within each region."""
    result = sort_by_multiple(_group_sample_df())
    assert list(result["region"]) == ["east", "east", "east", "west", "west"]
    assert list(result["sales"])[:3] == [150, 100, 50]


def test_total_sales_by_region():
    """total_sales_by_region == df.groupby("region")["sales"].sum()."""
    result = total_sales_by_region(_group_sample_df())
    assert result["east"] == 300
    assert result["west"] == 550


def test_merge_customer_info():
    """merge_customer_info == orders_df.merge(customers_df, on="customer_id") -- an inner join."""
    orders = pd.DataFrame({"customer_id": [1, 2], "amount": [50, 75]})
    customers = pd.DataFrame({"customer_id": [1, 2], "name": ["Ada", "Grace"]})
    result = merge_customer_info(orders, customers)
    assert list(result["name"]) == ["Ada", "Grace"]


def test_inner_join_products_drops_unmatched():
    """inner_join_products must use how="inner" -- unmatched rows are dropped."""
    orders = pd.DataFrame({"product_id": [1, 2, 3]})
    products = pd.DataFrame({"product_id": [1, 2], "name": ["Widget", "Gadget"]})
    result = inner_join_products(orders, products)
    assert len(result) == 2
''',
    },
    {
        "name": "tier3_advanced01",
        "title": "Inspecting, Pivoting, and Multi-Indexing",
        "summary": "df.info(), df.pivot_table(), multi-indexing (via groupby)",
        "readme": (
            "Implement:\n\n"
            "- `capture_info(df: pd.DataFrame) -> str` -- `df.info()` "
            "prints straight to stdout and returns `None`, so to actually "
            "*get* the text back, redirect it: `buf = io.StringIO(); "
            "df.info(buf=buf); return buf.getvalue()`.\n"
            "- `avg_sales_by_region_and_product(df) -> pd.Series` -- "
            "`df.groupby([\"region\", \"product\"])[\"sales\"].mean()` -- "
            "grouping by *two* columns produces a result indexed by a "
            "**`MultiIndex`** of `(region, product)` pairs, instead of a "
            "single flat index.\n"
            "- `sales_pivot_table(df) -> pd.DataFrame` -- "
            "`df.pivot_table(index=\"region\", columns=\"product\", "
            "values=\"sales\", aggfunc=\"sum\")` (regions as rows, "
            "products as columns, total sales as the cell values).\n"
            "- `sales_pivot_count(df) -> pd.DataFrame` -- same shape, "
            "but `aggfunc=\"count\"` instead of `\"sum\"` (how many "
            "orders per region/product, not their total).\n\n"
            "See the Study Reference presentation, Topic 10 (Advanced "
            "tier), for the theory."
        ),
        "stub": '''\
import io
import pandas as pd


def capture_info(df: pd.DataFrame) -> str:
    """df.info() redirected into a string via io.StringIO()."""
    raise NotImplementedError


def avg_sales_by_region_and_product(df: pd.DataFrame) -> pd.Series:
    """df.groupby(["region", "product"])["sales"].mean() -- a MultiIndex result."""
    raise NotImplementedError


def sales_pivot_table(df: pd.DataFrame) -> pd.DataFrame:
    """df.pivot_table(index="region", columns="product", values="sales", aggfunc="sum")."""
    raise NotImplementedError


def sales_pivot_count(df: pd.DataFrame) -> pd.DataFrame:
    """Same shape as sales_pivot_table, but aggfunc="count"."""
    raise NotImplementedError
''',
        "reference": '''\
import io
import pandas as pd


def capture_info(df: pd.DataFrame) -> str:
    buf = io.StringIO()
    df.info(buf=buf)
    return buf.getvalue()


def avg_sales_by_region_and_product(df: pd.DataFrame) -> pd.Series:
    return df.groupby(["region", "product"])["sales"].mean()


def sales_pivot_table(df: pd.DataFrame) -> pd.DataFrame:
    return df.pivot_table(index="region", columns="product", values="sales", aggfunc="sum")


def sales_pivot_count(df: pd.DataFrame) -> pd.DataFrame:
    return df.pivot_table(index="region", columns="product", values="sales", aggfunc="count")
''',
        "test": '''\
import pandas as pd
from exercises.stage10.tier3_advanced01.solution import (
    capture_info,
    avg_sales_by_region_and_product,
    sales_pivot_table,
    sales_pivot_count,
)


def test_capture_info():
    """capture_info must redirect df.info()'s stdout output into a returned string."""
    df = pd.DataFrame({"x": [1, 2, 3]})
    text = capture_info(df)
    assert "RangeIndex" in text


def _group_sample_df():
    return pd.DataFrame({
        "region": ["east", "west", "east", "west", "east"],
        "product": ["A", "A", "B", "B", "A"],
        "sales": [100, 250, 50, 300, 150],
    })


def test_avg_sales_by_region_and_product_is_multi_indexed():
    """Grouping by two columns must produce a pd.MultiIndex result."""
    result = avg_sales_by_region_and_product(_group_sample_df())
    assert isinstance(result.index, pd.MultiIndex)
    assert result[("east", "A")] == 125.0


def _pivot_sample_df():
    return pd.DataFrame({
        "region": ["east", "east", "west"],
        "product": ["A", "B", "A"],
        "sales": [100, 50, 200],
    })


def test_sales_pivot_table():
    """sales_pivot_table uses aggfunc="sum"."""
    result = sales_pivot_table(_pivot_sample_df())
    assert result.loc["east", "A"] == 100
    assert result.loc["west", "A"] == 200


def test_sales_pivot_count():
    """sales_pivot_count uses aggfunc="count" instead of "sum"."""
    result = sales_pivot_count(_pivot_sample_df())
    assert result.loc["east", "A"] == 1
''',
    },
    {
        "name": "tier3_advanced02",
        "title": "Apply and Dtype Optimization",
        "summary": "df.apply(), dtype-based memory optimization, multi-indexing (via set_index)",
        "readme": (
            "Implement:\n\n"
            "- `add_sales_tax_column(df, rate: float) -> pd.DataFrame` -- "
            "return a copy with a new `\"total\"` column: "
            "`df[\"sales\"].apply(lambda x: round(x * (1 + rate), 2))`.\n"
            "- `categorize_sales(df) -> pd.DataFrame` -- return a copy "
            "with a new `\"tier\"` column via "
            "`df[\"sales\"].apply(_categorize_amount)` (already given), "
            "which returns `\"low\"` (`x < 100`), `\"medium\"` "
            "(`100 <= x < 300`), or `\"high\"` (`x >= 300`).\n"
            "- `full_name_column(df) -> pd.DataFrame` -- return a copy "
            "with a new `\"full_name\"` column via **row-wise** apply: "
            "`df.apply(lambda row: f\"{row['first']} {row['last']}\", "
            "axis=1)` (`axis=1` runs the function once per *row* instead "
            "of once per column -- the other common shape of "
            "`.apply()`).\n"
            "- `optimize_dtypes(df) -> pd.DataFrame` -- return a copy "
            "with `region` cast to the `\"category\"` dtype "
            "(`df.astype({\"region\": \"category\"})`) -- a column with "
            "few distinct repeated string values takes far less memory "
            "as a `category` than as `object`.\n"
            "- `set_region_product_index(df) -> pd.DataFrame` -- "
            "`df.set_index([\"region\", \"product\"])` -- another way to "
            "get a `MultiIndex`, this time explicitly instead of as a "
            "side effect of `groupby`.\n\n"
            "See the Study Reference presentation, Topic 10 (Advanced "
            "tier), for the theory."
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
from exercises.stage10.tier3_advanced02.solution import (
    add_sales_tax_column,
    categorize_sales,
    full_name_column,
    optimize_dtypes,
    set_region_product_index,
)


def test_add_sales_tax_column():
    """add_sales_tax_column adds a "total" column via .apply() on the "sales" column."""
    df = pd.DataFrame({"sales": [100, 200]})
    result = add_sales_tax_column(df, 0.1)
    assert list(result["total"]) == [110.0, 220.0]


def test_categorize_sales():
    """categorize_sales adds a "tier" column via .apply(_categorize_amount)."""
    df = pd.DataFrame({"sales": [50, 150, 350]})
    result = categorize_sales(df)
    assert list(result["tier"]) == ["low", "medium", "high"]


def test_full_name_column_uses_row_wise_apply():
    """full_name_column must use df.apply(..., axis=1) -- one call per ROW, not per column."""
    df = pd.DataFrame({"first": ["Ada", "Grace"], "last": ["Lovelace", "Hopper"]})
    result = full_name_column(df)
    assert list(result["full_name"]) == ["Ada Lovelace", "Grace Hopper"]


def test_optimize_dtypes():
    """optimize_dtypes casts the "region" column to the "category" dtype."""
    df = pd.DataFrame({"region": ["east", "west", "east"]})
    result = optimize_dtypes(df)
    assert str(result["region"].dtype) == "category"


def test_set_region_product_index_is_multi_indexed():
    """set_region_product_index uses df.set_index([...]) to build a MultiIndex explicitly."""
    df = pd.DataFrame({"region": ["east", "west"], "product": ["A", "B"], "sales": [1, 2]})
    result = set_region_product_index(df)
    assert isinstance(result.index, pd.MultiIndex)
    assert result.loc[("east", "A"), "sales"] == 1
''',
    },
]
