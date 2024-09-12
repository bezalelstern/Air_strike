import csv

def write_missions_to_csv(missions):
    """

    :param missions:
    :return: make a csv file
    """
    filename = "missions_assign.csv"
    with open(filename, "w", newline='', encoding="utf-8") as file:
        fieldnames = ["Target", "Priority", "Pilot","Pilot Skill", "Aircraft","Speed", "Weather", "Distance","Fuel capacity","Mission fit score"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for mission in missions:
            writer.writerow({
                "Target": mission.target.city,
                "Priority": mission.target.priority,
                "Pilot": mission.pilot.name,
                "Pilot Skill": mission.pilot.skill_level,
                "Aircraft": mission.aircraft.type,
                "Speed": mission.aircraft.speed,
                "Weather" : mission.target.weather,
                "Distance": mission.target.distence,
                "Mission fit score": mission.sum()
            })

def print_csv():
    """
    print to console
    :return:
    """
    with open('missions_assign.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print(', '.join(row))