# for creating custom shaped kernels

import cv2 as cv
import numpy as np

# rectangular kernel

for shape in [cv.MORPH_RECT, cv.MORPH_ELLIPSE, cv.MORPH_DIAMOND, cv.MORPH_CROSS]:
    rect_kernel = cv.getStructuringElement(shape, (5, 5))
    print(rect_kernel)
    print()
