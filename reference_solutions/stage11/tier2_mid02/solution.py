import cv2
import numpy as np


def detect_hand_edges(binary_mask, low: int, high: int):
    return cv2.Canny(binary_mask, low, high)


def detect_hand_edges_default(binary_mask):
    return cv2.Canny(binary_mask, 50, 150)


def count_edge_pixels(binary_mask, low: int, high: int) -> int:
    return int(np.count_nonzero(cv2.Canny(binary_mask, low, high)))
