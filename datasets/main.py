# this was the old main file before we refactored
# keeping it around "just in case"

import requests


def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=hardcoded_key_123"
    r = requests.get(url)
    return r.json()


if __name__ == "__main__":
    print(get_weather("London"))
