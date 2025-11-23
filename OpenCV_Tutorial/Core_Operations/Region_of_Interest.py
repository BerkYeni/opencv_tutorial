import numpy as np
import cv2 as cv

img = cv.imread("OpenCV_Tutorial/Resources/starry_night.jpg")

moon = img[29:118, 398:495]
img[43:132, 151:248] = moon

cv.imshow("Image", img)
cv.waitKey(0)
