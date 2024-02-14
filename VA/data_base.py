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


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)


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



# def search_google(query):
#     import wikipedia as googleScrap
#     query = query.replace("google","")
#     query = query.replace("on google","")
#     query = query.replace("search", "")
#     query = query.replace("space","")
#     speak("This is what I found on Google")


#     try :
#         pywhatkit.search(query)
#         result = googleScrap.summary(query, 1)
#         speak(result)

#     except:
#         speak("no, Speakable Output")

# def search_youtube(query):
#     speak("Here is What I found")
#     query = query.replace("youtube","")
#     query = query.replace("search","")
#     query = query.replace("space","")
#     query = query.replace("on youtube","")
#     web = "https://www.youtube.com/results?search_query="+query
#     webbrowser.open(web)
#     pywhatkit.playonyt(query)
#     speak("Done")

# def search_wiki(query):
#     query = query.replace("wikipedia","")
#     query = query.replace("on wikipedia","")
#     query = query.replace("space","")
#     query = query.replace("search","")
#     speak("Searching from Wikipedia.....")
#     result = wikipedia.summary(query, 2)
    # speak(result)

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

    speak("I am SPACE, How may I help you")



def work(query) :
    if "launch" and "rocket" in query:
        srs.main()
    elif "close" in query :
        aw.closeaw(query)
    elif "launch" or "open" in query :
        aw.openaw(query)
    elif "youtube" in query :
        search_youtube(query)
    elif "google" in query:
        search_google(query)
    elif "wikipedia" in query:
        search_wiki(query)
    elif "what" and "time" in query:
        t = datetime.datetime.now().strftime("%H:%M")
        speak(f"the time is {t}")
    elif "exit" or "quit" in query:
        speak("quitting, thank you for using space!")
        exit()
    else :
        speak("can't Recognize, say that again or, Invalid Command! How may i help you")
        query = takeCommand().lower()
        work(query)
        
# wishMe()




# query = takeCommand().lower()
# work("launch the rocket")
