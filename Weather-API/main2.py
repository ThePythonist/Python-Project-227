import requests
from datetime import datetime


def normalize(data):
    temp = data['main']['temp'] - 273.15
    dt = str(datetime.fromtimestamp(data['dt']))
    return {"name": data['name'], "dt": dt, "temp": temp, "humidity": data['main']['humidity']}


def get_weather_data(city, key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
    response = requests.get(url)
    data = response.json()
    data = normalize(data)
    print(data)


while True:
    try:
        get_weather_data(city="tehran", key="ce28524cced047e5c594dabe55a408be")
        break
    except:
        print("Trying Again")
