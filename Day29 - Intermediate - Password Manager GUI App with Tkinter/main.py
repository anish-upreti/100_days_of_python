from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
               'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # Use this BLOCK 1 code or the BLOCK 2 code below. Both have same functionality.
    # --------------------- BLOCK 1-------------------
    pw_letters = [random.choice(letters) for letter in range(nr_letters)]
    pw_symbols = [random.choice(symbols) for symbol in range(nr_symbols)]
    pw_numbers = [random.choice(numbers) for number in range(nr_numbers)]

    password_list = pw_numbers + pw_letters + pw_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    # -------------------------------------------------

    # # Use this BLOCK 2 code or the one above. Both have same functionality.
    # # -----------------------BLOCK 2-----------------------------
    # password_list = []
    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)
    #
    # random.shuffle(password_list)
    #
    # password = ""
    # for char in password_list:
    #     password += char
    # # -------------------------------------------------------------

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    web_data = website_entry.get()
    pw_data = password_entry.get()
    email_data = email_entry.get()

    if len(web_data) == 0 or len(email_data) == 0 or len(pw_data) == 0:
        messagebox.showinfo(title="Error", message="Please do not leave any field empty.")
    else:
        is_yes = messagebox.askyesno(title=web_data, message=f"Data entered:\n Email: {email_data}\n "
                                                             f"Password: {pw_data}\n Do you want to save data?")

        if is_yes:
            with open("saved_data.txt", "a") as file:
                file.write(f"{web_data} | {email_data} | {pw_data}\n")
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("The Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock)
canvas.grid(row=0, column=1)

# labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)

password_label = Label(text="Password")
password_label.grid(row=3, column=0)

# Entry
website_entry = Entry(width=40)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "falano@gmail.com")

password_entry = Entry(width=22)
password_entry.grid(row=3, column=1)

# Button
generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=35, command=save_data)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
