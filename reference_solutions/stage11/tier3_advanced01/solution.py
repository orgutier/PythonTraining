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
