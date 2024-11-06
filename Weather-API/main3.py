import requests
from datetime import datetime
from queries import *


def normalize(data):
    temp = data['main']['temp'] - 273.15
    dt = str(datetime.fromtimestamp(data['dt']))
    return {"name": data['name'], "dt": dt, "temp": temp, "humidity": data['main']['humidity']}


def get_weather_data(city, key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
    response = requests.get(url)
    data = response.json()
    data = normalize(data)
    # print(data)
    save_data(data)
    print(f"A new record added to {data['name']} table")


tries = 1
while True:
    print("Try :", tries)
    try:
        get_weather_data(city=input("Enter city name : "), key="ce28524cced047e5c594dabe55a408be")
        break
    except Exception as error:
        print("Error :", error)
        print("Trying Again")
        tries += 1
