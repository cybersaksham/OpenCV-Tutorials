import cv2

# Reading image
"""
0 - Grayscale
1 - Coloured (Default)
-1 - Unchanged
"""
img = cv2.imread("lena.jpg", 0)
# If image does not exists then img will be None otherwise it will be matrix of pixels
print(img)

# Showing Image
cv2.imshow("Window Title", img)  # This window destroy immediately

# In order to stop destroying the window
# cv2.waitKey(5000)  # Destroy window after 5s
# k = cv2.waitKey(1)  # Window destroy only on pressing a key if destroyAllWindows() is called on that key
k = cv2.waitKey(0)  # Window destroy only on pressing any key

# Writing Image
if k == 27:  # ESC key
    cv2.destroyAllWindows()
elif k == ord("s"):  # S key
    cv2.imwrite("lena_copy.jpg", img)
