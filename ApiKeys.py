import os
from dotenv import load_dotenv

load_dotenv()
Accuweather = os.getenv("Accuweather")
OpenWeather = os.getenv("OpenWeather")
WeatherStack = os.getenv("WeatherStack")