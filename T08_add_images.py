import cv2

i1 = cv2.imread('messi5.jpg', 1)
i2 = cv2.imread('opencv-logo.png', 1)

i1 = cv2.resize(i1, (512, 512))
i2 = cv2.resize(i2, (512, 512))

# dst = cv2.add(i1, i2)
dst = cv2.addWeighted(i1, 1, i2, 0.2, 0)

cv2.imshow('final', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
