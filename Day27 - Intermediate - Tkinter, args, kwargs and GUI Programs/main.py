
from tkinter import *

window = Tk()
window.title("Test GUI")
window.minsize(width=600, height=300)

# Label
test_label =Label(text="This is a Label.")
test_label.pack()

test_label["text"] = "updated text"
test_label.config(text="second time updated text")


def button_click():
    print("Button got clicked")
    user_input_text = user_input.get()
    test_label.config(text= user_input_text)


button = Button(text="click here", command=button_click)
button.pack()

user_input = Entry(width=50)
user_input.pack()
window.mainloop()