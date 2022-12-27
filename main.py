from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


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

    if website == "" or password == "":
        messagebox.showerror(title="Error", message="There are field empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}"
                                                      f"\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
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
website.grid(column=0, row=1)
email = Label(text="Email/Usarname:")
email.grid(column=0, row=2)
password = Label(text="Password")
password.grid(column=0, row=3)

field_website = Entry(width=40)
field_website.grid(column=1, row=1, columnspan=2)
field_website.focus()
field_email = Entry(width=40)
field_email.grid(column=1, row=2, columnspan=2)
field_email.insert(0, "teste@teste.com")
field_word = Entry(width=22)
field_word.grid(column=1, row=3)

gen_pass = Button(text="Generate Password", command=generate_password)
gen_pass.grid(column=2, row=3)
add = Button(text="Add", width=34, command=save)
add.grid(column=1, row=4, columnspan=2)


window.mainloop()
