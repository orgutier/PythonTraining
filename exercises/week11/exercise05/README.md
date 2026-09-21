# Edges and Contours

Implement:

- `detect_edges(gray_image, low: int, high: int)` -- `cv2.Canny(gray_image, low, high)`.
- `detect_edges_default(gray_image)` -- `cv2.Canny(gray_image, 100, 200)` (commonly-used default thresholds).
- `count_edge_pixels(gray_image, low: int, high: int) -> int` -- `int(np.count_nonzero(cv2.Canny(gray_image, low, high)))`.
- `find_contours(binary_image) -> list` -- `cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]` (the first element of the tuple is the list of contours; the second, ignored here, is the hierarchy).
- `count_contours(binary_image) -> int` -- `len(find_contours(binary_image))`.
- `largest_contour_area(binary_image) -> float` -- `max(cv2.contourArea(c) for c in find_contours(binary_image))`.

See the Study Reference presentation, Topic 11, for the theory.
