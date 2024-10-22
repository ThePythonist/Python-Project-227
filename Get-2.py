import requests
from pprint import pprint

username = 'thepythonist'
url = 'https://api.github.com/users/{username}'.format(username=username)

response = requests.get(url)
data = response.json()
pprint(data)

# Print the user information
# print('Name:', data['login'])
# print('Public Repositories:', data['public_repos'])
# print('Followers:', data['followers'])
# print('Following:', data['following'])
