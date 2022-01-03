#importing packages
from imutils.video import VideoStream
import cv2 as cv
import time
import imutils
import datetime
import argparse

#constructing the argument parser and parse the argument
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="/path")
ap.add_argument("-a", "--min-area", type=int, default=100, help="minimum area size")
args = vars(ap.parse_args())

#if video argument is none, then we read from webcam
if args.get("video", None) is None:
    vs = VideoStream(src=0).start()
    time.sleep(2.0)
    
#else, we read from a video file
else:
    vs = cv.VideoCapture(args["video"])

#initializing the first frame
firstFrame = None

# loop over the frames of the video
while True:
	# grab the current frame and initialize the occupied/unoccupied
	# text
	frame = vs.read()
	frame = frame if args.get("video", None) is None else frame[1]
	text = "Unoccupied"
 
	# if the frame could not be grabbed, then we have reached the end
	# of the video
	if frame is None:
		break

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
 
 # loop over the contours
	for c in cnts:
		# if the contour is too small, ignore it
		if cv.contourArea(c) < args["min_area"]:
			continue
		
  # compute the bounding box for the contour, draw it on the frame,
		# and update the text
		(x, y, w, h) = cv.boundingRect(c)
		cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
		text = "Occupied"
  
  # draw the text and timestamp on the frame
	cv.putText(frame, "Room Status: {}".format(text), (10, 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
	cv.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10), cv.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
	
 # show the frame and record if the user presses a key
	cv.imshow("Security Feed", frame)
	cv.imshow("Thresh", thresh)
	cv.imshow("Frame Delta", frameDelta)
	key = cv.waitKey(1) & 0xFF
 
	# if the `q` key is pressed, break from the lop
	if key == ord("q"):
		break

# cleanup the camera and close any open windows
vs.stop() if args.get("video", None) is None else vs.release()
cv.destroyAllWindows()