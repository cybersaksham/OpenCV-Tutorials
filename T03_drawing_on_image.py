import cv2
import numpy as np

# img = cv2.imread("lena.jpg", 1)
img = np.zeros([600, 512, 3], np.uint8)

# Drawing
img = cv2.line(img, (100, 100), (200, 200), (0, 255, 0), 5)
img = cv2.arrowedLine(img, (150, 100), (250, 200), (0, 0, 255), 5)
img = cv2.rectangle(img, (200, 50), (300, 250), (255, 0, 0), 3)
img = cv2.rectangle(img, (350, 50), (450, 250), (255, 255, 0), -1)  # Fill with color
img = cv2.circle(img, (400, 350), 50, (0, 255, 255), -1)
img = cv2.putText(img, "Sample Text", (100, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 255), 2)

cv2.imshow("Window Title", img)

k = cv2.waitKey(0)

if k == 27:  # ESC key
    cv2.destroyAllWindows()
