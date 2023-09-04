import requests, json

based_url = 'https://cleanuri.com/api/v1'
endpoint = based_url + '/shorten'

data = { 'url': 'https://www.youtube.com/watch?v=559NRSm4LbE'}

response = requests.post(endpoint, data=data)
if response.status_code == 200:
    print(json.dumps(response.json(), indent=3))