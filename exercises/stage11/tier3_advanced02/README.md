# Face Gesture and Gaze Direction (Driver-Camera Style)

The face side of the pipeline, built entirely on Haar cascade files **already inside your `opencv-python` install** (`cv2.data.haarcascades`) -- genuinely trained files that run fully offline, no download or internet connection needed. This is the same coarse idea a driver-monitoring camera module uses: is a face visible, is it smiling, and roughly which way are the eyes pointing within it.

Implement:

- `load_face_cascade()` -- `cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")`.
- `load_eye_cascade()` -- `cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")`.
- `load_smile_cascade()` -- `cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")` -- a **facial gesture** detector: a smile is a gesture your face makes, and this cascade was trained specifically to recognize it.
- `is_cascade_loaded(cascade) -> bool` -- `not cascade.empty()` -- `.empty()` is `True` when the classifier failed to load (e.g. a bad path), so this is how you check a load actually worked before trying to use it.
- `detect_smile(face_gray_region, smile_cascade) -> bool` -- `detections = smile_cascade.detectMultiScale(face_gray_region, scaleFactor=1.7, minNeighbors=20)`, then `return len(detections) > 0`. (`scaleFactor`/`minNeighbors` are tuned higher than a typical face cascade's defaults -- smiles have far more visual variation than faces do, so a smile cascade needs more neighbor agreement before it commits to a detection.)
- `estimate_gaze_direction(face_box: tuple, eye_boxes: list, off_axis_ratio: float = 0.15) -> str` -- given an already-detected `face_box = (fx, fy, fw, fh)` and `eye_boxes = [(ex, ey, ew, eh), ...]` (exactly what `cascade.detectMultiScale(...)` returns), estimate which way the eyes are pointing **within the face box**: if `eye_boxes` is empty, return `"looking_away"` (no eyes detected -- occluded, closed, or turned too far to see). Otherwise compute `eye_centroid_x` -- the average of each eye box's own center x (`ex + ew / 2`) -- and `face_center_x = fx + fw / 2`; if `eye_centroid_x` is more than `fw * off_axis_ratio` to the left of `face_center_x`, return `"left"`; more than that to the right, `"right"`; otherwise `"center"`.

This is a **coarse proxy**, not true 3D gaze estimation (which needs a trained regression model, well beyond a Haar cascade) -- but it's exactly the kind of lightweight, fully-local heuristic a simple attention-monitoring feature can be built from.

See the Study Reference presentation, Topic 11 (Advanced tier), for the theory.
