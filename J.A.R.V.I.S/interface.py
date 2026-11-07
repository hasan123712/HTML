from tkinter import *
from tkinter import scrolledtext
from brain import ask_ai
from voice import speak, listen, wait_for_wake_word
from memory import load_memory, add_memory

# Main window
root = Tk()
root.title("J.A.R.V.I.S - AI ASSISTANT")
root.geometry("1100x700")
root.configure(bg="#080F1A")

history = load_memory()

# Colors
BACKGROUND = "#080F1A"
BLUE = "#00BFFF"
WHITE = "#FFFFFF"
GREEN = "#00FF99"

# Title
title = Label(
    root,
    text="J.A.R.V.I.S",
    font=("Arial", 30, "bold"),
    fg=BLUE,
    bg=BACKGROUND
)
title.pack(pady=15)

subtitle = Label(
    root,
    text="PERSONAL ARTIFICIAL INTELLIGENCE SYSTEM",
    font=("Arial", 10),
    fg=WHITE,
    bg=BACKGROUND
)
subtitle.pack()

# System status
status = Label(
    root,
    text="● SYSTEM ONLINE",
    font=("Arial", 12, "bold"),
    fg=GREEN,
    bg=BACKGROUND
)
status.pack(pady=15)

# AI visualizer placeholder
visualizer = Label(
    root,
    text="◉",
    font=("Arial", 85),
    fg=BLUE,
    bg=BACKGROUND
)
visualizer.pack(pady=10)

# Chat display
chat = scrolledtext.ScrolledText(
    root,
    width=100,
    height=18,
    bg="#101C2C",
    fg=WHITE,
    font=("Arial", 11),
    insertbackground=WHITE,
    relief=FLAT
)
chat.pack(padx=30, pady=15)

chat.insert(END, "JARVIS: Good evening. All systems are operational.\n\n")
chat.configure(state=DISABLED)


# Send message function
def send_message(event=None):

    global history

    message = entry.get().strip()

    if message == "":
        return

    entry.delete(0, END)

    chat.configure(state=NORMAL)
    chat.insert(END, "YOU: " + message + "\n\n")
    chat.insert(END, "JARVIS: Processing...\n\n")
    chat.configure(state=DISABLED)

    root.update()

    try:

        response = ask_ai(message, history)

        history = add_memory(history, message, response)

        chat.configure(state=NORMAL)

        chat.insert(END, "JARVIS: " + response + "\n\n")

        chat.configure(state=DISABLED)

        chat.see(END)

        speak(response)

    except Exception as error:

        chat.configure(state=NORMAL)

        chat.insert(END, "ERROR: " + str(error) + "\n\n")

        chat.configure(state=DISABLED)

# Voice input function
def voice_input():

    chat.configure(state=NORMAL)
    chat.insert(END, "JARVIS: Listening...\n\n")
    chat.configure(state=DISABLED)

    message = listen()

    if message:
        entry.delete(0, END)
        entry.insert(0, message)
        send_message()

# WAKE WORD MODE

def wake_word_mode():

    status.configure(text="● WAITING FOR HEY JARVIS", fg=GREEN)

    wait_for_wake_word()

    status.configure(text="● JARVIS ACTIVATED", fg=BLUE)

    message = listen(duration=5)

    if message:
        entry.delete(0, END)
        entry.insert(0, message)
        send_message()

    status.configure(text="● SYSTEM ONLINE", fg=GREEN)

# Input area
input_frame = Frame(root, bg=BACKGROUND)
input_frame.pack(pady=15)

entry = Entry(
    input_frame,
    width=65,
    font=("Arial", 14),
    bg="#17283D",
    fg=WHITE,
    insertbackground=WHITE,
    relief=FLAT
)
entry.pack(side=LEFT, padx=10, ipady=10)

entry.bind("<Return>", send_message)

send_button = Button(
    input_frame,
    text="SEND",
    font=("Arial", 12, "bold"),
    bg=BLUE,
    fg="black",
    width=12,
    command=send_message
)
send_button.pack(side=LEFT)

mic_button = Button(
    input_frame,
    text="MIC",
    font=("Arial", 12, "bold"),
    bg=GREEN,
    fg="black",
    width=8,
    command=voice_input
)

mic_button.pack(side=LEFT, padx=5)

wake_button = Button(
    input_frame,
    text="HEY JARVIS",
    font=("Arial", 12, "bold"),
    bg="#FF9900",
    fg="black",
    width=12,
    command=wake_word_mode
)

wake_button.pack(side=LEFT, padx=5)

# Footer
footer = Label(
    root,
    text="POWERED BY OLLAMA | QWEN 2.5",
    font=("Arial", 9),
    fg="#718096",
    bg=BACKGROUND
)
footer.pack(pady=10)

root.mainloop()