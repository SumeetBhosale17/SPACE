import pyautogui
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import pywhatkit


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 300)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def search_google(query):
    import wikipedia as googleScrap
    query = query.replace("on google","")
    query = query.replace("google","")
    query = query.replace("search", "")
    query = query.replace("space","")
    speak("opening google")
    speak("This is what I found on Google")


    try :
        pywhatkit.search(query)
        result = googleScrap.summary(query, 1)
        speak(result)

    except:
        speak("no, Speakable Output")

def search_youtube(query):
    speak("Here is What I found on youtube")
    query = query.replace("on youtube","")
    query = query.replace("youtube","")
    query = query.replace("search","")
    query = query.replace("space","")
    web = "https://www.youtube.com/results?search_query="+query
    webbrowser.open(web)
    speak("playing first video")
    pywhatkit.playonyt(query)
    speak("Done")

def search_wiki(query):
    query = query.replace("on wikipedia","")
    query = query.replace("wikipedia","")
    query = query.replace("space","")
    query = query.replace("search","")
    speak("Searching from Wikipedia")
    result = wikipedia.summary(query, 2)
    speak("According to wikipedia......")
    speak(result)
