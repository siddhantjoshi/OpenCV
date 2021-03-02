import os 
import cv2
import wikipedia 
import speech_recognition as speech_recognition

from gtts import gTTS 
from playsound import playsound

def getFromUser():
	recognizer = speech_recognition.Recognizer()
	with speech_recognition.Microphone() as source:
	    print("Say something!")
	    audio = recognizer.listen(source)
	try:
	    print("You said: " + recognizer.recognize_google(audio))
	except speech_recognition.UnknownValueError:
	    print("Google Speech Recognition could not understand audio")
	except speech_recognition.RequestError as exception:
	    print("Could not request results from Google Speech Recognition service; {0}".format(exception))

	return str(recognizer.recognize_google(audio))

while True:

	stringToSearch = getFromUser()
	result = wikipedia.summary(stringToSearch, sentences = 3)  
	print(result)
	audioOutputFile = gTTS(text=result, lang='en', slow=False) 
	audioOutputFile.save("output audio files/"+stringToSearch+".mp3") 
	playsound("output audio files/"+stringToSearch+".mp3")

	#exit code 
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

