import requests
from bs4 import BeautifulSoup


def get_price(symbol, url):
    URL = f"https://www.tgju.org/profile/{url}"
    r = requests.get(URL)

    soup = BeautifulSoup(r.content, 'html5lib')
    tds = soup.find_all("span", class_="value")
    # print(type(tds))
    value = str(tds[0]).split(">")[2].split("<")[0]
    print(symbol, ":", value)


symbols = {
    "dollar": "price_dollar_rl",
    "nim": "nim",
    "emami": "sekee",
    "rob": "rob",
    "tala18": "geram18",
    "ons": "ons",
}

for k, v in symbols.items():
    get_price(k, v)
