class Missions:
    def __init__(self, target, aircraft = None, pilot = None):
        self.target = target
        self.aircraft = aircraft
        self.pilot = pilot
        self.weights  = {
        "distance": 25,
        "pilot_skill": 25,
        "weather_conditions": 20,
        "priority": 30
    }

    def sum(self):
        sum = 0
        for key, value in self.weights.items():
            sum += value
        return round(sum,2)