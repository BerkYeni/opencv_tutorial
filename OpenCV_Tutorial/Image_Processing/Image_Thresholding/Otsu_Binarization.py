import random
import cv2 as cv
import numpy as np

# create noisy image
img = np.zeros((500, 500, 1), np.uint8)
img[100:400, 100:400] = 255
for i in range(500):
    for k in range(500):
        img[i, k] = (random.random() * 255 + img[i, k]) / 2

# img = cv.imread("noisy2.png", cv.IMREAD_GRAYSCALE)
# assert img is not None, "file could not be read, check with os.path.exists()"

# global thresholding
ret1, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

# Otsu's thresholding
ret2, th2 = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

# Otsu's thresholding after Gaussian filtering
blur = cv.GaussianBlur(img, (5, 5), 0)
ret3, th3 = cv.threshold(blur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

# plot all the images and their histograms
images = [img, 0, th1, img, 0, th2, blur, 0, th3]
titles = [
    "Original Noisy Image",
    "Histogram",
    "Global Thresholding (v=127)",
    "Original Noisy Image",
    "Histogram",
    "Otsu's Thresholding",
    "Gaussian filtered Image",
    "Histogram",
    "Otsu's Thresholding",
]

for title, image in zip(titles, images):
    cv.imshow(title, image)
cv.waitKey(0)

#     plt.subplot(3, 3, i * 3 + 1), plt.imshow(images[i * 3], "gray")
#     plt.title(titles[i * 3]), plt.xticks([]), plt.yticks([])
#     plt.subplot(3, 3, i * 3 + 2), plt.hist(images[i * 3].ravel(), 256)
#     plt.title(titles[i * 3 + 1]), plt.xticks([]), plt.yticks([])
#     plt.subplot(3, 3, i * 3 + 3), plt.imshow(images[i * 3 + 2], "gray")
#     plt.title(titles[i * 3 + 2]), plt.xticks([]), plt.yticks([])
# plt.show()
