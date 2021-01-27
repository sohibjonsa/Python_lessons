import requests

r = requests.get('https://randomuser.me/api/?results=5&gender=male&nat=us,gb')

data = r.json()['results']

for i in data:
    print(i['name']['first'], i['name']['last'], i['gender'], i['nat'])