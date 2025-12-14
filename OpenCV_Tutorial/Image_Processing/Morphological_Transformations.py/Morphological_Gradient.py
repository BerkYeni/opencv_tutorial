# morphological gradient is the difference between dilation and erosion

import cv2 as cv
import numpy as np
from Utils import add_padding

kernel = np.ones((5, 5), np.uint8)

img = cv.imread("OpenCV_Tutorial/Resources/j.png")
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)

cv.imshow("Original", add_padding(img))
cv.imshow("Gradient", add_padding(gradient))
cv.waitKey(0)
