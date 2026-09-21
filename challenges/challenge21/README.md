# Challenge 21 — Document Scanner Preprocessing Pipeline

**Do this after:** Week 11 (OpenCV)
**Correctness is pytest-tested:** `python tools/cli.py test challenge21` (or `pytest tests/test_challenge21.py`). The constraints below on *how* you write it are not something pytest can check -- grade those yourself.

## Problem

"Build the preprocessing for a document scanner app" is a real, portfolio-
worthy OpenCV exercise: grayscale -> blur -> edge-detect -> find the
biggest contour (the document itself, assuming it's the largest shape in
frame) -> draw its outline. This challenge builds that whole pipeline,
touching most of Week 11's toolkit along the way.

Implement:

```python
def preprocess_for_scan(image) -> dict:
    """{"gray": ..., "blurred": ..., "edges": ...} -- grayscale, then a 5x5 Gaussian blur, then Canny edge detection (thresholds 50, 150)."""

def find_document_contour(edges):
    """The single largest-area contour found in edges (cv2.findContours + max by cv2.contourArea), or None if there are no contours at all."""

def bounding_box_of_contour(contour) -> tuple:
    """(x, y, w, h) -- the axis-aligned bounding box of contour."""

def draw_document_outline(image, contour):
    """A COPY of image with a green (0, 255, 0), 3px rectangle drawn around contour's bounding box."""

def resize_to_fit(image, max_dimension: int):
    """image resized so its LARGER of (height, width) equals max_dimension, aspect ratio preserved."""
```

```python
pipeline = preprocess_for_scan(photo)
contour = find_document_contour(pipeline["edges"])
outlined = draw_document_outline(photo, contour)
small = resize_to_fit(photo, 200)
max(small.shape[:2])   # -> 200
```

## Constraints on HOW you write it

1. **`preprocess_for_scan` must chain exactly** `cv2.cvtColor(image,
   cv2.COLOR_BGR2GRAY)` -> `cv2.GaussianBlur(gray, (5, 5), 0)` ->
   `cv2.Canny(blurred, 50, 150)`, and return all three intermediate
   images, not just the final edges (useful for debugging a real
   pipeline, and testable independently).
2. **`find_document_contour` must use `cv2.findContours(edges,
   cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)` then pick the max by
   `cv2.contourArea`** -- not the first contour found, and not the one
   with the most points.
3. **`bounding_box_of_contour` must use `cv2.boundingRect(contour)`.**
4. **`draw_document_outline` must draw on a copy** (`image.copy()`),
   never mutating the caller's original `image` -- same discipline as
   any other drawing function.
5. **`resize_to_fit` must compute the target size from `image.shape`**
   (which is `(height, width, channels)`), scale both dimensions by the
   *same* factor (`max_dimension / max(height, width)`), and pass an
   explicit `(width, height)` tuple to `cv2.resize` -- not
   `fx=`/`fy=` percentage scaling.
6. **A docstring on `find_document_contour`** listing edge cases: an
   `edges` image with no contours at all (returns `None`, not an empty
   list or an error), and multiple contours of very different sizes (only
   the single largest is returned).
