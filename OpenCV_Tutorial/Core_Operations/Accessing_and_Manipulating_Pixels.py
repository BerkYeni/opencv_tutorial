import numpy as np
import cv2 as cv

img = cv.imread("OpenCV_Tutorial/Resources/starry_night.jpg")
print(img)

pixel = img[100, 100]
print(pixel)

blue_value = img[100, 100, 0]
print(blue_value)

img[100, 100] = [255, 255, 255]
print(img[100, 100])
