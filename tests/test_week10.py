import pytest
from exercises.week10.solution import (
    load_sales_data,
    total_sales_by_region,
    top_n_products,
)


@pytest.fixture
def sample_csv(tmp_path):
    content = (
        "product,region,sales\n"
        "Widget,East,100\n"
        "Gadget,West,200\n"
        "Widget,West,150\n"
        "Gizmo,East,50\n"
    )
    p = tmp_path / "sales.csv"
    p.write_text(content)
    return str(p)


def test_total_sales_by_region(sample_csv):
    df = load_sales_data(sample_csv)
    result = total_sales_by_region(df)
    assert result["East"] == 150
    assert result["West"] == 350


def test_top_n_products(sample_csv):
    df = load_sales_data(sample_csv)
    top2 = top_n_products(df, 2)
    assert list(top2["product"]) == ["Gadget", "Widget"]
