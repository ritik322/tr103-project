import pyttsx3
import datetime
import requests
import speech_recognition as sr
import pyautogui
from bs4 import BeautifulSoup
import os
import random
import webbrowser
from time import sleep

from SearchNow import reSearchYoutube, reSearchGoogle, searchGoogle, searchYoutube, searchWikipedia
from GreetMe import greetMe
from Dictapp import closeappweb, openappweb
from NewsRead import latestnews
from Calculatenumbers import Calc
from Whatsapp import sendMessage
from keyboard import volumeup, volumedown



engine = pyttsx3.init("sapi5")
engine.setProperty("voice", engine.getProperty("voices")[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)
    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
        return query.lower()
    except:
        print("Say that again")
        return "none"


def action_sleep():
    speak("Ok sir, You can call me anytime")
    exit()

def action_screenshot():
    im = pyautogui.screenshot()
    im.save("ss.jpg")
    speak("Screenshot taken")

def action_click_photo():
    pyautogui.press("super")
    pyautogui.typewrite("camera")
    pyautogui.press("enter")
    sleep(2)
    speak("SMILE")
    pyautogui.press("enter")

def action_hello():
    speak("Hello sir, how are you?")

def action_fine():
    speak("That's great, sir")

def action_how_are_you():
    speak("Perfect, sir")

def action_thanks():
    speak("You are welcome, sir")

def action_tired():
    speak("Playing your favourite songs, sir")
    songs = [
        "https://www.youtube.com/watch?v=n_FCrCQ6-bA",
        "https://www.youtube.com/watch?v=seEO3--Sy3c"
    ]
    webbrowser.open(random.choice(songs))

def action_pause():
    pyautogui.press("k")
    speak("Video paused")

def action_play():
    pyautogui.press("k")
    speak("Video played")

def action_mute():
    pyautogui.press("m")
    speak("Video muted")

def action_unmute():
    pyautogui.press("m")
    speak("Video unmuted")

def action_research_youtube():
    reSearchYoutube()

def action_research_google():
    reSearchGoogle()

def action_volume_up():
    speak("Turning volume up, sir")
    volumeup()

def action_volume_down():
    speak("Turning volume down, sir")
    volumedown()

def action_close_app(query):
    closeappweb(query)

def action_open_app(query):
    openappweb(query)

def action_google(query):
    searchGoogle(query)

def action_youtube(query):
    searchYoutube(query)

def action_wikipedia(query):
    searchWikipedia(query)

def action_news():
    latestnews()

def action_calculate(query):
    q = query.replace("calculate", "").strip()
    Calc(q)

def action_whatsapp():
    sendMessage()

def action_temperature():
    city = "Ludhiana"
    url = f"https://wttr.in/{city}?format=%t"
    temp = requests.get(url).text.strip()
    speak(f"The current temperature in {city} is {temp}")

def action_weather():
    search = "temperature in delhi"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find("div", class_="BNeawe").text
    speak(f"Current {search} is {temp}")

def action_time():
    strTime = datetime.datetime.now().strftime("%H:%M")
    speak(f"Sir, the time is {strTime}")

def action_reset_memory():
    if os.path.exists("Remember.txt"):
        os.remove("Remember.txt")
        speak("I have reset what I remember")
    else:
        speak("There is nothing to reset")

def action_remember(query):
    msg = query.replace("remember that", "").strip()
    speak("You told me to " + msg)
    with open("Remember.txt", "a") as f:
        f.write(msg + "\n")

def action_show_memory():
    if os.path.exists("Remember.txt"):
        with open("Remember.txt", "r") as f:
            speak("You told me to " + f.read())
    else:
        speak("I don't remember anything yet")

def action_shutdown():
    speak("Are you sure you want to shutdown?")
    shutdown = input("Do you wish to shutdown your computer? (yes/no): ")
    if shutdown == "yes":
        os.system("shutdown /s /t 1")


COMMAND_MAP = {
    "go to sleep": action_sleep,
    "screenshot": action_screenshot,
    "click my photo": action_click_photo,
    "hello": action_hello,
    "i am fine": action_fine,
    "how are you": action_how_are_you,
    "thank you": action_thanks,
    "tired": action_tired,
    "pause": action_pause,
    "play": action_play,
    "replay": action_play,
    "mute": action_mute,
    "unmute": action_unmute,
    "research": action_research_youtube,
    "search": action_research_google,
    "volume up": action_volume_up,
    "volume down": action_volume_down,
    "close": action_close_app,
    "open": action_open_app,
    "google": action_google,
    "youtube": action_youtube,
    "wikipedia": action_wikipedia,
    "news": action_news,
    "calculate": action_calculate,
    "whatsapp": action_whatsapp,
    "temperature": action_temperature,
    "weather": action_weather,
    "the time": action_time,
    "reset remember": action_reset_memory,
    "remember that": action_remember,
    "what do you remember": action_show_memory,
    "shut down my pc": action_shutdown,
}


def handle_command(query):
    for key, func in COMMAND_MAP.items():
        if key in query:                    
            if "open" in key or "close" in key or "google" in key or "youtube" in key or "wikipedia" in key or "calculate" in key:
                func(query)               
            else:
                func()                    
            return True
    return False


if __name__ == "__main__":
    greetMe()
    while True:
        q = takeCommand()
        handle_command(q)
