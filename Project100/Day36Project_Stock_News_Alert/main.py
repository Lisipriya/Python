import requests
from datetime import date
from datetime import timedelta
from twilio.rest import Client

STOCK = "TRIDENT.BSE"
COMPANY_NAME = "TRIDENT"
STOCK_API_KEY = "ZMHHKQNBNFBKLOYQ"
NEWS_API_KEY = "0f254f427f064aa1982df6f36022c73b"
STOCK_URL = "https://www.alphavantage.co/query"
NEWS_URL = "https://newsapi.org/v2/everything"
account_sid = "AC10089714966288b5f25d4475dcf470c3"
auth_token = "d6abe87aa79e3de3abb78983d0b9e930"
FROM_NUM = "+16513722177"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

today = date.today()
yesterday = str(today - timedelta(days=1))
day_before_yesterday = str(today - timedelta(days=2))

response = requests.get(STOCK_URL, params=parameters)
data = response.json()
yesterday_close = float(data["Time Series (Daily)"][yesterday]["4. close"])
day_before_yesterday_close = float(data["Time Series (Daily)"][day_before_yesterday]["4. close"])

incre_decre = yesterday_close - day_before_yesterday_close
up_down = None
if incre_decre > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

incre_decre_percentage = round((incre_decre / day_before_yesterday_close) * 100, 2)

if abs(incre_decre_percentage) > 2:
    news_parameter = {
        "qIntitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
        "language": "en",

    }
    news_response = requests.get(NEWS_URL, params=news_parameter)
    news_data = news_response.json()
    top_news = news_data["articles"][:3]
    article_list = [f"\n{COMPANY_NAME} {up_down}{incre_decre_percentage}%" \
                    f"\nHeadline: {news['title']}. Brief: {news['description']}" for news in top_news]
    client = Client(account_sid, auth_token)
    for article in article_list:
        message = client.messages \
            .create(
            body=article,
            from_=FROM_NUM,
            to="+919865575106"
    )

    print(message.status)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
