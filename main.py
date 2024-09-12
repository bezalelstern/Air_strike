import read_files
import api_zone
import missions

if __name__ == '__main__':
    pilots =  read_files.read_pilots()
    aircraft =  read_files.read_aircraft()
    targets =  read_files.read_targets()

    api_zone.get_location(targets)
    api_zone.get_weather(targets)

    group_targets =  missions.priority_targets(targets)
    missions.assign_mission(targets,pilots, aircraft)