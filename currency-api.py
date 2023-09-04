import requests, json

based_url = 'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/'

# # Get all currencies.
# response = requests.get('https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.json')
# if response.status_code == 200:
#     print(json.dumps(response.json(), indent=3))

# # Get the currency list with EUR as base currency
# response = requests.get('https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/eur.json')
# if response.status_code == 200:
#     print(json.dumps(response.json(), indent=3))

# Get the currency value for EUR to JPY.
response = requests.get('https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/eur/jpy.json')
if response.status_code == 200:
    print(json.dumps(response.json(), indent=3))
