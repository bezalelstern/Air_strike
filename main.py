import read_files
import api_zone

if __name__ == '__main__':
    pilots =  read_files.read_pilots()
    aircraft =  read_files.read_aircraft()
    targets =  read_files.read_targets()

    api_zone.get_location(targets)
