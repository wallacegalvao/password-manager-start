from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #

WHITE = '#EEEEEE'

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

#labels
website = Label(text="Website")
website.grid(column=0, row=1)
email = Label(text="Email/Username")
email.grid(column=0, row=2)
password = Label(text="Password")
password.grid(column=0, row=3)


#entries
website_input = Entry(width=52)
website_input.grid(column=1, row=1, columnspan=2)

website_email = Entry(width=52)
website_email.grid(column=1, row=2, columnspan=2)

website_password = Entry(width=34)
website_password.grid(column=1, row=3)

#buttons
generate = Button(text="Generate Password")
generate.grid(column=2, row=3)
add = Button(text="Add", width=44)
add.grid(column=1, row=4, columnspan=2)


window.mainloop()