import cv2
import numpy as np

img = cv2.imread("shapes.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(imgGray, 220, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    x, y, w, h = cv2.boundingRect(approx)
    if x < 5 and y < 5:
        continue
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 3)
    text = "Circle"
    if len(approx) == 3:
        text = "Triangle"
    elif len(approx) == 4:
        text = "Rectangle"
        aspectRatio = float(w) / h
        if 0.95 < aspectRatio < 1.05:
            text = "Square"
    elif len(approx) == 5:
        text = "Pentagon"
    elif len(approx) == 6:
        text = "Hexagon"
    elif len(approx) == 10:
        text = "Star"
    cv2.putText(img, text, (int(x + w / 3), int(y + h / 2)), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

cv2.imshow("Shapes", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
