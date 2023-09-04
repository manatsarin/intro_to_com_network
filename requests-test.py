import requests

response = requests.get('https://pantip.com')
print(f"Status code:\t {response.status_code}")
print(f"Content type:\t {response.headers['content-type']}")
print(f"Encoding:\t {response.encoding}")
print(f"Server:\t\t {response.headers['server']}")
#print(response.text)
