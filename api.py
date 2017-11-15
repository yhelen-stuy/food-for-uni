import json
import requests

f = open('./.secret_key', 'rU')
keys = json.loads(f.read())
f.close()

ZOMATO_KEY = keys['zomato_key']

# TEST CODE
# URL requesting 10 restaurants within 1000 meters of 40 lat -70 lon, serving italian
url = 'https://developers.zomato.com/api/v2.1/search?count=10&lat=40&lon=-70&radius=1000&cuisines=italian'
headers = {'user-key': ZOMATO_KEY}
req = requests.get(url, headers=headers)

d = req.json()
for r in d['restaurants']:
    print r['restaurant']['name']
