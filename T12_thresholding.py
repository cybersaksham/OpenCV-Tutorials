import cv2
import numpy as np

img = cv2.imread("gradient.png", 0)
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)  # If less than 127 then 0 otherwise 255
_, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)  # If less than 127 then 255 otherwise 0
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)  # If less than 127 then unchanged otherwise 127
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)  # If less than 127 then 0 otherwise unchanged
_, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)  # If less than 127 then unchanged otherwise 0

cv2.imshow("Image", img)
cv2.imshow("TH1", th1)
cv2.imshow("TH2", th2)
cv2.imshow("TH3", th3)
cv2.imshow("TH4", th4)
cv2.imshow("TH5", th5)

cv2.waitKey(0)
cv2.destroyAllWindows()
