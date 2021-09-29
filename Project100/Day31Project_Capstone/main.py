import random
import time
from tkinter import *
import pandas

random_dict = {}
words_dict = {}
BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pandas.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    initial_data = pandas.read_csv("data/tamil_words.csv")
    words_dict = initial_data.to_dict(orient="records")

else:
    words_dict = data.to_dict(orient="records")

def next_card():
    global random_dict, flip_timer
    random_dict = random.choice(words_dict)
    canvas.itemconfig(Translate_lang, text="English", fill="black")
    canvas.itemconfig(word_to_find, text=random_dict["English"], fill="black")
    canvas.itemconfig(background_card, image=front_img)
    flip_timer = windows.after(5000, func=flip_card)

def flip_card():
    canvas.itemconfig(background_card, image=back_img)
    canvas.itemconfig(Translate_lang, text="Tamil", fill="white")
    canvas.itemconfig(word_to_find, text=random_dict["Tamil"], fill="white")
    windows.after_cancel(flip_timer)

def new_data_file():
    words_dict.remove(random_dict)
    data = pandas.DataFrame(words_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


windows = Tk()
windows.title("Flashy")
windows.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = windows.after(3000, func=flip_card)

canvas = Canvas(height=526, width=800)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
background_card = canvas.create_image(400, 263, image=front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
Translate_lang = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_to_find = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=new_data_file)
right_button.grid(row=1, column=1)

next_card()

windows.mainloop()
