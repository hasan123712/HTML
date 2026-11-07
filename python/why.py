# ================================
# GAMING SCREENSHOT GALLERY
# ================================

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


# ------------------------------------------------
# PART 1 - CREATE THE MAIN TKINTER WINDOW
# ------------------------------------------------

screen = Tk()
screen.title("Gaming Gallery")
screen.geometry("450x500")
screen.config(bg="light blue")


# ------------------------------------------------
# PART 2 - ADD A TITLE LABEL
# ------------------------------------------------

heading_label = Label(
    screen,
    text="Gaming Gallery",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="dark blue",
    width=25
)
heading_label.pack(pady=15)


# ------------------------------------------------
# PART 3 - ADD IMAGE USING PIL
# ------------------------------------------------
# Make sure an image named "beamer.jpg" is saved in the same folder.

game_image = Image.open("beamer.jpg")
game_image = game_image.resize((300, 200))

game_photo = ImageTk.PhotoImage(game_image)

picture_label = Label(screen, image=game_photo, bg="light blue")
picture_label.pack(pady=10)


# ------------------------------------------------
# PART 4 - MESSAGEBOX FUNCTION
# ------------------------------------------------

def show_message():
    messagebox.showinfo(
        "Gaming Gallery",
        "Awesome gaming screenshot!"
    )


# ------------------------------------------------
# PART 5 - TOPLEVEL WINDOW FUNCTION
# ------------------------------------------------

def open_game_info():
    info_window = Toplevel(screen)
    info_window.title("Game Information")
    info_window.geometry("350x250")
    info_window.config(bg="light cyan")

    info_heading = Label(
        info_window,
        text="Game Information",
        font=("Arial", 16, "bold"),
        bg="light cyan",
        fg="dark blue"
    )
    info_heading.pack(pady=15)

    game_details = Label(
        info_window,
        text="Game Name: My Favourite Game\n"
             "Category: Adventure Game\n"
             "Description: One of my favourite gaming moments.",
        font=("Arial", 11),
        bg="light cyan",
        justify="left"
    )
    game_details.pack(pady=10)

    exit_button = Button(
        info_window,
        text="Close",
        bg="dark blue",
        fg="white",
        command=info_window.destroy
    )
    exit_button.pack(pady=15)


# ------------------------------------------------
# PART 6 - ADD BUTTON WIDGETS
# ------------------------------------------------

message_button = Button(
    screen,
    text="Like Screenshot",
    font=("Arial", 12, "bold"),
    bg="blue",
    fg="white",
    command=show_message
)
message_button.pack(pady=10)

info_button = Button(
    screen,
    text="View Game Information",
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    command=open_game_info
)
info_button.pack(pady=10)


# ------------------------------------------------
# PART 7 - RUN THE WINDOW
# ------------------------------------------------

screen.mainloop()