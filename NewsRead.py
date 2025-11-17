import requests
import json
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def latestnews():
    api_dict = {
        "business": "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=39c8a2d150fc4f55973e185c65e0eaba",
        "entertainment": "https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=39c8a2d150fc4f55973e185c65e0eaba",
        "health": "https://newsapi.org/v2/top-headlines?country=us&category=health&apiKey=39c8a2d150fc4f55973e185c65e0eaba",
        "technology": "https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=39c8a2d150fc4f55973e185c65e0eaba",
        "sports": "https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=39c8a2d150fc4f55973e185c65e0eaba"
    }

    speak("Which field news do you want? business, health, technology, sports, entertainment")
    field = input("Type field: ").lower()

    url = api_dict.get(field)

    if url is None:
        print("URL not found for category:", field)
        speak("Sorry, I did not find that category.")
        return

    response = requests.get(url).text
    news = json.loads(response)

    # check for errors
    if "articles" not in news:
        print("API Error:", news)
        speak("Sorry, I could not fetch the news due to an API error.")
        return

    speak("Here are the latest news headlines.")

    for article in news["articles"]:
        title = article.get("title")
        if title:
            print(title)
            speak(title)

        news_url = article.get("url")
        if news_url:
            print(f"More info: {news_url}")

        a = input("[1 to continue] [2 to stop]: ")
        if a == "2":
            break

    speak("That's all.")
