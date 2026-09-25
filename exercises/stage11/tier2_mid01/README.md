# Thresholding

Implement three ways to binarize a grayscale image:

- `apply_threshold(gray_image, thresh_value: int)` -- `cv2.threshold(gray_image, thresh_value, 255, cv2.THRESH_BINARY)[1]` (`cv2.threshold` returns `(used_threshold, result_image)` -- take `[1]`, the image).
- `apply_otsu_threshold(gray_image)` -- `cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]` -- Otsu's method picks the threshold value *automatically* from the image's histogram, so the `0` you pass for `thresh_value` is ignored.
- `apply_adaptive_threshold(gray_image)` -- `cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)` -- picks a *different* threshold for each local neighborhood instead of one global value, useful when lighting is uneven across the image.

See the Study Reference presentation, Topic 11 (Mid tier), for the theory.
