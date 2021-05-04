import json
from WeatherValues import *
from WeatherInfo import OpenWeatherInfo, AccuweatherInfo, WeatherStackInfo, WeatherInfo

def CityTolink(city):
    link = city.strip()
    link = link.replace(" ", "%20")
    link = link.replace("ą", "a")
    link = link.replace("ę", "e")
    link = link.replace("ć", "c")
    link = link.replace("ź", "z")
    link = link.replace("ó", "o")
    link = link.replace("ń", "n")
    return link

def AddDescriptionsWS(dlist):
    desc = ""
    for e in dlist:
        desc += e + " "
    return desc

def AddDescriptionsOW(dlist):
    desc = ""
    for e in dlist:
        desc += e["description"] + " "
    return desc

def Tempavg(tempdict):
    avg = (tempdict["Minimum"]["Value"] + tempdict["Maximum"]["Value"]) / 2
    return avg

def ReadWind(winddict):
    return Wind(winddict["Speed"]["Value"], winddict["Direction"]["Degrees"])

def MapOpenWeather(jsonstr):
    data = json.loads(jsonstr)
    info = OpenWeatherInfo(None, None, None, None, None, None, None, None, None, None, None)
    info.coordinates = Coordinates(data["coord"]["lon"], data["coord"]["lat"])
    info.country = data["sys"]["country"]
    info.humidity = data["main"]["humidity"]
    info.location = data["name"]
    info.pressure = data["main"]["pressure"]
    try:
        info.rain = data["rain"]["1h"]
    except:
        info.rain = 0
    info.sunrise = data["sys"]["sunrise"]
    info.sunset = data["sys"]["sunset"]
    info.temp = Temperatures(data["main"]["temp"], data["main"]["feels_like"], data["main"]["temp_max"], data["main"]["temp_min"])
    info.weather = OWeatherInfo(data["weather"][0]["id"], data["weather"][0]["main"], AddDescriptionsOW(data["weather"]), data["weather"][0]["icon"])
    info.wind = Wind(data["wind"]["speed"], data["wind"]["deg"])
    return info

def MapWeatherStack(jsonstr):
    data = json.loads(jsonstr)
    info = WeatherStackInfo(None, None, None, None, None, None, None, None, None, None)
    info.cloudcover = data["current"]["cloudcover"]
    info.desc = AddDescriptionsWS(data["current"]["weather_descriptions"])
    info.humidity = data["current"]["humidity"]
    info.pressure = data["current"]["pressure"]
    info.temp = Temperatures(data["current"]["temperature"], data["current"]["feelslike"], data["current"]["temperature"], data["current"]["temperature"])
    info.rtemp = data["current"]["feelslike"]
    info.time = data["location"]["localtime"]
    info.uvindex = data["current"]["uv_index"]
    info.visibility = data["current"]["visibility"]
    info.wind = Wind(data["current"]["wind_speed"], data["current"]["wind_degree"])
    return info

def MapAccuweather(jsonstr):
    data = json.loads(jsonstr)
    info = AccuweatherInfo(None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
    info.airquality = IndexedData(data["DailyForecasts"][0]["AirAndPollen"][0])
    info.cloudcover = data["DailyForecasts"][0]["Day"]["CloudCover"]
    info.date = data["Headline"]["EffectiveEpochDate"]
    info.desc = data["Headline"]["Text"]
    info.uvindex = IndexedData(data["DailyForecasts"][0]["AirAndPollen"][5])
    info.grass = IndexedData(data["DailyForecasts"][0]["AirAndPollen"][1])
    info.ice = data["DailyForecasts"][0]["Day"]["Ice"]["Value"]
    info.iceprob = data["DailyForecasts"][0]["Day"]["IceProbability"]
    info.mlink = data["DailyForecasts"][0]["MobileLink"]
    info.mold = IndexedData(data["DailyForecasts"][0]["AirAndPollen"][2])
    info.tree = IndexedData(data["DailyForecasts"][0]["AirAndPollen"][4])
    info.rain = data["DailyForecasts"][0]["Day"]["Rain"]["Value"]
    info.rainprob = data["DailyForecasts"][0]["Day"]["RainProbability"]
    info.rangweed = IndexedData(data["DailyForecasts"][0]["AirAndPollen"][3])
    info.rtempshade = Tempavg(data["DailyForecasts"][0]["RealFeelTemperatureShade"])
    info.snow = data["DailyForecasts"][0]["Day"]["Snow"]["Value"]
    info.snowprob = data["DailyForecasts"][0]["Day"]["SnowProbability"]
    info.sunhours = data["DailyForecasts"][0]["HoursOfSun"]
    info.temp = Temperatures(Tempavg(data["DailyForecasts"][0]["Temperature"]), Tempavg(data["DailyForecasts"][0]["RealFeelTemperature"]), data["DailyForecasts"][0]["Temperature"]["Maximum"]["Value"], data["DailyForecasts"][0]["Temperature"]["Minimum"]["Value"])
    info.wind = ReadWind(data["DailyForecasts"][0]["Day"]["Wind"])
    info.windgust = ReadWind(data["DailyForecasts"][0]["Day"]["WindGust"])
    return info