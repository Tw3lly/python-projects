from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    # If there is already a password in the entry field, delete it and generate a new password
    if len(password_entry.get()) > 1:
        password_entry.delete(0, 'end')
    # Choose random letters/symbols etc from list above in a random range, concatenate them and shuffle
    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)

    # Join list together
    password = "".join(password_list)
    # Add password into the password entry field
    password_entry.insert(0, password)
    # Adds password to clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add():
    """Gets the credentials' info user provided, saves them in a txt file and deletes user entries in the GUI"""
    # Get the info user provided and save them in a variable
    website = website_entry.get()
    username = name_entry.get()
    password = password_entry.get()

    # If any fields are empty, do not proceed with saving the credentials and show an error message.
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail/Username: "
                                                              f"{username} \nPassword: {password} \nWebsite: {website} ")
        # if is_ok popup returns 'True' continue saving data
        if is_ok:
            # Open file and append variables
            with open("data.txt", "a") as data:
                data.write(f"{website} | {username} | {password} \n")
            # Delete entries in website and password fields
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #

# Window setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas setup
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_logo)
canvas.grid(column=1, row=0, sticky='w')

# Buttons
generate_password_button = Button(text="Generate Password", command=password_generator)
generate_password_button.grid(column=1, row=3, columnspan=2, sticky='e')

# Will append user provided credentials to data.txt
add_button = Button(text="Add", width=36, command=add)
add_button.grid(column=1, row=4, columnspan=2)

# Entries
website_entry = Entry(width=43)
website_entry.grid(column=1, row=1, columnspan=2, sticky='w')
website_entry.focus()

name_entry = Entry(width=43)
name_entry.grid(column=1, row=2, columnspan=2, sticky='w')
name_entry.insert(0, "dummy@email.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky='w')

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

name_label = Label(text="Email/Username:")
name_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Mainloop for window
window.mainloop()
