import cv2 as cv
import numpy as np

# give bgr green to cvt color ask for hsv value
bgr_green = np.uint8([[[0, 255, 0]]])
hsv_green = cv.cvtColor(bgr_green, cv.COLOR_BGR2HSV)
print(hsv_green)
