import cv2
import numpy as np
from challenges.challenge21.solution import (
    preprocess_for_scan,
    find_document_contour,
    bounding_box_of_contour,
    draw_document_outline,
    resize_to_fit,
)


def _document_photo():
    image = np.zeros((200, 200, 3), dtype=np.uint8)
    cv2.rectangle(image, (40, 40), (160, 160), (255, 255, 255), -1)
    return image


def test_preprocess_for_scan_returns_all_stages():
    result = preprocess_for_scan(_document_photo())
    assert set(result.keys()) == {"gray", "blurred", "edges"}
    assert result["gray"].shape == (200, 200)
    assert result["edges"].shape == (200, 200)


def test_find_document_contour_finds_largest():
    edges = preprocess_for_scan(_document_photo())["edges"]
    contour = find_document_contour(edges)
    assert contour is not None
    x, y, w, h = bounding_box_of_contour(contour)
    assert 30 < x < 50 and 30 < y < 50
    assert 100 < w < 140 and 100 < h < 140


def test_find_document_contour_none_when_no_contours():
    blank_edges = np.zeros((50, 50), dtype=np.uint8)
    assert find_document_contour(blank_edges) is None


def test_draw_document_outline_does_not_mutate_original():
    image = _document_photo()
    original = image.copy()
    edges = preprocess_for_scan(image)["edges"]
    contour = find_document_contour(edges)
    outlined = draw_document_outline(image, contour)
    assert np.array_equal(image, original)
    assert not np.array_equal(outlined, image)


def test_resize_to_fit_preserves_aspect_ratio():
    image = np.zeros((100, 200, 3), dtype=np.uint8)
    result = resize_to_fit(image, 50)
    assert max(result.shape[:2]) == 50
    assert result.shape[0] / result.shape[1] == 100 / 200
