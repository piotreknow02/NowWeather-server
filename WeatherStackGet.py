import requests
from WeatherOperations import CityTolink
import ApiKeys as key
import WeatherOperations as wo

def GetCurrent(city):
    page = requests.get("http://api.weatherstack.com/current?access_key=" + key.WeatherStack + "&query=" + CityTolink(city))
    data = wo.MapWeatherStack(page.text)
    return data