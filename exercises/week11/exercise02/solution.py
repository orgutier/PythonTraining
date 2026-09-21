"""
OpenCV -- Color Conversion and Resizing
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_week11_exercise02.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/week11/exercise02/ and import it as a submodule (e.g.
`from exercises.week11.exercise02 import helpers`) -- solution.py just has to
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


def get_shape_after_resize(image, width: int, height: int) -> tuple:
    """resize_image(image, width, height).shape[:2]."""
    raise NotImplementedError
