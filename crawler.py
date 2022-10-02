import requests

from db import get_db

mydb = get_db()
mycol = mydb["Pokemon"]

BASE_URL = "https://pokeapi.co/api/v2/pokemon?offset=20&limit=1200"


def get_urls(url):
    print(f'Get urls from {url}')
    response = requests.get(url)
    response.raise_for_status()
    response_json = response.json()
    # print(response_json['results'])
    for x in response_json['results']:
        yield (x['url'])


def get_details():
    for url in get_urls(BASE_URL):
        # url = next(get_urls(BASE_URL))
        print(f'Get details from {url}')
        response = requests.get(url)
        response.raise_for_status()
        response_json = response.json()
        # print(response_json)
        detail = {
            'id': response_json['id'],
            'name': response_json['name'],
            'characteristics': {
                'stats': response_json['stats'],
                'species': response_json['species'],
                'moves': response_json['moves'],
                'abilities': response_json['abilities'],
                'height': response_json['height'],
                'weight': response_json['weight']
            }}
        x = mycol.insert_one(detail)
        print(x.inserted_id)

# for x in get_urls(BASE_URL):
#     print(x)
# get_details()
