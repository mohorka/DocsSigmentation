import cv2
import numpy as np
from rlsa import rlsa


def get_ROI(image: np.ndarray):
    threshold, bin_img = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    horizontal_smoothed = rlsa(bin_img, True, False, 16)
    vertical_smoothed = rlsa(bin_img, False, True, 8)
    smoothed_img = horizontal_smoothed & vertical_smoothed

    cv2.waitKey(0)

    threshold_inv, inv_smoothed_img = cv2.threshold(smoothed_img, 0, 255, cv2.THRESH_BINARY_INV)
    dilation_kernel = np.ones((5, 4), dtype=int)
    dilated_img = cv2.dilate(inv_smoothed_img, dilation_kernel, iterations=2)

    ret, labels = cv2.connectedComponents(dilated_img)

    roi = []
    roi_coordinates = []
    for label in range(1, ret):
        area = np.where(labels == label)
        roi_coordinates.append([np.amin(area[1]), np.amax(area[1]), np.amin(area[0]), np.amax(area[0])])
        roi.append(image[np.amin(area[0]): np.amax(area[0]), np.amin(area[1]):np.amax(area[1])])

    return roi_coordinates, roi
