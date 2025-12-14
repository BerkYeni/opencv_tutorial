# tophat is the difference between the original image and the opening of the image

import cv2 as cv
import numpy as np
from Utils import add_padding

kernel = np.ones((5, 5), np.uint8)

img = cv.imread("OpenCV_Tutorial/Resources/j.png")
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)

# blackhat is the difference between closing of the og image and the og image

blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)

cv.imshow("Original", add_padding(img))
cv.imshow("Tophat", add_padding(tophat))
cv.waitKey(0)
cv.destroyAllWindows()

cv.imshow("Original", add_padding(img))
cv.imshow("Blackhat", add_padding(blackhat))
cv.waitKey(0)
