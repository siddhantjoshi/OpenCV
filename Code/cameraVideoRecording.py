#import files which are needed
import numpy as np 
import cv2
import os

#filename
fileName = 'captureVideoFile.avi'

#get default capture device to get images
capture = cv2.VideoCapture(0)

#define extension of the video which is being recorded
videoType = cv2.VideoWriter_fourcc(*'XVID')

#get video file as output and attach all to variable
outputVideoFle = cv2.VideoWriter(fileName, videoType , 20.0, (64, 48))

#to get continuous frame of images 
while True:
	#create a frame with name My Image and show it 
	ret, frame = capture.read()
	
	#scale down video size
	scaleDownVideo = cv2.resize(frame,(64,48),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
	#show output 
	cv2.imshow('My image(Normal)', frame)
	cv2.imshow('My image(Scale Down)', scaleDownVideo)
	
	#store output file
	outputVideoFle.write(scaleDownVideo)
	
	#termination condition 
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

capture.release()
outputVideoFle.release()
cv2.destroyAllWindows()