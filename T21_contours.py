import cv2
import numpy as np

img = cv2.imread("opencv-logo.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgGray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print(len(contours))

cv2.drawContours(img, contours, -1, (0, 255, 255), 3)

cv2.imshow("Image", img)
cv2.imshow("Gray-Image", imgGray)

cv2.waitKey(0)
cv2.destroyAllWindows()
