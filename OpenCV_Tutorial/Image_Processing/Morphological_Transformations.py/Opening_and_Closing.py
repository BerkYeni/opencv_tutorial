# opening is erosion followed by dilation

import cv2 as cv
import numpy as np
from Utils import add_padding, add_noise

kernel = np.ones((5, 5), np.uint8)

img = cv.imread("OpenCV_Tutorial/Resources/j.png")
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

img_to_open = np.copy(img)
add_noise(img_to_open, True)

opened = cv.morphologyEx(img_to_open, cv.MORPH_OPEN, kernel)


# closing is the opposite of opening (dilation to erosion)
img_to_close = np.copy(img)
add_noise(img_to_close, False)

closed = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)

cv.imshow("Original", add_padding(img_to_open))
cv.imshow("Opened", add_padding(opened))
cv.waitKey(0)
cv.destroyAllWindows()

cv.imshow("Original", add_padding(img_to_close))
cv.imshow("Closed", add_padding(closed))
cv.waitKey(0)
