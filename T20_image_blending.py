"""
STEPS FOR IMAGE BLENDING USING PYRAMIDS
    1. Load 2 images
    2. Find gaussian pyramids to suitable level i.e. 5 or 6
    3. From gaussian pyramids construct laplacian pyramids
    4. Join images in each level of laplacian pyramids
    5. From the joint image pyramids, construct original image
"""

import cv2
import numpy as np

# Step 1: Loading images
apple = cv2.imread("apple.jpg")
orange = cv2.imread("orange.jpg")
print(apple.shape, orange.shape)

apple_orange = np.hstack((apple[:, :256], orange[:, 256:]))

cv2.imshow("Apple", apple)
cv2.imshow("Orange", orange)
cv2.imshow("Apple-Orange", apple_orange)

# Blending images by pyramids
layers = 6

# Step 2: Generating gaussian pyramids
apple_copy = apple.copy()
gp_apple = [apple_copy]
for i in range(layers):
    apple_copy = cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

orange_copy = orange.copy()
gp_orange = [orange_copy]
for i in range(layers):
    orange_copy = cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)

# Step 3: Generating laplacian pyramids
apple_copy = gp_apple[layers - 1]
lp_apple = [apple_copy]
for i in range(layers - 1, 0, -1):
    gaussian_extended = cv2.pyrUp(gp_apple[i])
    laplacian = cv2.subtract(gp_apple[i - 1], gaussian_extended)
    lp_apple.append(laplacian)

orange_copy = gp_orange[layers - 1]
lp_orange = [orange_copy]
for i in range(layers - 1, 0, -1):
    gaussian_extended = cv2.pyrUp(gp_orange[i])
    laplacian = cv2.subtract(gp_orange[i - 1], gaussian_extended)
    lp_orange.append(laplacian)

# Step 4: Joining pyramids
apple_orange_pyramid = []
n = 0
for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    n += 1
    cols, rows, ch = apple_lap.shape
    laplacian = np.hstack((apple_lap[:, 0:int(cols / 2)], orange_lap[:, int(cols / 2):]))
    apple_orange_pyramid.append(laplacian)

# Step 5: Reconstruct image
apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1, layers):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(apple_orange_pyramid[i], apple_orange_reconstruct)

cv2.imshow("Blended Image", apple_orange_reconstruct)

cv2.waitKey(0)
cv2.destroyAllWindows()
