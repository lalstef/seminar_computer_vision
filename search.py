import cv2
import numpy as np


def histogram(image):
    hist = cv2.calcHist([image], [0, 1, 2], None, (4, 6, 3), [0, 180, 0, 256, 0, 256])
    hist = cv2.normalize(hist).flatten()
    return hist


def describe(image):
    image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    height, width = image.shape[:2]
    center_x, center_y = [int(0, height / 2), int(0, width / 2)]

    parts = [
        (0, center_x, 0, center_y),  # top-left
        (center_x, width, 0, center_y),  # top-right
        (center_x, width, center_y, height),  # bottom-right
        (0, center_x, center_y, height),  # bottom-left
        (int(width * 0.25), int(width * 0.75), int(height * 0.25), int(height * 0.75))  # center
    ]

    features = []
    for start_x, end_x, start_y, end_y in parts:
        features.extend(histogram(image[start_x:end_x, start_y:end_y]))
    return features


def chi2_distance(hist_a, hist_b, eps=1e-10):
    # compute the chi-squared distance
    distance = 0.5 * np.sum(((hist_a - hist_b) ** 2) / (hist_a + hist_b + eps))

    # return the chi-squared distance
    return distance
