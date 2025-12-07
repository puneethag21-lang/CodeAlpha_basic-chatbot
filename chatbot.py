import tkinter as tk
from tkinter import scrolledtext
import datetime
import random

def get_response(msg):
    msg = msg.lower()

    # Greetings
    if msg in ["hello", "hi", "hey"]:
        return "Hi there! 👋"

    # Sad
    elif "sad" in msg:
        return "I'm sorry to hear that 😔. You’re stronger than you think. Want to talk?"

    # Happy
    elif "happy" in msg:
        return "That's amazing! 😄 Keep smiling!"

    # Jokes
    elif "joke" in msg:
        jokes = [
            "Why don't programmers like nature? Too many bugs 🐞😂",
            "What do you call 8 hobbits? A hobbyte! 😂",
            "Why did the computer get cold? Because it forgot to close its windows! 🧊😂"
        ]
        return random.choice(jokes)

    # Time
    elif "time" in msg:
        return "The current time is " + datetime.datetime.now().strftime("%I:%M %p") + " ⏰"

    # Date
    elif "date" in msg:
        return "Today's date is " + datetime.date.today().strftime("%B %d, %Y") + " 📅"

    # Exit
    elif msg in ["bye", "goodbye"]:
        return "Goodbye! Have a great day 😊"

    else:
        return "I didn't understand that 🤔. Try saying: hello, tell a joke, sad, happy, time."


def send_message():
    user_msg = entry.get()
    if user_msg.strip() == "":
        return

    chat_window.insert(tk.END, "You: " + user_msg + "\n")

    bot_msg = get_response(user_msg)
    chat_window.insert(tk.END, "Bot: " + bot_msg + "\n\n")

    entry.delete(0, tk.END)
    chat_window.see(tk.END)


# GUI Window Setup
root = tk.Tk()
root.title("Python Chatbot (Frontend)")
root.geometry("500x500")

# Chat Display Area
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12))
chat_window.pack(pady=10, fill=tk.BOTH, expand=True)

# Entry Box
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(side=tk.LEFT, fill=tk.X, padx=10, pady=10, expand=True)

# Send Button
send_btn = tk.Button(root, text="Send", font=("Arial", 12), command=send_message)
send_btn.pack(side=tk.RIGHT, padx=10, pady=10)

root.mainloop()
