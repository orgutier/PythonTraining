"""
OpenCV: Hand Posture & Face Gesture Recognition -- Preparing Frames for Detection
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


def to_grayscale(frame):
    """cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)."""
    raise NotImplementedError


def resize_for_processing(frame, width: int, height: int):
    """cv2.resize(frame, (width, height))."""
    raise NotImplementedError


def draw_detection_box(frame, box: tuple, color: tuple, thickness: int = 2):
    """Draw an outlined (x, y, w, h) box on a COPY of frame; return the copy."""
    raise NotImplementedError


def draw_multiple_boxes(frame, boxes: list, color: tuple):
    """Draw one box per (x, y, w, h) in boxes, on a copy; return the copy."""
    raise NotImplementedError
