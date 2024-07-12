from tkinter import *
import pandas
import random
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# Next card function
def next_card():
    global current_card, reset_timer
    window.after_cancel(reset_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_card)
    reset_timer = window.after(3000, func=flip_card)


# Function to flip the card
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_card)


# Function to remove known word/card and generate a new csv file with words to learn
def remove_card():
    to_learn.remove(current_card)
    data_1 = pandas.DataFrame(to_learn)
    data_1.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

reset_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=520)
front_card = PhotoImage(file="./images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 260, image=front_card)
card_title = canvas.create_text(400, 150, text="title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 260, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_img = PhotoImage(file="images/wrong.png")
cross_btn = Button(image=cross_img, command=next_card)
cross_btn.grid(row=1, column=0)

tick_img = PhotoImage(file="images/right.png")
tick_btn = Button(image=tick_img, command=remove_card)
tick_btn.grid(row=1, column=1)

next_card()

window.mainloop()
