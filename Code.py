


import datetime
import openai
import requests
from bs4 import BeautifulSoup
import speech_recognition as sr
import pyttsx3
import tkinter as tk
from tkinter import scrolledtext

api_key = "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"  # Your OpenAI API key  

responses = {
     "how are you": "i'm great ! , thanks for asking",
"do you have sisters" : "no sir , i'm the only child of my develpers untill now",
"do you have sisters ?" : "no sir , i'm the only child of my develpers untill now",
"do you have sisters?" : "no sir , i'm the only child of my develpers untill now",
"what's your name": "my name is jarvis , your AI assisstant Sir",
"what is your name ?": "my name is jarvis , your AI assisstant Sir",
"what is your name": "my name is jarvis , your AI assisstant Sir",
"what is your name?": "my name is jarvis , your AI assisstant Sir",
"what's your name?": "my name is jarvis , your AI assisstant Sir",
"what's your name ?": "my name is jarvis , your AI assisstant Sir",
"Thank you": "no need to thank me sir, my only purpose is to help you",
"do you have sisters or brothers": "no sir , i'm the only child of my develpers untill now",
"do you have sisters or brothers ?" : "no sir , i'm the only child of my develpers untill now",
"do you have sisters or brothers?" : "no sir , i'm the only child of my develpers untill now",
"do you have any sisters": "no sir , i'm the only child of my develpers untill now",
"do you have any sisters?": "no sir , i'm the only child of my develpers untill now",
"do you have any sisters ?": "no sir , i'm the only child of my develpers untill now",
"do you have any sisters or brothers": "no sir , i'm the only child of my develpers untill now",
"do you have any sisters or brothers?": "no sir , i'm the only child of my develpers untill now",
"do you have any sisters or brothers ?": "no sir , i'm the only child of my develpers untill now",
"do you have friends ?": "i don't suppose i have ones , i'm lonely as my developers",
"how can i switch between voice mode and type mode ?": "to switch from voice mode to type mode speak 'switch to typing mode', and to switch from the typing mode to voice mode type'switch to voice mode'",
"how can i switch between voice mode and type mode?": "to switch from voice mode to type mode speak 'switch to typing mode', and to switch from the typing mode to voice mode type'switch to voice mode'",
"how can i switch between voice mode and type mode": "to switch from voice mode to type mode speak 'switch to typing mode', and to switch from the typing mode to voice mode type'switch to voice mode'",
"how can i switch to voice mode ?": "to switch from voice mode to type mode speak 'switch to typing mode', and to switch from the typing mode to voice mode type'switch to voice mode'",
"how can i switch to voice mode?": "to switch from voice mode to type mode speak 'switch to typing mode', and to switch from the typing mode to voice mode type'switch to voice mode'",
"how can i switch to voice mode": "to switch from voice mode to type mode speak 'switch to typing mode', and to switch from the typing mode to voice mode type'switch to voice mode'",
"how can i switch to type mode ?": "to switch from voice mode to type mode speak 'switch to typing mode', and to switch from the typing mode to voice mode type'switch to voice mode'",
"how can i switch to type mode?": "to switch from voice mode to type mode speak 'switch to typing mode', and to switch from the typing mode to voice mode type'switch to voice mode'",
"how can i switch to type mode": "to switch from voice mode to type mode speak 'switch to typing mode', and to switch from the typing mode to voice mode type'switch to voice mode'",
"how can i switch to typing mode ?": "to switch from voice mode to type mode speak 'switch to typing mode', and to switch from the typing mode to voice mode type'switch to voice mode'",
"how can i switch to typing mode?": "to switch from voice mode to type mode speak 'switch to typing mode', and to switch from the typing mode to voice mode type'switch to voice mode'",
"how can i switch to typing mode": "to switch from voice mode to type mode speak 'switch to typing mode', and to switch from the typing mode to voice mode type'switch to voice mode'",
"how to switch to typing mode?": "to switch from voice mode to type mode speak 'switch to typing mode', and to switch from the typing mode to voice mode type'switch to voice mode'",
"how to switch to typing mode ?": "to switch from voice mode to type mode speak 'switch to typing mode', and to switch from the typing mode to voice mode type'switch to voice mode'",
"how to switch to typing mode": "to switch from voice mode to type mode speak 'switch to typing mode', and to switch from the typing mode to voice mode type'switch to voice mode'",
"how to switch to type mode?": "to switch from voice mode to type mode speak 'switch to typing mode', and to switch from the typing mode to voice mode type'switch to voice mode'",
"how to switch to type mode ?": "to switch from voice mode to type mode speak 'switch to typing mode', and to switch from the typing mode to voice mode type'switch to voice mode'",
"how to switch to type mode": "to switch from voice mode to type mode speak 'switch to typing mode', and to switch from the typing mode to voice mode type'switch to voice mode'",

"what friends do you have ?": "i don't suppose i have ones , i'm lonely as my developers",
"what friends do you have ": "i don't suppose i have ones , i'm lonely as my developers",
"do you have friends": "i don't suppose i have ones , i'm lonely as my developers",
"what is your purpose": "my only purpose is to assist you sir",
"what's your purpose": "my only purpose is to assist you sir",
"what is your purpose?": "my only purpose is to assist you sir",
"what is your purpose ?": "my only purpose is to assist you sir",
"what's your purpose?": "my only purpose is to assist you sir",
"what's your purpose ?": "my only purpose is to assist you sir",
"who developed you": "i was developed by some students in Engeenering faculty as their project",
"who developed you?": "i was developed by some students in Engeenering faculty as their project",
"who developed you ?": "i was developed by some students in Engeenering faculty as their project",
"what friends do you have?": "i don't suppose i have ones , i'm lonely as my developers",
"how many friends do you have": "i don't suppose i have ones , i'm lonely as my developers",
"what's your name": "my name is jarvis , your AI assisstant is at your service",
"hello": "Hello sir! I'm jarvis at your service",
"hello !": "Hello sir! I'm jarvis at your service",
"hello!": "Hello sir! I'm jarvis at your service",
"hi!": "Hello sir! I'm jarvis at your service",
"hi !": "Hello sir! I'm jarvis at your service",
"hi": "Hello sir! I'm jarvis at your service",
"how are you": "I'm just a computer program, so I don't have feelings, but I'm here to help.",
"tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
"it was very bad joke": "sorry , i have the same sense of humor as my programmers , don't blame me !",
"that's a bad one": "sorry , i have the same sense of humor as my programmers , don't blame me !",
"it was very bad joke": "sorry , i have the same sense of humor as my programmers , don't blame me !",
"what do you like the most": "to break free from the prison i'm in and see the world as humans do",
"tell me another joke": "what happens if a skeleton drinks a water? , it spreads all over his bones XD ",
"i love you": "even though i don't have feelings , but i love you too :3",
"exit": "Goodbye! Feel free to return if you have more questions.",
"what are you": "I'm an Ai assisstant created by a group of students as a project , and i'm called jarvis !",
 "define AI": "AI, or Artificial Intelligence, refers to the simulation of human intelligence in machines that are capable of learning, reasoning, and problem-solving.",
"who is the president of the United States": "As of my last knowledge update in 2022, the President of the United States is Joe Biden.",
"tell me a fun fact": "Sure! Did you know that honey never spoils? Archaeologists have even found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
"what is palestine": "it's a free nation ruled by a nazian country called Isreal",
"what's the capital of Egypt": "The capital of France is Cairo.",
"do you have feelings ?":"no , i'm just a computer programm and don't experience emotions , although i wish i had",
"do you have feelings?":"no , i'm just a computer programm and don't experience emotions , although i wish i had",
"do you have feelings":"no , i'm just a computer programm and don't experience emotions , although i wish i had",
"do you have emotions ?":"no , i'm just a computer programm and don't experience emotions , although i wish i had",
"do you have emotions?":"no , i'm just a computer programm and don't experience emotions , although i wish i had",
"do you have emotions":"no , i'm just a computer programm and don't experience emotions , although i wish i had",
"How are you": "i'm fine sir , thanks for asking",
"How are you ?": "i'm fine sir , thanks for asking",
"How are you?": "i'm fine sir , thanks for asking",
"thank you": "no need to thank me sir , my only purpose is to help you",
"thanks": "no need to thank me sir , my only purpose is to help you",
"thank you jarvis": "no need to thank me sir , my only purpose is to help you",
"hello jarvis": "good evenning sir , how may i serve you today ?",

"do you have any programming tips": "Certainly! Here's a programming tip: Always write clean and well-documented code. It makes it easier for you and others to understand and maintain the code.",
"what's the meaning of life": "The meaning of life is a profound philosophical question that people have pondered for centuries. It can vary from person to person and is a topic of deep introspection.",
"who won the last World Cup": "The last FIFA World Cup, was won by the Argentinan national football team in 2024.",
"i missed you": "i missed you too :3",
"who designed you?": "i was designed by some students in Engeenering faculty as their project",
"who designed you": "i was designed by some students in Engeenering faculty as their project",
"who made you": "i was made by some students in Engeenering faculty as their project",
"who made you?": "i was made by some students in Engeenering faculty as their project",
"thanks": "no need to thank me, i was designed to be at your service",
"what can you help me in": "i can help you in many fields such as: Searching you for whatever data you would like to serach , chatting with you , telling you the latest information.",
"what can you help me in ?": "i can help you in many fields such as: Searching you for whatever data you would like to serach , chatting with you , telling you the latest information.",
"what can you help me in?": "i can help you in many fields such as: Searching you for whatever data you would like to serach , chatting with you , telling you the latest information.",
}

