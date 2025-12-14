import cv2 as cv
import numpy as np
import random


def add_padding(img, padding=100):
    return cv.copyMakeBorder(img, *[padding] * 4, cv.BORDER_CONSTANT, value=0)


def add_noise(img, to_black):
    for i in range(img.shape[0]):
        for k in range(img.shape[1]):
            pixel = img[i, k]
            target_value = np.uint8(0) if to_black else np.uint8(255)
            if pixel == target_value:
                if random.random() > 0.5:
                    random_value = 255
                else:
                    random_value = 0
                img[i, k] = random_value
