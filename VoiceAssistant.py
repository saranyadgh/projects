import speech_recognition as sr
import pyttsx3
from datetime import datetime
import time
import wikipedia

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for a command from the user with a 5-second timeout."""
    with sr.Microphone() as source:
        print("Listening for a command...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            print("Recognizing speech...")
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
        except sr.WaitTimeoutError:
            speak("Listening timed out.")
        return None

def respond(command):
    """Respond to user commands within 3 seconds."""
    start_response_time = time.time()

    if "hello" in command:
        current_hour = datetime.now().hour
        if 5 <= current_hour < 12:
            response = "Good morning!"
        elif 12 <= current_hour < 18:
            response = "Good afternoon!"
        else:
            response = "Good evening!"
        speak(response)
    elif "time" in command:
        current_time = datetime.now().strftime("%H:%M:%S")
        response = f"The current time is {current_time}"
        speak(response)
    elif "date" in command:
        current_date = datetime.now().strftime("%Y-%m-%d")
        response = f"Today's date is {current_date}"
        speak(response)
    elif "wikipedia" in command:
        speak("What do you want to search for?")
        search_query = listen()
        if search_query:
            try:
                summary = wikipedia.summary(search_query, sentences=2)
                response = f"According to Wikipedia, {summary}"
                speak(response)
            except wikipedia.exceptions.DisambiguationError as e:
                speak(f"Multiple results found for {search_query}. Please be more specific.")
            except wikipedia.exceptions.PageError:
                speak(f"Sorry, I could not find any information on {search_query}.")
    else:
        response = "Sorry, I can only respond to 'hello', 'time', 'date', and 'search' commands."
        speak(response)

    end_response_time = time.time()
    total_response_time = end_response_time - start_response_time

    if total_response_time > 5:
        speak("Sorry, I took too long to respond.")

def introduce():
    """Introduce the voice assistant."""
    intro = "Hello, I am Kitty, your voice assistant. How can I help you today?"
    speak(intro)

def main():
    introduce()
    while True:
        command = listen()
        if command:
            if "ok bye" in command:
                speak("Ok! Bye")
                break
            respond(command)

if __name__ == "__main__":
    main()
