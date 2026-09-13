import numpy as np
import cv2
import pytest
from exercises.week11.solution import to_grayscale, resize_image, draw_rectangle


@pytest.fixture
def sample_image(tmp_path):
    img = np.zeros((50, 80, 3), dtype=np.uint8)
    img[:] = (100, 150, 200)
    path = tmp_path / "input.png"
    cv2.imwrite(str(path), img)
    return str(path)


def test_to_grayscale(sample_image, tmp_path):
    out = str(tmp_path / "gray.png")
    to_grayscale(sample_image, out)
    result = cv2.imread(out, cv2.IMREAD_UNCHANGED)
    assert result.ndim == 2


def test_resize_image(sample_image, tmp_path):
    out = str(tmp_path / "resized.png")
    resize_image(sample_image, out, 40, 20)
    result = cv2.imread(out)
    assert result.shape[:2] == (20, 40)


def test_draw_rectangle(sample_image, tmp_path):
    out = str(tmp_path / "rect.png")
    draw_rectangle(sample_image, out, (5, 5), (20, 20))
    before = cv2.imread(sample_image)
    after = cv2.imread(out)
    assert not (before == after).all()
