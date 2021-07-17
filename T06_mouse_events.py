import cv2
import numpy as np

# All Events in cv2
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)


def click_event(event, x, y, flags, param):
    global img
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = ""
    if event == cv2.EVENT_LBUTTONDOWN:
        img = DEFAULT.copy()
        text = f"{x}, {y}"
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1, cv2.LINE_AA)
        points.append((x, y))
        if len(points) >= 2 and len(points) != 0:
            for i in range(int(len(points) / 2)):
                cv2.arrowedLine(img,
                                (points[2 * i][0], points[2 * i][1]),
                                (points[2 * i + 1][0], points[2 * i + 1][1]),
                                (0, 255, 255), 2, cv2.LINE_AA)
    if event == cv2.EVENT_RBUTTONDOWN:
        img = DEFAULT.copy()
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        text = f"{blue}, {green}, {red}"
        color_img = np.zeros((512, 512, 3), np.uint8)
        color_img[:] = [blue, green, red]
        cv2.imshow('color', color_img)
    cv2.putText(img, text, (x, y - 10), font, 0.5, (255, 255, 0), 2)
    cv2.imshow('title', img)


# img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('lena.jpg', 1)
DEFAULT = img.copy()
cv2.imshow('title', img)
points = []

cv2.setMouseCallback('title', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
