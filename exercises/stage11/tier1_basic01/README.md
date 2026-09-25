# Loading and Inspecting Camera Frames

A camera-fed gesture-recognition pipeline starts with plain frame I/O -- and an OpenCV frame *is* a NumPy array, so `.shape` is a plain array attribute, not something OpenCV adds. Implement:

- `load_frame(path: str)` -- `cv2.imread(path)` (returns a NumPy array in BGR order, or `None` if the file can't be read).
- `save_frame(path: str, frame) -> bool` -- `cv2.imwrite(path, frame)`.
- `get_frame_dimensions(frame) -> tuple` -- `frame.shape[:2]`, i.e. `(height, width)` -- note **height first**, which trips up everyone coming from `(width, height)` conventions elsewhere.
- `create_blank_frame(height: int, width: int)` -- `np.zeros((height, width, 3), dtype=np.uint8)` -- a blank BGR frame, the same shape a real camera would hand you.
- `crop_to_roi(frame, y1: int, y2: int, x1: int, x2: int)` -- `frame[y1:y2, x1:x2]` -- ordinary NumPy array slicing, rows (`y`) before columns (`x`). This is how you crop to a **region of interest** (e.g. a detected face or hand box) in OpenCV -- there's no separate "crop function", because the frame is just an array.

See the Study Reference presentation, Topic 11 (Basic tier), for the theory.
