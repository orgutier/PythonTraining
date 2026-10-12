import cv2


def to_grayscale(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


def resize_for_processing(frame, width: int, height: int):
    return cv2.resize(frame, (width, height))


def draw_detection_box(frame, box: tuple, color: tuple, thickness: int = 2):
    result = frame.copy()
    x, y, w, h = box
    cv2.rectangle(result, (x, y), (x + w, y + h), color, thickness)
    return result


def draw_multiple_boxes(frame, boxes: list, color: tuple):
    result = frame.copy()
    for x, y, w, h in boxes:
        cv2.rectangle(result, (x, y), (x + w, y + h), color, 2)
    return result
