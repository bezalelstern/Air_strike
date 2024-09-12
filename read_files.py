import json
from classes import pilot
from  classes import aircraft_class
from  classes import target

def read_pilots() -> list:
    file_path = "data/pilots.json"
    with open(file_path, "r", encoding="utf8") as f:
        data = json.load(f)

    list_of_pilots = [pilot.Pilot(person["name"], person["skill_level"]) for person in data["pilots"]]
    return list_of_pilots


def read_aircraft() -> list:
    file_path = "data/aircrafts.json"
    with open(file_path, "r", encoding="utf8") as f:
        data = json.load(f)

    aircraft_list = [
        aircraft_class.Aircraft(
            aircraft_data['type'],
            aircraft_data['speed'],
            aircraft_data['fuel_capacity']
        )
        for aircraft_data in data['aircrafts']
    ]
    print(aircraft_list)
    return aircraft_list

def read_targets() -> list:
    file_path = "data/targets.json"
    with open(file_path, "r", encoding="utf8") as f:
        data = json.load(f)

    targets_list = [target.Target(
        target_data["City"],
        target_data["Priority"]
    )
    for target_data in data['targets']]
    return targets_list
