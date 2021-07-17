"""
Canny algorithm is composed of 5 steps:
1. Noise Reduction
2. Gradient Calculation
3. Non-maximum Suppression
4. Double Threshold
5. Edge Tracking by Hysteresis
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

lena = cv2.imread("lena.jpg", 0)
canny_lena = cv2.Canny(lena, 100, 200)

messy = cv2.imread("messi5.jpg", 0)
canny_messy = cv2.Canny(messy, 100, 200)

titles = ["Lena", "Canny", "Messy", "Canny"]
images = [lena, canny_lena, messy, canny_messy]

for i, item in enumerate(images):
    # images[i] = cv2.resize(images[i], (500, 500))
    images[i] = cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB)
    plt.subplot(2, 2, i + 1), plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
