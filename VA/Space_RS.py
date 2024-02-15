import time
import pyttsx3
# import data_base
import speech_recognition as sr
# Initialize the text-to-speech engine
engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('rate', 200)
# engine.setProperty('voices', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
    # print(text)  # Display the text


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
        takeCommand()
    return query


def locate_target():
    speak("Please enter the coordinates of the target:")
    coordinates = takeCommand().split(' ')
    speak("Target located at coordinates: " + ', '.join(coordinates))


def countdown():
    for i in range(10, 0, -1):
        speak(str(i))
        time.sleep(0.3)
    speak("Target destroyed!")


def launch_rocket():
    speak("Target located. Initiating launch sequence...")
    countdown()

def main():
    locate_target()
    launch_rocket()

# if __name__ == "__main__":
#     main()
# countdown()
# main()
