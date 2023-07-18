#!/opt/homebrew/bin/python3

import requests
import datetime

city_name = input("Enter the city name: ")
print(f'Here is {city_name}\'s weather focust for a week.')

api_key="592aadf603c0712f2436905fbe72c43c"

def getAPIData(endpoint,params):
    result = requests.get(endpoint,params=params)
    #breakpoint()
    return result.json()

data = getAPIData(
    "https://api.openweathermap.org/data/2.5/weather",
    {
    "appid":api_key,
    "q":city_name,
    "lang":"ja",
    "units":"metric"
    }
)

# print(json.dumps(data,indent=2))
# # print(data['main']['temp_max'])
# tz = datetime.timezone(datetime.timedelta(seconds=int(data['timezone'])))
# mytime = datetime.datetime.utcfromtimestamp(data['sys']['sunrise'])
# breakpoint()


#breakpoint()
print("-----------------------------------")
print('日の出:',datetime.datetime.fromtimestamp(data['sys']['sunrise'])) 
print('日の入り:',datetime.datetime.fromtimestamp(data['sys']['sunset'])) 
print('最低気温:',data["main"]["temp_min"]) #最低気温
print('最高気温:',data["main"]["temp_max"]) #最高気温
print('天気予報:',data["weather"][0]["description"]) #天気
print("-----------------------------------")