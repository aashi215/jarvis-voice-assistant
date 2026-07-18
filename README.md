# Jarvis Voice Assistant 🎙️

A Python-based voice assistant (inspired by Iron Man's Jarvis) that listens to voice commands, opens websites, tells the time, and chats using OpenAI's GPT models.

## Features

- 🎤 Voice command recognition (via Google Speech Recognition)
- 🔊 Text-to-speech responses (cross-platform, via pyttsx3)
- 🌐 Opens websites like YouTube, Wikipedia, Google on voice command
- 🕐 Tells the current time
- 💬 General conversation powered by OpenAI's chat models
- 🧠 "Using artificial intelligence" command saves AI-generated responses to text files
- 🔄 Reset chat history on command
- 🎵 Opens local music, FaceTime, and other apps (macOS)

## Requirements

- Python 3.11 or 3.12 (pyaudio doesn't have prebuilt wheels for newer versions yet)
- A working microphone
- An OpenAI API key (get one at platform.openai.com/api-keys)

## Setup

1. Clone the repository
```
git clone https://github.com/aashi215/jarvis-voice-assistant.git
cd jarvis-voice-assistant
```

2. Create and activate a virtual environment
```
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
```

3. Install dependencies
```
pip install -r requirements.txt
```

4. Add your API key
```
copy config.py.example config.py
```
Then open config.py and replace the placeholder:
```
apikey = "sk-your-real-key-here"
```

5. Run it
```
python jarvis.py
```

## Voice Commands

- "Open YouTube" / "Open Wikipedia" / "Open Google" → Opens the site in your browser
- "The time" → Tells you the current time
- "Open music" → Plays a local music file (macOS path, edit as needed)
- "Open FaceTime" → Opens FaceTime (macOS only)
- "Using artificial intelligence [your prompt]" → Sends prompt to OpenAI, saves response to Openai/ folder
- "Reset chat" → Clears conversation history
- "Jarvis quit" → Exits the assistant
- Anything else → Chats with you via GPT

## Notes

- config.py is git-ignored — never commit your real API key.
- The music/FaceTime/Passky commands use hardcoded macOS paths — edit these in jarvis.py if you're on Windows or Linux.
- Speech recognition requires an internet connection (it uses Google's API under the hood).

## Troubleshooting

**pyaudio fails to install:**
Make sure you're using Python 3.11 or 3.12, not a very new version like 3.14 — prebuilt wheels may not exist yet for the latest release.

**"python.exe not recognized":**
Make sure your virtual environment is activated ((.venv) should show in your terminal prompt) before installing or running anything.

## License

This project is open source and available for personal/educational use.
