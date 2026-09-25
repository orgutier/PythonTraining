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
