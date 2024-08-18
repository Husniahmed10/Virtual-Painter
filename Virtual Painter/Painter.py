import cv2 as cv
import mediapipe as mp
import time
import os
import numpy as np
import Hand_Tracking_Module as htm

BrushThick = 15
EraserThick = 100

folderPath = "Images"
myList = os.listdir(folderPath)
print(myList)

List = []

for imgpath in myList:
    image = cv.imread(f'{folderPath}/{imgpath}')
    if image is not None:
        resized_image = cv.resize(image, (1280, 125))
        List.append(resized_image)
    else:
        print(f"Error loading image: {imgpath}")

print(len(List))    
if len(List) > 0:
    images = List[0]
else:
    print("No images loaded. Exiting.")
    exit()
    
drawColor = (255, 0, 255)

cap = cv.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = htm.handDetector(min_detection_confidence=0.85)

xp, yp = 0, 0
canvas = np.zeros((720, 1280, 3), np.uint8)

while True:
    success, img = cap.read()
    if not success:
        print("Failed to grab frame")
        break
    
    img = cv.flip(img, 1)
    
    img = detector.findHands(img)
    lmlist = detector.findPosition(img, draw = False)
    
    if len(lmlist) != 0:
        
        x1, y1 = lmlist[8][1:]
        x2, y2 = lmlist[12][1:]
        
        fingers = detector.fingersup()
        
        if fingers[1] and fingers[2]:
            xp, yp = 0, 0
            print("Selection Mode")
            
            if y1 < 125:
                if 250 < x1 < 450:
                    images = List[0]
                    drawColor = (255, 0, 255)
                elif 550 < x1 < 750:
                    images = List[1]
                    drawColor = (255, 0, 0)
                elif 800 < x1 < 950:
                    images = List[2]
                    drawColor = (0, 255, 0)
                elif 1050 < x1 < 1200:
                    images = List[3]
                    drawColor = (0, 0, 0)
                    
            cv.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), drawColor, cv.FILLED)
            
        if fingers[1] and fingers[2] == False:
            cv.circle(img, (x1, y1), 15, drawColor, cv.FILLED)
            print("Drawing Mode")
            
            if xp == 0 and yp == 0:
                xp, yp = x1, y1
            
            if drawColor == (0, 0, 0):
                 cv.line(img, (xp, yp), (x1, y1), drawColor, EraserThick)
                 cv.line(canvas, (xp, yp), (x1, y1), drawColor, EraserThick)
            
            else:
                cv.line(img, (xp, yp), (x1, y1), drawColor, BrushThick)
                cv.line(canvas, (xp, yp), (x1, y1), drawColor, BrushThick)
            
            xp, yp = x1, y1
    
    imgGray = cv.cvtColor(canvas, cv.COLOR_BGR2GRAY)
    _, imgInv = cv.threshold(imgGray, 50, 255, cv.THRESH_BINARY_INV)
    imgInv = cv.cvtColor(imgInv,cv.COLOR_GRAY2BGR)
    img = cv.bitwise_and(img,imgInv)
    img = cv.bitwise_or(img,canvas)
            
                
    img[0:125, 0:1280] = images
    cv.imshow("Image", img)
    cv.imshow("canva", canvas)
    cv.imshow('inv', imgInv)
    cv.waitKey(1)
    
    
    