import datetime
import pyautogui
import webbrowser
import os
import cv2
import pywhatkit
import wikipedia
from time import sleep
from speak import say

sys_apps = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "paint": "mspaint.exe",
    "cmd": "cmd.exe",
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "excel": r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"
}

def execute_intent(intent_tag, user_text):
    if intent_tag == "greeting":
        say("Hello sir! How can I help you?")
        
    elif intent_tag == "goodbye":
        say("Goodbye sir.")

    elif intent_tag == "time":
        strTime = datetime.datetime.now().strftime("%H:%M")
        say(f"The time is {strTime}")

    elif intent_tag == "screenshot":
        say("Taking screenshot...")
        pyautogui.hotkey('win', 'd') 
        sleep(1)
        im = pyautogui.screenshot()
        im.save("screenshot.jpg")
        say("Screenshot saved.")

    elif intent_tag == "camera":
        say("Opening camera sir.")
        cap = cv2.VideoCapture(0)
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            cv2.imshow('Camera - Press SPACE to Click, Q to Exit', frame)
            
            k = cv2.waitKey(1)
            if k % 256 == 32: 
                img_name = "selfie.jpg"
                cv2.imwrite(img_name, frame)
                say("Photo captured successfully")
                break
            elif k % 256 == 113: 
                say("Closing camera without capturing")
                break
                
        cap.release()
        cv2.destroyAllWindows()

    elif intent_tag == "volume_up":
        pyautogui.press("volumeup", presses=5)
        say("Volume up.")

    elif intent_tag == "volume_down":
        pyautogui.press("volumedown", presses=5)
        say("Volume down.")

    elif intent_tag == "mute":
        pyautogui.press("volumemute")
        say("Mute toggled.")

    elif intent_tag == "google":
        query = user_text.replace("search google for", "").replace("search for", "").replace("google", "")
        say(f"Searching for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")

    elif intent_tag == "youtube":
        query = user_text.replace("play on youtube", "").replace("play", "").replace("watch", "")
        say(f"Playing {query} on YouTube")
        pywhatkit.playonyt(query)

    elif intent_tag == "wikipedia":
        query = user_text.replace("who is", "").replace("tell me about", "").replace("what is", "").replace("wikipedia", "")
        say(f"Searching Wikipedia for {query}")
        try:
            results = wikipedia.summary(query, sentences=2)
            say("According to Wikipedia")
            say(results)
        except:
            say("I couldn't find that page.")

    elif intent_tag == "open_app":
        say("Opening application")
        opened = False
        for app in sys_apps:
            if app in user_text:
                os.startfile(sys_apps[app])
                opened = True
                break
        if not opened:
            say("I do not have the path for that application yet.")

    else:
        say("I understood the command, but I am still learning how to do that.")