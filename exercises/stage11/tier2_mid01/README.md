# Skin-Tone Thresholding for Hand Segmentation

The first real step of hand-posture recognition: turn a color frame into a black-and-white **mask** of "probably skin" pixels. Implement:

- `to_hsv(frame)` -- `cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)`. Skin tones cluster much more tightly in HSV (Hue/Saturation/Value) than in BGR, which is why real skin detectors threshold in HSV, not raw color.
- `segment_skin(frame, lower, upper)` -- `hsv = to_hsv(frame)`, then `cv2.inRange(hsv, lower, upper)` -- `cv2.inRange` is itself a form of **thresholding**: every pixel becomes `255` if it falls inside `[lower, upper]` on all three channels, else `0`.
- `SKIN_HSV_LOWER`/`SKIN_HSV_UPPER` (module level, already given) -- `np.array([0, 20, 70], dtype=np.uint8)` / `np.array([20, 255, 255], dtype=np.uint8)`, a commonly-used approximate range for a broad span of skin tones under normal lighting.
- `refine_mask(mask)` -- `cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)[1]` -- a second, explicit binary threshold pass that guarantees the mask is purely `0`/`255` (useful once real masks pick up blur or JPEG noise later in a pipeline, even though `cv2.inRange`'s output is already binary on its own).

See the Study Reference presentation, Topic 11 (Mid tier), for the theory.
