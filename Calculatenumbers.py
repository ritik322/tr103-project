import wolframalpha
import pyttsx3
import speech_recognition

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WolfRamAlpha(query):
    apikey = "VHLP9H-XYALLL3QUX"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("The value is not answerable")
        return None

def Calc(query):
    term = str(query)
    term = term.replace("jarvis", "")
    term = term.replace("multiply", "*")
    term = term.replace("plus", "+")
    term = term.replace("minus", "-")
    term = term.replace("divide", "/")
    term = term.strip()

    try:
        result = WolfRamAlpha(term)
        if result:
            print(f"{result}")
            speak(result)
    except:
        speak("The value is not answerable")