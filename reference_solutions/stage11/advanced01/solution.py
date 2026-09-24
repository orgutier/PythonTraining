import cv2


def apply_gaussian_blur(image, ksize: int):
    return cv2.GaussianBlur(image, (ksize, ksize), 0)


def apply_strong_blur(image):
    return cv2.GaussianBlur(image, (15, 15), 0)


def find_contours(binary_image) -> list:
    return cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]


def count_contours(binary_image) -> int:
    return len(find_contours(binary_image))


def largest_contour_area(binary_image) -> float:
    return max(cv2.contourArea(c) for c in find_contours(binary_image))
