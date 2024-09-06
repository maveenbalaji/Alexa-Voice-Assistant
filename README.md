Here’s a detailed README for your Alexa-like virtual assistant project:

---

# Alexa Voice Assistant

**Overview**

This project is a simple Python-based voice assistant inspired by Amazon Alexa. It listens to user commands through the microphone, processes them using speech recognition, and responds with appropriate actions like playing songs, telling the time, searching for information on Wikipedia, sending WhatsApp messages, telling jokes, and more. The assistant uses various Python libraries to perform these tasks and respond to the user via speech.

## Features

- **Voice Commands**: Listens to commands like "play," "time," "search for," and responds accordingly.
- **Music Playback**: Play songs directly from YouTube.
- **Real-Time Information**: Provides current time, searches Wikipedia for quick information, and tells jokes.
- **Automation**: Can send WhatsApp messages via `pywhatkit`.
- **Jokes**: Provides fun jokes using the `pyjokes` library.
- **Control Volume**: Can adjust system volume using `pyautogui`.
- **Custom Responses**: Responds to phrases like "are you single" or "who are you" with custom dialogue.

## Tech Stack

- **Python**: The programming language used to develop the assistant.
- **Libraries Used**:
  - `speech_recognition`: For converting speech to text.
  - `pyttsx3`: For text-to-speech conversion.
  - `pywhatkit`: For playing YouTube songs and sending WhatsApp messages.
  - `datetime`: For getting the current time.
  - `wikipedia`: For retrieving information from Wikipedia.
  - `pyjokes`: For telling jokes.
  - `pyautogui`: For controlling system volume and other keyboard interactions.

## How It Works

1. **Speech Recognition**:
   - The assistant uses the `speech_recognition` library to listen for the "Alexa" keyword, and then processes commands.
   
2. **Text-to-Speech**:
   - The `pyttsx3` library is used to respond to commands through voice output.

3. **Command Handling**:
   - The assistant recognizes various commands:
     - **"Play [song]"**: Plays the specified song on YouTube.
     - **"Time"**: Tells the current time.
     - **"Search for [person/topic]"**: Provides a summary from Wikipedia.
     - **"Tell me a joke"**: Responds with a joke using `pyjokes`.
     - **"Send WhatsApp message"**: Sends a WhatsApp message to a specified number.

4. **Volume Control**:
   - Commands like "increase the volume" are executed using the `pyautogui` library, which interacts with the system volume controls.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/maveenbalaji/alexa-voice-assistant.git
   ```

2. Install dependencies:
   ```bash
   pip install speechrecognition pyttsx3 pywhatkit wikipedia pyjokes pyautogui
   ```

3. Set up microphone permissions and make sure your system can access audio input and output.

4. Run the script:
   ```bash
   python alexa_assistant.py
   ```

## Usage

1. **Initiate Voice Command**:
   - Run the Python script and say "Alexa" followed by a command. For example:
     - "Alexa, play Shape of You."
     - "Alexa, what time is it?"
     - "Alexa, search for Albert Einstein."
     - "Alexa, tell me a joke."

2. **WhatsApp Messaging**:
   - To send a WhatsApp message:
     - Say "Alexa, send WhatsApp message."
     - Follow the prompts to enter the phone number, message, and the time for sending.

3. **Control Volume**:
   - Say "Alexa, increase the volume" to increase the system volume.

4. **Exit**:
   - Say "Alexa, exit" to terminate the assistant.

## Future Improvements

- **Natural Language Processing**: Integrate NLP to make the assistant more conversational and understand more complex commands.
- **Voice Feedback Improvements**: Improve the speech recognition accuracy and response speed.
- **More Command Integration**: Add more features like controlling smart home devices, reading news, or integrating with other APIs.
