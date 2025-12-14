import numpy as np
import cv2 as cv

img = cv.imread("OpenCV_Tutorial/Resources/sudoku.jpg")
kernel = np.ones((5, 5), np.float32) / 25
dst = cv.filter2D(img, -1, kernel)

cv.imshow("Original", img)
cv.imshow("Filtered", dst)
cv.waitKey(0)
