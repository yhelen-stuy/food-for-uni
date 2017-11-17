import json
import requests

f = open('./.secret_key.txt', 'rU')
keys = json.loads(f.read())
f.close()

ZOMATO_KEY = keys['zomato_key']
FOOD_KEY = keys['food2fork_key']
ZOMATO_URL = 'https://developers.zomato.com/api/v2.1/'

ZOMATO_HEADER = {'user-key': ZOMATO_KEY}

# TEST CODE
# URL requesting 10 restaurants within 1000 meters of 40 lat -70 lon, serving italian
# url = 'https://developers.zomato.com/api/v2.1/search?count=10&lat=40&lon=-70&radius=1000&cuisines=italian'
# headers = {'user-key': ZOMATO_KEY}
# req = requests.get(url, headers=headers)

# d = req.json()
# for r in d['restaurants']:
#     print r['restaurant']['name']

# ZOMATO CODE
# Slow...
def restaurant_search(rest_id=None, query='', location='', radius=None,
                     max_amt=None, cuisines=[], sort='rating', order='desc'):
    '''Return the restaurants that match the parameters given.
    '''
    url = ZOMATO_URL + "/search"

    if location != '':
        location = find_location(query=location)[0]
    else:
        location = {'latitude': None, 'longitude': None}

    params = {'entity_id': rest_id,
                'q': query,
                'lat': location['latitude'],
                'lon': location['longitude'],
                'radius': radius,
                'count': max_amt,
                'cuisines': cuisines,
                'sort': sort,
                'order': order
            }
    req = requests.get(url, headers=ZOMATO_HEADER, params=params)
    # print req.url
    restaurants = req.json()
    return restaurants['restaurants']

def find_location(query, max_amt=1):
    url = ZOMATO_URL + "/locations"
    if max_amt < 1:
        return []
    params = {'query': query,
              'count': max_amt}
    req = requests.get(url, headers=ZOMATO_HEADER, params=params)
    locs = req.json()
    return locs['location_suggestions']

if __name__ == "__main__":
    # print find_location('New York City')
    # print find_location('boston')
    rs = restaurant_search(location='New york city', max_amt=2)
    for r in rs:
        print r
