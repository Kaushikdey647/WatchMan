import numpy as np
import cv2
import os
import serial
import time
from datetime import datetime

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
cwd = os.getcwd()
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)

while True:
    str = arduino.readline().decode().strip() # format the input data
    if str: #if not null
        dist = float(str)   #convert for processing
        if dist < 70:   #if less than 50
            print("INTRUSION DETECTED, Object Dist: ",dist)
            start = time.time()
            cap = cv2.VideoCapture(0)   #start capturing
            d = datetime.now().strftime("%m_%d_%Y") #date, for foldername
            t = datetime.now().strftime("%H_%M_%S")+".avi"  #time for filename
            vFile = os.path.join(cwd,d,t)   #join paths
            print(vFile)
            out = cv2.VideoWriter(vFile, fourcc, 20.0, (640,480))   #define output file
            while(cap.isOpened()):
                ret, frame = cap.read()
                if ret==True:
                    # frame = cv2.flip(frame,0)
                    # # write the flipped frame
                    out.write(frame)
                    #cv2.imshow('frame',frame)
                    if time.time() - start > 30:
                        break
                else:
                    break
            cap.release()
            out.release()
            cv2.destroyAllWindows()