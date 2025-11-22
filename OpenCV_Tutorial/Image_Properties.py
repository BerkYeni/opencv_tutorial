import numpy as np
import cv2 as cv

img = cv.imread("starry_night.jpg")

# returns row, column and channel amount
print(img.shape)  # (396, 500, 3)

# total number of pixels
print(img.size)  # 594000

# datatype of the image
print(img.dtype)  # uint8

# quote:
# img.dtype is very important while debugging because a large number of errors in OpenCV-Python code are caused by invalid datatype.
