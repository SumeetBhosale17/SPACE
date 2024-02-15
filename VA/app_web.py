import os
import pyautogui
import webbrowser
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 200)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


dictapp = {"command prompt":"cmd", "vs code": "code", "paint":"paint", "word":"winword", "powerpoint":"powerpoint", "chrome":"chrome", "excel":"excel", "notepad":"notepad"}
keys = list(dictapp.keys())
def openaw(query):

    if ".com" in query:
        query = query.replace("open", "")
        query = query.replace("launch", "")
        query = query.replace("space", "")
        query = query.replace(" ", "")
        if ".com" in query :
            speak(f"Launching {query}")
            webbrowser.open(f"https://www.{query}")
    else :
        for app in keys:
            if app in query:
                speak(f"launching {app}")
                os.system(f"start {dictapp[app]}")

def closeaw(query):
    if "tab" in query:
        speak("closing tab!")
        pyautogui.hotkey("ctrl","w")
    elif "window" in query:
        speak("closing the window....!")
        pyautogui.hotkey("win","d")

    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                speak(f"closing {app}")
                os.system(f"taskkill /f /im {dictapp[app]}.exe")



