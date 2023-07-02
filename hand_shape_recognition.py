# pip install opencv-python
# pip install mediapipe
import cv2
import sys
import mediapipe as mp
import math

def distance(p1, p2):
    return math.dist((p1.x, p1.y), (p2.x, p2.y))

def isStretch(finger):
    if finger == 4:
        if distance(points[finger], points[13]) < distance(points[finger - 1], points[13]):
            return False
        else:
            return True
    else:
        if distance(points[finger], points[0]) < distance(points[finger - 1], points[0]):
            return False
        else:
            return True

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera is not opend")
    sys.exit(1)

hand = mp_hands.Hands()

while True:
    res, frame = cap.read()

    if not res:
        print("Camera erorr")
        break
    
    frame = cv2.flip(frame, 1)
    image = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    results = hand.process(image)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style(),
            )

            points = hand_landmarks.landmark

            BigFinger = isStretch(4)
            PointFinger = isStretch(8)
            LongFinger = isStretch(12)
            RingFinger = isStretch(16)
            BabyFinger = isStretch(20)

            # F*** YOU 1
            if BigFinger == False and PointFinger == False and LongFinger == True and RingFinger == False and BabyFinger == False:
                cv2.putText(
                    frame,
                    "F*** YOU",
                    (int(points[0].x * frame.shape[1]), int(points[0].y * frame.shape[0])),
                    cv2.FONT_HERSHEY_COMPLEX,
                    1,
                    (0, 0, 255),
                    2,
                )
            
            # F*** YOU 2
            if BigFinger == True and PointFinger == False and LongFinger == True and RingFinger == False and BabyFinger == False:
                cv2.putText(
                    frame,
                    "F*** YOU",
                    (int(points[0].x * frame.shape[1]), int(points[0].y * frame.shape[0])),
                    cv2.FONT_HERSHEY_COMPLEX,
                    1,
                    (0, 0, 255),
                    2,
                )


            # I LOVE YOU
            if BigFinger == True and PointFinger == True and LongFinger == False and RingFinger == False and BabyFinger == True:
                cv2.putText(
                    frame,
                    "I LOVE YOU",
                    (int(points[0].x * frame.shape[1]), int(points[0].y * frame.shape[0])),
                    cv2.FONT_HERSHEY_COMPLEX,
                    1,
                    (203, 192, 255),
                    2,
                )

            # ROCK
            if BigFinger == False and PointFinger == False and LongFinger == False and RingFinger == False and BabyFinger == False:
                cv2.putText(
                    frame,
                    "ROCK",
                    (int(points[0].x * frame.shape[1]), int(points[0].y * frame.shape[0])),
                    cv2.FONT_HERSHEY_COMPLEX,
                    1,
                    (0, 255, 0),
                    2,
                )

            # SCISSORS
            if BigFinger == False and PointFinger == True and LongFinger == True and RingFinger == False and BabyFinger == False:
                cv2.putText(
                    frame,
                    "SCISSORS",
                    (int(points[0].x * frame.shape[1]), int(points[0].y * frame.shape[0])),
                    cv2.FONT_HERSHEY_COMPLEX,
                    1,
                    (0, 255, 0),
                    2,
                )

            # PAPER
            if BigFinger == True and PointFinger == True and LongFinger == True and RingFinger == True and BigFinger == True:
                cv2.putText(
                    frame,
                    "PAPER",
                    (int(points[0].x * frame.shape[1]), int(points[0].y * frame.shape[0])),
                    cv2.FONT_HERSHEY_COMPLEX,
                    1,
                    (0, 255, 0),
                    2,
                )


    cv2.imshow("MediaPipe", frame)

    key = cv2.waitKey(5) & 0xFF
    if key == 27:
        break

cv2.destroyAllWindows()
cap.release()