# Edge Detection on the Hand Silhouette

Once you have a binary hand mask (previous exercise), finding its outline is a natural next step toward the contour work in Advanced. Implement:

- `detect_hand_edges(binary_mask, low: int, high: int)` -- `cv2.Canny(binary_mask, low, high)`.
- `detect_hand_edges_default(binary_mask)` -- `cv2.Canny(binary_mask, 50, 150)` (commonly-used default thresholds for an already-binary mask).
- `count_edge_pixels(binary_mask, low: int, high: int) -> int` -- `int(np.count_nonzero(cv2.Canny(binary_mask, low, high)))`.

See the Study Reference presentation, Topic 11 (Mid tier), for the theory.
