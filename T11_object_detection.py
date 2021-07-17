import cv2
import numpy as np


def nothing(x):
    pass


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)

    cv2.namedWindow("Tracking")
    cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
    cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
    cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
    cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
    cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
    cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)

    while True:
        # frame = cv2.imread('smarties.png')
        _, frame = cap.read()

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        l_b = np.array([cv2.getTrackbarPos("LH", "Tracking"),
                        cv2.getTrackbarPos("LS", "Tracking"),
                        cv2.getTrackbarPos("LV", "Tracking")])
        u_b = np.array([cv2.getTrackbarPos("UH", "Tracking"),
                        cv2.getTrackbarPos("US", "Tracking"),
                        cv2.getTrackbarPos("UV", "Tracking")])

        mask = cv2.inRange(hsv, l_b, u_b)

        res = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow("frame", frame)
        cv2.imshow("mask", mask)
        cv2.imshow("res", res)

        k = cv2.waitKey(1)
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
