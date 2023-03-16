import requests
import smtplib
from twilio.rest import Client

STOCK = "AAPL"
COMPANY_NAME = "Apple Inc"


# functions

def send_email(smtp_location, from_email_address, password, to_email_address):
    connection = smtplib.SMTP(smtp_location)
    connection.starttls()
    connection.login(email=from_email_address, password=password)
    connection.sendmail(from_addr=from_email_address, to_addrs=to_email_address, msg=""

                        )

def make_api_request(endpoint, parameters):
    """"A function to make API requests"""
    response = requests.get(url=endpoint, params=parameters)
    response.raise_for_status()
    data = response.json()

    return data


def send_message(twilio_auth_sid, twilio_auth_token, twilio_phone_number, difference, stock_symbol, title,
                 description, article_source, article_author):
    client = Client(twilio_auth_sid, twilio_auth_token)
    if percentage_difference > 0:
        message_symbol = "🔼"
    elif percentage_difference == 0:
        message_symbol = "⛔"
    else:
        message_symbol = "🔽"

    message = client.messages.create(
        body=f"{stock_symbol}: {message_symbol}{difference}%\n\n"
             f"Headline: {title}\n\n"
             f"Brief: {description}\n\n"
             f"Source: {article_source}, {article_author}",
        from_=twilio_phone_number,
        to="+233505043400"
    )

    print(message.sid)


# api keys
STOCK_API_KEY = "GAJ2S0H9J8N9NHE4"
NEWS_API_KEY = "07b46a7ebc3e492da8fc8bc321770a74"

# api endpoints
STOCK_API_ENDPOINT = "https://www.alphavantage.co/query?"
NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything?"

STOCK_API_PARAMETERS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

# twilio authentication
TWILIO_AUTH_SID = "AC3710e934e179ccba277bc5f83daa1d94"
TWILIO_AUTH_TOKEN = "2f5334670a6a6a19d643ee55a6503cac"
TWILIO_PHONE_NUMBER = "+17755228278"

# make api request to alphavantage.com
stock_data = make_api_request(endpoint=STOCK_API_ENDPOINT, parameters=STOCK_API_PARAMETERS)
daily_data = stock_data['Time Series (Daily)']

# create a list of daily values
daily_data_list = [value for (key, value) in daily_data.items()]

# create a list of daily keys which are dates
daily_data_keys = [key for (key, value) in daily_data.items()]

yesterday_data = daily_data_list[0]
yesterday_date = daily_data_keys[0]
yesterday_closing_price = float(yesterday_data['4. close'])

day_before_yesterday_data = daily_data_list[1]
day_before_yesterday_date = daily_data_keys[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data['4. close'])

price_difference = (yesterday_closing_price - day_before_yesterday_closing_price)
percentage_difference = round((price_difference / yesterday_closing_price) * 100)
absolute_percentage_difference = abs(percentage_difference)

# newsapi parameters
NEWS_API_PARAMETERS = {
    "apiKey": NEWS_API_KEY,
    "q": COMPANY_NAME,
    "from": day_before_yesterday_date,
    "to": yesterday_date
}

# make api request to newsapi.com
news_data = make_api_request(endpoint=NEWS_API_ENDPOINT, parameters=NEWS_API_PARAMETERS)

# create a list of the first 3 articles
articles = news_data['articles'][0:3]
for article in articles:
    source = article['source']['name']
    author = article['author']
    headline = article['title']
    brief = article['description']
    send_message(twilio_auth_sid=TWILIO_AUTH_SID, twilio_auth_token=TWILIO_AUTH_TOKEN,
                 twilio_phone_number=TWILIO_PHONE_NUMBER, difference=absolute_percentage_difference,
                 stock_symbol=STOCK, title=headline, description=brief, article_source=source, article_author=author)
