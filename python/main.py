from imutils.video import VideoStream
import numpy as np
import cv2 as cv
import serial
import time
from datetime import datetime
import time
import imutils
import datetime
import argparse

fourcc = cv.VideoWriter_fourcc(*'DIVX')
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="/path")
ap.add_argument("-a", "--min-area", type=int, default=100, help="minimum area size")
args = vars(ap.parse_args())

if args.get("video", None) is None:
    vs = VideoStream(src=0).start()
    time.sleep(2.0)

else:
    vs = cv.VideoCapture(args["video"])

firstFrame = None

while True:
    str = arduino.readline().decode().strip() # format the input data
    if str: #if not null
        dist = float(str)   #convert for processing
        if dist < 50:   #if less than 50
            print("INTRUSION DETECTED, Object Dist: ",dist)
            start = time.time()
            cap = cv.VideoCapture(0)   #start capturing
            t = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")+".avi"  #time for filename
            out = cv.VideoWriter(t, fourcc, 20.0, (640,480))   #define output file
            while(cap.isOpened()):
                str = arduino.readline() # keep reading, idk how else to discard values
                ret, frame = cap.read()
                if ret==True:
                    out.write(frame)
                    cv.imshow('frame',frame)
                    # if time.time() - start > 30: 
                        # break
                else:
                    break
            cap.release()
            out.release()
            cv.destroyAllWindows()