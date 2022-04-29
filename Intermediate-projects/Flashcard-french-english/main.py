from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# Open CSV with pandas, if file is not found create a new one.
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# Functions
def new_card():
    """Picks a random card from a dictionary"""
    # Fixes bug where if you keep pressing any of the buttons, timer will still count and flip after 3 seconds.
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    # Picks random card from dictionary
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=flashcard_front)
    # Sets timer back on again, calls flip card function
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    """Flips the flashcard to show the answer"""
    canvas.itemconfig(canvas_image, image=flashcard_back)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")


def remove_card():
    """If user knows card, it will remove the card from the dictionary and update a CSV file"""
    to_learn.remove(current_card)
    word_to_save = pandas.DataFrame(to_learn)
    # Index=false makes sure it only saves the records and not the index in csv file
    word_to_save.to_csv("data/words_to_learn.csv", index=False)
    new_card()


# ----- UI SETUP ------ #

# Window setup
window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# After 3 seconds, card should flip
flip_timer = window.after(3000, func=flip_card)
# Canvas setup
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
flashcard_front = PhotoImage(file="images/card_front.png")
flashcard_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 260, image=flashcard_front)
canvas.grid(column=0, row=0, columnspan=2)

# Create text printed on canvas
title_text = canvas.create_text(400, 150, text="Title", fill="black", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", fill="black", font=("Ariel", 60, "bold"))

# Buttons
right_button_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, borderwidth=0, command=remove_card)
right_button.grid(column=1, row=1)

wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, borderwidth=0, command=new_card)
wrong_button.grid(column=0, row=1)

new_card()

# Window loop
window.mainloop()
