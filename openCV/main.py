import mediapipe as mp
from cv2 import cv2
import math

captured = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

Drag = False
DragLeave = True

while True:
    ret, frame = captured.read()
    if cv2.waitKey(1) == 27:
        break
    if ret:
        frame = cv2.flip(frame, 1)
        Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        Flipped = cv2.flip(frame, 1)
        results = hands.process(frame)
        if results.multi_hand_landmarks:
            for hand in results.multi_hand_landmarks:
                mpDraw.draw_landmarks(frame, hand, mpHands.HAND_CONNECTIONS)
                h, w, c = frame.shape

                # Check Hovering
                HoverDist = math.sqrt(((hand.landmark[8].x - hand.landmark[5].x) * w) ** 2 + (
                        (hand.landmark[8].y - hand.landmark[5].y) * h) ** 2)
                if HoverDist > 30:
                    frame = cv2.putText(frame, "Hovering at (" + str(int(hand.landmark[8].x*w)) + ", " + str(int(hand.landmark[8].y*h)) + ")",
                                        (20, 20), cv2.FONT_HERSHEY_PLAIN, 1, 2)

                # Check Clicking
                ClickedDist = math.sqrt(((hand.landmark[8].x - hand.landmark[12].x) * w) ** 2 + (
                        (hand.landmark[8].y - hand.landmark[12].y) * h) ** 2)
                if ClickedDist < 22 and HoverDist > 30:
                    frame = cv2.putText(frame, "Clicked at (" + str(int(hand.landmark[8].x*w)) + ", " + str(int(hand.landmark[8].y*h)) + ")",
                                        (20, 40), cv2.FONT_HERSHEY_PLAIN, 1, 2)

                # Checking Drag
                DragDist = math.sqrt(((hand.landmark[8].x - hand.landmark[4].x) * w) ** 2 + (
                        (hand.landmark[8].y - hand.landmark[4].y) * h) ** 2)

                if DragDist < 15 and ClickedDist < 22:
                    frame = cv2.putText(frame, "Picked up and Dragging",
                                        (20, 60), cv2.FONT_HERSHEY_PLAIN, 1, 2)
                else:
                    if Drag:
                        frame = cv2.putText(frame, "Dropped", (20, 60), cv2.FONT_HERSHEY_PLAIN, 1, 2)
                    Drag = False

        cv2.imshow("Mediapipe", frame)
cv2.destroyAllWindows()