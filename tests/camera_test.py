import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera test failed!")
    exit()

print("Camera test passed!")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Could not read camera frame.")
        break

    cv2.imshow("Camera Test", frame)

    key = cv2.waitKey(1)

    if key == ord("q") or key == 27:
        break

cap.release()
cv2.destroyAllWindows()