from  itertools import groupby

from classes.missions import Missions



def priority_targets(targets):

    sorted_targets = sorted(targets, key=lambda x: x.priority, reverse=True)
    group_targets = []
    for priority, group in groupby(sorted_targets, lambda x: x.priority):
        list_targets = list(group)
        group_targets.append(list_targets)




def assign_mission(targets, pilots, aircrafts):
    for target in targets:
        conditision = 20
        distance = 20
        pilot_skill = 25
        conditision *= target.condition
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

