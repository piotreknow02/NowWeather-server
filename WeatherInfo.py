from WeatherValues import Wind, OWeatherInfo, Temperatures

class OpenWeatherInfo:
    def __init__(self, coordinates, country, weather, temp, pressure, humidity, wind, rain, sunrise, sunset, location):
        self.coordinates = coordinates
        self.country = country
        self.weather = weather
        self.temp = temp
        self.pressure = pressure
        self.humidity = humidity
        self.wind = wind
        self.rain = rain
        self.sunrise = sunrise
        self.sunset = sunset
        self.location = location

class WeatherStackInfo:
    def __init__(self, time, temp, desc, wind, pressure, humidity, cloudcover, rtemp, uvindex, visibility):
        self.time = time
        self.temp = temp
        self.desc = desc
        self.wind = wind
        self.pressure = pressure
        self.humidity = humidity
        self.cloudcover = cloudcover
        self.rtemp = rtemp
        self.uvindex = uvindex
        self.visibility = visibility

class AccuweatherInfo:
    def __init__(self, mlink, date, temp, rtempshade, sunhours, airquality, mold, grass, tree, rangweed, uvindex, desc, wind, windgust, rainprob, snowprob, iceprob, cloudcover, rain, snow, ice):
        self.mlink = mlink
        self.date = date
        self.temp = temp
        self.rtempshade = rtempshade
        self.sunhours = sunhours
        self.airquality = airquality
        self.mold = mold
        self.grass = grass
        self.tree = tree
        self.rangweed = rangweed
        self.uvindex = uvindex
        self.desc = desc
        self.wind = wind
        self.windgust = windgust
        self.rainprob = rainprob
        self.snowprob = snowprob
        self.iceprob = iceprob
        self.cloudcover = cloudcover
        self.rain = rain
        self.snow = snow
        self.ice = ice

class WeatherInfo(AccuweatherInfo, OpenWeatherInfo, WeatherStackInfo):
    def __init__(self, accinfo, owinfo, wsinfo):
        def avg(elist):
            av = 0
            for e in elist:
                av += e
            av /= len(elist)
            return av
        def windavg(elist):
            wav = Wind(0, 0)
            for e in elist:
                wav.speed += e.speed
                wav.direction += e.direction
            wav.speed /= len(elist)
            wav.direction /= len(elist)
            return wav
        def tempavg(elist):
            tavg = Temperatures(0, 0, 0, 0)
            for el in elist:
                tavg.temp += el.temp
                tavg.rtemp += el.rtemp
                tavg.mintemp += el.mintemp
                tavg.maxtemp += el.maxtemp
            tavg.temp /= len(elist)
            tavg.rtemp /= len(elist)
            tavg.mintemp /= len(elist)
            tavg.maxtemp /= len(elist)
            return tavg
        self.date = accinfo.date
        self.time = wsinfo.time
        self.cloudcover = avg((accinfo.cloudcover, wsinfo.cloudcover))
        self.humidity = avg((wsinfo.humidity, owinfo.humidity))
        self.airquality = accinfo.airquality.__dict__
        self.sunrise = owinfo.sunrise
        self.sunset = owinfo.sunset
        self.sunhours = accinfo.sunhours
        self.coordinates = owinfo.coordinates.__dict__
        self.country = owinfo.country
        self.desc = accinfo.desc + ", " + wsinfo.desc
        self.rain = accinfo.rain
        self.snow = accinfo.snow
        self.ice = accinfo.rainprob
        self.rainprob = accinfo.rainprob
        self.snowprob = accinfo.snowprob
        self.iceprob = accinfo.iceprob
        self.location = owinfo.location
        self.mlink = accinfo.mlink
        self.pressure = avg((wsinfo.pressure, owinfo.pressure))
        self.airquality = accinfo.airquality.__dict__
        self.grass = accinfo.grass.__dict__
        self.mold = accinfo.mold.__dict__
        self.tree = accinfo.tree.__dict__
        self.rangweed = accinfo.rangweed.__dict__
        self.uvindex = accinfo.uvindex.__dict__
        self.uvindexvalue = wsinfo.uvindex
        self.visibility = wsinfo.visibility
        self.weather = owinfo.weather.__dict__
        self.wind = windavg((owinfo.wind, wsinfo.wind, accinfo.wind)).__dict__
        self.rtempshade = accinfo.rtempshade
        self.temp = tempavg((owinfo.temp, wsinfo.temp, accinfo.temp)).__dict__