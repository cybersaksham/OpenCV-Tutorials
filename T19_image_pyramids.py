import cv2
import numpy as np
from matplotlib import pyplot as plt

lena = cv2.imread("lena.jpg")
# lr1 = cv2.pyrDown(lena)
# lr2 = cv2.pyrDown(lr1)
# hr1 = cv2.pyrUp(lr2)
# hr2 = cv2.pyrUp(hr1)

layer = lena.copy()
gp = []

for i in range(5):
    layer = cv2.pyrDown(layer)
    gp.append(layer)

layer = gp[4]
cv2.imshow("Upper Level Gaussian Pyramid", layer)

lp = []

for i in range(4, 0, -1):
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i - 1], gaussian_extended)
    cv2.imshow(f"LP {i}", laplacian)

cv2.imshow("Lena", lena)
# cv2.imshow("lr1", lr1)
# cv2.imshow("lr2", lr2)
# cv2.imshow("hr1", hr1)
# cv2.imshow("hr2", hr2)

# for i, item in enumerate(gp):
#     cv2.imshow(f"Gp {i}", item)

cv2.waitKey(0)
cv2.destroyAllWindows()
