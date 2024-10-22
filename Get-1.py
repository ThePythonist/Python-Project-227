import requests

url = 'https://en.wikipedia.org/w/api.php'
params = {
    'action': 'query',
    'format': 'json',
    'titles': 'Python (programming language)',
    'prop': 'extracts',
    'explaintext': True
}

response = requests.get(url, params=params)
data = response.json()

# Print the extract of the Earth page
page_id = next(iter(data['query']['pages']))
print(data['query']['pages'][page_id]['extract'])
