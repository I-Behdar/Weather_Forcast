import argparse

from weather_app import fetch_weather

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Weather forcast for a specific city')

    parser.add_argument('city', type=str,
                        help='Name of a city')

    args = parser.parse_args()

    output = fetch_weather(city=args.city)
    print(f"Current temp: {output[0]} °C, Feel-like temp: {output[1]} °C, Sky: {output[2]}")