import argparse
import requests


def parser():
    parser = argparse.ArgumentParser(description='Weather forcast for a specific city')

    parser.add_argument('city', type=str,
                        help='Name of a city')

    args = parser.parse_args()
    return args


data = parser()


def coordinates(city):
    r = requests.get(f'https://www.geocode.farm/v3/json/forward/?addr={city}&lang=en')
    lat_lon = r.json()
    return lat_lon['geocoding_results']['RESULTS'][0]['COORDINATES']


def fetch_weather(city):
    city_lat = float(coordinates(city)['latitude'])
    city_lon = float(coordinates(city)['longitude'])
    r = requests.get(f'https://fcc-weather-api.glitch.me/api/current?lat={city_lat}&lon={city_lon}')
    forcast = r.json()
    return [round(forcast['main']['temp']), round(forcast['main']['feels_like']), forcast['weather'][0]['main']]


output = fetch_weather(city=data.city)
print(f"Current temp: {output[0]} °C, Feel-like temp: {output[1]} °C, Sky: {output[2]}")
