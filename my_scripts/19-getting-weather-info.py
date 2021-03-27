# author: Ercan Atar
# linkedin.com/in/ercanatar/
################################################
# https://home.openweathermap.org/ sitesinden hava durumu bilgisini çekicez.

import requests
from pprint import pprint

API_Key=""
city=input("enter a city: ")
base_url="http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city
weather_data=requests.get(base_url).json()
pprint(weather_data)