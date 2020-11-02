import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=5 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
            speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Hello sir. How may I help you?")
    
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listenting...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recongnizing...")
        query = r.recognize_google(audio, language='en-in')
        print("user said:", query)
        speak("you said")
        speak(query)

    except Exception as e:
        print("say that again please..")
        return "none"
    return query
if __name__ == "__main__":
    wishMe()
takecommand()

    
