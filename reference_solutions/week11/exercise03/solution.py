import cv2


def draw_rectangle(image, pt1: tuple, pt2: tuple, color: tuple):
    result = image.copy()
    cv2.rectangle(result, pt1, pt2, color, thickness=2)
    return result


def draw_filled_rectangle(image, pt1: tuple, pt2: tuple, color: tuple):
    result = image.copy()
    cv2.rectangle(result, pt1, pt2, color, thickness=-1)
    return result


def draw_bounding_boxes(image, boxes: list, color: tuple):
    result = image.copy()
    for x1, y1, x2, y2 in boxes:
        cv2.rectangle(result, (x1, y1), (x2, y2), color, 2)
    return result
