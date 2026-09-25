# Edge Detection with Canny

Implement:

- `detect_edges(gray_image, low: int, high: int)` -- `cv2.Canny(gray_image, low, high)`.
- `detect_edges_default(gray_image)` -- `cv2.Canny(gray_image, 100, 200)` (commonly-used default thresholds).
- `count_edge_pixels(gray_image, low: int, high: int) -> int` -- `int(np.count_nonzero(cv2.Canny(gray_image, low, high)))`.

See the Study Reference presentation, Topic 11 (Mid tier), for the theory.
