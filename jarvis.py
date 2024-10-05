from time import strftime
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pythoncom

print("Initializing Jarvis")

MASTER = "Boss"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour <12:
        speak("Good Morning" + MASTER)

    elif hour>=12 and hour<18:
        speak("Good Afternoon" + MASTER)
    else:
        speak("Good Evening" + MASTER)


    speak("How may I assist you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language ='en-in')
        print(f"user said: {query}\n")
        
    except Exception as e:
        # print(e)

        print("Sorry i didn't catch that...")
        speak("Sorry i didn't catch that...")
        return "None"
    return query
speak("Initializing Jarvis...")
wishMe()
query = takeCommand().lower()


#Logic

if 'wikipedia' in query.lower():
    speak('Searching wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences =2)
    print(results)
    speak(results)


if 'open youtube' in query.lower():
    webbrowser.open("youtube.com")

if 'open meet' in query.lower():
    webbrowser.open("meet.google.com")    


if 'open google' in query.lower():
    webbrowser.open("google.com") 
   
if 'play music' in query.lower():
    music_dir = 'D:\\mp3'   
    songs = os.listdir(music_dir)
    print(songs)
    os.startfile(os.path.join(music_dir, songs[0]))
if 'the time' in query:
    strTime = datetime.datetime.now().strftime("%H:%M:S")
    speak(f"Sir, the time is {strTime}")

if 'open CCTV' in query.lower():
   webbrowser.open("")
