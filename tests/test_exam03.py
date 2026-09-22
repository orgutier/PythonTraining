"""
Tests for Exam 3 -- Product Analytics & Photo Pipeline API (Stages 10-13).
"""
from unittest.mock import Mock
import cv2
import numpy as np
import pandas as pd
import pytest
from fastapi.testclient import TestClient

import exams.exam03.solution as exam03
from exams.exam03.solution import (
    sales_by_category,
    pivot_revenue_by_region_and_month,
    merge_with_targets,
    flag_underperforming,
    preprocess_product_photo,
    crop_to_largest_contour,
    compute_brightness,
    ThreadSafeCounter,
    fetch_all_metadata_concurrently,
    app,
)

client = TestClient(app)


@pytest.fixture(autouse=True)
def _reset_module_state():
    exam03._sales_df = pd.DataFrame(columns=["category", "region", "month", "revenue"])
    exam03._targets_df = pd.DataFrame(columns=["category", "target"])
    exam03._photo_counter = ThreadSafeCounter()
    yield


@pytest.fixture
def sales_df():
    return pd.DataFrame([
        {"category": "toys", "region": "east", "month": "jan", "revenue": 100.0},
        {"category": "toys", "region": "west", "month": "jan", "revenue": 50.0},
        {"category": "tools", "region": "east", "month": "jan", "revenue": 200.0},
        {"category": "toys", "region": "east", "month": "feb", "revenue": 30.0},
    ])


@pytest.fixture
def targets_df():
    return pd.DataFrame([
        {"category": "toys", "target": 300.0},
        {"category": "tools", "target": 100.0},
    ])


def _white_square_on_black():
    image = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.rectangle(image, (20, 20), (80, 80), (255, 255, 255), -1)
    return image


# --------------------------------------------------------------------------- Stage 10

def test_sales_by_category_sums_and_sorts(sales_df):
    result = sales_by_category(sales_df)
    assert list(result["category"]) == ["tools", "toys"]
    assert list(result["revenue"]) == [200.0, 180.0]


def test_sales_by_category_returns_fresh_reset_index(sales_df):
    result = sales_by_category(sales_df)
    assert list(result.index) == list(range(len(result)))


def test_pivot_revenue_by_region_and_month(sales_df):
    pivot = pivot_revenue_by_region_and_month(sales_df)
    assert pivot.loc["east", "jan"] == 300.0
    assert pivot.loc["west", "jan"] == 50.0
    assert pivot.loc["east", "feb"] == 30.0
    assert pivot.loc["west", "feb"] == 0


def test_merge_with_targets_computes_pct(sales_df, targets_df):
    merged = merge_with_targets(sales_df, targets_df)
    toys_row = merged[merged["category"] == "toys"].iloc[0]
    assert toys_row["revenue"] == 180.0
    assert toys_row["pct_of_target"] == pytest.approx(180.0 / 300.0)
    tools_row = merged[merged["category"] == "tools"].iloc[0]
    assert tools_row["pct_of_target"] == pytest.approx(200.0 / 100.0)


def test_flag_underperforming_filters_below_threshold(sales_df, targets_df):
    merged = merge_with_targets(sales_df, targets_df)
    flagged = flag_underperforming(merged, threshold=0.7)
    categories = set(flagged["category"])
    assert "toys" in categories
    assert "tools" not in categories


# --------------------------------------------------------------------------- Stage 11

def test_preprocess_product_photo_returns_all_stages():
    result = preprocess_product_photo(_white_square_on_black())
    assert set(result.keys()) == {"gray", "blurred", "thresh"}
    assert result["gray"].shape == (100, 100)
    assert result["thresh"].shape == (100, 100)


def test_crop_to_largest_contour_crops_to_square():
    cropped = crop_to_largest_contour(_white_square_on_black())
    assert 50 < cropped.shape[0] < 70
    assert 50 < cropped.shape[1] < 70


def test_crop_to_largest_contour_no_contours_returns_original():
    blank = np.zeros((50, 50, 3), dtype=np.uint8)
    result = crop_to_largest_contour(blank)
    assert result.shape == blank.shape


def test_compute_brightness_bright_vs_dark():
    dark = np.zeros((20, 20, 3), dtype=np.uint8)
    bright = np.full((20, 20, 3), 255, dtype=np.uint8)
    assert compute_brightness(bright) > compute_brightness(dark)


# --------------------------------------------------------------------------- Stage 12

def test_thread_safe_counter_increment():
    counter = ThreadSafeCounter()
    for _ in range(5):
        counter.increment()
    assert counter.value == 5


def test_thread_safe_counter_concurrent_increments():
    import threading as th
    counter = ThreadSafeCounter()

    def bump():
        for _ in range(200):
            counter.increment()

    threads = [th.Thread(target=bump) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert counter.value == 800


def _fake_response(json_data):
    response = Mock()
    response.json.return_value = json_data
    response.raise_for_status.return_value = None
    return response


def test_fetch_all_metadata_concurrently_preserves_order_and_counts():
    session = Mock()
    session.get.side_effect = lambda url: _fake_response({"url": url})
    counter = ThreadSafeCounter()
    urls = [f"https://example.test/{i}" for i in range(6)]
    results = fetch_all_metadata_concurrently(session, urls, counter, max_workers=3)
    assert [r["url"] for r in results] == urls
    assert counter.value == 6


# --------------------------------------------------------------------------- Stage 13

def test_sales_summary_endpoint(sales_df):
    exam03._sales_df = sales_df
    response = client.get("/sales/summary")
    assert response.status_code == 200
    data = response.json()
    categories = {row["category"] for row in data}
    assert categories == {"toys", "tools"}


def test_underperforming_endpoint_default_threshold_flags_nothing(sales_df, targets_df):
    exam03._sales_df = sales_df
    exam03._targets_df = targets_df
    response = client.get("/sales/underperforming")
    assert response.status_code == 200
    assert response.json() == []


def test_underperforming_endpoint_custom_threshold_flags_toys(sales_df, targets_df):
    exam03._sales_df = sales_df
    exam03._targets_df = targets_df
    response = client.get("/sales/underperforming", params={"threshold": 0.7})
    categories = {row["category"] for row in response.json()}
    assert categories == {"toys"}


def test_underperforming_endpoint_rejects_out_of_range_threshold():
    response = client.get("/sales/underperforming", params={"threshold": 2.0})
    assert response.status_code == 422


def test_photo_fetch_count_endpoint_reflects_counter():
    exam03._photo_counter.increment()
    exam03._photo_counter.increment()
    response = client.get("/photos/fetch-count")
    assert response.status_code == 200
    assert response.json() == {"count": 2}
