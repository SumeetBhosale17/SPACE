import time
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    print(text)  # Display the text

def locate_target():
    speak("Please enter the coordinates of the target:")
    coordinates = input().split(',')
    speak("Target located at coordinates: " + ', '.join(coordinates))

def launch_rocket():
    speak("Target located. Initiating launch sequence...")
    countdown()

def countdown():
    for i in range(10, 0, -1):
        speak(str(i))
        time.sleep(1)
    speak("Target destroyed!")

def main():
    locate_target()
    launch_rocket()

if __name__ == "__main__":
    main()

