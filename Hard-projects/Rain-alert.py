# Rain alert that will send a text message in case of rain using Opean Weather Map for weather status and sms messaging using Twilio.

import requests
from twilio.rest import Client
import os

# Open weather set-up
LAT = 10.604980  # CHANGE THIS
LONG = 10.003822  # CHANGE THIS
OWM_API_KEY = os.environ.get("OWM_API_KEY")  # CHANGE THIS

# Twilio Setup
twilio_account_sid = os.environ.get("TWILIO_SID")  # CHANGE THIS
twilio_auth_token = os.environ.get("TWILIO_AUTH_TOKEN")  # CHANGE THIS

# Parameters for Opean Weather
parameters = {
    "lat": LAT,
    "lon": LONG,
    "appid": OWM_API_KEY,
    "exclude": "current,minutely,daily",
}
# Submbit request to openweathermap and save response to a variable. 
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()


will_rain = False
# We only need to check the upcoming 12 hours and we only want the weather ID for each hour. 
# We loop through the list and save only the parts we need. 
weather_code_ids = [weather_data["hourly"][n]["weather"][0]["id"] for n in range(0, 12)]

# We loop through the IDs and check if any of them are less than 700, in that case its likely snowing/raining
for i in weather_code_ids:
    if i < 700:
        will_rain = True
        
# If our previous forloop found that any of the weather codes are below 700, text message will be sent. 
if will_rain:
    client = Client(twilio_account_sid, twilio_auth_token)
    message = client.messages.create(body="It's going to rain today, bring an umbrella.",
                                     from_='TWILIO_NUMBER', 
                                     to='YOUR_NUMBER')
                                     # CHANGE THIS ^ 
    # Prints status of text-message. 
    print(message.status)
