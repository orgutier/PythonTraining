"""
OpenCV: Hand Posture & Face Gesture Recognition -- Loading and Inspecting Camera Frames
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage11_tier1_basic01.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage11/tier1_basic01/ and import it as a submodule (e.g.
`from exercises.stage11.tier1_basic01 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import cv2
import numpy as np


def load_frame(path: str):
    """cv2.imread(path)."""
    raise NotImplementedError


def save_frame(path: str, frame) -> bool:
    """cv2.imwrite(path, frame)."""
    raise NotImplementedError


def get_frame_dimensions(frame) -> tuple:
    """frame.shape[:2] -- (height, width)."""
    raise NotImplementedError


def create_blank_frame(height: int, width: int):
    """np.zeros((height, width, 3), dtype=np.uint8)."""
    raise NotImplementedError


def crop_to_roi(frame, y1: int, y2: int, x1: int, x2: int):
    """frame[y1:y2, x1:x2] -- rows (y) before columns (x)."""
    raise NotImplementedError
