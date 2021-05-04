import requests
import json
import ApiKeys as key
import WeatherOperations as wo

def GetCurrent(city):
    page = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" + city +"&appid=" + key.OpenWeather + "&units=metric")
    data = wo.MapOpenWeather(page.text)
    return data