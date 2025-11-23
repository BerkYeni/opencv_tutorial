import cv2 as cv
import numpy as np
from Utils.Utils import show


# highly useful while extracting any part of the image
# , defining and working with non-rectangular ROI's, and etc


# adding logo on top of image
img = cv.imread("starry_night.jpg")
logo = cv.imread("OpenCV_Logo_with_text.png")


show(logo)

# resize cuz too big
rows, cols, channels = logo.shape
print(rows, cols)
resized_rows, resized_cols = rows // 5, cols // 5
logo = cv.resize(logo, (resized_rows, resized_cols))
show(logo)

rows, cols, channels = logo.shape
logo_x = 15
logo_y = 15
# roi = img[15 : rows + 15, 15 : cols + 15]  # region of interest
roi = img[logo_x : rows + logo_x, logo_y : cols + logo_y]  # region of interest
show(roi)

# create mask of logo and inverse mask of logo also
img2gray = cv.cvtColor(logo, cv.COLOR_BGR2GRAY)
show(img2gray)

# mask of pixels with value greater than 200 (which is the white background)
_, mask = cv.threshold(img2gray, 200, 255, cv.THRESH_BINARY)
show(mask)

inverse_mask = cv.bitwise_not(mask)  # bit operation used here
show(inverse_mask)

# get background and foreground pixels with mask and combine them to get the desired roi
img1_bg = cv.bitwise_and(roi, roi, mask=mask)
show(img1_bg)

img2_fg = cv.bitwise_and(logo, logo, mask=inverse_mask)
show(img2_fg)

img_sum = cv.add(img1_bg, img2_fg)
show(img_sum)
img[logo_x : rows + logo_x, logo_y : cols + logo_y] = img_sum


show(img)
cv.destroyAllWindows()
