from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = field_website.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Nothing saved.")
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f"E-mail: {data[website]['email']}"
                                                       f"\nPassword: {data[website]['password']}")
        else:
            messagebox.showinfo(title="Error", message=f"{website} not found.")
    finally:
        field_website.delete(0, END)
        field_word.delete(0, END)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letter
    shuffle(password_list)

    password = "".join(password_list)
    field_word.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = field_website.get()
    email = field_email.get()
    password = field_word.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if website == "" or password == "":
        messagebox.showerror(title="Error", message="There are field empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            field_website.delete(0, END)
            field_word.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=30, padx=20)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website = Label(text="Website:")
website.grid(column=0, row=2, sticky="w")
email = Label(text="Email/Usarname:")
email.grid(column=0, row=1, sticky="w")
password = Label(text="Password")
password.grid(column=0, row=3, sticky="w")

field_website = Entry(width=22)
field_website.grid(column=1, row=2)
field_website.focus()
field_email = Entry(width=41)
field_email.grid(column=1, row=1, columnspan=2)
field_email.insert(0, "teste@teste.com")
field_word = Entry(width=22)
field_word.grid(column=1, row=3)

gen_pass = Button(text="Generate Password", width=15, command=generate_password)
gen_pass.grid(column=2, row=3, sticky="w")
add = Button(text="Add", width=34, command=save)
add.grid(column=1, row=4, columnspan=2)
search = Button(text="Search", width=15, command=find_password)
search.grid(column=2, row=2, sticky="w")


window.mainloop()