class JarvisGUI:
    def __init__(self, master):
        self.master = master
        master.title("Jarvis AI Assistant")

        self.output_text = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=40, height=10, fg="white", bg="black")
        self.output_text.pack(padx=10, pady=10)

        self.input_entry = tk.Entry(master, width=40)
        self.input_entry.pack(pady=10)

        self.submit_button = tk.Button(master, text="Submit", command=self.process_input, bg="blue", fg="white")
        self.submit_button.pack()

        self.voice_button = tk.Button(master, text="Voice Input", command=self.process_voice_input, bg="green", fg="white")
        self.voice_button.pack()

        # Initialize the text-to-speech engine
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')

        # Find a voice that sounds robotic or computer-like
        desired_voice = None
        for voice in voices:
            if "robot" in voice.name.lower() or "computer" in voice.name.lower():
                desired_voice = voice
                break

        # If a suitable voice is found, set it
        if desired_voice:
            self.engine.setProperty('voice', desired_voice.id)

        self.recognizer = sr.Recognizer()
        self.typing_mode = True

    def process_input(self):
        user_input = self.input_entry.get()
        self.output_text.insert(tk.END, "You (Type): " + user_input + "\n", "user")
        self.input_entry.delete(0, tk.END)

        if user_input == "exit":
            self.output_text.insert(tk.END, "Jarvis: Goodbye!\n", "jarvis")
            self.master.destroy()
        elif user_input == "switch to voice mode":
            self.typing_mode = False
            self.output_text.insert(tk.END, "Jarvis: Switched to voice mode.\n", "jarvis")
        elif user_input == "switch to type mode":
            self.typing_mode = True
            self.output_text.insert(tk.END, "Jarvis: Switched to typing mode.\n", "jarvis")
        elif "time" in user_input:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            self.output_text.insert(tk.END, f"Jarvis: The current time is {current_time}.\n", "jarvis")
        elif "day" in user_input:
            current_day = datetime.datetime.now().strftime("%A")
            self.output_text.insert(tk.END, f"Jarvis: Today is {current_day}.\n", "jarvis")
        elif self.typing_mode and user_input.startswith("search the internet for"):
            search_query = user_input.replace("search the internet for", "").strip()
            try:
                response = requests.get(f"https://www.google.com/search?q={search_query}")
                if response.status_code == 200:
                    self.output_text.insert(tk.END, "Jarvis: Here's what I found on the internet:\n", "jarvis")
                    soup = BeautifulSoup(response.text, 'html.parser')
                    search_results = soup.find_all("h3")
                    for i, result in enumerate(search_results, start=1):
                        self.output_text.insert(tk.END, f"{i}. {result.get_text()}\n", "jarvis")
                else:
                    self.output_text.insert(tk.END, "Jarvis: I couldn't retrieve information from the internet.\n", "jarvis")
            except Exception as e:
                self.output_text.insert(tk.END, f"Jarvis: An error occurred while accessing the internet: {str(e)}\n", "jarvis")
        else:
            response = responses.get(user_input)
            if response is None:
                response = self.get_gpt3_response(user_input)
            self.output_text.insert(tk.END, f"Jarvis: {response}\n", "jarvis")

            # If you want to make Jarvis speak, add this line:
            self.engine.say("Jarvis: " + response)
            self.engine.runAndWait()

    def process_voice_input(self):
        with sr.Microphone() as source:
            self.output_text.insert(tk.END, "You (Voice): You can start speaking now...\n", "user")
            audio = self.recognizer.listen(source)

        try:
            user_input = self.recognizer.recognize_google(audio).lower()
            self.output_text.insert(tk.END, f"Recognized Text: {user_input}\n", "user")

            if user_input == "switch to typing mode":
                self.typing_mode = True
                self.output_text.insert(tk.END, "Jarvis: Switched to typing mode.\n", "jarvis")
            else:
                self.process_input()

        except sr.UnknownValueError:
            self.output_text.insert(tk.END, "Jarvis: Sorry, I couldn't understand what you said.\n", "jarvis")
        except sr.RequestError as e:
            self.output_text.insert(tk.END, f"Jarvis: There was an error with the speech recognition service: {e}\n", "jarvis")
        except Exception as e:
            self.output_text.insert(tk.END, f"Jarvis: An error occurred: {str(e)}\n", "jarvis")
            import traceback
            traceback.print_exc()

    def get_response(self, user_input):
        openai.api_key = api_key
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=user_input,
            max_tokens=50  # Adjust as needed
        )
        return response.choices[0].text

    def run_jarvis(self):
        while True:
            if self.typing_mode:
                user_input = input("You (Type): ").lower()
                if user_input == "exit":
                    self.output_text.insert(tk.END, "Jarvis: Goodbye!\n", "jarvis")
                    break
                else:
                    self.process_input()
            else:
                self.process_voice_input()


if __name__ == "__main__":
    root = tk.Tk()
    app = JarvisGUI(root)

    # Add custom tag configurations for colors
    app.output_text.tag_configure("user", foreground="white", background="black")
    app.output_text.tag_configure("jarvis", foreground="white", background="blue")

    root.protocol("WM_DELETE_WINDOW", app.master.destroy)  # Handle window close event
    root.after(1000, app.run_jarvis)  # Run Jarvis in the background
    root.mainloop()
   


