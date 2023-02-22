import requests

response = requests.get(url='https://api.sunrise-sunset.org/json?')
response.raise_for_status()

data=response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
print(f"sunrise = {sunrise} sunset = {sunset}")