import requests
import datetime

#----------------------------------API KEYS----------------------------------#
stock_price_api = 'SELECT YOUR API'
news_api = 'SELECT YOUR API'
twilio_api = 'SELECT YOUR API'
twilio_account_sid = 'SELECT YOUR API'


#----------------------------------API ENDPOINTS----------------------------------#
news_endpoint = 'https://newsapi.org/v2/everything'
stock_endpoint = 'https://www.alphavantage.co/query'
twilio_endpoint ='https://api.twilio.com/2010-04-01'


#----------------------------------API PARAMETERS----------------------------------#
stock_params = {
  'apikey' : stock_price_api,
  'function':'TIME_SERIES_DAILY',
  'symbol':'TSLA',
  'interval': '1min'
}

new_api_params = {
'apiKey':news_api,
  'q' : 'tesla'
}

twilio_params = {

}


#----------------------------------API ENDPOINTS----------------------------------#
news_response = requests.get(news_endpoint,params = new_api_params)
stock_response = requests.get(stock_endpoint,params = stock_params)
# twilio_response  = requests.get(twilio_endpoint,params = t)



#----------------------------------API DATAS----------------------------------#
stock_data = stock_response.json()
news_data = news_response.json()



today = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime("%2022-%m-%d")
yesterday = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime("%2022-%m-%d")


today_price = stock_data['Time Series (Daily)'][today]['4. close']
yesterday_price = stock_data['Time Series (Daily)'][yesterday]['4. close']
percentage = abs(((float(today_price) - float(yesterday_price)) / float(today_price)) * 100)


news = news_data['articles'][0]['title']
if percentage >= 10 :
  print('Hurray!')

#TODO 2: Check If The Subtracting Result From TODO1 is More/Less 10 Percent








