"""
OpenCV -- Image I/O and Shape
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_week11_exercise01.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/week11/exercise01/ and import it as a submodule (e.g.
`from exercises.week11.exercise01 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import cv2


def load_image(path: str):
    """cv2.imread(path)."""
    raise NotImplementedError


def save_image(path: str, image) -> bool:
    """cv2.imwrite(path, image)."""
    raise NotImplementedError


def get_dimensions(image) -> tuple:
    """image.shape[:2] -- (height, width)."""
    raise NotImplementedError


def get_channel_count(image) -> int:
    """image.shape[2] if 3-dimensional, else 1."""
    raise NotImplementedError
