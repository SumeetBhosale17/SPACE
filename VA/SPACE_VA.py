import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install speechrecognition 
import data_base 
from data_base import speak
from data_base import takeCommand
import search_web


    

data_base.wishMe()
while True:
    query = takeCommand().lower()
    # query = "what is the time now"
    # if "exit" or "quit" in query:
    #     speak("quitting Sir, Thank you for using Space!")
    #     exit()
    # else:
    data_base.work(query)
    