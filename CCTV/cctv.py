import threading
import time
import numpy as np
import cv2
import requests
import json

global checker
checker = 0
#cap = cv2.VideoCapture(0)
#https://api.thingspeak.com/update?api_key=A7C155A7ZBI9IWLO&field1=0
class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name + "\n")
      while(True):
          #print("I entered run")
          #print(str(checker) + "\n")
          global checker
          cc = checker
          if cc == 1:
             cap = cv2.VideoCapture(1)
             fourcc = cv2.VideoWriter_fourcc(*'XVID')
             out = cv2.VideoWriter('F:\\CCTV Footage\\output.avi',fourcc, 20.0, (640,480))
             print("Recording is ON")
             while(cap.isOpened() and cc == 1):
                ret, frame = cap.read()
                #global checker
                cc = checker
                if ret==True:
                   #frame = cv2.flip(frame,0)
                   out.write(frame)
                   cv2.imshow('frame',frame)
                   if cc == 0:
                      print("Recording is OFF")
                      cap.release()
                      out.release()
                      cv2.destroyAllWindows()
                      break
                      
                   
                   
                
                      
         

class myThread2 (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name +"\n")
      while(True):
         try:
             check = requests.get("https://api.thingspeak.com/channels/479406/feeds.json?api_key=FAONR5W0K0WWGE30&results=1")
             check = json.loads(check.content.decode('utf-8'))
             global checker
             checker = int(check["feeds"][0]["field1"])
         except:
            print("Shit, that server giving fuckAll values again.")
          #print("Thread2: {}".format(checker))
          

                  
# Create new threads
thread1 = myThread(1, "Thread-1",1)
thread2 = myThread2(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

print ("Exiting Main Thread\n")

