import speech_recognition as sr
import os
import webbrowser
import pyttsx3
import openai
import datetime

# Replace with your actual OpenAI API Key
openai.api_key = "your-api-key-here"

chat_history = ""
nameA = "Jarvis"
user_name = "User"

# Initialize TTS engine once
engine = pyttsx3.init()


def say(text):
    engine.say(text)
    engine.runAndWait()


def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 6:
        print("Good Night Sir")
        say("Good Night Sir")
    elif 6 <= hour < 12:
        print("Good Morning Sir")
        say("Good Morning Sir")
    elif 12 <= hour < 17:
        print("Good Afternoon Sir")
        say("Good Afternoon Sir")
    else:
        print("Good Evening Sir")
        say("Good Evening Sir")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = r.listen(source)
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I did not understand.")
            return ""
        except sr.RequestError as e:
            print(f"Speech Recognition error: {e}")
            return ""


def chat_with_jarvis(query):
    global chat_history
    chat_history += f"{user_name}: {query}\n{nameA}: "

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant named Jarvis."},
                {"role": "user", "content": query}
            ],
            temperature=0.7,
            max_tokens=256
        )
        reply = response['choices'][0]['message']['content']
        chat_history += f"{reply}\n"
        print(f"{nameA}: {reply}")
        say(reply)
        return reply
    except Exception as e:
        print(f"Error during OpenAI response: {e}")
        return "Some error occurred. Sorry from Jarvis."


def ai_file_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=256
        )
        response_text = response['choices'][0]['message']['content']
        if not os.path.exists("Openai"):
            os.mkdir("Openai")
        filename = prompt.strip().replace(" ", "_")[:20]
        with open(f"Openai/{filename}.txt", "w") as f:
            f.write(response_text)
    except Exception as e:
        print(f"Error saving response: {e}")


def calculate():
    opt = input("Choose operation [+ - * /]: ").strip()
    count = int(input("How many numbers? "))
    if count < 1:
        print("Invalid count.")
        return

    result = float(input("Enter number: "))
    for _ in range(count - 1):
        n = float(input("Enter next number: "))
        if opt == '+':
            result += n
        elif opt == '-':
            result -= n
        elif opt == '*':
            result *= n
        elif opt == '/':
            if n != 0:
                result /= n
            else:
                print("Cannot divide by zero.")
                return
    print("Result:", result)
    say(f"The result is {result}")


def main():
    global nameA, user_name
    print("Welcome to Jarvis A.I")
    say("Jarvis A.I activated.")
    wish_me()

    while True:
        query = input("Enter your command (or 'exit' to quit): ").lower().strip()

        if 'exit' in query:
            print("Thanks for using Jarvis.")
            say("Goodbye Sir")
            break
        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")
        elif 'open google' in query:
            webbrowser.open("https://google.com")
        elif 'show photos' in query:
            photos_dir='C:\\Users\\Admin\\Desktop\\Images'
            if os.path.exists(photos_dir):
                pics = os.listdir(photos_dir)
                for i, photo in enumerate(pics):
                    print(f"{i}: {photo}")
                try:
                    choice = int(input("Enter the photo number to open: "))
                    os.startfile(os.path.join(photos_dir, pics[choice]))
                except Exception as e:
                    print("Invalid selection or file open error.")
            else:
                print("Pictures folder not found.")
        elif 'time' in query:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Current time: {now}")
            say(f"The time is {now}")
        elif 'date' in query:
            today = datetime.date.today()
            print(f"Today's date: {today}")
            say(f"Today is {today}")
        elif 'open chrome' in query:
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            if os.path.exists(chrome_path):
                os.startfile(chrome_path)
            else:
                print("Chrome not found.")
        elif 'open cmd' in query:
            os.system("start cmd")
        elif 'what is your name' in query:
            print(f"My name is {nameA}.")
            say(f"My name is {nameA}")
        elif 'who is your creator' in query:
            creator_info = "I was created by Mr. Owner using Python."
            print(creator_info)
            say(creator_info)
        elif 'change your name' in query:
            nameA = input("What should be my new name? ")
            print("Name changed successfully.")
            say(f"My new name is {nameA}")
        elif 'change my name' in query or 'add my name' in query:
            user_name = input("What should I call you? ")
            print("Name saved successfully.")
            say(f"Okay, I will call you {user_name}")
        elif 'calculate' in query:
            calculate()
        else:
            chat_with_jarvis(query)


if __name__ == "__main__":
    main()
