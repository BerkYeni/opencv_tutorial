import numpy as np
import cv2 as cv

img = cv.imread("starry_night.jpg")

b, g, r = cv.split(img)  # this is costly, use the method below (numpy indexing)
# or
b = img[:, :, 0]
g = img[:, :, 1]
r = img[:, :, 2]

cv.imshow("Image", b)
cv.waitKey(0)
cv.imshow("Image", g)
cv.waitKey(0)
cv.imshow("Image", r)
cv.waitKey(0)

print(b)

img = cv.merge((b, g, r))
cv.imshow("Image", img)
cv.waitKey(0)

img[:, :, 0] = 0  # set all blue values to 0
cv.imshow("Image", img)
cv.waitKey(0)
