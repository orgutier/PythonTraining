"""
OpenCV -- Color Conversion, Resizing, and Drawing
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage11_tier1_basic02.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage11/tier1_basic02/ and import it as a submodule (e.g.
`from exercises.stage11.tier1_basic02 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import cv2


def to_grayscale(image):
    """cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)."""
    raise NotImplementedError


def to_rgb(image):
    """cv2.cvtColor(image, cv2.COLOR_BGR2RGB)."""
    raise NotImplementedError


def resize_image(image, width: int, height: int):
    """cv2.resize(image, (width, height))."""
    raise NotImplementedError


def resize_by_scale(image, scale: float):
    """cv2.resize(image, None, fx=scale, fy=scale)."""
    raise NotImplementedError


def draw_rectangle(image, pt1: tuple, pt2: tuple, color: tuple):
    """Draw an outlined rectangle on a COPY of image; return the copy."""
    raise NotImplementedError


def draw_bounding_boxes(image, boxes: list, color: tuple):
    """Draw one rectangle per (x1, y1, x2, y2) in boxes, on a copy."""
    raise NotImplementedError
