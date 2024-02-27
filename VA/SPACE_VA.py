'''
___________MODULES__________

pip install pyttsx3
pip install speechrecognition
pip install pywhatkit
pip install wikipedia
pip install bs4
pip install pynput

'''

import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install speechrecognition 
import data_base 
from data_base import speak
from data_base import takeCommand
import search_web


    

data_base.wishMe()
while True:
    speak("How can I assist you")
    query = takeCommand().lower()
#     # query = "what is the time now"
#     # if "exit" or "quit" in query:
#     #     speak("quitting Sir, Thank you for using Space!")
#     #     exit()
#     # else:
    data_base.work(query)

# data_base.work("launch missile")
    