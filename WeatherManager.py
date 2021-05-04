from WeatherInfo import WeatherInfo
import AccuweatherGet as acc
import OpenWeatherGet as owm
import WeatherStackGet as ws
import json

def GetInfo(city):
    accinfo = acc.GetCurrent(city)
    owinfo = owm.GetCurrent(city)
    wsinfo = ws.GetCurrent(city)
    sharedinfo = WeatherInfo(accinfo, owinfo, wsinfo)
    jsonstr = json.dumps(sharedinfo.__dict__)
    return jsonstr