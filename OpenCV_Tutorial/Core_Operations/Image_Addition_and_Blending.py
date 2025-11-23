import cv2 as cv
import numpy as np

img1 = cv.imread("starry_night.jpg")

# Addition
x = np.uint8([250])
y = np.uint8([10])

# OpenCV addition is saturated
opencv_addition = cv.add(x, y)
print(opencv_addition)

# Numpy addition is a modulo
numpy_addition = x + y  # 260 -> 4
print(numpy_addition)

# Use OpenCV addition for better results


# Blending
# blending is also addition but with weights
# w between 0 and 1,
# result = img1*(1 - w) + img2*w

img = cv.imread("starry_night.jpg")

img1 = img[50:300, 0:240]
img2 = img[50:300, 240:480]

result = cv.addWeighted(img1, 0.3, img2, 0.7, 0)
cv.imshow("Image", result)
cv.waitKey(0)

for i in range(10):
    x = i / 10
    result = cv.addWeighted(img1, x, img2, 1 - x, 0)
    cv.imshow("Image", result)
    cv.waitKey(0)


cv.destroyAllWindows()
