import speech_recognition as sr
import os
import webbrowser
import pyttsx3
import openai
import datetime

openai.api_key = 'Not giving my Own Api Key to Public'

chatStr = ""

def chat(query):
    global chatStr
    chatStr += f"Souvik: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-004",  # Updated model name
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    try:
        response_text = response["choices"][0]["text"]
        say(response_text)
        chatStr += f"{response_text}\n"
        return response_text
    except Exception as e:
        print(f"Error during API response: {e}")
        return "Some error occurred. Sorry from Jarvis"

def ai(prompt):
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"
    response = openai.Completion.create(
        model="text-davinci-004",  # Updated model name
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    try:
        response_text = response["choices"][0]["text"]
        text += response_text
        if not os.path.exists("Openai"):
            os.mkdir("Openai")
        with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
            f.write(text)
    except Exception as e:
        print(f"Error during API response: {e}")

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Listening...")
            audio = r.listen(source)
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I did not understand.")
            return ""
        except sr.RequestError as e:
            print(f"Error with the speech recognition service: {e}")
            return "Some error occurred. Sorry from Jarvis"

if __name__ == '__main__':
    print('Welcome to Jarvis A.I')
    say("Jarvis A.I")
    while True:
        if chatStr=="exit":
            break
