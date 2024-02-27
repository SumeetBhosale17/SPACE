import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import pywhatkit
import datetime
import search_web 
from search_web import search_google
from search_web import search_wiki
from search_web import search_youtube
import app_web as aw
import Space_RS as srs
import temp_weat as tw
import pyautogui
import kb


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




def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("Good Morning!")
    elif hour>=12 and hour<16:
        speak("Good AfterNoon!")
    elif hour>=16 and hour < 20:
        speak("Good Evening!")
    else :
        speak("Good Night!")

    speak("I am SPACE,")



def work(query) :
    if "hello" in query :
        speak("Hi sir, How may I help you")
    elif "what are you" in query or "who are you" in query:
        speak("I'm SPACE, STRATEGIC PERSONAL ASSISTANT with COGNITIVE EXPERTISE. I'm a voice assistant who will assist you in various tasks such as Launching missiles etcetra.")
    elif "why" in query and "created" or "made" in query:
        speak("I have been created to assist military in battles, by helping them to launch missiles on their command.")
    elif "launch" in query and "missile" in query:
        srs.main()
    elif "close" in query:
        aw.closeaw(query)
    elif "open" in query or "launch" in query:
        aw.openaw(query)
    elif "youtube" in query:
        search_youtube(query)
    elif "google" in query:
        search_google(query)
    elif "wikipedia" in query:
        search_wiki(query)
    elif "what" in query and "time" in query:
        t = datetime.datetime.now().strftime("%H:%M")
        speak(f"the time is {t}")
    elif "temperature" in query :
        tw.search_temp()
    elif "weather" in query :
        tw.weather()
    elif "pause" in query:
        pyautogui.press("k")
        speak("video paused")
    elif "play" in query:
        pyautogui.press("k")
        speak("video playing")
    elif "mute" in query:
        pyautogui.press("m")
        speak("video muted")
    elif "volume up" in query or "increase volume" in query or "up volume" in query:
        speak("increasing volume")
        kb.volume_up()
    elif "volume down" in query or "decreasing volume"in query or "down volume" in query:
        speak("decreasing volume")
        kb.volume_down()
    elif "exit" in query or "quit" in query:
        speak("quitting, thank you for using space!")
        exit()
    else:
        speak("Can't recognize that command. Please say it again or ask for help.")
        query = takeCommand().lower()
        work(query)

        
# wishMe()




# query = takeCommand().lower()
# work("weather")
