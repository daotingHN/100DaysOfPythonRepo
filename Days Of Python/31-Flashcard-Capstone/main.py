from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


# ---------------------------- DATA SETUP ------------------------------- #
# ------ Make Dictionary ------ #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")  # Param for Orienting Dictionary organization


# ---------------------------- FUNCTION SETUP ------------------------------- #
def next_card():
    global current_card, flip_timer
    # Timer Reset
    window.after_cancel(flip_timer)
    # Choose Card
    current_card = random.choice(to_learn)
    # Text Reset
    canvas.itemconfig(card_language, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    # Card Reset
    canvas.itemconfig(card_background, image=card_front_img)
    # Start Timer
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    # Text Change
    canvas.itemconfig(card_language, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    # Card Change
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    # Move to next card
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
# ------ Window Methods ------ #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Card Flip Timer
flip_timer = window.after(3000, func=flip_card)


# ------ Card Front Image ------ #
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)

# Card Texts
card_language = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))

# Card Configuration
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


# ------ Buttons Front Image ------ #
# Wrong Button
wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

# Right Button
right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)


# ---------------------------- PROGRAM PROPER ------------------------------- #
next_card()
window.mainloop()
