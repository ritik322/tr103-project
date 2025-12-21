import pyttsx3

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 
engine.setProperty('rate', 180) 

def say(text):
    print(f"AI: {text}") 
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    say("System is now using the offline engine.")