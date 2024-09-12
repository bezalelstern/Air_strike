import json
import caculations
import requests


def get_location(targets):
    """

    :param targets:
    :return: noun
    """
    for target in targets:
        lucation2 = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={target.city}&APPID=d6a9a801ea56fc97a66d57e476d39bfa")
        list = lucation2.json()  #
        let = list[0]["lat"]
        lon = list[0]["lon"]
        target.distence = caculations.haversine_distance(let, lon)
    return


def get_weather(targets):
    for target in targets:
        weather = requests.get(
            f"https://api.openweathermap.org/data/2.5/forecast?q={target.city}&APPID=d6a9a801ea56fc97a66d57e476d39bfa")
        weather_data = weather.json()

        midnight_weather = []
        for weather_data in weather_data['list']:
            if "00:00:00" in weather_data['dt_txt']:
                midnight_weather.append(weather_data)
                condition= {'condition': weather_data['weather'][0]['main']}
                target.condition = caculations.weather_score(condition)
                target.weather = weather_data['weather'][0]['main']
                break

