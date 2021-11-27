import math

import cv2
import mouse
import wx
import HandTrackingModule as htm
import keyboard

app = wx.App(False)
width, height = wx.GetDisplaySize()

cap = cv2.VideoCapture(0)

detector = htm.handDetector(detectionCon=0.7)
i = 0
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    cv2.putText(img, 'Press q to quit', (10, 30), cv2.FONT_HERSHEY_DUPLEX, 0.5,
                (255, 0, 0), 1)
    cv2.imshow("Img", img)
    i += 1
    if i == 2:
        lm = detector.findPosition(img)
        r = 0.0
        try:
            mouse.move(lm[8][1] * 2, lm[8][2] * 2)
            print("Mouse pointer hovering")

            if ((((lm[4][1] - lm[8][1]) ** 2) +
                 ((lm[4][2] - lm[8][2]) ** 2)) ** 0.5) / 240 < 0.05:
                mouse.click()

            if ((((lm[4][1] - lm[9][1]) ** 2) +
                 ((lm[4][2] - lm[9][2]) ** 2)) ** 0.5) / 240 < 0.1:
                keyboard.press_and_release('up')
                print("Scrolling up")

            if ((((lm[4][1] - lm[5][1]) ** 2) +
                 ((lm[4][2] - lm[5][2]) ** 2)) ** 0.5) / 240 < 0.1:
                keyboard.press_and_release('down')
                print("Scrolling down")

            if ((((lm[12][1] - lm[8][1]) ** 2) +
                 ((lm[12][2] - lm[8][2]) ** 2)) ** 0.5) / 240 < 0.1:
                keyboard.press_and_release('Esc')
                print("Escape")

            if ((((lm[4][1] - lm[17][1]) ** 2) +
                 ((lm[4][2] - lm[17][2]) ** 2)) ** 0.5) / 240 < 0.1:
                keyboard.press_and_release('Enter')
                print("Enter")

            if ((((lm[4][1] - lm[16][1]) ** 2) +
                 ((lm[4][2] - lm[16][2]) ** 2)) ** 0.5) / 240 < 0.1:
                keyboard.press_and_release('Backspace')
                print("Backspace")

        except:
            print("NO HAND VISIBLE")
        finally:
            i = 0

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break