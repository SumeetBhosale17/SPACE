import pyttsx3
import datetime
import speech_recognition as sr 


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 300)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


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

    speak("I am SPACE")

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

    
if __name__ == '__main__':
    wishMe()
    speak("How can I help you?")
    while True:
        takeCommand()
        query = takeCommand().lower()

        if "what" and "time" in query:
            t = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {t}")




        elif "launch" and "rocket" in query:
            speak("Lauching the Rocket in ")
            engine.setProperty('rate',170)
            speak("3..... 2..... 1......")
            engine.setProperty('rate', 300)
            speak("The Rocket is launched!")

        elif "quit" or "exit" in query :
            speak("Quitting!")
            exit()