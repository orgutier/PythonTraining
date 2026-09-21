import cv2
import numpy as np


def detect_edges(gray_image, low: int, high: int):
    return cv2.Canny(gray_image, low, high)


def detect_edges_default(gray_image):
    return cv2.Canny(gray_image, 100, 200)


def count_edge_pixels(gray_image, low: int, high: int) -> int:
    return int(np.count_nonzero(cv2.Canny(gray_image, low, high)))


def find_contours(binary_image) -> list:
    return cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]


def count_contours(binary_image) -> int:
    return len(find_contours(binary_image))


def largest_contour_area(binary_image) -> float:
    return max(cv2.contourArea(c) for c in find_contours(binary_image))
