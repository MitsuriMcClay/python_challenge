from flask import Flask ,request
import requests

app = Flask('worldweather')

def getAPIData(city_name):
    api_key="592aadf603c0712f2436905fbe72c43c"
    myparams={
        "appid":api_key,
        "q":city_name,
        "lang":"ja",
        "units":"metric"
    }
    result = requests.get("https://api.openweathermap.org/data/2.5/weather",params=myparams)
    return result.json()

@app.route('/')
def myapi():
    name = request.args.get('city_name')
    data = getAPIData(name)
    temp = data["main"]["temp_min"]
    breakpoint()
    return f'<h1>最高気温: {temp}</h1>'

    #f'<h1>Hello {name}! you are {family[name]} years old.</h1>' #{'name': name, 'age': age}

app.run(host='0.0.0.0',port=900)