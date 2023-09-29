BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import os 
cwd = os.getcwd() 
import pandas
import random


#Create dataframe 
word_data = pandas.read_csv("/Users/khaido/Library/CloudStorage/GoogleDrive-khaitroyy@gmail.com/My Drive/Code/day-31-flashcard/data/french_words.csv")
data_dict = word_data.to_dict(orient="records")
random_word = {}

#Selected word 

def generate_random_word():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(data_dict)
    canvas.itemconfig(canvas_image, image = card_front_image)
    canvas.itemconfig(title_text, text= "French", fill = "black")
    canvas.itemconfig(word_text, text= random_word["French"], fill = "black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image = card_back_image)
    canvas.itemconfig(title_text, text= "English", fill = "white")
    canvas.itemconfig(word_text, text= random_word["English"], fill = "white")

def save_known_word():
    data_dict.remove(random_word)
    data = pandas.DataFrame(data_dict)
    data.to_csv("word_to_learn.csv")

window = Tk()
window.title("Flashy")
window.minsize(width=800, height=526)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

#Add images

right_image = PhotoImage(file="/Users/khaido/Library/CloudStorage/GoogleDrive-khaitroyy@gmail.com/My Drive/Code/day-31-flashcard/images/right.png")
wrong_image = PhotoImage(file="/Users/khaido/Library/CloudStorage/GoogleDrive-khaitroyy@gmail.com/My Drive/Code/day-31-flashcard/images/wrong.png")
card_front_image = PhotoImage(file="/Users/khaido/Library/CloudStorage/GoogleDrive-khaitroyy@gmail.com/My Drive/Code/day-31-flashcard/images/card_front.png")
card_back_image = PhotoImage(file="/Users/khaido/Library/CloudStorage/GoogleDrive-khaitroyy@gmail.com/My Drive/Code/day-31-flashcard/images/card_back.png")

#Canvas 

canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 263, image = card_front_image)
canvas.grid(column=0, row=0, columnspan=2)
title_text = canvas.create_text(400, 150, font=("Arial",30, "italic"))
word_text = canvas.create_text(400, 263, font=("Arial",60, "bold"))

#Button

wrong_button = Button(image=wrong_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command= generate_random_word)
wrong_button.grid(column=0, row= 1)

right_button = Button(image=right_image,highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command= save_known_word)
right_button.grid(column=1, row= 1)

generate_random_word()

window.mainloop()