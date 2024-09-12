import read_files
import api_zone
import missions
import writh_csv

if __name__ == '__main__':
    #מייבא קובץ טייסים
    pilots =  read_files.read_pilots()
    #מייבא קובץ מטוסים
    aircraft =  read_files.read_aircraft()
    #מייבא קובץ מטרות
    targets =  read_files.read_targets()

    #מקבל את מיקום המטרה ומחשב מרחק
    api_zone.get_location(targets)

    #בודק את מזג האוויר
    api_zone.get_weather(targets)

    #מצוות משימות ומחשב עדיפות
    missions =  missions.assign_mission(targets,pilots, aircraft)

    #מייצא רשימת מטרות ל-csv
    writh_csv.write_missions_to_csv(
        missions)

    #מדפיס את המשימות
    writh_csv.print_csv()