# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import cv2
import pickle
import numpy as np

rectW,rectH = 107, 48
cap=cv2.VideoCapture('video.mp4')

with open('carParkPos', 'rb') as f:
    posList=pickle.load(f)
def check(imgPro):
    spaceCount = 0
    for pos in posList:
        x,y=pos
        crop=imgPro[y:y+rectH,x:x+rectW]
        count=cv2.countNonZero(crop)
        if count<900:
            spaceCount +=1
            color=(0,255,0)
            thick = 5
        else:
            color=(0,0,255)
            thick = 2
        cv2.rectangle(img,pos, (x+rectW, y+rectH) , color,thick)
    cv2.rectangle(img, (45,30), (250, 75), (100,0,100), -1)
    cv2.putText(img, f'Free: {spaceCount}/{len(posList)}', (50,60), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,255),2 )

while True:
    _,img = cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray, (3,3),1)
    Thre= cv2.adaptiveThreshold(blur, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV, 25,16)
    blur=cv2.medianBlur(Thre, 5)
    kernel=np.ones((3,3),np.uint8)
    dilate=cv2.dilate(blur,kernel,iterations=1)
    check(dilate)
    
    cv2.imshow("Image", img)
    cv2.waitKey(15)
    



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
