import speech_recognition as sr
import pyttsx3
import webbrowser

# Initialize the speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Define the voice assistant function
def voice_assistant():
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)

        try:
            # Use the speech recognition library to convert speech to text
            query = recognizer.recognize_google(audio)
            print("You said:", query)

            # Check for keywords in the user's query
            if "reminder" in query:
                # Extract the reminder details from the query and set the reminder
                reminder_text = query.replace("reminder", "").strip()
                set_reminder(reminder_text)

            elif "to-do list" in query:
                # Extract the task details from the query and add it to the to-do list
                task_text = query.replace("to-do list", "").strip()
                add_to_do(task_text)

            elif "search" in query:
                # Extract the search query from the user's query
                search_query = query.replace("search", "").strip()

                # Open the web browser and perform the search
                search_web(search_query)

            elif "exit" in query:
                # Exit the voice assistant if the user says "exit"
                print("Goodbye!")
                break

        except sr.UnknownValueError:
            print("Sorry, I didn't understand that. Please try again.")
        except sr.RequestError:
            print("Sorry, my speech service is currently unavailable. Please try again later.")

# Function to set a reminder
def set_reminder(text):
    # Implement the code to set a reminder based on the provided text
    print("Setting reminder:", text)

# Function to add a task to the to-do list
def add_to_do(text):
    # Implement the code to add the provided text as a task to the to-do list
    print("Adding to-do task:", text)

# Function to search the web
def search_web(query):
    # Open the web browser and perform the search
    webbrowser.open_new_tab(f"https://www.google.com/search?q={query}")

# Run the voice assistant
voice_assistant()
