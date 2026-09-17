import cv2
from ultralytics import YOLO

from config.config import CONFIDENCE_THRESHOLD, ALERT_ENABLED, ALERT_COOLDOWN
from detector.alert import check_alert
from storage.db import create_database, insert_detection

MODEL_PATH = "models/best.pt"


def detect_video(video_path):
    model = YOLO(MODEL_PATH)
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Video could not be opened.")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
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

                insert_detection(class_name, confidence)

                if ALERT_ENABLED:
                    check_alert(class_name, ALERT_COOLDOWN)

        cv2.imshow("Road Sign Video Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    create_database()

    video_path = input("Enter video path: ")
    detect_video(video_path)