import requests
from bs4 import BeautifulSoup


def get_price(symbol):
    URL = f"https://www.tgju.org/profile/{symbol}"
    r = requests.get(URL)

    soup = BeautifulSoup(r.content, 'html5lib')
    tds = soup.find_all("span", class_="value")
    # print(type(tds))
    value = str(tds[0]).split(">")[2].split("<")[0]
    print(value)

get_price('price_dollar_rl')
