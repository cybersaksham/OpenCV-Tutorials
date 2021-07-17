import cv2
import numpy as np

messi = cv2.imread("messi5.jpg")
gray_messi = cv2.cvtColor(messi, cv2.COLOR_BGR2GRAY)
face = cv2.imread("messi_face.png", 0)
w, h = face.shape[::-1]

res = cv2.matchTemplate(gray_messi, face, cv2.TM_CCOEFF_NORMED)
threshold = 0.57
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(messi, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

cv2.imshow("Messi", messi)
# cv2.imshow("Messi Face", face)
# cv2.imshow("Result", res)

cv2.waitKey(0)
cv2.destroyAllWindows()
