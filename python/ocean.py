# ================================
# OCEAN BLUE PROFILE FORM
# ================================

from tkinter import *

# ------------------------------------------------
# PART 1 - CREATE A TKINTER WINDOW
# ------------------------------------------------

screen = Tk()
screen.title("Ocean Blue Profile")
screen.geometry("450x450")
screen.config(bg="light blue")


# ------------------------------------------------
# PART 2 - CREATE A FRAME
# ------------------------------------------------

profile_frame = Frame(screen, bg="white", padx=20, pady=20)
profile_frame.grid(row=0, column=0, padx=30, pady=30)


# ------------------------------------------------
# PART 3 - ADD LABEL WIDGETS
# ------------------------------------------------

heading_label = Label(
    profile_frame,
    text="My Profile",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="dark blue",
    width=25
)
heading_label.grid(row=0, column=0, columnspan=2, pady=10)

first_label = Label(profile_frame, text="First Name:", bg="white", font=("Arial", 11))
first_label.grid(row=1, column=0, sticky="w", pady=5)

grade_label = Label(profile_frame, text="Grade:", bg="white", font=("Arial", 11))
grade_label.grid(row=2, column=0, sticky="w", pady=5)

sport_label = Label(profile_frame, text="Favourite Sport:", bg="white", font=("Arial", 11))
sport_label.grid(row=3, column=0, sticky="w", pady=5)

details_label = Label(profile_frame, text="About Me:", bg="white", font=("Arial", 11))
details_label.grid(row=4, column=0, sticky="nw", pady=5)


# ------------------------------------------------
# PART 4 - ADD ENTRY AND TEXT WIDGETS
# ------------------------------------------------

first_entry = Entry(profile_frame, width=30)
first_entry.grid(row=1, column=1, pady=5)

grade_entry = Entry(profile_frame, width=30)
grade_entry.grid(row=2, column=1, pady=5)

sport_entry = Entry(profile_frame, width=30)
sport_entry.grid(row=3, column=1, pady=5)

details_text = Text(profile_frame, width=23, height=5)
details_text.grid(row=4, column=1, pady=5)


# ------------------------------------------------
# PART 5 - BUTTON FUNCTION
# ------------------------------------------------

def display_profile():
    first = first_entry.get()
    grade = grade_entry.get()
    sport = sport_entry.get()
    details = details_text.get("1.0", END).strip()

    output_label.config(
        text="Welcome, " + first + "!\n"
             "Grade: " + grade + "\n"
             "Favourite Sport: " + sport + "\n"
             "About: " + details
    )


# ------------------------------------------------
# PART 6 - ADD BUTTON WIDGET
# ------------------------------------------------

display_button = Button(
    profile_frame,
    text="Display My Profile",
    bg="dark blue",
    fg="white",
    font=("Arial", 11, "bold"),
    command=display_profile
)
display_button.grid(row=5, column=0, columnspan=2, pady=15)


# ------------------------------------------------
# PART 7 - DISPLAY RESULT
# ------------------------------------------------

output_label = Label(
    profile_frame,
    text="Your profile will appear here.",
    bg="light cyan",
    fg="black",
    width=35,
    height=5,
    wraplength=300,
    justify="left"
)
output_label.grid(row=6, column=0, columnspan=2, pady=10)


# ------------------------------------------------
# PART 8 - RUN THE WINDOW
# ------------------------------------------------

screen.mainloop()