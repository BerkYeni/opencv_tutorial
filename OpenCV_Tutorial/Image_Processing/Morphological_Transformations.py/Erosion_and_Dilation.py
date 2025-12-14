# basic idea of erosion is just like soil erosion, it erodes away the boundaries
# try to keep foreground in white
# kernel slides, pixel is white only if
# all the pixels inside the kernel are white

import cv2 as cv
import numpy as np
from Utils import add_padding

kernel = np.ones((5, 5), np.uint8)

img = cv.imread("OpenCV_Tutorial/Resources/j.png")
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

eroded = cv.erode(img, kernel, iterations=1)

cv.imshow("Original", add_padding(img))
cv.imshow("Erosion", add_padding(eroded))


# dilation is the opposite of erosion
dilated = cv.dilate(img, kernel, iterations=1)

cv.imshow("Dilated", add_padding(dilated))
cv.waitKey(0)
