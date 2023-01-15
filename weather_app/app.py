import argparse
import requests


def parser():
    parser = argparse.ArgumentParser(description='Weather forcast for a specific city')

    parser.add_argument('city', type=str,
                        help='Name of a city')

    args = parser.parse_args()
    return args


def get_city_coordinates(city):
    r = requests.get(f'https://www.geocode.farm/v3/json/forward/?addr={city}&lang=en')
    lat_lon = r.json()
    try:
        return lat_lon['geocoding_results']['RESULTS'][0]['COORDINATES']
    except KeyError:
        print(lat_lon['geocoding_results']['STATUS'])


def fetch_weather(city):
    try:
        city_lat = float(get_city_coordinates(city)['latitude'])
        city_lon = float(get_city_coordinates(city)['longitude'])
        r = requests.get(f'https://fcc-weather-api.glitch.me/api/current?lat={city_lat}&lon={city_lon}')
        forcast = r.json()
        return [round(forcast['main']['temp']), round(forcast['main']['feels_like']), forcast['weather'][0]['main']]
    except (KeyError, TypeError):
        print(f"{city} was not found!")


if __name__ == '__main__':
    args = parser()
    output = fetch_weather(city=args.city)
    if output is not None:
        print(f"Current temp: {output[0]} °C, Feel-like temp: {output[1]} °C, Sky: {output[2]}")
