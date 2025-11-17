import os 
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dictapp = {
    "commandprompt": "cmd",
    "paint": "paint",
    "word": "winword",
    "excel": "excel",
    "chrome": "chrome",
    "vscode": "code",
    "powerpoint": "powerpnt"
}

def openappweb(query):
    speak("Launching, sir")
    query = query.replace("open", "").replace("jarvis", "").replace("launch", "").strip()
    
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace(" ", "")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        found = False
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")
                found = True
                break
        
        if not found:
            pyautogui.press("super")
            sleep(0.5)
            pyautogui.typewrite(query)
            sleep(0.5)
            pyautogui.press("enter")

def closeappweb(query):
    speak("Closing, sir")
    
    tab_counts = {
        "one tab": 1,
        "two tab": 2,
        "three tab": 3,
        "four tab": 4,
        "five tab": 5
    }
    
    for phrase, count in tab_counts.items():
        if phrase in query:
            for i in range(count):
                pyautogui.hotkey("ctrl", "w")
                if i < count - 1:
                    sleep(0.5)
            speak("All tabs closed")
            return
    
    if "close all tab" in query.lower():
        pyautogui.hotkey("alt", "f4")
        speak("All tabs closed")
    else:
        for app in dictapp.keys():
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")
                break