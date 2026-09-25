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
