from tkinter import *
import pandas
import random
# values
current_card = {}
to_learn = {}
black = "#030000"
green = "#8AE30E"
cool_color = "#1182CF"
white = "#FBFCFC"
Font = "Ariel"
try:
    french_words = pandas.read_csv("Untitled spreadsheet - Sheet1.csv")
except FileNotFoundError:
    original_data = pandas.read_csv('Untitled spreadsheet - Sheet1.csv')
    to_learn = original_data.to_dict()
else:
    to_learn = french_words.to_dict(orient="records")

# definitions


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn")
    get_french_word()


def get_french_word():
    global flip_timer, current_card
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_bg_image, image=image)
    canvas.itemconfig(card_word, fill=black)
    canvas.itemconfig(card_title, fill=black)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["french"])
    flip_timer = window.after(3000, change_card_back)


def change_card_back():
    canvas.itemconfig(canvas_bg_image, image=back_image)
    canvas.itemconfig(card_word, text=current_card["english"])
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, fill=white)
    canvas.itemconfig(card_title, fill=white)
# work_section


window = Tk()
window.title("Translate_flash_cards")
window.config(bg=cool_color)
window.config(padx=50, pady=50)

flip_timer = window.after(3000, func=change_card_back)

canvas = Canvas(height=526, width=800, bg=cool_color, highlightthickness=0)
image = PhotoImage(file="card_front.png")
back_image = PhotoImage(file="card_back.png")
canvas_bg_image = canvas.create_image(400, 263, image=image)

card_title = canvas.create_text(400, 150, text="FrenchWord:", font=(Font, 40, "italic"))
card_word = canvas.create_text(400, 264, text="word", font=(Font, 60, "bold"))

image_check = PhotoImage(file="right.png")
check_button = Button(image=image_check, highlightthickness=0, command=get_french_word)
check_button.grid(row=1, column=1)

image_x = PhotoImage(file="wrong.png")
x_button = Button(image=image_x, highlightthickness=0, command=is_known)
x_button.grid(row=1, column=0)
canvas.grid(row=0, column=0, columnspan=2)
get_french_word()


window.mainloop()
