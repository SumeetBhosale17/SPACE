import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install speechrecognition 
import data_base 
from data_base import speak
from data_base import takeCommand
import search_web



# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)
# engine.setProperty('rate', 300)


# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()



# def takeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening.....")
#         r.pause_threshold = 1
#         audio = r.listen(source)
#     try :
#         print("Recognizing......")
#         query = r.recognize_google(audio, language='en-in')
#         print(f"User said : {query}\n")
#     except Exception as e:
#         # print(e)
#         speak("Say that again.....")
#         return "None"
#     return query

    

data_base.wishMe()
while True:
    query = takeCommand().lower()
    if "exit" or "quit" in query:
        speak("quitting Sir, Thank you for using Space!")
        exit()
    else:
        data_base.work(query)
    