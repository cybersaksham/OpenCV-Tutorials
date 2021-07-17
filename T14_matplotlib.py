import cv2
from matplotlib import pyplot as plt

# Images
img1 = cv2.imread("lena.jpg")
img2 = cv2.imread("gradient.png")
img3 = cv2.imread("messi5.jpg")
img4 = cv2.imread("opencv-logo.png")
img5 = cv2.imread("smarties.png")
images = [img1, img2, img3, img4, img5]
titles = ["lena", "gradient", "messi", "opencv", "smarties"]

for i in range(len(images)):
    images[i] = cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB)  # Converting BGR to RGB format for matplotlib
    images[i] = cv2.resize(images[i], (500, 500))
    plt.subplot(2, 3, i + 1), plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])  # Removing ticks

plt.show()
