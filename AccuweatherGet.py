import requests
import json
from WeatherOperations import CityTolink
import ApiKeys as key
import WeatherOperations as wo

def GetCurrent(city):
    localization = requests.get("http://dataservice.accuweather.com/locations/v1/search?q=" + CityTolink(city) + "&apikey=" + key.Accuweather)
    lockey = json.loads(localization.text)
    page = requests.get("http://dataservice.accuweather.com/forecasts/v1/daily/1day/" + lockey[0]["ParentCity"]["Key"] + "?apikey=" + key.Accuweather + "&details=true&metric=true")
    data = wo.MapAccuweather(page.text)
    return data