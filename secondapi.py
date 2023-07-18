
openweatherurl = 'https://api.openweathermap.org/data/2.5/weather'

from flask import Flask, request
import requests
import json

app = Flask('mitsurisapp')
myapikey="592aadf603c0712f2436905fbe72c43c"
#print("Type whatever country name you want!")
#country_name=input()

def getAPIdata(country_name,units):
    myparameters={
        "appid": myapikey,
        "q": country_name,
        "lang": "ja",
        "units": units
    }
    result=requests.get(openweatherurl, params=myparameters)
    return result.json()

#data = getAPIdata(country_name)
#print('This is the humidity in', country_name, ':', data["main"]["humidity"])

#{'coord': {'lon': -150.0003, 'lat': 64.0003}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': '雲', 'icon': '03d'}], 'base': 'stations', 'main': {'temp': 16.25, 'feels_like': 15.58, 'temp_min': 16.25, 'temp_max': 16.25, 'pressure': 1007, 'humidity': 63, 'sea_level': 1007, 'grnd_level': 958}, 'visibility': 10000, 'wind': {'speed': 2.55, 'deg': 342, 'gust': 1.92}, 'clouds': {'all': 48}, 'dt': 1688785733, 'sys': {'country': 'US', 'sunrise': 1688730849, 'sunset': 1688804117}, 'timezone': -28800, 'id': 5879092, 'name': 'アラスカ州', 'cod': 200}

@app.route("/")
def myapiproject():
    country=request.args.get('country_name')
    desired_info = request.args.get('info')
    desired_units = request.args.get('units')
    data=getAPIdata(country,desired_units)
    info=data["main"][desired_info]
    return f'This is {country}\'s {desired_info} {info}.'

app.run(host='0.0.0.0' ,port=5001)


