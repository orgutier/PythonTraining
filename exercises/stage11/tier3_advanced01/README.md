# Hand Posture via Contours and Convexity Defects

The centerpiece: turn a binary hand mask into a posture label (`"fist"`, `"partial"`, `"open_hand"`) with **no trained model file at all** -- purely contour geometry. (See `exercises/stage11/training_your_own_cascade/README.md` if you'd rather train a real hand-detector cascade of your own instead of using this algorithmic approach.)

Implement:

- `preprocess_hand_mask(mask)` -- `blurred = cv2.GaussianBlur(mask, (5, 5), 0)`, then `return cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)[1]`. This is **convolution filtering**: `GaussianBlur` slides a weighted-average kernel over every pixel, smoothing the jagged, staircase-like edges a raw binary mask has -- without it, those tiny jagged bumps register as spurious convexity defects below and throw off the finger count.
- `find_hand_contour(binary_mask)` -- `cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)` returns `(contours, hierarchy)`; return `max(contours, key=cv2.contourArea)` -- the largest contour, i.e. the hand silhouette itself (ignoring any small noise blobs).
- `count_extended_fingers(binary_mask) -> int` -- `contour = find_hand_contour(binary_mask)`; `hull_indices = cv2.convexHull(contour, returnPoints=False)`, then `sort` them (`np.sort(hull_indices, axis=0)` -- `cv2.convexityDefects` requires the hull indices in sorted order, a common gotcha); `defects = cv2.convexityDefects(contour, hull_indices)`; if `defects` is `None`, return `0`; otherwise count how many defects have a depth greater than `MIN_DEFECT_DEPTH` (already given as `8.0`) -- `defect[0][3] / 256.0` is that defect's depth in pixels (OpenCV packs it as a fixed-point integer, hence the `/ 256.0`). Each valley **between** two adjacent raised fingers shows up as one deep convexity defect.
- `classify_hand_posture(binary_mask) -> str` -- `count_extended_fingers(binary_mask)`, then `"fist"` if `0`, `"open_hand"` if `>= 4`, else `"partial"`.

See the Study Reference presentation, Topic 11 (Advanced tier), for the theory.
