import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

def get_rainfall(city="Mumbai"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    response = requests.get(url)
    data = response.json()

    # Rain data (if available)
    rain = data.get("rain", {})

    rainfall = rain.get("1h", 0)  # mm in last hour

    return rainfall

def get_weather(city="Mumbai"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    rain = data.get("rain", {})
    rainfall = rain.get("1h", 0)

    temp = data["main"]["temp"]

    return {
        "rainfall": rainfall,
        "temperature": temp
    }

def get_aqi(lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"

    response = requests.get(url)
    data = response.json()

    aqi = data["list"][0]["main"]["aqi"]

    return aqi