
from ultralytics import YOLO
import cv2
import time
import csv
from datetime import datetime

# Load YOLO model
model = YOLO("yolov8n.pt")

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam!")
    exit()

# Counting variables
up_count = 0
down_count = 0
class_counts = {}

# Store previous positions
previous_positions = {}

# FPS variables
prev_time = 0

# CSV logging
csv_file = open("counting_results.csv", "a", newline="")
csv_writer = csv.writer(csv_file)

if csv_file.tell() == 0:
    csv_writer.writerow(["Object", "Direction", "Time"])

print("Smart Object Counting System Started!")
print("Press R to reset counts")
print("Press Q to quit")

try:

    while True:

        ret, frame = cap.read()

        if not ret:
            print("Failed to capture frame")
            break

        height, width = frame.shape[:2]

        # Horizontal counting line
        line_y = height // 2

        # YOLO object detection and ByteTrack tracking
        results = model.track(
            frame,
            persist=True,
            tracker="bytetrack.yaml",
            conf=0.2,
            iou=0.5,
            verbose=False
        )

        # Draw counting line
        cv2.line(
            frame,
            (0, line_y),
            (width, line_y),
            (0, 255, 255),
            2
        )

        # Process detected objects
        if results[0].boxes is not None:

            boxes = results[0].boxes

            if boxes.id is not None:

                track_ids = boxes.id.int().cpu().tolist()
                class_ids = boxes.cls.int().cpu().tolist()
                coordinates = boxes.xyxy.cpu().tolist()
                confidences = boxes.conf.cpu().tolist()

                for box, track_id, class_id, confidence in zip(
                    coordinates,
                    track_ids,
                    class_ids,
                    confidences
                ):

                    x1, y1, x2, y2 = map(int, box)

                    # Object center
                    center_x = (x1 + x2) // 2
                    center_y = (y1 + y2) // 2

                    # Object name
                    class_name = model.names[class_id]

                    # Draw bounding box
                    cv2.rectangle(
                        frame,
                        (x1, y1),
                        (x2, y2),
                        (0, 255, 0),
                        2
                    )

                    # Draw center point
                    cv2.circle(
                        frame,
                        (center_x, center_y),
                        5,
                        (0, 0, 255),
                        -1
                    )

                    # Display label, ID, and confidence
                    label = f"{class_name} ID:{track_id} {confidence:.2f}"

                    cv2.putText(
                        frame,
                        label,
                        (x1, max(y1 - 10, 20)),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5,
                        (255, 255, 255),
                        2
                    )

                    # Check line crossing
                    if track_id in previous_positions:

                        previous_y = previous_positions[track_id]

                        # Top to bottom
                        if previous_y < line_y and center_y >= line_y:

                            down_count += 1

                            class_counts[class_name] = (
                                class_counts.get(class_name, 0) + 1
                            )

                            print(f"{class_name} crossed DOWN")

                            csv_writer.writerow([
                                class_name,
                                "DOWN",
                                datetime.now().strftime(
                                    "%Y-%m-%d %H:%M:%S"
                                )
                            ])

                            csv_file.flush()

                        # Bottom to top
                        elif previous_y > line_y and center_y <= line_y:

                            up_count += 1

                            class_counts[class_name] = (
                                class_counts.get(class_name, 0) + 1
                            )

                            print(f"{class_name} crossed UP")

                            csv_writer.writerow([
                                class_name,
                                "UP",
                                datetime.now().strftime(
                                    "%Y-%m-%d %H:%M:%S"
                                )
                            ])

                            csv_file.flush()

                    # Update previous position
                    previous_positions[track_id] = center_y

        # Total count
        total_count = up_count + down_count

        # FPS calculation
        current_time = time.time()

        if prev_time != 0:
            fps = 1 / (current_time - prev_time)
        else:
            fps = 0

        prev_time = current_time

        # FPS display
        cv2.putText(
            frame,
            f"FPS: {fps:.2f}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

        # UP count
        cv2.putText(
            frame,
            f"UP: {up_count}",
            (20, 75),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 0, 0),
            2
        )

        # DOWN count
        cv2.putText(
            frame,
            f"DOWN: {down_count}",
            (20, 110),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 0, 255),
            2
        )

        # Total count
        cv2.putText(
            frame,
            f"TOTAL COUNT: {total_count}",
            (20, 145),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 255),
            2
        )

        # Class-wise count
        y_position = 180

        for class_name, count in class_counts.items():

            cv2.putText(
                frame,
                f"{class_name}: {count}",
                (20, y_position),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 255, 255),
                2
            )

            y_position += 25

        # Instructions
        cv2.putText(
            frame,
            "R: Reset | Q: Quit",
            (20, height - 20),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            2
        )

        # Show camera window
        cv2.imshow("Smart Object Counting System", frame)

        # Keyboard controls
        key = cv2.waitKey(1) & 0xFF

        # Reset counts
        if key == ord("r") or key == ord("R"):

            up_count = 0
            down_count = 0
            class_counts.clear()
            previous_positions.clear()

            print("Counts Reset!")

        # Quit
        elif key == ord("q") or key == ord("Q"):
            break

finally:

    cap.release()
    cv2.destroyAllWindows()
    csv_file.close()

    print("System stopped successfully!")
    print("Results saved in counting_results.csv")

