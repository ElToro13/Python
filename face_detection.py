import numpy as np
import cv2
import serial

ser = serial.Serial(port='COM8', baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS)

ser1 = serial.Serial(port='COM6', baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS)

detector= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
def move(angle1,angle2):
    if(0<= angle1 <=500):
        if(0<= angle2 <=500):
            angle1=angle1*0.36
            angle2=angle2*0.36

            angle1=int(angle1)
            ser.write(chr(255))
            ser.write(chr(angle1))

            angle2=int(angle2)
            ser1.write(chr(255))
            ser1.write(chr(angle2))
        
        
                
    else:
         print("Value exceeds")
               
    
while(True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    if(len(faces)!=0):
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            print (x,y)
            move(x,y)
    cv2.imshow('frame',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
