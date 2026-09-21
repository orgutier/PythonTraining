"""
OpenCV -- Drawing on Images
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the aggregated test suite in
tests/test_week11.py imports directly from here. Need a helper function or
class of your own? Add another .py file next to this one inside
exercises/week11/exercise03/ and import it as a submodule (e.g.
`from exercises.week11.exercise03 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import cv2


def draw_rectangle(image, pt1: tuple, pt2: tuple, color: tuple):
    """Draw an outlined rectangle on a COPY of image; return the copy."""
    raise NotImplementedError


def draw_filled_rectangle(image, pt1: tuple, pt2: tuple, color: tuple):
    """Draw a FILLED rectangle (thickness=-1) on a copy; return the copy."""
    raise NotImplementedError


def draw_bounding_boxes(image, boxes: list, color: tuple):
    """Draw one rectangle per (x1, y1, x2, y2) in boxes, on a copy."""
    raise NotImplementedError
