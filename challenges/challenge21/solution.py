"""
Challenge 21 - Document Scanner Preprocessing Pipeline
Interview-style challenge. Correctness is pytest-tested (see
tests/test_challenge21.py / `python tools/cli.py test challenge21`); see
README.md in this folder for the full problem statement and the constraints
your solution must follow (a full cvtColor/GaussianBlur/Canny/findContours pipeline, the largest-contour trick, and an aspect-ratio-preserving resize).

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module, matching the convention used by
exercises/weekNN/solution.py.
"""


import cv2


def preprocess_for_scan(image) -> dict:
    """{"gray", "blurred", "edges"} -- cvtColor -> GaussianBlur(5,5) -> Canny(50,150)."""
    raise NotImplementedError


def find_document_contour(edges):
    """The largest-area contour in edges (by cv2.contourArea), or None if there are none."""
    raise NotImplementedError


def bounding_box_of_contour(contour) -> tuple:
    """(x, y, w, h) via cv2.boundingRect."""
    raise NotImplementedError


def draw_document_outline(image, contour):
    """A copy of image with a green 3px rectangle around contour's bounding box."""
    raise NotImplementedError


def resize_to_fit(image, max_dimension: int):
    """image resized so its larger dimension equals max_dimension, aspect ratio preserved."""
    raise NotImplementedError
