

class Coordinates:
    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude

class Wind:
    def __init__(self, speed, direction):
        self.speed = speed
        self.direction = direction

class OWeatherInfo:
    def __init__(self, locid, main, desc, iconid):
        self.locid = locid
        self.main = main
        self.desc = desc
        self.iconid = iconid

class Temperatures:
    def __init__(self, temp, rtemp, maxtemp, mintemp):
        self.temp = temp
        self.rtemp = rtemp
        self.maxtemp = maxtemp
        self.mintemp = mintemp

class IndexedData:
    def __init__(self, jsondict):
        self.name = jsondict["Name"]
        self.value = jsondict["Value"]
        self.index = jsondict["Category"]