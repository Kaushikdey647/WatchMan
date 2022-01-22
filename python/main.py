from imutils.video import VideoStream
import cv2 as cv
import serial
import time
from datetime import datetime
import time
import imutils
import argparse

fourcc = cv.VideoWriter_fourcc(*'DIVX')
arduino = serial.Serial(port='COM12', baudrate=9600, timeout=.1)

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


curr = time.time()

objend = time.time()

detectedy = False

detectedx = False

while True:
    str = arduino.readline().decode('utf-8').strip() # format the input data
    if str: #if not null
        try:
            dist = float(str)
        except:
            continue;
        finally:
            if dist < 50:   #if less than 50
                print("INTRUSION DETECTED, Object Dist: ",dist)
                #alll the times
                cap = cv.VideoCapture(0)   #start capturing
                t = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")+".avi"  #time for filename
                out = cv.VideoWriter(t, fourcc, 20.0, (640,480))   #define output file
                while(cap.isOpened()):
                    str = arduino.readline() # keep reading, idk how else to discard values
                    curr = time.time()
                    ret, frame = cap.read()
                    if ret==True:
                        frame = frame if args.get("video", None) is None else frame[1]
                        text = "Unoccupied"

                        # resize the frame, convert it to grayscale, and blur it
                        frame = imutils.resize(frame, width=500)
                        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                        gray = cv.GaussianBlur(gray, (21, 21), 0)

                        # if the first frame is None, initialize it
                        if firstFrame is None:
                            firstFrame = gray
                            continue

                        # compute the absolute difference between the current frame and
                        # first frame
                        frameDelta = cv.absdiff(firstFrame, gray)
                        thresh = cv.threshold(frameDelta, 25, 255, cv.THRESH_BINARY)[1]
                        
                        # dilate the thresholded image to fill in holes, then find contours on thresholded image
                        thresh = cv.dilate(thresh, None, iterations=2)
                        cnts = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
                        cnts = imutils.grab_contours(cnts)

                        for c in cnts:
                            # if the contour is too small, ignore it
                            if cv.contourArea(c) < args["min_area"]:
                                if(detectedy == True):
                                    detectedx = False
                                    objend = time.time()
                                continue
                            (x, y, w, h) = cv.boundingRect(c)
                            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                            detectedy = True
                            detectedx = True
                            text = "Occupied"
                        # draw the text and timestamp on the frame
                        cv.putText(frame, "Room Status: {}".format(text), (10, 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                        cv.putText(frame, datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10), cv.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
                        # show the frame and record if the user presses a key
                        cv.imshow("Security Feed", frame)
                        cv.imshow("Thresh", thresh)
                        cv.imshow("Frame Delta", frameDelta)
                        key = cv.waitKey(1) & 0xFF
                        out.write(frame)
                        if(detectedy == True and detectedx == False and (time.time() - objend >30)):
                            detectedy == False
                            break
                        # if the `q` key is pressed, break from the lop
                        if key == ord("q"):
                            break
                    else:
                        break
                cap.release()
                out.release()
                cv.destroyAllWindows()