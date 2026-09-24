"""
OpenCV -- Cascade Classifiers
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage11_advanced02.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage11/advanced02/ and import it as a submodule (e.g.
`from exercises.stage11.advanced02 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import cv2


def load_default_face_cascade():
    """cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")."""
    raise NotImplementedError


def load_cascade_from_path(path: str):
    """cv2.CascadeClassifier(path)."""
    raise NotImplementedError


def is_cascade_loaded(cascade) -> bool:
    """not cascade.empty()."""
    raise NotImplementedError
