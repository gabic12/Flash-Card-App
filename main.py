from tkinter import *
import pandas
import random

def get_word():
    """Get a random French word from the list and starts the timer"""
    global current_card, flip_timer
    window.after_cancel(flip_timer) #Cancel the timer if a button is pressed
    current_card = random.choice(words_list)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front_image)
    flip_timer = window.after(3000, flip_card) #Reset the timer

def flip_card():
    """Changes the card picture and display the word translation in English"""
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")

def incorrect_word():
    """Wrong words will be saved in a new .csv file"""
    incorrect_words.append(current_card)
    new_data = pandas.DataFrame(incorrect_words)
    new_data.to_csv("data/incorrect_words.csv", index=False)
    get_word()

data = pandas.read_csv("data/french_words.csv")
words_list = data.to_dict(orient="records") #List of dictionaries
current_card = {}
incorrect_words = []

#Tkinter UI
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg="#B1DDC6")

flip_timer = window.after(3000, flip_card) #After 3 seconds, the card will flip

#Images
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
wrong_button_image = PhotoImage(file="images/wrong.png")
right_button_image = PhotoImage(file="images/right.png")

#Canvas
canvas = Canvas(width=800, height=526, bg="#B1DDC6", highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=card_front_image)
language_text = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=1, column=1,  columnspan=2)

#Buttons
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=incorrect_word)
wrong_button.grid(row=2, column=1)
right_button = Button(image=right_button_image, highlightthickness=0, command=get_word)
right_button.grid(row=2, column=2)

get_word()

window.mainloop()