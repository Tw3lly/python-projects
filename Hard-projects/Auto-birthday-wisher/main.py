import smtplib
import datetime as dt
import random
import pandas

# Define sender and receiver
sender = "Private Person <from@example.com>"
receiver = "A Test User <to@example.com>"

# Choose a random letter
letter_list = ["./letter_templates/letter_1.txt", "./letter_templates/letter_2.txt", "./letter_templates/letter_3.txt"]
random_letter = random.choice(letter_list)

# Current time information
current_time = dt.datetime.now()
day = current_time.day
month = current_time.month

# Open csv file
data = pandas.read_csv("birthdays.csv")

# Iterate through CSV/dataframe to find our entry
for index, row in data.iterrows():
    # If day matches up with any of the entries birth month and day, then take this person's info and save to variable.
    if row.month == month and row.day == day:
        person = row
        # Open a random letter chosen and replace name with the persons name and save it to variable.
        with open(random_letter, "r") as letter:
            contents = letter.read().replace("[NAME]", person['name'])

        # open SMTP connection and send email with the contents.
        with smtplib.SMTP("smtp.email.com") as server:
            server.login("email", "password")
            server.sendmail(from_addr=sender, to_addrs=receiver, msg=f"Subject: Birthday wishes\n\n{contents}")
