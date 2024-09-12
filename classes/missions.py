class Missions:
    def __init__(self, target, aircraft = None, pilot = None):
        self.target = target
        self.aircraft = aircraft
        self.pilot = pilot
        self.weights  = {
        "distance": 20,
        "aircraft_type": 25,
        "pilot_skill": 25,
        "weather_conditions": 20,
        "execution_time": 10
    }

    def sum(self):
        sum = 0
        for key, value in self.weights.items():
            sum += value
        return sum