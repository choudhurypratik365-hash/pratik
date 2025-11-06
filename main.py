import speech_recognition as sr
import webbrowser
import pyttsx3
import pyaudio
import musiclibrary

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
tts = pyttsx3.init()

def speak(text):
    tts.say(text)
    tts.runAndWait()

def processCommand(command):
    command = command.lower()
    if "open google" in command:
        webbrowser.open("https://google.com")
    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
    elif "open whatsapp" in command:
        webbrowser.open("https://web.whatsapp.com") # better for desktop
    if command.lower().startswith("play"):
        song=command.lower().split(" ")[1]
        link=musiclibrary.music[song]
        webbrowser.open(link)
    else:
        speak("Sorry, I didn't understand the command.")

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        try:
            with sr.Microphone() as source:
                print("listening.......")
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)
                word= recognizer.recognize_google(audio)

            if "jarvis" in word.lower():
                speak("yeah")
                with sr.Microphone() as source:
                    print("jarvis active.......")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                    command = recognizer.recognize_google(audio)
                    processCommand(command)

        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
        except Exception as e:
            print(f"Error: {e}")



