import requests
import smtplib
from newsapi import NewsApiClient
import datetime as dt

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

NEWS_API_KEY = "63928176adaf4b57a93930106a06c165"
STCK_PRC_API_KEY = "N55390ZP9AGA01RT"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
today = dt.datetime.now()
days_1 = dt.timedelta(1)
days_2 = dt.timedelta(2)

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol":"tsla",
    "interval":"30min",
    "apikey":STCK_PRC_API_KEY,    
}

url = 'https://www.alphavantage.co/query'
stock_response = requests.get(url=url, params=stock_parameters)
stock_price = stock_response.json()

stock_price_yesterday = stock_price["Time Series (Daily)"][str(today.date()-days_1)]["4. close"]
print(stock_price_yesterday)

#TODO 2. - Get the day before yesterday's closing stock price

stock_price_2_days_older = stock_price["Time Series (Daily)"][str(today.date()-days_2)]["4. close"]
print(stock_price_2_days_older)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

diff_stock_price = abs(float(stock_price_2_days_older)-float(stock_price_yesterday))
print(diff_stock_price)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

percentage_diff = 100*(diff_stock_price/float(stock_price_2_days_older))
print(percentage_diff)
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
newsapi = NewsApiClient(api_key=NEWS_API_KEY)

# /v2/top-headlines

if percentage_diff > 5:
    top_headlines = newsapi.get_top_headlines(q='tesla',
                                            category='business',
                                            language='en',
                                            country='us')

    news_title = top_headlines["articles"][0]["title"]
    news_description = top_headlines["articles"][0]["description"]
    print(news_title)
    print(news_description)
    

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

