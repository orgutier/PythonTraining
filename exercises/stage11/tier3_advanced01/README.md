# Blurring and Contours

Implement:

- `apply_gaussian_blur(image, ksize: int)` -- `cv2.GaussianBlur(image, (ksize, ksize), 0)` (`ksize` must be odd).
- `apply_strong_blur(image)` -- same idea with a fixed, larger kernel: `cv2.GaussianBlur(image, (15, 15), 0)`. Blurring is **convolution filtering**: a small kernel window slides over every pixel, replacing it with a weighted average of its neighbors -- a bigger kernel (as here) averages over a wider neighborhood, producing a blurrier result.
- `find_contours(binary_image) -> list` -- `cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]` (the first element of the tuple is the list of contours; the second, ignored here, is the hierarchy).
- `count_contours(binary_image) -> int` -- `len(find_contours(binary_image))`.
- `largest_contour_area(binary_image) -> float` -- `max(cv2.contourArea(c) for c in find_contours(binary_image))`.

See the Study Reference presentation, Topic 11 (Advanced tier), for the theory.
