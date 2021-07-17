import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("sudoku.png", 0)

lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))

sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelX = np.uint8(np.absolute(sobelX))

sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)

titles = ["Image", "Laplacian", "Sobel X", "Sobel Y", "Sobel Combined"]
images = [img, lap, sobelX, sobelY, sobelCombined]

for i, item in enumerate(images):
    # images[i] = cv2.resize(images[i], (500, 500))
    images[i] = cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB)
    plt.subplot(2, 3, i + 1), plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
