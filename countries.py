import requests, json

def country_info(name):
    endpoint = f'https://restcountries.com/v3.1/name/{name}'
    response = requests.get(endpoint)
    if response.status_code == 200:
        print(json.dumps(response.json(), indent=3))


country_info('thai')