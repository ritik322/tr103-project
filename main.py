import pyttsx3
import datetime
import requests
import speech_recognition 
import pyautogui
from bs4 import BeautifulSoup
import os
import random
import webbrowser
from SearchNow import reSearchYoutube, reSearchGoogle
from time import sleep

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

if __name__ == "__main__":
    from GreetMe import greetMe
    greetMe()
    while True:
        query = takeCommand().lower()
        if "go to sleep" in query:
            speak("Ok sir, You can call me anytime")
            break 
        
        elif "screenshot" in query:
            im = pyautogui.screenshot()
            im.save("ss.jpg")
            speak("Screenshot taken")
            
        elif "click my photo" in query:
            pyautogui.press("super")
            pyautogui.typewrite("camera")
            pyautogui.press("enter")
            sleep(2)
            speak("SMILE")
            pyautogui.press("enter")

        elif "hello" in query:
            speak("Hello sir, how are you?")
        elif "i am fine" in query:
            speak("That's great, sir")
        elif "how are you" in query:
            speak("Perfect, sir")
        elif "thank you" in query:
            speak("You are welcome, sir")
        elif "tired" in query:
            speak("Playing your favourite songs, sir")
            songs = [
                "https://www.youtube.com/watch?v=n_FCrCQ6-bA&pp=ygUPc2lkaHUgbXVzZSB3YWxh",
                "https://www.youtube.com/watch?v=seEO3--Sy3c&pp=ygUPc2lkaHUgbXVzZSB3YWxh"
            ]
            webbrowser.open(random.choice(songs))
    
        elif "pause" in query:
            pyautogui.press("k")
            speak("Video paused")
        elif "play" in query or "replay" in query:
            pyautogui.press("k")
            speak("Video played")
        elif "mute" in query:
            pyautogui.press("m")
            speak("Video muted")
        elif "unmute" in query:
            pyautogui.press("m")
            speak("Video unmuted")
        elif "research" in query:
            reSearchYoutube()
        elif "search" in query:
            reSearchGoogle()
        elif "volume up" in query:
            from keyboard import volumeup
            speak("Turning volume up, sir")
            volumeup()
        elif "volume down" in query:
            from keyboard import volumedown
            speak("Turning volume down, sir")
            volumedown()
        elif "close" in query:
            from Dictapp import closeappweb
            closeappweb(query)
        elif "open" in query:
            from Dictapp import openappweb
            openappweb(query)
        elif "google" in query:
            from SearchNow import searchGoogle
            searchGoogle(query)
        elif "youtube" in query:
            from SearchNow import searchYoutube
            searchYoutube(query)
        elif "wikipedia" in query:
            from SearchNow import searchWikipedia
            searchWikipedia(query)
            
        elif "news" in query:
            from NewsRead import latestnews
            latestnews()
            
        elif "calculate" in query:
            from Calculatenumbers import Calc
            query = query.replace("calculate", "").replace("jarvis", "").strip()
            Calc(query)
            
        elif "whatsapp" in query:
            from Whatsapp import sendMessage
            sendMessage()
            
        elif "temperature" in query:
            city = "Ludhiana"
            url = f"https://wttr.in/{city}?format=%t"
            try:
                temp = requests.get(url).text.strip()
                speak(f"The current temperature in {city} is {temp}")
                print(f"The current temperature in {city} is {temp}")
            except:
                speak("Sorry, I could not fetch the weather right now.")
                
        elif "weather" in query:
            search = "temperature in delhi"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"Current {search} is {temp}")
            
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")    
            speak(f"Sir, the time is {strTime}")
            
        elif "sleep" in query:
            speak("Going to sleep, sir")
            exit()
            
        elif "reset remember" in query:
            if os.path.exists("Remember.txt"):
                os.remove("Remember.txt") 
                speak("I have reset what I remember")
            else:
                speak("There is nothing to reset")
                    
        elif "remember that" in query:
            rememberMessage = query.replace("remember that", "").replace("jarvis", "").strip()
            speak("You told me to " + rememberMessage)
            with open("Remember.txt", "a") as remember:
                remember.write(rememberMessage + "\n")

        elif "what do you remember" in query:
            if os.path.exists("Remember.txt"):
                with open("Remember.txt", "r") as remember:
                    content = remember.read()
                    speak("You told me to " + content)
            else:
                speak("I don't remember anything yet")
        
        elif "shut down my pc" in query:
            speak("Are you sure you want to shutdown")
            shutdown = input("Do you wish to shutdown your computer? (yes/no): ")
            if shutdown == "yes":
                os.system("shutdown /s /t 1")
            elif shutdown == "no":
                break