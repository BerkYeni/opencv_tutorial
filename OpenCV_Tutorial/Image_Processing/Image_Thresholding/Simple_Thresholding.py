import cv2 as cv
import numpy as np

# create gradient
gradient = np.tile(np.linspace(0, 255, 500, dtype=np.uint8), (500, 1))

# different kinds of thresholding
ret, thresh1 = cv.threshold(gradient, 127, 255, cv.THRESH_BINARY)
ret, thresh2 = cv.threshold(gradient, 127, 255, cv.THRESH_BINARY_INV)
ret, thresh3 = cv.threshold(gradient, 127, 255, cv.THRESH_TRUNC)
ret, thresh4 = cv.threshold(gradient, 127, 255, cv.THRESH_TOZERO)
ret, thresh5 = cv.threshold(gradient, 127, 255, cv.THRESH_TOZERO_INV)

titles = ["Original Image", "BINARY", "BINARY_INV", "TRUNC", "TOZERO", "TOZERO_INV"]
images = [gradient, thresh1, thresh2, thresh3, thresh4, thresh5]

for title, image in zip(titles, images):
    cv.imshow(title, image)

cv.waitKey(0)
