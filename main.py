import cv2
import numpy as np
from ROI import get_ROI


img = 'test_image.jpg'
img_color = cv2.imread(img)
img_gray = cv2.imread(img, 0)

coordinates, roi = get_ROI(img_gray)

for coordinate in coordinates:
    cv2.rectangle(img_color, (coordinate[0], coordinate[2]), (coordinate[1], coordinate[3]), (0, 0, 0), 1)

cv2.imshow('result', img_color)
cv2.waitKey(0)
cv2.destroyAllWindows()
