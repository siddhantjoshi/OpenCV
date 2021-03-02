#import files which are needed
import numpy as np 
import cv2

#get default capture device to get images
capture = cv2.VideoCapture(0)

#to get continuous frame of images 
while True:
	#create a frame with name My Image and show it 
	rat, frame = capture.read()
	cv2.imshow('My image(Normal)', frame)

	#create a frame with gray scaling on it
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	cv2.imshow('My image(with gray scaling)', gray)

	#check if user as press 'q' from on keyboard
	#	YES ->quit task
	#	NO  ->Continue
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break
