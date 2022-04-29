from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# List of letters and symbols for our password generator.
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
    # save the data in a format of a list so we can get proper formatting to JSON file
    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }

    # If any fields are empty, do not proceed with saving the credentials and show an error message.
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail/Username: "
                                                              f"{username} \nPassword: {password} \nWebsite: {website} ")
        # if is_ok popup returns 'True' continue saving data
        if is_ok:
            # Open file and append variables
            # Reading old data, updating and saving/write the updated data.
            try:
                # Try open as read
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
                # If file do not exist, open as write and createa a file
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
                # If file was opened, update and write to it.
            else:
                # Update data
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    # Save updated data
                    json.dump(data, data_file, indent=4)
                # Finally, delete entries
            finally:
                # Delete entries in website and password fields
                website_entry.delete(0, 'end')
                password_entry.delete(0, 'end')


# ------------------------- SEARCH FUNCTION ---------------------------- #
def find_password():
    """Searches data file for website entry provided by user and returns credentials if it exists in file"""
    # Get the website entry user provided
    website = website_entry.get()
    # Try to open file
    try:
        with open("data.json", "r") as data_file:
            search_data = json.load(data_file)
    # If file does not exist, generate error
    except FileNotFoundError:
        messagebox.showerror(title="Oops", message="No data file found.")
    # If file opens, search for data in json file and generate a popup which prints out the details
    else:
        if website in search_data:
            password = search_data[website]['password']
            username = search_data[website]['email']
            messagebox.showinfo(title="Website found",
                                message=f"Website:{website} \n Username:{username}\n Password:{password}")
        else:
            messagebox.showerror(title="Oops", message="No data found for this entry.")


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

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=1, row=1, columnspan=2, sticky='e')

# Will append user provided credentials to data.txt
add_button = Button(text="Add", width=36, command=add)
add_button.grid(column=1, row=4, columnspan=2)

# Entries
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1, sticky='w', columnspan=2)
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
