
from tkinter import *


def convert():
    miles = float(user_input.get())
    km = round((miles * 1.609), 2)
    result_label.config(text=f"{km}")


window = Tk()
window.title("Mile To Kilometer Convertor")
window.config(padx=100, pady=100)

user_input = Entry()
user_input.grid(row=0, column=1)

miles_label = Label(text="miles")
miles_label.grid(row= 0, column=2)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(row= 1, column=0)

result_label = Label(text="0")
result_label.grid(row= 1, column=1)

km_label = Label(text="km")
km_label.grid(row= 1, column=2)

button = Button(text="calculate", command=convert)
button.grid(row= 2, column=1)

window.mainloop()