import cv2

img = cv2.imread("messi5.jpg", 1)

print(img.shape)  # Tuple of no of rows, columns & channels
print(img.size)  # Total no of pixels
print(img.dtype)  # Image datatype

b, g, r = cv2.split(img)  # Split channels of image
img = cv2.merge((b, g, r))  # Merge given channels into an image


def click_event(event, x, y, flags, param):
    global points
    # Working with ROI (Region of Interest)
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(points) % 3 == 0 and len(points) != 0:
            points = []
        points.append((y, x))
        if len(points) == 3:
            from_copy = img[points[0][0]:points[1][0], points[0][1]:points[1][1]]
            y2 = points[2][0] + points[1][0] - points[0][0]
            x2 = points[2][1] + points[1][1] - points[0][1]
            img[points[2][0]:y2, points[2][1]:x2] = from_copy
            cv2.imshow('image', img)


points = []
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)

cv2.destroyAllWindows()
