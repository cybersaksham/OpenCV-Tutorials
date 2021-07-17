import cv2

# cap = cv2.VideoCapture("filename")  # For a particular video file
cap = cv2.VideoCapture(0)  # For device camera

# Frame Dimensions
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(width, height)

# Saving Video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("output.mp4", fourcc, 20.0, (640, 480))

while cap.isOpened():  # If filename is incorrect returns False
    # Reading Frames
    ret, frame = cap.read()

    if ret:
        # Showing Frames
        cv2.imshow("Window Title", frame)

        # Saving Frames
        out.write(frame)

        # In Grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Window Title", gray)

        if cv2.waitKey(1) == 27:
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
