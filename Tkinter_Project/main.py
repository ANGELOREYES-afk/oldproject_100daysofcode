from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label["text"] = "New Text"
my_label.place(x=100, y=200)
# pack

# Button


def button_clicked():
    my_label["text"] = input1.get()


button = Button(text="Click Me", command=button_clicked)



# Entry

input1 = Entry(width=10)
# Add some text to begin with
input1.insert(END, string="Some text to begin with.")
# returns value of input
print(input1.get())


window.mainloop()
