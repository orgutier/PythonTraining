import cv2


def apply_threshold(gray_image, thresh_value: int):
    return cv2.threshold(gray_image, thresh_value, 255, cv2.THRESH_BINARY)[1]


def apply_otsu_threshold(gray_image):
    return cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


def apply_adaptive_threshold(gray_image):
    return cv2.adaptiveThreshold(
        gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2
    )
