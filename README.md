# Jarvis A.I - Voice Assistant using Python and OpenAI

Jarvis is a customizable voice assistant built with Python, OpenAI's GPT API, and local system tools. It can respond to voice commands, open websites, manage files, tell the time and date, do calculations, and even chat with users using GPT-based conversation.

## ✨ Features

- 🎤 Voice command input (via microphone)
- 💬 Conversational AI using OpenAI's GPT (ChatGPT)
- 🌐 Opens websites like YouTube, Google, Chrome, etc.
- 🖼️ Shows photos from your Pictures folder
- 📅 Tells date and time
- 🧮 Performs basic arithmetic calculations
- 🗣️ Text-to-speech (TTS) for responses
- 🧠 Stores conversation history for continued context
- 💾 Saves AI responses to files

## 🛠️ Requirements

Install the dependencies using pip:

```bash
pip install openai pyttsx3 SpeechRecognition pyaudio
```
🧠 OpenAI API Key
Replace the following line with your actual OpenAI key:

python
Copy
Edit
openai.api_key = "your-api-key-here"
You can get your API key from OpenAI's website.

🚀 How to Run
Clone this repository or copy the script.

Run the Python file using:

bash
Copy
Edit
python jarvis_ai.py
Interact with Jarvis using either keyboard or voice.

📂 Folder Structure
bash
Copy
Edit
Openai/             # Contains AI response text files
Pictures/           # Generic image directory used to display photos
jarvis_ai.py        # Main assistant script
README.md           # This file
⚠️ Disclaimer
This project is a personal AI assistant prototype. It is intended for educational or experimental use only.
