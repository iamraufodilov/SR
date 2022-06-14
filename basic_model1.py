# load libraries
import speech_recognition as sr
import pyttsx3

# initialize the recognizer
r = sr.Recognizer()


# function to convert text to speech
def text2speech(sentence):
    engine = pyttsx3.init()
    engine.say(sentence)
    engine.runAndWait()


# lets try
sentence = "Hello, Rauf Odilov. I am your text to speech model"
text2speech(sentence)


# install microphone 

with sr.Microphone() as microphone:
    print("please remove the background sound")
    r.adjust_for_ambient_noise(microphone, duration=2)
    print("You can speak now")

    audio = r.listen(microphone)

    text_of_audio = r.recognize_google(audio)
    text_of_audio.lower()

    print("I think you said: ", text_of_audio)