
import requests

from weather_app.api_utils import json_to_latitude_longitude

def get_city_coordinates(city):
    r = requests.get(f'https://www.geocode.farm/v3/json/forward/?addr={city}&lang=en')
    content = r.json()
    try:
        return json_to_latitude_longitude(content)
    except KeyError as e:
        raise e


def fetch_weather(city):
    try:
        city_lat = float(get_city_coordinates(city)['latitude'])
        city_lon = float(get_city_coordinates(city)['longitude'])
        r = requests.get(f'https://fcc-weather-api.glitch.me/api/current?lat={city_lat}&lon={city_lon}')
        forcast = r.json()
        return [round(forcast['main']['temp']), round(forcast['main']['feels_like']), forcast['weather'][0]['main']]
    except (KeyError, TypeError):
        print(f"{city} was not found!")