import pyttsx3
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup #pip install bs4


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try :
        print("Recognizing......")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")
    except Exception as e:
        # print(e)
        speak("Say that again.....")
        return "None"
    return query



def search_temp():
    speak("may i know which city or town :")
    city = takeCommand().lower()
    search = f"temperature in {city}"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data =BeautifulSoup(r.text, "html.parser")
    temp = data.find("div", class_ = "BNeawe").text
    speak(f"current {search} is {temp}")

def weather():
    speak("may i know which city or town :")
    city = takeCommand().lower()
    search = f"weather in {city}"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data =BeautifulSoup(r.text, "html.parser")
    temp = data.find("div", class_ = "BNeawe").text
    speak(f"current {search} is {temp}")