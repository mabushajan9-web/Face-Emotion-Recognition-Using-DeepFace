import cv2
from deepface import DeepFace
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break
    try:
        results = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        if isinstance(results, dict):
            results = [results]
        for result in results:
            region = result["region"]
            dominant_emotion = result["dominant_emotion"]
            x, y, w, h = region["x"], region["y"], region["w"], region["h"]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(
                frame,
                f"{dominant_emotion}",
                (x, y - 10),
                font,
                0.9,
                (0, 0, 255),
                2,
                cv2.LINE_4
            )
    except Exception as e:
        print("No face detected or error:", str(e))
    cv2.imshow("Live Emotion Recognition", frame)
    key = cv2.waitKey(1)
    if key == ord('q') or key == 27:
        break
cap.release()
cv2.destroyAllWindows()
