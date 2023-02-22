import requests

api_key = 'fb998fcfb28bc4ac04269efc3a427264'
lat = 42.534901
long = -92.445312
api = f'https://api.openweenathermap.org/data/2.5/onecall'

weather_params = {
    'lat': lat,
    'lon': long,
    'appid': api_key,
    'exclude': 'current,minutely,daily'
}

data = requests.get(api, params=weather_params)
print(data.json())
