import cv2
import numpy as np


def detect_edges(gray_image, low: int, high: int):
    return cv2.Canny(gray_image, low, high)


def detect_edges_default(gray_image):
    return cv2.Canny(gray_image, 100, 200)


def count_edge_pixels(gray_image, low: int, high: int) -> int:
    return int(np.count_nonzero(cv2.Canny(gray_image, low, high)))
