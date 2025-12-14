# removes high frequency

# opencv has four blurs


def add_salt_pepper_noise(image, salt_prob=0.01, pepper_prob=0.01):
    noisy = image.copy()
    rnd = np.random.rand(*image.shape[:2])
    noisy[rnd < salt_prob] = 255
    noisy[(rnd >= salt_prob) & (rnd < salt_prob + pepper_prob)] = 0
    return noisy


import cv2 as cv
import numpy as np

sudoku = cv.imread("OpenCV_Tutorial/Resources/sudoku.jpg")
noisy_logo = cv.imread("OpenCV_Tutorial/Resources/noisy_opencv_logo.png")
bilateral_img = cv.imread("OpenCV_Tutorial/Resources/bilateral_example.png")

# Averaging
averaging = cv.blur(noisy_logo, (5, 5))

cv.imshow("Original", noisy_logo)
cv.imshow("Averaging", averaging)
cv.waitKey(0)
cv.destroyAllWindows()

# Gaussian
gaussian = cv.GaussianBlur(noisy_logo, (5, 5), 0)

cv.imshow("Original", noisy_logo)
cv.imshow("Gaussian", gaussian)
cv.waitKey(0)
cv.destroyAllWindows()

# Median
noisy = add_salt_pepper_noise(sudoku, 0.15, 0.15)
median = cv.medianBlur(noisy, 5)
cv.imshow("Noisy", noisy)
cv.imshow("Median", median)
cv.waitKey(0)
cv.destroyAllWindows()


# Bilateral
bilateral = cv.bilateralFilter(bilateral_img, 9, 75, 75)
cv.imshow("Original", bilateral_img)
cv.imshow("Bilateral", bilateral)
cv.waitKey(0)

# for blur in [averaging, gaussian]:
