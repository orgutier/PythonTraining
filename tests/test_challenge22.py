import numpy as np
from challenges.challenge22.solution import (
    load_default_face_cascade,
    load_grayscale,
    detect_faces,
    redact_regions,
    adaptive_binary,
    save_redacted,
)


def test_load_default_face_cascade_loads():
    cascade = load_default_face_cascade()
    assert cascade.empty() is False


def test_detect_faces_returns_empty_list_on_blank_image():
    cascade = load_default_face_cascade()
    blank = np.zeros((100, 100), dtype=np.uint8)
    result = detect_faces(blank, cascade)
    assert result == []
    assert isinstance(result, list)


def test_redact_regions_fills_black_and_does_not_mutate_original():
    image = np.full((50, 50, 3), 255, dtype=np.uint8)
    original = image.copy()
    redacted = redact_regions(image, [(10, 10, 10, 10)])
    assert np.array_equal(image, original)
    assert redacted[15, 15].tolist() == [0, 0, 0]
    assert redacted[0, 0].tolist() == [255, 255, 255]


def test_redact_regions_clips_out_of_bounds_box():
    image = np.full((20, 20, 3), 255, dtype=np.uint8)
    redacted = redact_regions(image, [(15, 15, 100, 100)])
    assert redacted[19, 19].tolist() == [0, 0, 0]


def test_adaptive_binary_returns_binary_image():
    gray = np.random.randint(0, 255, (30, 30), dtype=np.uint8)
    result = adaptive_binary(gray)
    assert result.shape == (30, 30)
    assert set(np.unique(result)).issubset({0, 255})


def test_load_and_save_grayscale_roundtrip(tmp_path):
    image = np.full((10, 10, 3), 128, dtype=np.uint8)
    path = str(tmp_path / "img.png")
    assert save_redacted(image, path) is True
    gray = load_grayscale(path)
    assert gray.shape == (10, 10)
