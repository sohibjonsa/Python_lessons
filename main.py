import requests

p = {'results':5, 'gender':'male', 'nat':['us', 'gb']}
url = 'https://randomuser.me/api/'
r = requests.get(url, p)
data = r.json()['results']

for i in data:
    print(i['name']['first'], i['name']['last'], i['gender'], i['nat'])