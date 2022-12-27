from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

field_email = Entry(width=40)
field_email.grid(column=1, row=2, columnspan=2)

field_word = Entry(width=22)
field_word.grid(column=1, row=3)

gen_pass = Button(text="Generate Password")
gen_pass.grid(column=2, row=3)
add = Button(text="Add", width=34)
add.grid(column=1, row=4, columnspan=2)



window.mainloop()
