import speech_recognition as sr
import os
import re
import webbrowser
import datetime
import pyttsx3
from openai import OpenAI
from config import apikey

# https://youtu.be/Z3ZAJoi4x6Q

client = OpenAI(api_key=apikey)
chatStr = ""

tts_engine = pyttsx3.init()


def say(text):
    """Cross-platform text-to-speech (works on macOS/Windows/Linux)."""
    print(f"Jarvis: {text}")
    try:
        tts_engine.say(text)
        tts_engine.runAndWait()
    except Exception as e:
        print(f"[TTS error: {e}]")


def chat(query):
    global chatStr
    chatStr += f"Harry: {query}\nJarvis: "
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are Jarvis, a helpful voice assistant."},
                {"role": "user", "content": chatStr},
            ],
            temperature=0.7,
            max_tokens=256,
        )
        reply = response.choices[0].message.content.strip()
    except Exception as e:
        reply = f"Sorry, I hit an error talking to OpenAI: {e}"

    say(reply)
    chatStr += f"{reply}\n"
    return reply


def ai(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=256,
        )
        answer = response.choices[0].message.content.strip()
    except Exception as e:
        say(f"Sorry, I hit an error: {e}")
        return

    text = f"OpenAI response for Prompt: {prompt}\n*************************\n\n{answer}"

    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # Build a safe filename instead of assuming "intelligence" is in the prompt
    raw_name = prompt.split("intelligence")[-1].strip() or "response"
    safe_name = re.sub(r'[\\/*?:"<>|]', "_", raw_name)[:80]

    with open(f"Openai/{safe_name}.txt", "w") as f:
        f.write(text)

    say("I've saved that response for you, sir.")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception:
            return "Some Error Occurred. Sorry from Jarvis"


if __name__ == "__main__":
    print("Welcome to Jarvis A.I")
    say("Jarvis A.I, at your service.")

    sites = [
        ["youtube", "https://www.youtube.com"],
        ["wikipedia", "https://www.wikipedia.com"],
        ["google", "https://www.google.com"],
    ]

    while True:
        query = takeCommand()
        query_lower = query.lower()

        matched = False
        for name, url in sites:
            if f"open {name}" in query_lower:
                say(f"Opening {name} sir...")
                webbrowser.open(url)
                matched = True

        if matched:
            continue

        if "open music" in query_lower:
            musicPath = "/Users/harry/Downloads/downfall-21371.mp3"
            os.system(f'open "{musicPath}"')  # macOS only; use "start" on Windows, "xdg-open" on Linux

        elif "the time" in query_lower:
            hour = datetime.datetime.now().strftime("%H")
            minute = datetime.datetime.now().strftime("%M")
            say(f"Sir, time is {hour} bajke {minute} minutes")

        elif "open facetime" in query_lower:
            os.system("open /System/Applications/FaceTime.app")

        elif "open pass" in query_lower:
            os.system("open /Applications/Passky.app")

        elif "using artificial intelligence" in query_lower:
            ai(prompt=query)

        elif "jarvis quit" in query_lower:
            say("Goodbye, sir.")
            exit()

        elif "reset chat" in query_lower:
            chatStr = ""
            say("Chat history cleared.")

        else:
            print("Chatting...")
            chat(query)
