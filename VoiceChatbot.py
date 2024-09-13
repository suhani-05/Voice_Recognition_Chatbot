import speech_recognition as sr
import pyttsx3

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set up speech recognition function
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return "I didn't catch that."
        except sr.RequestError:
            print("Sorry, there was an issue with the request.")
            return "Request error."

# Text-to-speech function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Simple rule-based chatbot logic
def chatbot_response(user_input):
    user_input = user_input.lower()
    
    if "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a chatbot, but I'm functioning well!"
    elif "What is the weather today" in user_input:
        return "It's cloudy!"
    elif "exit" in user_input:
        return "Goodbye! Have a great day!"
    # elif "what is your favorite food" in user_input:
    #     return "I don't eat, but I imagine pizza is a great choice!"
    else:
        return "I'm sorry, I don't have a response for that."

# Main loop to interact with the voice-enabled chatbot
if __name__ == "__main__":
    while True:
        print("Please speak:")
        user_text = recognize_speech()  # Get voice input
        if user_text == "exit":
            speak("Goodbye! Have a great day!")
            break
        
        response = chatbot_response(user_text)  # Get chatbot response
        print(f"Bot: {response}")
        speak(response)  # Speak chatbot response
