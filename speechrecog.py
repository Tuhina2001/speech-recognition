import speech_recognition as sr
import pyttsx3

#Initializing the recognizer
r = sr.Recognizer()

#Function to convert text to speech
def SpeakText(command):
    #Initializing the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

SpeakText("Hello World")

#Using microphone as source for input
with sr.Microphone() as source2:
    #waiting for a second to let the recognizer adjust the energy threshold
    #based on the surrounding noise level
    print("Silence please, calibrating background noise")
    r.adjust_for_ambient_noise(source2, duration=2)
    print("Calibrated, now speak......")

    #listening for the user's input
    audio2 = r.listen(source2)

    #Using google to recognize audio
    MyText = r.recognize_google(audio2)
    MyText = MyText.lower()
    print(MyText)
