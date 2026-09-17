import cv2
from ultralytics import YOLO

from config.config import (
    CONFIDENCE_THRESHOLD,
    STOP_SIGN_CLASS,
    ALERT_ENABLED,
    ALERT_COOLDOWN
)
from detector.alert import check_alert
from storage.db import create_database, insert_detection

MODEL_PATH = "models/best.pt"

model = YOLO(MODEL_PATH)


def detect_webcam():

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Webcam could not be opened.")
        return

    while True:

        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame.")
            break

        results = model(frame, conf=CONFIDENCE_THRESHOLD)

        for result in results:

            for box in result.boxes:

                class_id = int(box.cls[0])
                confidence = float(box.conf[0])
                class_name = model.names[class_id]

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                cv2.rectangle(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    frame,
                    f"{class_name} {confidence:.2f}",
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2
                )

                # Save detection to database
                insert_detection(class_name, confidence)

                # Trigger alert for STOP sign
                if ALERT_ENABLED:
                    check_alert(
                        class_name,
                        confidence,
                        ALERT_COOLDOWN
                    )

        cv2.imshow("Live Road Sign Detection", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            print("Detection stopped.")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    create_database()
    detect_webcam()