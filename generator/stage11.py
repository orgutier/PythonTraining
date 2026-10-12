"""
Stage 11 -- OpenCV: Hand Posture & Face Gesture Recognition.

Rolled onto the tier-named exercise convention: a minimum of two exercises
per Basic/Mid/Advanced tier. Every exercise builds toward one real system:
a webcam-style pipeline that reads hand posture (fist / partial / open
hand, via skin-color segmentation + convexity defects -- no trained model
file needed, and therefore no licensing risk: see
exercises/stage11/training_your_own_cascade/README.md if you want to go
further and train a real Haar cascade of your own) and face gesture / gaze
direction (via the Haar cascade files OpenCV already ships inside
opencv-python -- genuinely "trained files that run locally", no download
needed -- the same coarse approach a driver-monitoring camera module
uses: is a face visible, is it smiling, and roughly which way are the
eyes pointing within it).

All test images are built synthetically with numpy/cv2 drawing primitives
(no external image files needed, no webcam needed), since images are just
NumPy arrays -- that's the whole point of this stage.

Coverage plan (every item below is exercised by the trainee's own code,
generally 2+ times across these 6 exercises):

  Basic:    cv2.imread, cv2.imwrite, cv2.cvtColor, cv2.resize,
            cv2.rectangle, image.shape, numpy
  Mid:      cv2.Canny(), thresholding
  Advanced: cv2.findContours(), cv2.GaussianBlur(), cv2.CascadeClassifier,
            convolution filtering
"""

STAGE = "stage11"
TOPIC = "OpenCV: Hand Posture & Face Gesture Recognition"
OVERVIEW = (
    "Six exercises, two per tier, building one pipeline: loading/prepping "
    "camera frames in Basic; skin-tone thresholding and edge detection on "
    "the hand silhouette in Mid; counting extended fingers via contours "
    "and convexity defects, plus face/smile/gaze-direction detection via "
    "OpenCV's own bundled Haar cascades, in Advanced."
)

