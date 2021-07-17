import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("opencv-logo.png")
img2 = cv2.imread("Noise_salt_and_pepper.png")
img3 = cv2.imread("lena.jpg")

kernal = np.ones((5, 5), np.float32) / 25
dst = cv2.filter2D(img, -1, kernal)
blur = cv2.blur(img, (5, 5))
gauss_blur = cv2.GaussianBlur(img, (5, 5), 0)
median = cv2.medianBlur(img2, 5)  # Kernal size must be odd except 1
bilateral = cv2.bilateralFilter(img3, 9, 75, 75)  # To preserve edges

titles = ["Image", "2D Convolution", "Blurred", "Gaussian Blur",
          "Salt & Pepper", "Median Blur",
          "Lena", "Bi-Lateral"]
images = [img, dst, blur, gauss_blur, img2, median, img3, bilateral]

for i, item in enumerate(images):
    images[i] = cv2.resize(images[i], (500, 500))
    images[i] = cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB)
    row = 2
    column = 4
    plt.subplot(row, column, i + 1), plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
