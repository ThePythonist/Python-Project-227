import requests


def get_weather_data(city, key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
    response = requests.get(url)
    data = response.json()
    print(data['name'])
    print(data['dt'])
    print(data['main']['temp'])
    print(data['main']['humidity'])


while True:
    try:
        get_weather_data(city="shiraz", key="ce28524cced047e5c594dabe55a408be")
        break
    except:
        print("Trying Again")
