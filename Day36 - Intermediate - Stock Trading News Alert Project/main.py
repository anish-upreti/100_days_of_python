import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "_YOUR_STOCK_API_KEY_"     # use your own stock api key
NEWS_API_KEY = "_YOUR_NEWS_API_KEY_"       # use your own news api key
twilio_sid = "__YOUR_TWILIO_ACCOUNT_ID__"  # use your own account sid from twilio
auth_token = "__YOUR_TWILIO_AUTH_TOKEN__"  # use your own auth token from twilio

# Use of alpha vantage api
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Get yesterday's closing stock price.
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_data = response.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]
yd_data = stock_data_list[0]
yd_closing_price = yd_data["4. close"]
print(yd_closing_price)

# Get the day before yesterday's closing stock price
day_before_yd_data = stock_data_list[1]
day_before_yd_closing_price = day_before_yd_data["4. close"]
print(day_before_yd_closing_price)

# Find the positive difference
diff = float(yd_closing_price) - float(day_before_yd_closing_price)
print(diff)
emoji = None
if diff > 1:
    emoji = "🔺"
else:
    emoji = "🔻"

# find percentage difference in price between closing price yesterday and closing price the day before yesterday.
percent_diff = round((diff / float(yd_closing_price)) * 100)
print(percent_diff)

# If percentage is greater than 5 then print("Get News").
# if percent_diff > 5:
#     print("Get News")

# Use of News API
# Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if abs(percent_diff) > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT,params=news_params)
    articles = news_response.json()["articles"]
    # Use Python slice operator to create a list that contains the first 3 articles
    three_articles = articles[:3]

    # Use of twilio API
    # Create a new list of the first 3 articles' headline and description using list comprehension.
    formatted_articles = [(f'{STOCK_NAME}:{emoji}{percent_diff}%\nHeadline: {article["title"]}.'
                           f' \nBrief: {article["description"]}') for article in three_articles]

    # Send each article as a separate message via Twilio.
    client = Client(twilio_sid, auth_token)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="YOUR TWILIO VIRTUAL NUMBER",  # use your own twilio virtual number
            to="YOUR TWILIO VERIFIED REAL NUMBER"  # use your own verified real number in twilio
        )


