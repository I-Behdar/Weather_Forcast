This project automatically fetches and saves weather reports for a chosen city using GitHub Actions
  
## Installation
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Usage
### Command-line
```bash
usage: main.py [-h] city

Weather forcast for a specific city

positional arguments:
  city        Name of a city

options:
  -h, --help  show this help message and exit
```

```bash
python3 weather_app/main.py warsaw
Current temp: 4 °C, Feel-like temp: 0 °C, Sky: Clouds
```

### Python
```python
>>> from weather_app import fetch_weather
>>> fetch_weather("warsaw")
[4, 0, 'Clouds']
```