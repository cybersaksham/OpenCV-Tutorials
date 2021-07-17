import cv2
import numpy as np
from matplotlib import pyplot as plt

# black = np.zeros((200, 200), np.uint8)
# cv2.rectangle(black, (0, 100), (200, 200), (255, 255, 255), -1)
# cv2.rectangle(black, (0, 50), (100, 100), 127, -1)

lena = cv2.imread("lena.jpg", 0)
# b, g, r = cv2.split(lena)

# cv2.imshow("Black", black)
cv2.imshow("Lena", lena)
hist = cv2.calcHist([lena], [0], None, [256], [0, 256])

# plt.hist(black.ravel(), 256, [0, 256])
# lena = cv2.cvtColor(lena, cv2.COLOR_BGR2RGB)
# plt.hist(lena.ravel(), 256, [0, 256])
# plt.hist(b.ravel(), 256, [0, 256])
# plt.hist(g.ravel(), 256, [0, 256])
# plt.hist(r.ravel(), 256, [0, 256])
plt.plot(hist)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
