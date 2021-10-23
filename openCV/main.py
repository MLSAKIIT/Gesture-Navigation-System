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

                # Check Right Clicking
                RightClickedDist = math.sqrt(((hand.landmark[8].x - hand.landmark[12].x) * w) ** 2 + (
                        (hand.landmark[8].y - hand.landmark[12].y) * h) ** 2)
                if RightClickedDist < 22 and HoverDist > 30:
                    frame = cv2.putText(frame, "Right Clicked at (" + str(int(hand.landmark[8].x*w)) + ", " + str(int(hand.landmark[8].y*h)) + ")",
                                        (20, 40), cv2.FONT_HERSHEY_PLAIN, 1, 2)

                # Check Left Clicking
                LeftClickedDist = math.sqrt(((hand.landmark[8].x - hand.landmark[4].x) * w) ** 2 + (
                        (hand.landmark[8].y - hand.landmark[4].y) * h) ** 2)
                if LeftClickedDist < 22 and HoverDist > 30:
                    frame = cv2.putText(frame, "Left Clicked at (" + str(int(hand.landmark[8].x * w)) + ", " + str(
                        int(hand.landmark[8].y * h)) + ")",
                                        (20, 60), cv2.FONT_HERSHEY_PLAIN, 1, 2)

                # Checking Drag
                if RightClickedDist < 22 and LeftClickedDist < 15:
                    frame = cv2.putText(frame, "Picked up and Dragging",
                                        (20, 80), cv2.FONT_HERSHEY_PLAIN, 1, 2)
                else:
                    if Drag:
                        frame = cv2.putText(frame, "Dropped", (20, 80), cv2.FONT_HERSHEY_PLAIN, 1, 2)
                    Drag = False

               #Copy contents to clipboard

                CopyDist1 = math.sqrt(((hand.landmark[5].x - hand.landmark[7].x) * w) ** 2 + (
                        (hand.landmark[5].y - hand.landmark[7].y) * h) ** 2)
                CopyDist2 = math.sqrt(((hand.landmark[9].x - hand.landmark[11].x) * w) ** 2 + (
                        (hand.landmark[9].y - hand.landmark[11].y) * h) ** 2)
                CopyDist3 = math.sqrt(((hand.landmark[13].x - hand.landmark[15].x) * w) ** 2 + (
                        (hand.landmark[13].y - hand.landmark[15].y) * h) ** 2)
                CopyDist4 = math.sqrt(((hand.landmark[17].x - hand.landmark[19].x) * w) ** 2 + (
                        (hand.landmark[17].y - hand.landmark[19].y) * h) ** 2)
                CopyDist5 = math.sqrt(((hand.landmark[5].x - hand.landmark[6].x) * w) ** 2 + (
                        (hand.landmark[5].y - hand.landmark[6].y) * h) ** 2)
                CopyDist6 = math.sqrt(((hand.landmark[9].x - hand.landmark[10].x) * w) ** 2 + (
                        (hand.landmark[9].y - hand.landmark[10].y) * h) ** 2)
                CopyDist7 = math.sqrt(((hand.landmark[13].x - hand.landmark[14].x) * w) ** 2 + (
                        (hand.landmark[13].y - hand.landmark[14].y) * h) ** 2)
                CopyDist8 = math.sqrt(((hand.landmark[17].x - hand.landmark[18].x) * w) ** 2 + (
                        (hand.landmark[17].y - hand.landmark[18].y) * h) ** 2)




                if (CopyDist1 < 25 and CopyDist2<25 and CopyDist3<25 and CopyDist4<25) or \
                        (CopyDist5 < 25 and CopyDist6<25 and CopyDist7<25 and CopyDist8<25) :
                    frame = cv2.putText(frame, "Content copied to clipboard. " ,
                                        (20, 100), cv2.FONT_HERSHEY_PLAIN, 1, 2)



                #Pasting Contents
                PasteDist = math.sqrt(((hand.landmark[4].x - hand.landmark[16].x) * w) ** 2 + (
                        (hand.landmark[4].y - hand.landmark[16].y) * h) ** 2)

                if PasteDist < 22 and HoverDist > 30:
                    frame = cv2.putText(frame, "Pasting contents",
                                        (20, 100), cv2.FONT_HERSHEY_PLAIN, 1, 2)
                # Checking scroll up
                ScrollDistUp = math.sqrt(((hand.landmark[8].x - hand.landmark[7].x) * w) ** 2 + (
                        (hand.landmark[8].y - hand.landmark[7].y) * h) ** 2)

                if ScrollDistUp <15:
                    frame = cv2.putText(frame, "Scrolling up",
                                        (20, 60), cv2.FONT_HERSHEY_PLAIN, 1, 2)    
                    
                # Checking scroll down
                ScrollDownDist = math.sqrt(((hand.landmark[12].x - hand.landmark[11].x) * w) ** 2 + (
                        (hand.landmark[12].y - hand.landmark[11].y) * h) ** 2)

                if ScrollDownDist <5:
                    frame = cv2.putText(frame, "Scrolling down",
                                        (20, 60), cv2.FONT_HERSHEY_PLAIN, 1, 2) 
                # Checking zoom in
                ZoomInDist = math.sqrt(((hand.landmark[5].x - hand.landmark[4].x) * w) ** 2 + (
                        (hand.landmark[5].y - hand.landmark[4].y) * h) ** 2)

                if ZoomInDist <10:
                    frame = cv2.putText(frame, "Zooming in",
                                        (20, 60), cv2.FONT_HERSHEY_PLAIN, 1, 2)     
           
                # Checking zoom out
                ZoomOutDist = math.sqrt(((hand.landmark[4].x - hand.landmark[17].x) * w) ** 2 + (
                        (hand.landmark[4].y - hand.landmark[17].y) * h) ** 2)

                if ZoomOutDist <35:
                    frame = cv2.putText(frame, "Zooming out",
                                        (20, 60), cv2.FONT_HERSHEY_PLAIN, 1, 2)   
                # Checking cut
                CutDist = math.sqrt(((hand.landmark[20].x - hand.landmark[15].x) * w) ** 2 + (
                        (hand.landmark[20].y - hand.landmark[15].y) * h) ** 2)

                if CutDist <25:
                    frame = cv2.putText(frame, "Cut",
                                        (20, 60), cv2.FONT_HERSHEY_PLAIN, 1, 2) 

                # Alternative Gesture 1

                G1Dist1 = math.sqrt(((hand.landmark[4].x - hand.landmark[1].x) * w) ** 2 + (
                        (hand.landmark[4].y - hand.landmark[1].y) * h) ** 2)
                G1Dist2 = math.sqrt(((hand.landmark[17].x - hand.landmark[20].x) * w) ** 2 + (
                        (hand.landmark[17].y - hand.landmark[20].y) * h) ** 2)

                if CopyDist5<25 and CopyDist6<25 and CopyDist7<25 and G1Dist1>70 and G1Dist2>55:
                    frame = cv2.putText(frame, "Alternative Gesture 1",
                                        (20, 120), cv2.FONT_HERSHEY_PLAIN, 1, 2)


                # Alternative Gesture 2

                G2Dist1 = math.sqrt(((hand.landmark[5].x - hand.landmark[8].x) * w) ** 2 + (
                        (hand.landmark[5].y - hand.landmark[8].y) * h) ** 2)

                if CopyDist6 < 25 and CopyDist7 < 25 and G1Dist1 > 80 and G1Dist2 > 55 and G2Dist1 > 60 and (hand.landmark[8].y)*h<(hand.landmark[5].y)*h:
                    frame = cv2.putText(frame, "Alternative Gesture 2",
                                        (20, 120), cv2.FONT_HERSHEY_PLAIN, 1, 2)

                    
        cv2.imshow("Mediapipe", frame)
cv2.destroyAllWindows()
