import cv2
import numpy as np

i1 = np.zeros((250, 500, 3), np.uint8)
i1 = cv2.rectangle(i1, (200, 0), (300, 100), (255, 255, 255), -1)

i2 = np.zeros((250, 500, 3), np.uint8)
i2 = cv2.rectangle(i2, (250, 0), (500, 250), (255, 255, 255), -1)

# i1 = cv2.resize(cv2.imread('lena.jpg'), (512, 512))
# i2 = cv2.resize(cv2.imread('messi5.jpg'), (512, 512))

bitAND = cv2.bitwise_and(i1, i2)
bitOR = cv2.bitwise_or(i1, i2)
bitNOR1 = cv2.bitwise_not(i1)
bitNOR2 = cv2.bitwise_not(i2)
bitXOR = cv2.bitwise_xor(i1, i2)

cv2.imshow('image1', i1)
cv2.imshow('image2', i2)
cv2.imshow('bitAND', bitAND)
cv2.imshow('bitOR', bitOR)
cv2.imshow('bitNOR - i1', bitNOR1)
cv2.imshow('bitNOR - i2', bitNOR2)
cv2.imshow('bitXOR', bitXOR)

cv2.waitKey(0)
cv2.destroyAllWindows()
