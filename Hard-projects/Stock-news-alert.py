import requests
from twilio.rest import Client

#
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

NEWS_API_KEY = "Change This"
STOCK_API_KEY = "Change This"

twilio_account_sid = "Change This"
twilio_auth_token = "Change This"
twilio_phone = "Change This"

news_parameters = {
    "q": STOCK,
    "pageSize": 3,
    "apiKey": NEWS_API_KEY,
}

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY

}

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# Take data from news API and save it as a dictionary. 
news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
news_response.raise_for_status()
news_data = news_response.json()["articles"]

# Get stock data from API
stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()
# Convert data to list so we can slice it
stock_data = stock_response.json()["Time Series (Daily)"]
stock_data_list = list(stock_data.keys())
# Get the latest entries as stock exchange is closed on weekends/holidays
last_entry = stock_data_list[0]
day_before = stock_data_list[1]
last_entry_close = float(stock_data[last_entry]["4. close"])
day_before_close = float(stock_data[day_before]["4. close"])


def get_stock_percentage_change():
    return (float(last_entry_close) - float(day_before_close)) / float(day_before_close) * 100


def text_myself(body_input):
    client = Client(twilio_account_sid, twilio_auth_token)
    message = client.messages.create(body=body_input,
                                     from_=twilio_phone,
                                     to='Change this')
    print(message.status)


titles = []
briefs = []
urls = []

for i in range(3):
    # Append each title, description and url so we can call them later in txt message.
    titles.append(news_data[i]['title'])
    briefs.append(news_data[i]['description'])
    urls.append(news_data[i]['url'])
    # If there is a percentage difference of 5% (negative or plus) Send text message with top 3 articles.
    if get_stock_percentage_change() >= 5:
        text_myself(f"TSLA: 🔺{round(get_stock_percentage_change())}\nHeadline: {titles[i]}\nBrief: {briefs[i]}\nURL: {urls[i]}")
    elif get_stock_percentage_change() <= -5:
        text_myself(f"TSLA: 🔻{round(get_stock_percentage_change())}\nHeadline: {titles[i]}\nBrief: {briefs[i]}\nURL: {urls[i]}")
