from  itertools import groupby

from classes.missions import Missions


def priority_targets(target):
    return target.priority*2/10


def assign_mission(targets, pilots, aircrafts):
    missions = []
    for target in targets:
        conditision = 20
        distance = 25
        pilot_skill = 25
        conditision *= target.condition
        priority = 30
        priority *= priority_targets(target)
        for aircraft in aircrafts:
            actual_rang = aircraft.fuel_capacity/2
            if actual_rang < target.distence:
                delta = target.distence - actual_rang
                points_to_reduce = (delta // 100)
                distance -= points_to_reduce
            for pilot in pilots:
                tmp = pilot.skill_level / 10
                pilot_skill *= tmp
                mission = Missions(target, aircraft, pilot)
                mission.weights["weather_conditions"] = conditision
                mission.weights["distance"] = distance
                mission.weights["pilot_skill"] = pilot_skill
                missions.append(mission)
    sorted = sorted_missions(missions)
    return sorted


def sorted_missions(missions):
    sorted_missions = sorted(missions, key=lambda x: x.sum(), reverse=True)
    return sorted_missions

