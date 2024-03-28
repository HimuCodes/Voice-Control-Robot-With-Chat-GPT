# Voice Control Robot with ChatGPT Assistant

This project combines the power of Arduino (Wi-Fi enabled) and Python to create a versatile voice-controlled robot assistant leveraging the OpenAI ChatGPT API. While actual robot control isn't implemented here (focusing on voice interaction and ChatGPT communication), it serves as a foundation for exciting possibilities.

**Project Structure:**

* **Arduino Code (main.ino):**
   - Connects to a Wi-Fi network for internet access.
   - Interacts with the ChatGPT API using a dedicated library (`ChatGPT.hpp`).
   - Demonstrates sending text messages to ChatGPT and receiving JSON responses.
* **Python Code (voice_assistant.py):** (Optional)
   - Enables voice control functionality on a separate device (e.g., Raspberry Pi).
   - Uses speech recognition to capture user commands.
   - Provides functionalities like setting reminders, managing a to-do list, and web search using the browser.

**Hardware (for Arduino Part):**

* Arduino board (any model with Wi-Fi capabilities)

**Software:**

**For Arduino Code:**

* Arduino IDE ([https://www.arduino.cc/en/software](https://www.arduino.cc/en/software))
* ArduinoJson library ([https://arduinojson.org/](https://arduinojson.org/))
* ArduinoBearSSL library ([invalid URL removed]) (optional, for secure communication)
* ChatGPT library (`ChatGPT.hpp`) (download or implement your own)

**For Python Code (Optional):**

* Python 3.x ([https://www.python.org/downloads/](https://www.python.org/downloads/))
* SpeechRecognition library (`pip install SpeechRecognition`)
* PyTextToSpeech library (`pip install pyttsx3`)
* webbrowser library (included in standard library)

**Getting Started (Arduino Part):**

1. **Install Libraries:**
   Open the Arduino IDE, go to Sketch > Include Library > Manage Libraries. Install the required libraries: ArduinoJson (if not already installed) and ArduinoBearSSL (if desired). You'll need to find and install the `ChatGPT.hpp` library separately.

2. **Replace Placeholders:**
   In the Arduino code (`main.ino`), update the following with your credentials:
     - `<WIFI_SSID>`: Your Wi-Fi network name (SSID)
     - `<WIFI_PW>`: Your Wi-Fi network password
     - `<OpenAI_API_KEY>`: Your OpenAI API key (create a free account at [https://openai.com/](https://openai.com/))

3. **Upload the Code:**
   Connect your Arduino board, select the correct board and port, and upload the code using the Arduino IDE.

4. **Verify Connection:**
   Open the serial monitor (usually at 115200 baud) in the Arduino IDE. Upon successful Wi-Fi connection, you should see a "Connected!" message.

**Understanding the Arduino Code:**

- **WiFi Connection:**
   The code establishes a connection to your Wi-Fi network using the provided credentials, allowing the Arduino to access the internet and communicate with the ChatGPT API.

- **OpenAI API Setup:**
   - The code initializes the ChatGPT object using the BearSSL client for secure communication (optional). This library helps encrypt the communication with the OpenAI API, enhancing security.
   - Disabling Server Name Indication (SNI) is included for testing purposes only. In production environments, it's crucial to remove this line to ensure secure communication.

**ChatGPT Messages:**

The code demonstrates sending basic messages to ChatGPT and printing the JSON response:

```c++
String result;

// Send a simple message, extracting only the content part of the response
Serial.println("[ChatGPT] Only print a content message");
if (chat_gpt.simple_message("gpt-3.5-turbo-0301", "user", "Planning a 3-day trip to San Diego", result)) {
  Serial.println("===OK===");
  Serial.println(result);
} else {
  Serial.println("===ERROR===");
  Serial.println(result);
}

// Send a full message request, printing the entire JSON response
Serial.println("\n\n[ChatGPT] Print full message(JSON Type)");
if (chat_gpt.full_message("gpt-3.5-turbo", "user", "What is the OpenAI mission?", result)) {
  Serial.println("===OK");
    Serial.println(result);
  } else {
    Serial.println("===ERROR===");
    Serial.println(result);
  }
```
**Understanding the Python Code:**

**1. Import Statements:**

- **SpeechRecognition:** Enables speech-to-text conversion for recognizing user commands.
- **pyttsx3:** Facilitates text-to-speech for providing audible responses.
- **webbrowser:** Opens web pages for conducting web searches.

**2. Initializing Engines:**

- **recognizer = sr.Recognizer():** Creates a speech recognizer instance for audio processing.
- **engine = pyttsx3.init():** Initializes the text-to-speech engine for voice output.

**3. Voice Assistant Function:**

- **voice_assistant():** Encapsulates the main voice interaction loop:
   - **while True:** Continuously listens for user commands.
   - **with sr.Microphone() as source:** Uses the microphone for audio input.
   - **print("Listening..."):** Provides visual feedback to the user.
   - **audio = recognizer.listen(source):** Records audio from the microphone.
   - **try...except:** Handles potential errors during speech recognition or API calls:
     - **query = recognizer.recognize_google(audio):** Sends audio to Google's speech-to-text API for transcription.
     - **print("You said:", query):** Displays the recognized query for confirmation.
     - **if "reminder"...elif "to-do list"...elif "search"...elif "exit":** Identifies keywords in the query to trigger specific actions.
     - **set_reminder(reminder_text):** Calls a placeholder function for setting reminders (details not yet implemented).
     - **add_to_do(task_text):** Calls a placeholder function for adding tasks to a to-do list (not yet implemented).
     - **search_web(search_query):** Opens a web browser with the specified search query.
     - **print("Goodbye!"):** Exits the assistant when the user says "exit".
   - **sr.UnknownValueError:** Handles errors when the speech recognizer fails to understand the audio.
   - **sr.RequestError:** Catches errors related to communication with the speech recognition API.

**4. Placeholder Functions:**

- **set_reminder(text):** Currently prints a placeholder message; requires implementation for actual reminder functionality.
- **add_to_do(text):** Currently prints a placeholder message; needs implementation for task management.
- **search_web(query):** Uses `webbrowser.open_new_tab()` to perform a web search using Google.

**5. Running the Assistant:**

- **voice_assistant():** Calls the main function to initiate the voice assistant.
