import json
import caculations
import requests
def get_location(targets):
    #lucation = requests.get("https://api.openweathermap.org/data/2.5/forecast?q=yemen&APPID=d6a9a801ea56fc97a66d57e476d39bfa")
    for target in targets:
        lucation2 = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={target.city}&APPID=d6a9a801ea56fc97a66d57e476d39bfa")
        list = lucation2.json()  #
        let = list[0]["lat"]
        lon = list[0]["lon"]
        target.distence = caculations.haversine_distance(let, lon)
