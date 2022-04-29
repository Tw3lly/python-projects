import requests
from datetime import datetime
import smtplib

sender = "Private Person <from@example.com>"
receiver = "A Test User <to@example.com>"

message = f"""\
Subject: ISS is overhead
To: {receiver}
From: {sender}

ISS is overhead, get out and look!"""

MY_LAT = 10.000  # Your latitude
MY_LONG = 10.000  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.
def in_range():
    """Function that checks if Iss coordinates is withing range of your coordinates"""
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    else:
        return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

# Takes data to check if it's nighttime or not based on your coordinates
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

# Takes the current time so we can compare and see if it's dark or light outside
time_now = datetime.now()

# If you want to run the program every 60 seconds solution:
# While True:
# time.sleep(60)
if in_range():
    # If the current hour is greater than sunset hour or lower than sunrise hour, that means it's dark
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        # If it's dark, send email. 
        with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:  # CHANGE THIS
            server.login("uname", "password") #  CHANGE THIS
            server.sendmail(sender, receiver, message)
    else:
        pass