EXERCISES = [
    {
        "name": "tier1_basic01",
        "title": "Loading and Inspecting Camera Frames",
        "summary": "cv2.imread, cv2.imwrite, image.shape, numpy",
        "readme": (
            "A camera-fed gesture-recognition pipeline starts with plain "
            "frame I/O -- and an OpenCV frame *is* a NumPy array, so "
            "`.shape` is a plain array attribute, not something OpenCV "
            "adds. Implement:\n\n"
            "- `load_frame(path: str)` -- `cv2.imread(path)` (returns a "
            "NumPy array in BGR order, or `None` if the file can't be "
            "read).\n"
            "- `save_frame(path: str, frame) -> bool` -- "
            "`cv2.imwrite(path, frame)`.\n"
            "- `get_frame_dimensions(frame) -> tuple` -- `frame.shape[:2]`, "
            "i.e. `(height, width)` -- note **height first**, which trips "
            "up everyone coming from `(width, height)` conventions "
            "elsewhere.\n"
            "- `create_blank_frame(height: int, width: int)` -- "
            "`np.zeros((height, width, 3), dtype=np.uint8)` -- a blank "
            "BGR frame, the same shape a real camera would hand you.\n"
            "- `crop_to_roi(frame, y1: int, y2: int, x1: int, x2: int)` -- "
            "`frame[y1:y2, x1:x2]` -- ordinary NumPy array slicing, rows "
            "(`y`) before columns (`x`). This is how you crop to a "
            "**region of interest** (e.g. a detected face or hand box) in "
            "OpenCV -- there's no separate \"crop function\", because the "
            "frame is just an array.\n\n"
            "See the Study Reference presentation, Topic 11 (Basic "
            "tier), for the theory."
        ),
        "stub": '''\
import cv2
import numpy as np


def load_frame(path: str):
    """cv2.imread(path)."""
    raise NotImplementedError


def save_frame(path: str, frame) -> bool:
    """cv2.imwrite(path, frame)."""
    raise NotImplementedError


def get_frame_dimensions(frame) -> tuple:
    """frame.shape[:2] -- (height, width)."""
    raise NotImplementedError


def create_blank_frame(height: int, width: int):
    """np.zeros((height, width, 3), dtype=np.uint8)."""
    raise NotImplementedError


def crop_to_roi(frame, y1: int, y2: int, x1: int, x2: int):
    """frame[y1:y2, x1:x2] -- rows (y) before columns (x)."""
    raise NotImplementedError
''',
        "reference": '''\
import cv2
import numpy as np


def load_frame(path: str):
    return cv2.imread(path)


def save_frame(path: str, frame) -> bool:
    return cv2.imwrite(path, frame)


def get_frame_dimensions(frame) -> tuple:
    return frame.shape[:2]


def create_blank_frame(height: int, width: int):
    return np.zeros((height, width, 3), dtype=np.uint8)


def crop_to_roi(frame, y1: int, y2: int, x1: int, x2: int):
    return frame[y1:y2, x1:x2]
''',
        "test": '''\
import numpy as np
from exercises.stage11.tier1_basic01.solution import (
    load_frame,
    save_frame,
    get_frame_dimensions,
    create_blank_frame,
    crop_to_roi,
)


def test_save_and_load_roundtrip(tmp_path):
    """save_frame/load_frame round-trip via cv2.imwrite/cv2.imread."""
    path = str(tmp_path / "frame.png")
    original = np.zeros((20, 30, 3), dtype=np.uint8)
    original[:, :] = (0, 0, 255)
    assert save_frame(path, original) is True
    loaded = load_frame(path)
    assert loaded is not None
    assert loaded.shape == (20, 30, 3)


def test_load_missing_file_returns_none():
    """cv2.imread must return None (not raise) for a missing file."""
    assert load_frame("/nonexistent/path/to/frame.png") is None


def test_get_frame_dimensions_is_height_then_width():
    """get_frame_dimensions == frame.shape[:2] -- height first, not (width, height)."""
    frame = np.zeros((20, 30, 3), dtype=np.uint8)
    assert get_frame_dimensions(frame) == (20, 30)


def test_create_blank_frame():
    """create_blank_frame == np.zeros((height, width, 3), dtype=np.uint8)."""
    frame = create_blank_frame(10, 20)
    assert frame.shape == (10, 20, 3)
    assert frame.sum() == 0


def test_crop_to_roi_is_plain_array_slicing():
    """crop_to_roi must be frame[y1:y2, x1:x2] -- rows before columns."""
    frame = np.arange(100).reshape(10, 10).astype(np.uint8)
    cropped = crop_to_roi(frame, 2, 5, 3, 6)
    assert cropped.shape == (3, 3)
''',
    },
    {
        "name": "tier1_basic02",
        "title": "Preparing Frames for Detection",
        "summary": "cv2.cvtColor, cv2.resize, cv2.rectangle",
        "readme": (
            "Every detector in this stage (skin thresholding, Haar "
            "cascades) needs frames prepared first. Implement:\n\n"
            "- `to_grayscale(frame)` -- `cv2.cvtColor(frame, "
            "cv2.COLOR_BGR2GRAY)` -- Haar cascades run on grayscale, "
            "never color.\n"
            "- `resize_for_processing(frame, width: int, height: int)` "
            "-- `cv2.resize(frame, (width, height))` -- note the "
            "argument order here **is** `(width, height)`, the opposite "
            "of `.shape`'s `(height, width)`. Real pipelines resize "
            "every incoming frame to a fixed size first, so detection "
            "runs at a predictable, controllable cost.\n"
            "- `draw_detection_box(frame, box: tuple, color: tuple, "
            "thickness: int = 2)` -- `box` is `(x, y, w, h)`. Work on "
            "**a copy** (`frame.copy()`, since `cv2.rectangle` draws in "
            "place) and `cv2.rectangle(copy, (x, y), (x + w, y + h), "
            "color, thickness)`, returning the copy.\n"
            "- `draw_multiple_boxes(frame, boxes: list, color: tuple)` "
            "-- work on a copy; call `draw_detection_box`'s underlying "
            "`cv2.rectangle` logic once per `(x, y, w, h)` box in "
            "`boxes`, then return the copy. Always drawing onto a copy "
            "(never the original `frame` parameter) matters because "
            "`cv2.rectangle` mutates the array it's given -- without "
            "copying first, drawing detections on the same source frame "
            "twice would compound, and the caller's original frame would "
            "silently change too.\n\n"
            "See the Study Reference presentation, Topic 11 (Basic "
            "tier), for the theory."
        ),
        "stub": '''\
import cv2


def to_grayscale(frame):
    """cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)."""
    raise NotImplementedError


def resize_for_processing(frame, width: int, height: int):
    """cv2.resize(frame, (width, height))."""
    raise NotImplementedError


def draw_detection_box(frame, box: tuple, color: tuple, thickness: int = 2):
    """Draw an outlined (x, y, w, h) box on a COPY of frame; return the copy."""
    raise NotImplementedError


def draw_multiple_boxes(frame, boxes: list, color: tuple):
    """Draw one box per (x, y, w, h) in boxes, on a copy; return the copy."""
    raise NotImplementedError
''',
        "reference": '''\
import cv2


def to_grayscale(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


def resize_for_processing(frame, width: int, height: int):
    return cv2.resize(frame, (width, height))


def draw_detection_box(frame, box: tuple, color: tuple, thickness: int = 2):
    result = frame.copy()
    x, y, w, h = box
    cv2.rectangle(result, (x, y), (x + w, y + h), color, thickness)
    return result


def draw_multiple_boxes(frame, boxes: list, color: tuple):
    result = frame.copy()
    for x, y, w, h in boxes:
        cv2.rectangle(result, (x, y), (x + w, y + h), color, 2)
    return result
''',
        "test": '''\
import numpy as np
from exercises.stage11.tier1_basic02.solution import (
    to_grayscale,
    resize_for_processing,
    draw_detection_box,
    draw_multiple_boxes,
)


def _bgr_frame():
    frame = np.zeros((10, 10, 3), dtype=np.uint8)
    frame[:, :] = (255, 0, 0)
    return frame


def test_to_grayscale_drops_channel_dim():
    """to_grayscale must use cv2.COLOR_BGR2GRAY, producing a 2D array."""
    gray = to_grayscale(_bgr_frame())
    assert gray.shape == (10, 10)


def test_resize_for_processing_uses_width_height_order():
    """resize_for_processing passes (width, height) to cv2.resize -- the opposite of .shape's (height, width)."""
    resized = resize_for_processing(_bgr_frame(), 20, 5)
    assert resized.shape[:2] == (5, 20)


def test_draw_detection_box_does_not_mutate_original():
    """draw_detection_box must draw on frame.copy(), leaving the original untouched."""
    frame = np.zeros((20, 20, 3), dtype=np.uint8)
    result = draw_detection_box(frame, (2, 2, 8, 8), (255, 255, 255))
    assert np.array_equal(frame, np.zeros((20, 20, 3), dtype=np.uint8))
    assert result[2, 2].tolist() == [255, 255, 255]


def test_draw_multiple_boxes_draws_all_and_does_not_mutate():
    """draw_multiple_boxes draws every box from a copy, leaving the original frame untouched."""
    frame = np.zeros((30, 30, 3), dtype=np.uint8)
    boxes = [(1, 1, 4, 4), (10, 10, 5, 5)]
    result = draw_multiple_boxes(frame, boxes, (255, 0, 0))
    assert result[1, 1].tolist() == [255, 0, 0]
    assert result[10, 10].tolist() == [255, 0, 0]
    assert frame.sum() == 0
''',
    },
    {
        "name": "tier2_mid01",
        "title": "Skin-Tone Thresholding for Hand Segmentation",
        "summary": "thresholding",
        "readme": (
            "The first real step of hand-posture recognition: turn a "
            "color frame into a black-and-white **mask** of \"probably "
            "skin\" pixels. Implement:\n\n"
            "- `to_hsv(frame)` -- `cv2.cvtColor(frame, "
            "cv2.COLOR_BGR2HSV)`. Skin tones cluster much more tightly "
            "in HSV (Hue/Saturation/Value) than in BGR, which is why "
            "real skin detectors threshold in HSV, not raw color.\n"
            "- `segment_skin(frame, lower, upper)` -- `hsv = "
            "to_hsv(frame)`, then `cv2.inRange(hsv, lower, upper)` -- "
            "`cv2.inRange` is itself a form of **thresholding**: every "
            "pixel becomes `255` if it falls inside `[lower, upper]` on "
            "all three channels, else `0`.\n"
            "- `SKIN_HSV_LOWER`/`SKIN_HSV_UPPER` (module level, already "
            "given) -- `np.array([0, 20, 70], dtype=np.uint8)` / "
            "`np.array([20, 255, 255], dtype=np.uint8)`, a commonly-used "
            "approximate range for a broad span of skin tones under "
            "normal lighting.\n"
            "- `refine_mask(mask)` -- `cv2.threshold(mask, 127, 255, "
            "cv2.THRESH_BINARY)[1]` -- a second, explicit binary "
            "threshold pass that guarantees the mask is purely `0`/`255` "
            "(useful once real masks pick up blur or JPEG noise later in "
            "a pipeline, even though `cv2.inRange`'s output is already "
            "binary on its own).\n\n"
            "See the Study Reference presentation, Topic 11 (Mid tier), "
            "for the theory."
        ),
        "stub": '''\
import cv2
import numpy as np

SKIN_HSV_LOWER = np.array([0, 20, 70], dtype=np.uint8)
SKIN_HSV_UPPER = np.array([20, 255, 255], dtype=np.uint8)


def to_hsv(frame):
    """cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)."""
    raise NotImplementedError


def segment_skin(frame, lower, upper):
    """cv2.inRange(to_hsv(frame), lower, upper)."""
    raise NotImplementedError


def refine_mask(mask):
    """cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)[1]."""
    raise NotImplementedError
''',
        "reference": '''\
import cv2
import numpy as np

SKIN_HSV_LOWER = np.array([0, 20, 70], dtype=np.uint8)
SKIN_HSV_UPPER = np.array([20, 255, 255], dtype=np.uint8)


def to_hsv(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


def segment_skin(frame, lower, upper):
    hsv = to_hsv(frame)
    return cv2.inRange(hsv, lower, upper)


def refine_mask(mask):
    return cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)[1]
''',
        "test": '''\
import numpy as np
from exercises.stage11.tier2_mid01.solution import (
    to_hsv,
    segment_skin,
    refine_mask,
    SKIN_HSV_LOWER,
    SKIN_HSV_UPPER,
)


def _skin_toned_frame():
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    frame[20:80, 20:80] = (120, 150, 200)  # a BGR skin-tone swatch
    return frame


def test_to_hsv_converts_color_space():
    """to_hsv must use cv2.COLOR_BGR2HSV, changing pixel values from the BGR input."""
    frame = _skin_toned_frame()
    hsv = to_hsv(frame)
    assert hsv.shape == frame.shape
    assert not np.array_equal(hsv, frame)


def test_segment_skin_isolates_the_skin_toned_region():
    """segment_skin must mark the skin-toned swatch 255 and the black background 0."""
    frame = _skin_toned_frame()
    mask = segment_skin(frame, SKIN_HSV_LOWER, SKIN_HSV_UPPER)
    assert mask[50, 50] == 255
    assert mask[5, 5] == 0
    assert np.count_nonzero(mask) == 60 * 60


def test_refine_mask_stays_binary():
    """refine_mask must produce a purely 0/255 mask via an explicit threshold pass."""
    frame = _skin_toned_frame()
    mask = segment_skin(frame, SKIN_HSV_LOWER, SKIN_HSV_UPPER)
    refined = refine_mask(mask)
    assert set(np.unique(refined)).issubset({0, 255})
    assert np.array_equal(refined, mask)
''',
    },
    {
        "name": "tier2_mid02",
        "title": "Edge Detection on the Hand Silhouette",
        "summary": "cv2.Canny()",
        "readme": (
            "Once you have a binary hand mask (previous exercise), "
            "finding its outline is a natural next step toward the "
            "contour work in Advanced. Implement:\n\n"
            "- `detect_hand_edges(binary_mask, low: int, high: int)` -- "
            "`cv2.Canny(binary_mask, low, high)`.\n"
            "- `detect_hand_edges_default(binary_mask)` -- "
            "`cv2.Canny(binary_mask, 50, 150)` (commonly-used default "
            "thresholds for an already-binary mask).\n"
            "- `count_edge_pixels(binary_mask, low: int, high: int) -> "
            "int` -- `int(np.count_nonzero(cv2.Canny(binary_mask, low, "
            "high)))`.\n\n"
            "See the Study Reference presentation, Topic 11 (Mid tier), "
            "for the theory."
        ),
        "stub": '''\
import cv2
import numpy as np


def detect_hand_edges(binary_mask, low: int, high: int):
    """cv2.Canny(binary_mask, low, high)."""
    raise NotImplementedError


def detect_hand_edges_default(binary_mask):
    """cv2.Canny(binary_mask, 50, 150)."""
    raise NotImplementedError


def count_edge_pixels(binary_mask, low: int, high: int) -> int:
    """int(np.count_nonzero(cv2.Canny(binary_mask, low, high)))."""
    raise NotImplementedError
''',
        "reference": '''\
import cv2
import numpy as np


def detect_hand_edges(binary_mask, low: int, high: int):
    return cv2.Canny(binary_mask, low, high)


def detect_hand_edges_default(binary_mask):
    return cv2.Canny(binary_mask, 50, 150)


def count_edge_pixels(binary_mask, low: int, high: int) -> int:
    return int(np.count_nonzero(cv2.Canny(binary_mask, low, high)))
''',
        "test": '''\
import numpy as np
from exercises.stage11.tier2_mid02.solution import (
    detect_hand_edges,
    detect_hand_edges_default,
    count_edge_pixels,
)


def _hand_mask():
    mask = np.zeros((100, 100), dtype=np.uint8)
    mask[20:80, 20:80] = 255
    return mask


def test_detect_hand_edges_finds_the_silhouette_boundary():
    """detect_hand_edges must find edge pixels around the mask's boundary."""
    edges = detect_hand_edges(_hand_mask(), 50, 150)
    assert edges.sum() > 0


def test_detect_hand_edges_default_uses_50_150():
    """detect_hand_edges_default == cv2.Canny(binary_mask, 50, 150), same output shape as input."""
    edges = detect_hand_edges_default(_hand_mask())
    assert edges.shape == (100, 100)


def test_count_edge_pixels():
    """count_edge_pixels counts nonzero pixels in the Canny output."""
    assert count_edge_pixels(_hand_mask(), 50, 150) > 0
''',
    },
    {
        "name": "tier3_advanced01",
        "title": "Hand Posture via Contours and Convexity Defects",
        "summary": "cv2.findContours(), cv2.GaussianBlur(), convolution filtering",
        "readme": (
            "The centerpiece: turn a binary hand mask into a posture "
            "label (`\"fist\"`, `\"partial\"`, `\"open_hand\"`) with **no "
            "trained model file at all** -- purely contour geometry. "
            "(See `exercises/stage11/training_your_own_cascade/README.md` "
            "if you'd rather train a real hand-detector cascade of your "
            "own instead of using this algorithmic approach.)\n\n"
            "Implement:\n\n"
            "- `preprocess_hand_mask(mask)` -- `blurred = "
            "cv2.GaussianBlur(mask, (5, 5), 0)`, then `return "
            "cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)[1]`. "
            "This is **convolution filtering**: `GaussianBlur` slides a "
            "weighted-average kernel over every pixel, smoothing the "
            "jagged, staircase-like edges a raw binary mask has -- "
            "without it, those tiny jagged bumps register as spurious "
            "convexity defects below and throw off the finger count.\n"
            "- `find_hand_contour(binary_mask)` -- "
            "`cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, "
            "cv2.CHAIN_APPROX_SIMPLE)` returns `(contours, hierarchy)`; "
            "return `max(contours, key=cv2.contourArea)` -- the largest "
            "contour, i.e. the hand silhouette itself (ignoring any "
            "small noise blobs).\n"
            "- `count_extended_fingers(binary_mask) -> int` -- "
            "`contour = find_hand_contour(binary_mask)`; `hull_indices = "
            "cv2.convexHull(contour, returnPoints=False)`, then `sort` "
            "them (`np.sort(hull_indices, axis=0)` -- "
            "`cv2.convexityDefects` requires the hull indices in sorted "
            "order, a common gotcha); `defects = "
            "cv2.convexityDefects(contour, hull_indices)`; if `defects` "
            "is `None`, return `0`; otherwise count how many defects "
            "have a depth greater than `MIN_DEFECT_DEPTH` (already given "
            "as `8.0`) -- `defect[0][3] / 256.0` is that defect's depth "
            "in pixels (OpenCV packs it as a fixed-point integer, hence "
            "the `/ 256.0`). Each valley **between** two adjacent raised "
            "fingers shows up as one deep convexity defect.\n"
            "- `classify_hand_posture(binary_mask) -> str` -- "
            "`count_extended_fingers(binary_mask)`, then `\"fist\"` if "
            "`0`, `\"open_hand\"` if `>= 4`, else `\"partial\"`.\n\n"
            "See the Study Reference presentation, Topic 11 (Advanced "
            "tier), for the theory."
        ),
        "stub": '''\
import cv2
import numpy as np

MIN_DEFECT_DEPTH = 8.0


def preprocess_hand_mask(mask):
    """GaussianBlur(mask, (5, 5), 0), then an explicit binary threshold pass."""
    raise NotImplementedError


def find_hand_contour(binary_mask):
    """The largest contour from cv2.findContours(binary_mask, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE)."""
    raise NotImplementedError


def count_extended_fingers(binary_mask) -> int:
    """Convex hull + convexity defects on find_hand_contour(...); count defects deeper than MIN_DEFECT_DEPTH."""
    raise NotImplementedError


def classify_hand_posture(binary_mask) -> str:
    """"fist" if count_extended_fingers == 0, "open_hand" if >= 4, else "partial"."""
    raise NotImplementedError
''',
        "reference": '''\
import cv2
import numpy as np

MIN_DEFECT_DEPTH = 8.0


def preprocess_hand_mask(mask):
    blurred = cv2.GaussianBlur(mask, (5, 5), 0)
    return cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)[1]


def find_hand_contour(binary_mask):
    contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return max(contours, key=cv2.contourArea)


def count_extended_fingers(binary_mask) -> int:
    contour = find_hand_contour(binary_mask)
    hull_indices = cv2.convexHull(contour, returnPoints=False)
    hull_indices = np.sort(hull_indices, axis=0)
    defects = cv2.convexityDefects(contour, hull_indices)
    if defects is None:
        return 0
    return sum(1 for d in defects if d[0][3] / 256.0 > MIN_DEFECT_DEPTH)


def classify_hand_posture(binary_mask) -> str:
    count = count_extended_fingers(binary_mask)
    if count == 0:
        return "fist"
    if count >= 4:
        return "open_hand"
    return "partial"
''',
        "test": '''\
import math
import cv2
import numpy as np
from exercises.stage11.tier3_advanced01.solution import (
    preprocess_hand_mask,
    find_hand_contour,
    count_extended_fingers,
    classify_hand_posture,
)


def _fist_mask():
    mask = np.zeros((300, 300), dtype=np.uint8)
    cv2.circle(mask, (150, 150), 80, 255, -1)
    return mask


def _star_mask(num_points, canvas=300, cx=150, cy=150, outer_r=110, inner_r=35):
    """A num_points-pointed star: a hand silhouette stand-in with exactly
    num_points "fingertips" and num_points valleys between them, built from
    plain trigonometry so the expected convexity-defect count is exact."""
    pts = []
    n = num_points * 2
    for i in range(n):
        angle = math.pi / 2 + i * (2 * math.pi / n)
        r = outer_r if i % 2 == 0 else inner_r
        x = int(cx + r * math.cos(angle))
        y = int(cy - r * math.sin(angle))
        pts.append([x, y])
    mask = np.zeros((canvas, canvas), dtype=np.uint8)
    cv2.fillPoly(mask, [np.array(pts, dtype=np.int32)], 255)
    return mask


def test_preprocess_hand_mask_stays_binary_and_same_shape():
    """preprocess_hand_mask must blur then re-threshold, staying binary and same shape."""
    mask = _fist_mask()
    processed = preprocess_hand_mask(mask)
    assert processed.shape == mask.shape
    assert set(np.unique(processed)).issubset({0, 255})


def test_find_hand_contour_returns_the_largest_contour():
    """find_hand_contour must pick the largest contour by area."""
    mask = preprocess_hand_mask(_fist_mask())
    contour = find_hand_contour(mask)
    assert cv2.contourArea(contour) > 15000


def test_count_extended_fingers_on_a_fist():
    """A closed fist (a plain circle, no fingertip points) must report 0 extended fingers."""
    mask = preprocess_hand_mask(_fist_mask())
    assert count_extended_fingers(mask) == 0


def test_count_extended_fingers_on_a_three_point_star():
    """A 3-pointed star has exactly 3 deep valleys between its "fingertips"."""
    mask = preprocess_hand_mask(_star_mask(3))
    assert count_extended_fingers(mask) == 3


def test_count_extended_fingers_on_a_five_point_star():
    """A 5-pointed star (an "open hand" stand-in) has exactly 5 deep valleys."""
    mask = preprocess_hand_mask(_star_mask(5))
    assert count_extended_fingers(mask) == 5


def test_classify_hand_posture_buckets():
    """classify_hand_posture: 0 -> "fist", 1-3 -> "partial", 4+ -> "open_hand"."""
    assert classify_hand_posture(preprocess_hand_mask(_fist_mask())) == "fist"
    assert classify_hand_posture(preprocess_hand_mask(_star_mask(3))) == "partial"
    assert classify_hand_posture(preprocess_hand_mask(_star_mask(5))) == "open_hand"
''',
    },
    {
        "name": "tier3_advanced02",
        "title": "Face Gesture and Gaze Direction (Driver-Camera Style)",
        "summary": "cv2.CascadeClassifier",
        "readme": (
            "The face side of the pipeline, built entirely on Haar "
            "cascade files **already inside your `opencv-python` "
            "install** (`cv2.data.haarcascades`) -- genuinely trained "
            "files that run fully offline, no download or internet "
            "connection needed. This is the same coarse idea a "
            "driver-monitoring camera module uses: is a face visible, is "
            "it smiling, and roughly which way are the eyes pointing "
            "within it.\n\n"
            "Implement:\n\n"
            "- `load_face_cascade()` -- "
            "`cv2.CascadeClassifier(cv2.data.haarcascades + "
            "\"haarcascade_frontalface_default.xml\")`.\n"
            "- `load_eye_cascade()` -- "
            "`cv2.CascadeClassifier(cv2.data.haarcascades + "
            "\"haarcascade_eye.xml\")`.\n"
            "- `load_smile_cascade()` -- "
            "`cv2.CascadeClassifier(cv2.data.haarcascades + "
            "\"haarcascade_smile.xml\")` -- a **facial gesture** "
            "detector: a smile is a gesture your face makes, and this "
            "cascade was trained specifically to recognize it.\n"
            "- `is_cascade_loaded(cascade) -> bool` -- `not "
            "cascade.empty()` -- `.empty()` is `True` when the "
            "classifier failed to load (e.g. a bad path), so this is how "
            "you check a load actually worked before trying to use it.\n"
            "- `detect_smile(face_gray_region, smile_cascade) -> bool` "
            "-- `detections = "
            "smile_cascade.detectMultiScale(face_gray_region, "
            "scaleFactor=1.7, minNeighbors=20)`, then `return "
            "len(detections) > 0`. (`scaleFactor`/`minNeighbors` are "
            "tuned higher than a typical face cascade's defaults -- "
            "smiles have far more visual variation than faces do, so a "
            "smile cascade needs more neighbor agreement before it "
            "commits to a detection.)\n"
            "- `estimate_gaze_direction(face_box: tuple, eye_boxes: "
            "list, off_axis_ratio: float = 0.15) -> str` -- given an "
            "already-detected `face_box = (fx, fy, fw, fh)` and "
            "`eye_boxes = [(ex, ey, ew, eh), ...]` (exactly what "
            "`cascade.detectMultiScale(...)` returns), estimate which "
            "way the eyes are pointing **within the face box**: if "
            "`eye_boxes` is empty, return `\"looking_away\"` (no eyes "
            "detected -- occluded, closed, or turned too far to see). "
            "Otherwise compute `eye_centroid_x` -- the average of each "
            "eye box's own center x (`ex + ew / 2`) -- and "
            "`face_center_x = fx + fw / 2`; if `eye_centroid_x` is more "
            "than `fw * off_axis_ratio` to the left of `face_center_x`, "
            "return `\"left\"`; more than that to the right, "
            "`\"right\"`; otherwise `\"center\"`.\n\n"
            "This is a **coarse proxy**, not true 3D gaze estimation "
            "(which needs a trained regression model, well beyond a "
            "Haar cascade) -- but it's exactly the kind of "
            "lightweight, fully-local heuristic a simple attention-"
            "monitoring feature can be built from.\n\n"
            "See the Study Reference presentation, Topic 11 (Advanced "
            "tier), for the theory."
        ),
        "stub": '''\
import cv2


def load_face_cascade():
    """cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")."""
    raise NotImplementedError


def load_eye_cascade():
    """cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")."""
    raise NotImplementedError


def load_smile_cascade():
    """cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")."""
    raise NotImplementedError


def is_cascade_loaded(cascade) -> bool:
    """not cascade.empty()."""
    raise NotImplementedError


def detect_smile(face_gray_region, smile_cascade) -> bool:
    """True if smile_cascade.detectMultiScale(face_gray_region, scaleFactor=1.7, minNeighbors=20) finds anything."""
    raise NotImplementedError


def estimate_gaze_direction(face_box: tuple, eye_boxes: list, off_axis_ratio: float = 0.15) -> str:
    """"looking_away" if no eyes; else "left"/"right"/"center" from the eye centroid vs. face center."""
    raise NotImplementedError
''',
        "reference": '''\
import cv2


def load_face_cascade():
    return cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


def load_eye_cascade():
    return cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")


def load_smile_cascade():
    return cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")


def is_cascade_loaded(cascade) -> bool:
    return not cascade.empty()


def detect_smile(face_gray_region, smile_cascade) -> bool:
    detections = smile_cascade.detectMultiScale(face_gray_region, scaleFactor=1.7, minNeighbors=20)
    return len(detections) > 0


def estimate_gaze_direction(face_box: tuple, eye_boxes: list, off_axis_ratio: float = 0.15) -> str:
    if not eye_boxes:
        return "looking_away"
    fx, fy, fw, fh = face_box
    face_center_x = fx + fw / 2
    eye_centroid_x = sum(ex + ew / 2 for ex, ey, ew, eh in eye_boxes) / len(eye_boxes)
    offset = eye_centroid_x - face_center_x
    threshold = fw * off_axis_ratio
    if offset < -threshold:
        return "left"
    if offset > threshold:
        return "right"
    return "center"
''',
        "test": '''\
from unittest.mock import Mock
import cv2
import numpy as np
from exercises.stage11.tier3_advanced02.solution import (
    load_face_cascade,
    load_eye_cascade,
    load_smile_cascade,
    is_cascade_loaded,
    detect_smile,
    estimate_gaze_direction,
)


def test_load_face_cascade_loads_successfully():
    """load_face_cascade must load one of OpenCV's own bundled, already-trained cascades."""
    assert is_cascade_loaded(load_face_cascade()) is True


def test_load_eye_cascade_loads_successfully():
    """load_eye_cascade must load successfully too."""
    assert is_cascade_loaded(load_eye_cascade()) is True


def test_load_smile_cascade_loads_successfully():
    """load_smile_cascade must load successfully -- a facial GESTURE detector, not just a face detector."""
    assert is_cascade_loaded(load_smile_cascade()) is True


def test_is_cascade_loaded_false_for_a_bad_path():
    """is_cascade_loaded must be False when the classifier failed to load."""
    bad_cascade = cv2.CascadeClassifier("/nonexistent/cascade.xml")
    assert is_cascade_loaded(bad_cascade) is False


def test_detect_smile_uses_the_tuned_scale_and_neighbors():
    """detect_smile must call detectMultiScale with scaleFactor=1.7, minNeighbors=20, and interpret len()>0 as a smile."""
    region = np.zeros((50, 50), dtype=np.uint8)

    smiling_cascade = Mock()
    smiling_cascade.detectMultiScale.return_value = [(10, 10, 20, 20)]
    assert detect_smile(region, smiling_cascade) is True
    smiling_cascade.detectMultiScale.assert_called_once_with(region, scaleFactor=1.7, minNeighbors=20)

    neutral_cascade = Mock()
    neutral_cascade.detectMultiScale.return_value = []
    assert detect_smile(region, neutral_cascade) is False


def test_estimate_gaze_direction_center():
    """Eyes centered within the face box must estimate "center"."""
    face = (100, 80, 200, 200)
    eyes = [(150, 120, 30, 20), (230, 120, 30, 20)]
    assert estimate_gaze_direction(face, eyes) == "center"


def test_estimate_gaze_direction_left_and_right():
    """Eyes shifted well to one side of the face center must estimate that side."""
    face = (100, 80, 200, 200)
    left_eyes = [(110, 120, 30, 20), (150, 120, 30, 20)]
    right_eyes = [(250, 120, 30, 20), (290, 120, 30, 20)]
    assert estimate_gaze_direction(face, left_eyes) == "left"
    assert estimate_gaze_direction(face, right_eyes) == "right"


def test_estimate_gaze_direction_no_eyes_is_looking_away():
    """No detected eyes at all must estimate "looking_away", not crash or default to "center"."""
    face = (100, 80, 200, 200)
    assert estimate_gaze_direction(face, []) == "looking_away"
''',
    },
]
