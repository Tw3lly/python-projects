import requests

# Constants
QUESTIONS = 10
QUESTION_TYPE = "boolean"

# Parameters to pass into API
parameters = {
    "amount": QUESTIONS,
    "type": QUESTION_TYPE,
}

# Gets data from API using our parameters above.
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()

# We save the data we pulled in a variable, then we pull the result only from that data.
data = response.json()
question_data = data["results"]
