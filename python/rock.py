from tkinter import *
from tkinter import messagebox
import random
root = Tk()
root.title("Rock Paper Scissors")
root.configure(bg="light blue")
root.geometry("650x450")
player_score = 0
computer_score = 0
title = Label(root,
              text="ROCK PAPER SCISSORS",
              font=("Arial", 22),
              bg="light blue")

title.place(x=170, y=20)
label1 = Label(root,
               text="Choose your move!",
               font=("Arial", 14),
               bg="light blue")

label1.place(x=250, y=80)
score = Label(root,
              text="Player: 0     Computer: 0",
              font=("Arial", 14),
              bg="light blue")

score.place(x=220, y=130)
result = Label(root,
               text="Make your first move!",
               font=("Arial", 13),
               bg="light blue")

result.place(x=220, y=190)
def play(player_choice):

    global player_score
    global computer_score

    choices = ["Rock", "Paper", "Scissors"]

    computer_choice = random.choice(choices)

    if player_choice == computer_choice:

        result.config(text="It's a Tie!")

    elif player_choice == "Rock" and computer_choice == "Scissors":

        result.config(text="You Win!")

        player_score = player_score + 1

    elif player_choice == "Paper" and computer_choice == "Rock":

        result.config(text="You Win!")

        player_score = player_score + 1

    elif player_choice == "Scissors" and computer_choice == "Paper":

        result.config(text="You Win!")

        player_score = player_score + 1

    else:

        result.config(text="Computer Wins!")

        computer_score = computer_score + 1

    
    score.config(text="Player: " + str(player_score) +
                 "     Computer: " + str(computer_score))

    
    choice.config(text="You: " + player_choice +
                  "     Computer: " + computer_choice)



choices = ["Rock", "Paper", "Scissors"]

x = 110

for item in choices:

    button = Button(root,
                    text=item,
                    font=("Arial", 14),
                    width=10,
                    bg="orange",
                    command=lambda move=item: play(move))

    button.place(x=x, y=260)

    x = x + 150



choice = Label(root,
               text="",
               font=("Arial", 12),
               bg="light blue")

choice.place(x=190, y=330)



def reset():

    global player_score
    global computer_score

    player_score = 0
    computer_score = 0

    score.config(text="Player: 0     Computer: 0")

    result.config(text="Make your first move!")

    choice.config(text="")



reset_button = Button(root,
                      text="Reset Game",
                      command=reset,
                      bg="red",
                      fg="white")

reset_button.place(x=280, y=380)


root.mainloop()