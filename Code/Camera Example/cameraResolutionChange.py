#import files which are needed
import numpy as np 
import cv2

#get default capture device to get images
capture = cv2.VideoCapture(0)

#create functions to decrease/increase resolution of image
def changeImageResolution(frame, width, height):
	scaleDownVideo = cv2.resize(frame,(width,height),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
	return scaleDownVideo

#to get continuous frame of images 
while True:
	#create a frame with name My Image and show it 
	rat, frame = capture.read()
	cv2.imshow('My image(Normal)', frame)
	
	#call function
	scaleDownVideo = changeImageResolution(frame,68, 48)

	#scale doen image
	cv2.imshow('My image(Scale Down)', scaleDownVideo)
	
	#check if user as press 'q' from on keyboard
	#	YES ->quit task
	#	NO  ->Continue
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break
capture.release()
cv2.destroyAllWindows()